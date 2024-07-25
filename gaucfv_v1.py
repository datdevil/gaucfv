import hashlib
import json
import requests
import wmi
import winreg as reg
from datetime import datetime
import platform
import pytz

def main():
    idcpu = get_hardware_id("Win32_Processor", "ProcessorId")
    idgpu = get_hardware_id("Win32_VideoController", "DeviceID")

    if idcpu and idgpu:
        unique_id = generate_unique_id(idcpu, idgpu)
        print(f"KEY: {unique_id}")

        # Thu thập thông tin hệ thống
        system_info = get_system_info()

        reg_value = read_registry()
        if reg_value is None:
            # Nếu không có registry
            if not check_name_exist_on_server(unique_id):
                print("KEY chưa tồn tại trên server")
                if write_to_registry(unique_id):
                    send_http_post(unique_id, system_info, True)  # Gửi yêu cầu POST để tạo mới
                    write_to_file("you_file.pro", unique_id)
                else:
                    print("Lỗi khi tạo mới")
            else:
                print("KEY đã tồn tại trên server nhưng không có sẵn.")
                if write_to_registry(unique_id):
                    send_http_post(unique_id, system_info, False)  # Gửi yêu cầu PATCH để cập nhật
                    write_to_file("you_file.pro", unique_id)
                else:
                    print("Lỗi khi tạo mới")
        else:
            # Nếu có registry
            print(f"Đã tìm thấy KEY tồn tại: {reg_value}")
            if validate_name(reg_value):
                if check_name_exist_on_server(reg_value):
                    print("KEY đã tồn tại trên server.")
                    send_http_post(reg_value, system_info, False)  # Gửi yêu cầu PATCH để cập nhật
                    write_to_file("you_file.pro", reg_value)
                else:
                    print("Xóa KEY và tạo mới...")
                    delete_registry()
                    if write_to_registry(unique_id):
                        send_http_post(unique_id, system_info, True)  # Gửi yêu cầu POST để tạo mới
                        write_to_file("you_file.pro", unique_id)
                    else:
                        print("Lỗi khi tạo mới")
            else:
                print("KEY không hợp lệ, xóa KEY và tạo mới.")
                delete_registry()
                if write_to_registry(unique_id):
                    send_http_post(unique_id, system_info, True)  # Gửi yêu cầu POST để tạo mới
                    write_to_file("you_file.pro", unique_id)
                else:
                    print("Lỗi khi tạo mới")
    else:
        print("Không thể lấy thông tin ID")

def generate_unique_id(idcpu, idgpu):
    try:
        combined_id = idcpu + idgpu
        md5_hash = hashlib.md5(combined_id.encode()).hexdigest()
        return md5_hash[:12].upper() 
    except Exception as e:
        print(f"Lỗi khi tạo unique ID: {e}")
        return None

def get_hardware_id(wmi_class, wmi_property):
    try:
        c = wmi.WMI()
        for item in c.query(f"SELECT {wmi_property} FROM {wmi_class}"):
            return getattr(item, wmi_property)
    except Exception as e:
        print(f"Lỗi khi lấy thông tin ID: {e}")
        return None

def get_system_info():
    try:
        c = wmi.WMI()

        # Lấy tổng dung lượng RAM và chuyển đổi sang GB
        total_memory = c.Win32_ComputerSystem()[0].TotalPhysicalMemory
        if isinstance(total_memory, str):
            total_memory = int(total_memory)
        ram_gb = round(total_memory / (1024 ** 3))  

        # Lấy thông tin hệ điều hành
        os_name = platform.system()
        os_version = platform.release()
        os_info = c.Win32_OperatingSystem()[0]
        os_caption = os_info.Caption
        os_version_full = os_caption.strip() if os_caption else f"{os_name} {os_version}"

        # Lấy thông tin múi giờ
        timezone = datetime.now(pytz.timezone("Asia/Ho_Chi_Minh")).strftime('%A%Z%z')

        # Lấy thông tin hệ thống
        system_info = {
            "computer_name": c.Win32_ComputerSystem()[0].Name,
            "cpu": c.Win32_Processor()[0].Name,
            "gpu": c.Win32_VideoController()[0].Name,
            "ram": f"{ram_gb}GB", 
            "os_version": os_version_full,  
            "serial_number": c.Win32_BIOS()[0].SerialNumber,  
            "mainboard": f"{c.Win32_BaseBoard()[0].Manufacturer} {c.Win32_BaseBoard()[0].Product}",  # Kết hợp Manufacturer và Product
            "timezone": timezone  
        }
        
        return system_info
    except Exception as e:
        print(f"Lỗi khi lấy thông tin hệ thống: {e}")
        return {}

def send_http_post(reg_value, system_info, is_new=False):
    url = "https://your-server-url.com//"
    try:
        timestamp = int(datetime.now().timestamp())
        data = {
            "name": reg_value,
            "date": timestamp,
            "info": system_info  
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "your_api_token_here"
        }
        
        if is_new:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            print(f"Tạo Mới Code = {response.status_code}")
        else:
            response = requests.patch(f"{url}{reg_value}", data=json.dumps(data), headers=headers)
            print(f"Cập Nhật Code = {response.status_code}")
    except Exception as e:
        print(f"Lỗi khi gửi HTTP request: {e}")

def check_name_exist_on_server(reg_value):
    url = f"https://your-server-url.com//{reg_value}"
    try:
        headers = {"Authorization": "your_api_token_here"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"KEY '{reg_value}' đã tồn tại trên server.")
            return True
        else:
            print(f"KEY '{reg_value}' chưa tồn tại trên server. Mã lỗi: {response.status_code}")
            return False
    except Exception as e:
        print(f"Lỗi khi kiểm tra name trên server: {e}")
        return False

def write_to_registry(value):
    try:
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, "Software\\you_sofware")
        reg.SetValueEx(key, "you_sofware", 0, reg.REG_SZ, value)
        reg.CloseKey(key)
        print(f"Đã tạo KEY '{value}'")
        return True
    except Exception as e:
        print(f"Lỗi khi tạo KEY: {e}")
        return False

def read_registry():
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\\you_sofware", 0, reg.KEY_READ)
        reg_value, _ = reg.QueryValueEx(key, "you_sofware")
        reg.CloseKey(key)
        print(f"Đọc giá trị từ KEY: {reg_value}")
        return reg_value
    except FileNotFoundError:
        print("Không tìm thấy KEY")
        return None
    except Exception as e:
        print(f"Lỗi khi đọc KEY: {e}")
        return None

def write_to_file(file_name, content):
    try:
        with open(file_name, "w") as f:
            f.write(content)
        print(f"Đã ghi dữ liệu vào file {file_name}.")
    except Exception as e:
        print(f"Lỗi khi ghi vào file {file_name}: {e}")

def delete_registry():
    try:
        reg.DeleteKey(reg.HKEY_CURRENT_USER, "Software\\you_sofware")
        print("Đã xóa KEY.")
    except Exception as e:
        print(f"Lỗi khi xóa KEY: {e}")

def validate_name(name):
    return len(name) == 12

if __name__ == "__main__":
    main()
