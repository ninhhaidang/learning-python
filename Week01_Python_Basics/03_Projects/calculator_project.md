# Week 1 - Project: Python Calculator

**Dự án Calculator tích hợp kiến thức Week 1**

## 🎯 Mục tiêu

- Tích hợp tất cả kiến thức đã học trong Week 1
- Xây dựng calculator với giao diện text-based
- Xử lý input, validation, và error handling
- Sử dụng functions để tổ chức code tốt hơn
- Thực hành làm việc với menu và lựa chọn người dùng

## 📋 Yêu cầu chức năng

### 🔢 1. Phép toán cơ bản

Tạo chức năng thực hiện các phép toán:

- Cộng (+)
- Trừ (-)
- Nhân (\*)
- Chia (/)
- Chia lấy dư (%)
- Lũy thừa (\*\*)

**Yêu cầu kỹ thuật:**

- Xử lý chia cho 0
- Xử lý lũy thừa quá lớn
- Định dạng kết quả đẹp

### 🌡️ 2. Chuyển đổi nhiệt độ

Tạo chức năng chuyển đổi giữa:

- Celsius ↔ Fahrenheit
- Celsius ↔ Kelvin

**Công thức:**

- F = (C × 9/5) + 32
- K = C + 273.15

### 📏 3. Chuyển đổi độ dài

Tạo chức năng chuyển đổi giữa:

- Meter ↔ Kilometer
- Meter ↔ Centimeter
- Meter ↔ Feet (1m = 3.28084ft)

### 💰 4. Chuyển đổi tiền tệ

Tạo chức năng chuyển đổi giữa:

- USD ↔ VND (tỷ giá: 1 USD = 24,000 VND)
- EUR ↔ VND (tỷ giá: 1 EUR = 26,000 VND)

### 📐 5. Tính toán hình học

Tạo chức năng tính chu vi và diện tích:

- **Hình tròn**: chu vi = 2πr, diện tích = πr²
- **Hình chữ nhật**: chu vi = 2(d+r), diện tích = d×r
- **Hình tam giác**: diện tích = ½×đáy×cao
- **Hình vuông**: chu vi = 4×cạnh, diện tích = cạnh²

### 📜 6. Lịch sử tính toán

- Lưu trữ 10 phép tính gần nhất
- Hiển thị lịch sử
- Xóa lịch sử

### 🎛️ 7. Menu điều hướng

Tạo menu chính với các lựa chọn:

```
📋 MENU CHÍNH:
1. Phép toán cơ bản
2. Chuyển đổi nhiệt độ
3. Chuyển đổi độ dài
4. Chuyển đổi tiền tệ
5. Tính toán hình học
6. Xem lịch sử
7. Xóa lịch sử
0. Thoát
```

## 🛠️ Yêu cầu kỹ thuật

### Input Validation

- Kiểm tra input số hợp lệ
- Xử lý exception (try-except)
- Thông báo lỗi rõ ràng

### Code Organization

- Chia thành functions riêng biệt
- Sử dụng docstring cho functions
- Comments rõ ràng

### User Experience

- Giao diện thân thiện
- Header và footer đẹp
- Pause để user đọc kết quả
- Xử lý Ctrl+C gracefully

## 📝 Ví dụ input/output

### Ví dụ 1: Phép toán cơ bản

```
🧮 PYTHON CALCULATOR - WEEK 1 PROJECT
============================================================

📋 MENU CHÍNH:
1. Phép toán cơ bản
...
Chọn chức năng (0-7): 1

➕ PHÉP TOÁN CỞ BẢN
------------------------------
Nhập số thứ nhất: 15
Nhập phép toán: +
Nhập số thứ hai: 7

✅ Kết quả: 15.0 + 7.0 = 22
```

### Ví dụ 2: Chuyển đổi nhiệt độ

```
Chọn chức năng (0-7): 2

🌡️  CHUYỂN ĐỔI NHIỆT ĐỘ
------------------------------
1. Celsius sang Fahrenheit
2. Fahrenheit sang Celsius
...
Chọn loại chuyển đổi: 1
Nhập nhiệt độ Celsius: 25

✅ 25.0°C = 77.0°F
```

### Ví dụ 3: Tính toán hình học

```
Chọn chức năng (0-7): 5

📐 TÍNH TOÁN HÌNH HỌC
------------------------------
1. Hình tròn (chu vi và diện tích)
...
Chọn hình: 1
Nhập bán kính: 5

✅ Hình tròn bán kính 5.0:
   Chu vi: 31.42
   Diện tích: 78.54
```

### Ví dụ 4: Xem lịch sử

```
Chọn chức năng (0-7): 6

📜 LỊCH SỬ TÍNH TOÁN
----------------------------------------
 1. 15.0 + 7.0 = 22
 2. Temperature conversion: 25.0°C = 77.0°F
 3. Geometry: Circle r=5.0: C=31.42, A=78.54
----------------------------------------
```

### Ví dụ 5: Xử lý lỗi

```
Nhập số thứ nhất: abc
❌ Lỗi: Vui lòng nhập một số hợp lệ!
Nhập số thứ nhất: 10

Nhập phép toán: /
Nhập số thứ hai: 0
❌ Lỗi: Không thể chia cho 0!
```

## 🏗️ Hướng dẫn triển khai

### Bước 1: Tạo cấu trúc cơ bản

1. Import các module cần thiết
2. Tạo global variables (lịch sử, tỷ giá)
3. Tạo utility functions (input validation, format result)

### Bước 2: Implement từng chức năng

1. Basic arithmetic function
2. Temperature conversion function
3. Length conversion function
4. Currency conversion function
5. Geometry calculation function

### Bước 3: Tạo hệ thống menu

1. Display header function
2. Display menu function
3. Main loop với switch-case logic

### Bước 4: Xử lý lịch sử

1. Add to history function
2. Display history function
3. Clear history function

### Bước 5: Testing và debugging

1. Test từng chức năng
2. Test edge cases
3. Test error handling

## 🎯 Mức độ hoàn thành

### Cơ bản (70%)

- [ ] Menu chính hoạt động
- [ ] Phép toán cơ bản (+, -, \*, /)
- [ ] 1-2 loại chuyển đổi đơn vị
- [ ] Validation cơ bản

### Khá (85%)

- [ ] Tất cả phép toán cơ bản (bao gồm %, \*\*)
- [ ] Tất cả chuyển đổi nhiệt độ và độ dài
- [ ] Tính toán hình học cơ bản
- [ ] Error handling tốt

### Giỏi (100%)

- [ ] Tất cả chức năng yêu cầu
- [ ] Lịch sử tính toán
- [ ] Giao diện đẹp với emoji và formatting
- [ ] Code tổ chức tốt với functions
- [ ] Documentation đầy đủ

## 💡 Gợi ý

### Code Structure

```python
import math

# Global variables
calculation_history = []
EXCHANGE_RATES = {...}

# Utility functions
def get_number_input(prompt):
    # Validation logic here
    pass

def add_to_history(calculation, result):
    # History management
    pass

# Feature functions
def basic_arithmetic():
    pass

def temperature_conversion():
    pass

# Main program
def main():
    while True:
        display_menu()
        choice = get_integer_input("Chọn: ")

        if choice == 1:
            basic_arithmetic()
        # ... other choices

        input("Nhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()
```

### Best Practices

- Sử dụng f-strings cho formatting
- Tạo constants cho magic numbers
- Validation input trước khi xử lý
- Meaningful variable names
- Comments cho logic phức tạp

## 📚 Kiến thức cần sử dụng

- Variables và data types
- Input/output
- Conditional statements (if/elif/else)
- Loops (while)
- Functions
- String formatting
- Exception handling (try/except)
- Math module
- Lists và dictionaries (basic)

---

**Chúc bạn coding vui vẻ! 🚀**

> Nhớ test từng chức năng một cách kỹ lưỡng và xử lý các edge cases!
