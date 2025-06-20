# 🚀 Week 1 - Projects: Dự Án Thực Hành

## 📁 Cấu trúc Projects

```
03_Project/
├── project1_calculator/      # Máy tính nâng cao
├── project2_profile/         # Trình tạo hồ sơ cá nhân
└── README.md                 # File này
```

---

## 🎯 Dự án 1: Máy tính nâng cao

### 📖 Mô tả

Xây dựng calculator nâng cao có thể thực hiện nhiều phép tính và có giao diện user-friendly.

### 🔧 Tính năng

1. **Phép tính cơ bản**: +, -, \*, /
2. **Phép tính nâng cao**: Lũy thừa (^), Căn bậc hai, Phần trăm
3. **Hàm khoa học**: Sin, Cos, Tan (bonus)
4. **Chức năng bộ nhớ**: Lưu trữ và gọi lại kết quả
5. **Xác thực đầu vào**: Xử lý đầu vào không hợp lệ
6. **Menu người dùng**: Hệ thống menu tương tác

### 📋 Yêu cầu

- Chương trình chạy trong loop cho đến khi user chọn exit
- Menu rõ ràng, dễ sử dụng
- Handle errors gracefully
- Code được organize tốt với functions

### 🎯 Tính năng mong đợi

```
====== MÁY TÍNH NÂNG CAO ======
1. Máy tính cơ bản (+, -, *, /)
2. Máy tính khoa học
3. Bộ chuyển đổi đơn vị
4. Lịch sử
5. Thoát

Chọn tùy chọn (1-5):
```

### 📁 Files cần tạo:

- `calculator.py`: Main program
- `functions.py`: Calculator functions
- `utils.py`: Utility functions

---

## 🎯 Dự án 2: Trình tạo hồ sơ cá nhân

### 📖 Mô tả

Tạo chương trình thu thập thông tin cá nhân và generate profile card đẹp mắt với nhiều format khác nhau.

### 🔧 Tính năng

1. **Thu thập dữ liệu**: Thu thập thông tin cá nhân toàn diện
2. **Xác thực**: Xác thực email, số điện thoại, tuổi
3. **Nhiều định dạng**: Danh thiếp, tóm tắt CV, tiểu sử mạng xã hội
4. **Tùy chọn xuất**: Lưu vào file text
5. **Mẫu thiết kế**: Nhiều mẫu card khác nhau
6. **Thống kê**: Tính toán một số thống kê cá nhân

### 📋 Thông tin cần thu thập

- Cá nhân: Họ tên, tuổi, ngày sinh, địa điểm
- Liên hệ: Email, điện thoại, mạng xã hội
- Nghề nghiệp: Chức danh, công ty, kinh nghiệm
- Sở thích: Hobby, kỹ năng, mục tiêu
- Thể chất: Chiều cao, cân nặng (tùy chọn)

### 🎯 Kết quả mẫu

```
╔══════════════════════════════════════╗
║           THẺ HỒ SƠ                  ║
╠══════════════════════════════════════╣
║ Họ tên: Nguyễn Văn A                 ║
║ Tuổi: 25 | Địa điểm: TP Hồ Chí Minh  ║
║ Nghề: Lập trình viên Python          ║
║ Email: nguyenvana@email.com          ║
║ Sở thích: Lập trình, Nhạc, Du lịch   ║
╚══════════════════════════════════════╝
```

### 📁 Files cần tạo:

- `profile_generator.py`: Main program
- `validation.py`: Input validation functions
- `templates.py`: Card templates
- `data_storage.py`: Save/load functionality

---

## 📊 Tiêu chí chấm điểm

### Dự án 1: Máy tính nâng cao (50 điểm)

- **Tính năng (20 điểm)**: Tất cả tính năng yêu cầu hoạt động đúng
- **Chất lượng code (10 điểm)**: Sạch sẽ, dễ đọc, có comment tốt
- **Xử lý lỗi (10 điểm)**: Xác thực đầu vào và thông báo lỗi phù hợp
- **Trải nghiệm người dùng (10 điểm)**: Dễ sử dụng, hướng dẫn rõ ràng

### Dự án 2: Trình tạo hồ sơ (50 điểm)

- **Thu thập dữ liệu (15 điểm)**: Thu thập thông tin toàn diện
- **Xác thực (10 điểm)**: Xác thực đầu vào phù hợp
- **Định dạng đầu ra (15 điểm)**: Đẹp mắt, định dạng tốt
- **Tổ chức code (10 điểm)**: Cấu trúc và functions tốt

### Điểm thưởng (Tối đa 20 điểm)

- **Tính năng bổ sung**: Chức năng thêm
- **Thiết kế sáng tạo**: Cách tiếp cận đổi mới
- **Tài liệu**: File README chi tiết
- **Kiểm thử**: Test các tình huống khác nhau

---

## 🏆 Tính năng thử thách (Bonus)

### Cải tiến máy tính:

- [ ] Vẽ đồ thị (ASCII đơn giản)
- [ ] Giải phương trình
- [ ] Tính toán ma trận
- [ ] Chuyển đổi cơ số (nhị phân, hex, octal)
- [ ] Hàm thống kê

### Cải tiến trình tạo hồ sơ:

- [ ] Tạo mã QR cho thông tin liên hệ
- [ ] Hỗ trợ đa ngôn ngữ
- [ ] Tích hợp ASCII art cho ảnh
- [ ] Xác thực liên kết mạng xã hội
- [ ] Xuất sang các định dạng khác (JSON, CSV)

---

## 🔧 Hướng dẫn phát triển

### 1. Giai đoạn lập kế hoạch

- [ ] Phác thảo luồng chương trình
- [ ] Liệt kê tất cả functions cần thiết
- [ ] Thiết kế giao diện người dùng (text-based)
- [ ] Lập kế hoạch cho các tình huống lỗi

### 2. Giai đoạn phát triển

- [ ] Bắt đầu với chức năng cơ bản
- [ ] Thêm tính năng từng bước
- [ ] Test kỹ lưỡng từng tính năng
- [ ] Refactor và tối ưu

### 3. Giai đoạn kiểm thử

- [ ] Test với đầu vào hợp lệ
- [ ] Test với đầu vào không hợp lệ
- [ ] Test các trường hợp biên
- [ ] Kiểm thử chấp nhận của người dùng

### 4. Giai đoạn tài liệu

- [ ] Thêm comment vào code
- [ ] Tạo hướng dẫn sử dụng
- [ ] Ghi chép các vấn đề đã biết
- [ ] Viết bài phản ánh

---

## 📝 Yêu cầu nộp bài

### Files cần nộp:

1. **Source Code**: Tất cả files .py
2. **Tài liệu**: README.md cho mỗi dự án
3. **Test Cases**: Đầu vào và đầu ra mẫu
4. **Bài phản ánh**: Những gì đã học, khó khăn gặp phải

### Định dạng nộp bài:

```
Week01_Projects_[TenBan]/
├── project1_calculator/
│   ├── calculator.py
│   ├── functions.py
│   ├── utils.py
│   └── README.md
├── project2_profile/
│   ├── profile_generator.py
│   ├── validation.py
│   ├── templates.py
│   └── README.md
└── reflection.md
```

---

## 🎯 Kết quả học tập

Sau khi hoàn thành các dự án này, bạn sẽ có thể:

- [ ] Cấu trúc một chương trình Python lớn hơn
- [ ] Sử dụng functions để tổ chức code
- [ ] Xử lý đầu vào người dùng và xác thực
- [ ] Thực hiện xử lý lỗi
- [ ] Tạo giao diện thân thiện với người dùng
- [ ] Debug và test chương trình
- [ ] Viết tài liệu cho code một cách đúng đắn

---

## 🔗 Tài liệu tham khảo

### Tài liệu Python:

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Math Module](https://docs.python.org/3/library/math.html)

### Hướng dẫn:

- [Real Python - Python Functions](https://realpython.com/defining-your-own-python-function/)
- [Python Error Handling](https://realpython.com/python-exceptions/)

---

**Lịch trình**: Hoàn thành cả hai dự án trong 3-4 ngày, dành 1 ngày cho tài liệu và kiểm thử.
