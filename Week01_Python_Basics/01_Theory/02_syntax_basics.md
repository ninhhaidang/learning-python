# Cú Pháp Cơ Bản Python

## 1. Indentation (Thụt Lề)

Python sử dụng indentation để nhóm các câu lệnh thay vì dấu ngoặc nhọn `{}` như các ngôn ngữ khác.

### Ví dụ:

```python
# Đúng
if True:
    print("This is indented")
    print("This is also indented")

# Sai - IndentationError
if True:
print("This will cause an error")
```

### Quy tắc Indentation:

- Sử dụng **4 spaces** (khuyến nghị) hoặc **1 tab**
- Phải **nhất quán** trong toàn bộ chương trình
- Không trộn lẫn spaces và tabs

## 2. Comments (Chú Thích)

Comments giúp giải thích code và không được thực thi.

### Single-line Comments:

```python
# Đây là comment một dòng
print("Hello World")  # Comment cuối dòng
```

### Multi-line Comments:

```python
"""
Đây là comment nhiều dòng
Có thể viết nhiều dòng
Để giải thích code phức tạp
"""

'''
Cũng có thể sử dụng dấu nháy đơn
Để tạo comment nhiều dòng
'''
```

### Docstrings:

```python
def my_function():
    """
    Đây là docstring - tài liệu cho function
    Mô tả chức năng, tham số, và giá trị trả về
    """
    return "Hello"
```

## 3. Variables (Biến)

### Khai báo biến:

```python
# Python tự động xác định kiểu dữ liệu
name = "John"        # String
age = 25             # Integer
height = 5.9         # Float
is_student = True    # Boolean
```

### Quy tắc đặt tên biến:

```python
# Đúng
user_name = "John"
user_age = 25
_private_var = "hidden"
MyClass = "Class name"

# Sai
2name = "Invalid"        # Bắt đầu bằng số
user-name = "Invalid"    # Có dấu gạch ngang
if = "Invalid"           # Từ khóa reserved
```

### Naming Conventions:

- **snake_case**: cho variables và functions
- **PascalCase**: cho classes
- **UPPER_CASE**: cho constants

```python
# Variables và functions
user_name = "John"
def calculate_area():
    pass

# Classes
class DataProcessor:
    pass

# Constants
MAX_SIZE = 100
PI = 3.14159
```

## 4. Keywords (Từ Khóa)

Python có 35 từ khóa reserved không thể dùng làm tên biến:

```python
import keyword
print(keyword.kwlist)

# Output:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## 5. Statements và Expressions

### Statement:

Câu lệnh thực hiện một hành động

```python
x = 5          # Assignment statement
print("Hi")    # Function call statement
if x > 0:      # Conditional statement
    pass
```

### Expression:

Biểu thức tạo ra một giá trị

```python
x + y          # Arithmetic expression
x > 5          # Comparison expression
"Hello" * 3    # String expression
```

## 6. Line Structure

### Logical Lines:

```python
# Một logical line
x = 1

# Nhiều statements trong một line (không khuyến nghị)
x = 1; y = 2; print(x + y)
```

### Physical Lines:

```python
# Line continuation với backslash
total = 1 + 2 + 3 + \
        4 + 5 + 6

# Line continuation với parentheses (khuyến nghị)
total = (1 + 2 + 3 +
         4 + 5 + 6)

# Với lists, dicts
my_list = [1, 2, 3,
           4, 5, 6]
```

## 7. Code Blocks

Python sử dụng indentation để định nghĩa code blocks:

```python
# If statement
if condition:
    # Code block
    statement1
    statement2

# Function definition
def my_function():
    # Code block
    statement1
    statement2

# Loop
for i in range(5):
    # Code block
    print(i)
```

## 8. Encoding

Python 3 mặc định sử dụng UTF-8:

```python
# Chỉ định encoding (thường không cần thiết)
# -*- coding: utf-8 -*-

# Unicode strings
greeting = "Xin chào"
name = "Nguyễn Văn A"
```

## 9. Ví Dụ Thực Tế

```python
# Program tính diện tích hình chữ nhật
"""
Chương trình tính diện tích và chu vi hình chữ nhật
Author: Student
Date: 2024
"""

# Constants
PROGRAM_NAME = "Rectangle Calculator"

# Variables
length = 10.5    # Chiều dài
width = 8.2      # Chiều rộng

# Calculations
area = length * width                    # Diện tích
perimeter = 2 * (length + width)        # Chu vi

# Output
print(f"Program: {PROGRAM_NAME}")
print(f"Length: {length}")
print(f"Width: {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
```

## 10. Best Practices

### 1. **Code Readability**

```python
# Tốt
user_age = 25
if user_age >= 18:
    print("Adult")

# Không tốt
a = 25
if a >= 18: print("Adult")
```

### 2. **Meaningful Names**

```python
# Tốt
temperature_celsius = 25
max_retry_attempts = 3

# Không tốt
temp = 25
x = 3
```

### 3. **Consistent Formatting**

```python
# Tốt - spaces around operators
result = a + b * c

# Không tốt
result=a+b*c
```

### 4. **Comments Usage**

```python
# Tốt - explain WHY, not WHAT
# Calculate compound interest for investment planning
interest = principal * (1 + rate) ** time

# Không tốt
interest = principal * (1 + rate) ** time  # Calculate interest
```

## Bài Tập Thực Hành

1. Viết chương trình với comments giải thích từng dòng
2. Tạo variables với các naming conventions khác nhau
3. Thực hành line continuation với biểu thức dài
4. Sửa lỗi indentation trong code cho sẵn

## Lỗi Thường Gặp

1. **IndentationError**: Sai thụt lề
2. **SyntaxError**: Sai cú pháp
3. **NameError**: Tên biến chưa được định nghĩa
4. **TypeError**: Sai kiểu dữ liệu
