# Gaucfv

Gaucfv là một ứng dụng Python để thu thập và gửi thông tin hệ thống của máy tính đến một máy chủ từ xa. Dự án này bao gồm các tính năng chính như:

- Tạo và quản lý ID phần cứng duy nhất cho máy tính để quản lý bản quyền.
- Thu thập thông tin hệ thống như CPU, GPU, RAM, và hệ điều hành để quản lý bản quyền.
- Gửi thông tin đến máy chủ thông qua HTTP POST và PATCH requests để quản lý bản quyền.

## Cài Đặt

1. **Cài đặt các thư viện phụ thuộc**

   Đảm bảo bạn đã cài đặt các thư viện cần thiết. Bạn có thể cài đặt chúng bằng cách sử dụng `pip`:

   ```bash
   pip install requests wmi pytz
2. **Cấu hình biến môi trường**
Đặt token API của bạn vào biến môi trường API_TOKEN. Bạn có thể làm điều này bằng cách thêm dòng sau vào tệp cấu hình môi trường của bạn
```bash
   export API_TOKEN="your_api_token_here"
   
*Hoặc trên Windows:*
```bash
   setx API_TOKEN "your_api_token_here"

**Giải thích:**
- **Cài đặt thư viện phụ thuộc**: Danh sách các thư viện cần thiết và cách cài đặt chúng. Bạn sử dụng lệnh `pip` để cài đặt các thư viện Python cần thiết.
- **Cấu hình biến môi trường**: Hướng dẫn cách thiết lập biến môi trường để bảo mật thông tin nhạy cảm như token API. Lưu ý không công khai token này.

### 3. Cách Sử Dụng

## Cách Sử Dụng

1. **Chạy ứng dụng**

   Chạy script Python chính:

   ```bash
   python your_script_name.py

**Giải thích:**
- **Chạy ứng dụng**: Cung cấp lệnh để chạy ứng dụng. Thay thế `your_script_name.py` bằng tên file của script Python của bạn.

### 4. Các Chức Năng

## Các Chức Năng

- **`generate_unique_id(idcpu, idgpu)`**: Tạo ID duy nhất từ ID CPU và GPU.
- **`get_hardware_id(wmi_class, wmi_property)`**: Lấy ID phần cứng từ WMI.
- **`get_system_info()`**: Thu thập thông tin hệ thống.
- **`send_http_post(reg_value, system_info, is_new=False)`**: Gửi thông tin đến máy chủ.
- **`check_name_exist_on_server(reg_value)`**: Kiểm tra sự tồn tại của ID trên máy chủ.
- **`write_to_registry(value)`**: Ghi giá trị vào registry Windows.
- **`read_registry()`**: Đọc giá trị từ registry Windows.
- **`write_to_file(file_name, content)`**: Ghi dữ liệu vào tệp.
- **`delete_registry()`**: Xóa giá trị khỏi registry Windows.
- **`validate_name(name)`**: Xác thực tính hợp lệ của ID.
## Cảnh Báo

- Đảm bảo không chia sẻ token API công khai.
- Nếu bạn lỡ đưa token vào mã nguồn, hãy ngay lập tức đổi token và xóa khỏi lịch sử commit.
## Giấy Phép

Dự án này được cấp phép theo [Giấy phép MIT](https://opensource.org/licenses/MIT).
## Thông Tin Liên Hệ

Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ qua email hoặc gửi yêu cầu trên GitHub Issues.
