# GAUCFV

- Tạo và quản lý ID phần cứng duy nhất cho máy tính để quản lý bản quyền phần mềm.
- Thu thập thông tin hệ thống như CPU, GPU, RAM, và hệ điều hành để quản lý bản quyền phần mềm.
- Gửi thông tin đến máy chủ thông qua HTTP POST và PATCH requests để quản lý bản quyền phần mềm.

## Cài Đặt
1. Clone repository:
2. 
    ```bash
    git clone https://github.com/datdevil/gaucfv.git
    ```
    
3. Cài đặt các thư viện yêu cầu:

    ```bash
    pip install -r requirements.txt
    ```

4. Cấu hình các biến môi trường:

    ```bash
    export API_SERVER_URL="https://your-server-url.com/"
    export API_TOKEN="your_api_token_here"
    ```

5. Chạy ứng dụng:

    ```bash
    python your_script_name.py
    ```
    
## Các Chức Năng

- `generate_unique_id(idcpu, idgpu)`: Tạo ID duy nhất từ ID CPU và GPU.
- `get_hardware_id(wmi_class, wmi_property)`: Lấy ID phần cứng từ WMI.
- `get_system_info()`: Thu thập thông tin hệ thống.
- `send_http_post(reg_value, system_info, is_new=False)`: Gửi thông tin đến máy chủ.
- `check_name_exist_on_server(reg_value)`: Kiểm tra sự tồn tại của ID trên máy chủ.
- `write_to_registry(value)`: Ghi giá trị vào registry Windows.
- `read_registry()`: Đọc giá trị từ registry Windows.
- `write_to_file(file_name, content)`: Ghi dữ liệu vào tệp.
- `delete_registry()`: Xóa giá trị khỏi registry Windows.
- `validate_name(name)`: Xác thực tính hợp lệ của ID.

## Cảnh Báo

- Đảm bảo không chia sẻ token API công khai.

## Xác Minh Mã

Để xác minh tính minh bạch của mã nguồn, vui lòng tham khảo liên kết sau: [Thông tin minh bạch](https://github.com/datdevil/gaucfv/blob/main/README.md).

## Giấy Phép

Dự án này được cấp phép theo [Giấy phép MIT](https://opensource.org/licenses/MIT).

## Giải Thích Về Các Báo Cáo Phát Hiện Phần Mềm Độc Hại

Chúng tôi nhận thức được rằng một số công cụ quét bảo mật đã phát hiện các cảnh báo phần mềm độc hại đối với mã nguồn của chúng tôi. Chúng tôi đã thực hiện các bước sau để xác minh và giải quyết vấn đề này:

1. **Kiểm Tra Mã Nguồn**: Chúng tôi đã kiểm tra mã nguồn của mình và không phát hiện bất kỳ mã độc nào.
2. **Quét Bằng Các Công Cụ Khác**: Chúng tôi đã sử dụng các công cụ quét khác và không nhận được cảnh báo tương tự.
3. **Cập Nhật Phần Mềm Bảo Mật**: Chúng tôi đã cập nhật phần mềm bảo mật của mình để đảm bảo rằng các báo cáo sai không xuất hiện.
4. **Liên Hệ Với Nhà Cung Cấp Phần Mềm Bảo Mật**: Chúng tôi đã liên hệ với các nhà cung cấp phần mềm bảo mật để báo cáo các cảnh báo sai và yêu cầu họ kiểm tra lại.

Chúng tôi cam kết bảo mật và minh bạch và sẽ tiếp tục theo dõi và kiểm tra mã của mình để đảm bảo an toàn.


## Thông Tin Liên Hệ

Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ qua email hoặc gửi yêu cầu trên GitHub Issues.
