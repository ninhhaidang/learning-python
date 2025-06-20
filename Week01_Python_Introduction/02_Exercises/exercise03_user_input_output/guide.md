# Exercise 03: User Input & Output - Guide

## 🎯 Mục tiêu học tập

Bài tập này giúp bạn:

- Học cách sử dụng hàm `input()` để tương tác với người dùng
- Xử lý các kiểu dữ liệu khác nhau từ input
- Chuyển đổi kiểu dữ liệu (type conversion)
- Tạo output được định dạng đẹp mắt
- Thực hiện tính toán cơ bản với dữ liệu người dùng

## 📋 Chuẩn bị

### Kiến thức cần nắm:

- Hàm `print()` và `input()`
- Kiểu dữ liệu: string, int, float, boolean
- Type conversion: `int()`, `float()`, `str()`
- String formatting với f-strings
- Phép tính toán cơ bản

### Tools cần thiết:

- Python 3.x
- Text editor hoặc IDE
- Terminal để chạy chương trình

## 🚀 Hướng dẫn từng bước

### Bước 1: Thiết lập structure cơ bản

```python
# Tạo header chương trình
print("=== Personal Information Collector ===")
print()
print("Please enter your information:")
```

**💡 Giải thích:**

- Sử dụng `print()` để tạo header và hướng dẫn
- `print()` rỗng tạo dòng trống để format đẹp

### Bước 2: Thu thập thông tin cơ bản

```python
# Input string - không cần conversion
full_name = input("Enter your full name: ")

# Input number - cần convert từ string
age_str = input("Enter your age: ")
age = int(age_str)

# Hoặc viết gọn hơn
age = int(input("Enter your age: "))
```

**💡 Tips:**

- `input()` luôn trả về string
- Phải convert sang int/float khi cần tính toán
- Nên xử lý từng bước trước khi viết gọn

### Bước 3: Xử lý các kiểu dữ liệu khác nhau

```python
# Float input
height = float(input("Enter your height in meters: "))

# String input
favorite_color = input("Enter your favorite color: ")

# Boolean-like input
student_input = input("Are you a student? (yes/no): ")
is_student = student_input.lower() == "yes"

# Integer input for calculations
current_year = int(input("Enter current year: "))
```

**💡 Kỹ thuật quan trọng:**

- Sử dụng `.lower()` để handle cả "Yes", "YES", "yes"
- So sánh string để tạo boolean value

### Bước 4: Thực hiện tính toán

```python
# Tính toán birth year
birth_year = current_year - age

# Chuyển đổi height sang feet
height_feet = height * 3.28084

# Tính BMI (giả sử có weight)
# BMI = weight / (height^2)
# Hoặc tính toán khác dựa trên yêu cầu
```

### Bước 5: Format output đẹp mắt

```python
print()
print("=== PERSONAL PROFILE ===")
print("┌─────────────────────────────────┐")
print("│         PROFILE SUMMARY         │")
print("├─────────────────────────────────┤")
print(f"│ Name: {full_name:<20} │")
print(f"│ Age: {age} years old{'':<12} │")
print(f"│ Height: {height}m ({height_feet:.2f} feet) │")
print(f"│ Favorite Color: {favorite_color:<12} │")
print(f"│ Student Status: {'Yes' if is_student else 'No':<10} │")
print(f"│ Birth Year: {birth_year:<16} │")
print("└─────────────────────────────────┘")
```

**💡 String formatting tips:**

- `{name:<20}` - căn trái với 20 ký tự
- `{value:.2f}` - hiển thị 2 chữ số thập phân
- `{'Yes' if condition else 'No'}` - conditional expression

## 🔍 Các vấn đề thường gặp

### Lỗi 1: ValueError khi convert

```python
# Sai - user nhập text thay vì số
age = int(input("Enter age: "))  # User nhập "twenty"

# Solution: Add validation
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number")
    age = 0  # default value
```

### Lỗi 2: String formatting không đúng

```python
# Sai
print(f"Name: {name} Age: {age}")

# Đúng - có spacing và format
print(f"Name: {name:<15} Age: {age} years")
```

### Lỗi 3: Boolean conversion

```python
# Sai - không handle các case khác nhau
is_student = input("Student? ") == "yes"

# Đúng - handle multiple formats
student_input = input("Are you a student? (yes/no): ").lower()
is_student = student_input in ["yes", "y", "true", "1"]
```

## 💡 Mẹo nâng cao

### 1. Input validation

```python
while True:
    try:
        age = int(input("Enter age: "))
        if age > 0:
            break
        else:
            print("Age must be positive")
    except ValueError:
        print("Please enter a valid number")
```

### 2. Multi-line strings

```python
profile = f"""
=== PROFILE ===
Name: {name}
Age: {age}
Height: {height}m
"""
print(profile)
```

### 3. Dynamic formatting

```python
# Tính width dựa trên content
max_width = max(len(name), len(favorite_color)) + 10
border = "─" * max_width
print(f"┌{border}┐")
```

## 🧪 Test cases

### Test 1: Normal input

```
Input: Alice, 25, 1.68, Blue, no, 2024
Expected: Correct calculations và formatting
```

### Test 2: Edge cases

```
Input: Very Long Name, 0, 0.5, Red, yes, 2024
Expected: Handle long names, edge values
```

### Test 3: Different formats

```
Input: john, 30, 1.8, GREEN, YES, 2024
Expected: Handle case differences
```

## ✅ Checklist hoàn thành

- [ ] Thu thập được tất cả input cần thiết
- [ ] Chuyển đổi kiểu dữ liệu đúng cách
- [ ] Thực hiện tính toán chính xác
- [ ] Output có format đẹp mắt
- [ ] Xử lý được các case khác nhau của yes/no
- [ ] Code có comment giải thích rõ ràng

## 🔗 Kiến thức liên quan

- **Input/Output operations**: Cơ bản về tương tác user
- **Type conversion**: Chuyển đổi giữa string, int, float
- **String formatting**: f-strings, format specifiers
- **Conditional expressions**: Ternary operator
- **String methods**: `.lower()`, `.strip()`, etc.

## 🎯 Thử thách thêm

1. **Validation**: Thêm kiểm tra input hợp lệ
2. **More calculations**: BMI, ideal weight, age group
3. **Better formatting**: Colors, alignment, borders
4. **File output**: Lưu profile vào file
5. **Multiple profiles**: Thu thập nhiều người

Chúc bạn coding vui vẻ! 🚀
