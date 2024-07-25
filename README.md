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
