# Hệ Thống Quản Lý Học Tập (Student Management System)

Hệ thống quản lý học tập được xây dựng bằng Python, hỗ trợ quản lý sinh viên, giảng viên, môn học, lớp học và điểm số. Ứng dụng sử dụng giao diện dòng lệnh (CLI) với kiến trúc phân lớp rõ ràng.

## 🎬 Trình Bày

![Screenshot ứng dụng SMS](Screenshot%20From%202025-11-17%2000-34-37.png)

*Ứng dụng chạy trong Docker với giao diện CLI thân thiện, hỗ trợ đầy đủ tiếng Việt*

### Tính Năng Nổi Bật

✨ Giao diện CLI thân thiện | 🔐 Xác thực theo vai trò | 📊 Quản lý toàn diện | ⚡ Hiệu suất cao | 🐳 Docker Ready

### Chạy Nhanh

```bash
docker-compose up --build
```

## ✨ Tính Năng

### 👨‍💼 Quản Trị Viên (Admin)
- ✅ Quản lý sinh viên (Thêm, Sửa, Xóa, Xem danh sách)
- ✅ Quản lý giảng viên (Thêm, Sửa, Xóa, Xem danh sách)
- ✅ Quản lý môn học (Thêm, Sửa, Xóa, Xem danh sách)
- ✅ Quản lý lớp học (Thêm, Sửa, Xóa, Xem danh sách)
- ✅ Đổi mật khẩu

### 👨‍🎓 Sinh Viên (Student)
- ✅ Xem lịch học
- ✅ Xem điểm số
- ✅ Đăng ký môn học
- ✅ Đổi mật khẩu

### 👨‍🏫 Giảng Viên (Lecturer)
- ✅ Nhập điểm cho sinh viên
- ✅ Xem danh sách lớp học phụ trách
- ✅ Đổi mật khẩu

## 🏗️ Kiến Trúc

Dự án được xây dựng theo kiến trúc phân lớp (Layered Architecture) với các thành phần:

- **Models**: Định nghĩa các thực thể dữ liệu (User, Student, Lecturer, Subject, Class, Grade)
- **Repositories**: Quản lý truy cập dữ liệu (in-memory storage)
- **Services**: Xử lý logic nghiệp vụ
- **Controllers**: Điều phối luồng xử lý và tương tác với người dùng
- **UI**: Giao diện menu và hiển thị

## 💻 Yêu Cầu Hệ Thống

- Python 3.8 trở lên
- Không cần cài đặt thêm thư viện bên ngoài (chỉ sử dụng thư viện chuẩn của Python)

## 🚀 Cài Đặt

### Cách 1: Chạy trực tiếp với Python

1. Clone hoặc tải dự án về máy
2. Di chuyển vào thư mục dự án:
```bash
cd SMS
```

3. Chạy ứng dụng:
```bash
python main.py
```

### Cách 2: Sử dụng Docker (Khuyến nghị)

**⚠️ Lưu ý quan trọng**: Phải chạy các lệnh Docker từ thư mục `SMS` (thư mục gốc của dự án), không phải từ thư mục `src`.

```bash
# Đảm bảo bạn đang ở thư mục SMS (thư mục chứa Dockerfile)
cd SMS

# Sử dụng Docker Compose (Khuyến nghị)
docker-compose up --build

# Hoặc sử dụng Docker trực tiếp
docker build -t sms-app .
docker run -it --rm sms-app
```

**Giải thích lỗi thường gặp:**
- Nếu bạn thấy lỗi `failed to read dockerfile: open Dockerfile: no such file or directory`, có nghĩa là bạn đang chạy lệnh từ sai thư mục
- Hãy đảm bảo bạn đang ở thư mục `SMS` (thư mục chứa file `Dockerfile` và `main.py`)

## 📖 Sử Dụng

1. **Khởi động ứng dụng**: Chạy `python main.py` hoặc sử dụng Docker
2. **Đăng nhập**: Nhập username và password (xem [Tài Khoản Mặc Định](#tài-khoản-mặc-định))
3. **Sử dụng menu**: Chọn các chức năng từ menu hiển thị
4. **Đăng xuất**: Chọn tùy chọn "Đăng xuất" hoặc nhấn `Ctrl+C`

### Ví dụ sử dụng

```
============================================================
            HỆ THỐNG QUẢN LÝ HỌC TẬP
============================================================
============================================================
                  ĐĂNG NHẬP HỆ THỐNG
============================================================
Username: student01
Password: 123456
✓ Đăng nhập thành công!
Chào mừng Nguyễn Văn A (student)
```

## 📁 Cấu Trúc Dự Án

```
SMS/
├── main.py                 # File chính để chạy ứng dụng
├── src/
│   ├── models/            # Các model dữ liệu
│   │   ├── user.py        # User, Student, Lecturer, Admin
│   │   ├── subject.py     # Subject model
│   │   ├── class_model.py # Class model
│   │   └── grade.py       # Grade model
│   ├── repositories/      # Data access layer
│   │   ├── base_repository.py
│   │   ├── user_repository.py
│   │   ├── subject_repository.py
│   │   ├── class_repository.py
│   │   └── grade_repository.py
│   ├── services/          # Business logic layer
│   │   ├── auth_service.py
│   │   ├── student_service.py
│   │   ├── lecturer_service.py
│   │   ├── subject_service.py
│   │   ├── class_service.py
│   │   └── grade_service.py
│   ├── controllers/       # Controller layer
│   │   └── app_controller.py
│   ├── ui/               # User interface
│   │   └── menu.py
│   └── interfaces/       # Interface definitions
│       ├── repository_interface.py
│       └── notification_interface.py
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Docker ignore file
└── README.md            # File này
```

## 🔐 Tài Khoản Mặc Định

Hệ thống tự động khởi tạo các tài khoản mặc định khi chạy lần đầu:

### Quản Trị Viên
- **Username**: `admin01`
- **Password**: `admin123`
- **Chức năng**: Quản lý toàn bộ hệ thống

### Sinh Viên
- **Username**: `student01`
- **Password**: `123456`
- **User ID**: `051111`
- **Tên**: Nguyễn Văn A

### Giảng Viên
- **Username**: `lecturer01`
- **Password**: `123456`
- **User ID**: `051211`
- **Tên**: Prof. Alan
- **Khoa**: Khoa học Máy tính

## 🐳 Docker

Dự án đã được cấu hình sẵn để chạy với Docker.

### Hướng dẫn chi tiết:

#### Sử dụng Docker Compose (Dễ nhất)

```bash
# Từ thư mục SMS
cd SMS
docker-compose up --build
```

#### Sử dụng Docker trực tiếp

```bash
# 1. Build image (từ thư mục SMS)
cd SMS
docker build -t sms-app .

# 2. Chạy container
docker run -it --rm sms-app
```

#### Các lệnh hữu ích khác

```bash
# Chạy ở chế độ background
docker-compose up -d --build

# Xem logs
docker-compose logs -f

# Dừng container
docker-compose down

# Xóa image
docker rmi sms-app
```

### Lợi ích khi sử dụng Docker:
- ✅ Môi trường chạy nhất quán
- ✅ Không cần cài đặt Python trên máy
- ✅ Dễ dàng triển khai
- ✅ Cô lập với hệ thống

## 📝 Lưu Ý

- Dữ liệu được lưu trữ trong bộ nhớ (in-memory), sẽ mất khi ứng dụng dừng
- Ứng dụng sử dụng giao diện dòng lệnh, cần terminal hỗ trợ UTF-8 để hiển thị tiếng Việt đúng
- Khi chạy với Docker, cần sử dụng flag `-it` để có thể tương tác với ứng dụng

## 🔄 Phát Triển Tương Lai

- [ ] Lưu trữ dữ liệu vào database (SQLite/PostgreSQL)
- [ ] Thêm giao diện web
- [ ] Export báo cáo (PDF, Excel)
- [ ] Gửi thông báo email
- [ ] API RESTful
- [ ] Xác thực 2 lớp

## 📄 License

Dự án này được phát triển cho mục đích học tập và nghiên cứu.

## 👥 Đóng Góp

Mọi đóng góp đều được chào đón! Vui lòng tạo issue hoặc pull request.

---

**Phát triển bởi**: [Tên của bạn/nhóm]  
**Ngôn ngữ**: Python 3.11+  
**Kiến trúc**: Layered Architecture (MVC Pattern)
