# 🛠️ Week 1 - Exercises: Thực Hành Python Cơ Bản

## 📋 Hướng dẫn làm bài

### 📁 Cấu trúc thư mục

```
02_Exercises/
├── exercises/          # Đề bài tập
├── solutions/          # Đáp án có giải thích
└── practice_files/     # File Python để thực hành
```

### 📝 Cách làm bài

1. Đọc đề bài trong thư mục `exercises/`
2. Tự làm trước khi xem đáp án
3. Chạy code và test kết quả
4. So sánh với đáp án trong `solutions/`
5. Nếu sai, đọc giải thích và làm lại

---

## 🎯 Bài tập 1: Hello World và Variables

**Mục tiêu**: Làm quen với print(), variables, và basic operations

### Đề bài:

1. In ra màn hình "Hello, Python World!"
2. Tạo variable `name` với tên của bạn
3. Tạo variable `age` với tuổi của bạn
4. In ra: "My name is [name] and I am [age] years old"
5. Tính và in tuổi của bạn sau 10 năm

### Code mẫu để bắt đầu:

```python
# Bài 1: Hello World và Variables
# TODO: Viết code của bạn ở đây

```

---

## 🎯 Bài tập 2: Type Conversion và Calculations

**Mục tiêu**: Thực hành type conversion và các phép tính

### Đề bài:

1. Tạo string `num_str = "123"`
2. Convert thành integer và lưu vào `num_int`
3. Tạo string `pi_str = "3.14159"`
4. Convert thành float và lưu vào `pi_float`
5. Tính chu vi hình tròn với bán kính `num_int`
6. In kết quả với 2 chữ số thập phân

### Công thức:

- Chu vi = 2 × π × r

---

## 🎯 Bài tập 3: String Operations

**Mục tiêu**: Thực hành string concatenation và formatting

### Đề bài:

1. Tạo variables: `first_name`, `last_name`, `city`
2. Tạo `full_name` bằng cách ghép first_name và last_name
3. Tạo câu giới thiệu sử dụng f-string
4. In ra với format: "Hi, I'm [full_name] from [city]"
5. In độ dài của full_name

---

## 🎯 Bài tập 4: Input và Interactive Program

**Mục tiêu**: Tạo chương trình tương tác với user

### Đề bài:

Tạo chương trình hỏi user:

1. Tên
2. Năm sinh
3. Thành phố
4. Tính tuổi hiện tại (2024 - năm sinh)
5. In thông tin đầy đủ

### Expected output:

```
Enter your name: Alice
Enter birth year: 1995
Enter your city: Ho Chi Minh
Hello Alice! You are 29 years old and live in Ho Chi Minh.
```

---

## 🎯 Bài tập 5: Boolean và Comparisons

**Mục tiêu**: Làm việc với boolean values và comparison operators

### Đề bài:

1. Tạo 2 numbers: `a = 15`, `b = 10`
2. Tạo boolean variables cho các so sánh:
   - `is_greater`: a > b
   - `is_equal`: a == b
   - `is_different`: a != b
3. In tất cả kết quả với format rõ ràng

---

## 🎯 Bài tập 6: Simple Calculator

**Mục tiêu**: Kết hợp input, type conversion, và calculations

### Đề bài:

Tạo calculator đơn giản:

1. Hỏi user nhập 2 số
2. Thực hiện các phép tính: +, -, \*, /
3. In tất cả kết quả
4. Handle division by zero (bonus)

### Expected output:

```
Enter first number: 10
Enter second number: 3
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
```

---

## 🎯 Bài tập 7: Personal Information Card

**Mục tiêu**: Kết hợp tất cả kiến thức đã học

### Đề bài:

Tạo chương trình thu thập thông tin và tạo "business card":

1. Họ tên
2. Tuổi
3. Nghề nghiệp
4. Email
5. Số điện thoại

Xuất ra dạng card đẹp mắt.

### Expected output:

```
===============================
|     PERSONAL INFO CARD      |
===============================
| Name: Nguyen Van A          |
| Age: 25 years old           |
| Job: Data Scientist         |
| Email: nguyenvana@email.com |
| Phone: 0123456789           |
===============================
```

---

## 🎯 Bài tập 8: Temperature Converter

**Mục tiêu**: Thực hành formula calculations

### Đề bài:

1. Hỏi user nhập nhiệt độ Celsius
2. Convert sang Fahrenheit và Kelvin
3. In kết quả với format đẹp

### Công thức:

- Fahrenheit = (Celsius × 9/5) + 32
- Kelvin = Celsius + 273.15

---

## 🎯 Bài tập 9: Area Calculator

**Mục tiêu**: Geometry calculations với user input

### Đề bài:

Tạo calculator tính diện tích:

1. Hỏi user chọn hình: rectangle, circle, triangle
2. Hỏi thông số cần thiết
3. Tính và in diện tích

### Công thức:

- Rectangle: length × width
- Circle: π × r²
- Triangle: (base × height) / 2

---

## 🎯 Bài tập 10: Data Validation

**Mục tiêu**: Kiểm tra và validate user input

### Đề bài:

1. Hỏi user nhập tuổi
2. Kiểm tra input có phải số không
3. Kiểm tra tuổi có hợp lệ không (0-150)
4. In message phù hợp

### Hint:

Sử dụng `str.isdigit()` để kiểm tra string có phải số không.

---

## 📊 Scoring System

### Điểm số từng bài:

- **Bài 1-3**: 5 điểm mỗi bài (cơ bản)
- **Bài 4-6**: 10 điểm mỗi bài (trung bình)
- **Bài 7-9**: 15 điểm mỗi bài (khó)
- **Bài 10**: 20 điểm (challenging)

### Thang điểm:

- **90-100**: Excellent (A)
- **80-89**: Good (B)
- **70-79**: Average (C)
- **< 70**: Need more practice

---

## 🏃‍♂️ Challenge Exercises (Bonus)

### Challenge 1: BMI Calculator

Tính chỉ số BMI và đưa ra nhận xét sức khỏe.

### Challenge 2: Time Converter

Convert giữa seconds, minutes, hours, days.

### Challenge 3: Password Strength Checker

Kiểm tra độ mạnh của password dựa trên length và character types.

---

## 📝 Submission Checklist

- [ ] Hoàn thành tất cả 10 bài tập chính
- [ ] Code chạy không lỗi
- [ ] Output đúng format yêu cầu
- [ ] Có comments giải thích code
- [ ] Test với nhiều input khác nhau
- [ ] (Optional) Hoàn thành challenge exercises

---

**Next**: Kiểm tra đáp án trong thư mục `solutions/` và làm project trong `03_Project/`
