# 📖 Week 1 - Theory: Giới Thiệu Python và Môi Trường Phát Triển

## 📚 Mục lục

1. [Python là gì và tại sao chọn Python?](#1-python-là-gì)
2. [Cài đặt môi trường phát triển](#2-cài-đặt-môi-trường)
3. [Python Syntax cơ bản](#3-python-syntax-cơ-bản)
4. [Variables và Data Types](#4-variables-và-data-types)
5. [Input/Output cơ bản](#5-inputoutput-cơ-bản)

---

## 1. Python là gì?

### 🐍 Giới thiệu Python

Python là ngôn ngữ lập trình high-level, interpreted, và general-purpose được tạo ra bởi Guido van Rossum năm 1991.

### ✨ Đặc điểm nổi bật

- **Dễ học, dễ đọc**: Syntax giống ngôn ngữ tự nhiên
- **Interpreted**: Không cần compile, chạy trực tiếp
- **Cross-platform**: Chạy trên Windows, Mac, Linux
- **Open source**: Miễn phí và có cộng đồng lớn
- **Versatile**: Web, AI, Data Science, Automation, etc.

### 🎯 Tại sao Python cho Data Science?

1. **Thư viện phong phú**: NumPy, Pandas, Matplotlib, Scikit-learn
2. **Cộng đồng mạnh**: Hỗ trợ và tài liệu dồi dào
3. **Jupyter Notebook**: Interactive development
4. **Performance**: Tích hợp với C/C++ cho tốc độ
5. **Industry adoption**: Được sử dụng rộng rãi

### 🌍 Ứng dụng trong GIS và Viễn thám

- **Xử lý dữ liệu raster**: GDAL, Rasterio
- **Phân tích vector**: Geopandas, Shapely
- **Machine Learning**: Scikit-learn, TensorFlow
- **Visualization**: Matplotlib, Folium, Plotly
- **Automation**: Batch processing, workflows

---

## 2. Cài đặt Môi Trường

### 🐍 Lựa chọn 1: Anaconda (Khuyến nghị)

Anaconda là distribution Python chứa sẵn các package cần thiết cho Data Science.

#### Bước cài đặt:

1. **Download**: Truy cập [anaconda.com](https://www.anaconda.com/products/distribution)
2. **Chọn version**: Python 3.9+ cho hệ điều hành của bạn
3. **Install**: Chạy installer và follow hướng dẫn
4. **Verify**: Mở Anaconda Navigator hoặc terminal

#### Kiểm tra cài đặt:

```bash
# Mở terminal/command prompt
python --version
conda --version
jupyter --version
```

### 💻 Lựa chọn 2: Python Official + pip

Nếu bạn muốn cài đặt lightweight hơn:

1. **Download Python**: [python.org/downloads](https://www.python.org/downloads/)
2. **Install packages**:

```bash
pip install jupyter pandas numpy matplotlib
```

### 🔧 Cài đặt VS Code

1. **Download**: [code.visualstudio.com](https://code.visualstudio.com/)
2. **Install Python Extension**:
   - Mở VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search "Python" by Microsoft
   - Install

### 📝 Cài đặt Git (Tùy chọn nhưng khuyến nghị)

- **Windows**: [git-scm.com](https://git-scm.com/)
- **Mac**: `brew install git` hoặc Xcode Command Line Tools
- **Linux**: `sudo apt install git` (Ubuntu/Debian)

---

## 3. Python Syntax Cơ Bản

### 🔤 Comments (Ghi chú)

```python
# Đây là single-line comment

\"\"\"
Đây là multi-line comment
Có thể viết nhiều dòng
\"\"\"

'''
Cách khác để viết
multi-line comment
'''
```

### 📏 Indentation (Thụt đầu dòng)

Python sử dụng indentation để định nghĩa code blocks:

```python
# Đúng
if True:
    print("Hello")  # 4 spaces hoặc 1 tab
    print("World")

# Sai - IndentationError
if True:
print("Hello")  # Không có indentation
```

### 🎯 Case Sensitivity

Python phân biệt chữ hoa chữ thường:

```python
name = "Python"
Name = "Java"
NAME = "C++"

print(name)  # Python
print(Name)  # Java
print(NAME)  # C++
```

### 📝 Naming Conventions

- **Variables/functions**: snake_case (my_variable, calculate_area)
- **Constants**: UPPER_CASE (PI, MAX_SIZE)
- **Classes**: PascalCase (MyClass, DataProcessor)

---

## 4. Variables và Data Types

### 🔢 Declaring Variables

```python
# Không cần khai báo kiểu dữ liệu
name = "Alice"          # String
age = 25               # Integer
height = 1.75          # Float
is_student = True      # Boolean
```

### 📊 Basic Data Types

#### 🔤 String

```python
# Tạo string
first_name = "John"
last_name = 'Doe'
full_name = \"\"\"John Doe\"\"\"

# String concatenation
greeting = "Hello " + first_name
print(greeting)  # Hello John

# String formatting
message = f"My name is {first_name} {last_name}"
print(message)  # My name is John Doe
```

#### 🔢 Numbers

```python
# Integer
count = 10
year = 2024

# Float
temperature = 25.5
pi = 3.14159

# Operations
result = count + temperature  # 35.5
power = 2 ** 3               # 8 (2^3)
division = 10 / 3            # 3.333...
integer_division = 10 // 3   # 3
remainder = 10 % 3           # 1
```

#### ✅ Boolean

```python
is_active = True
is_completed = False

# Boolean operations
result1 = True and False  # False
result2 = True or False   # True
result3 = not True        # False
```

### 🔍 Type Checking

```python
name = "Python"
print(type(name))      # <class 'str'>
print(isinstance(name, str))  # True

age = 25
print(type(age))       # <class 'int'>
```

### 🔄 Type Conversion

```python
# String to number
age_str = "25"
age_int = int(age_str)      # 25
height_str = "1.75"
height_float = float(height_str)  # 1.75

# Number to string
count = 10
count_str = str(count)      # "10"

# Boolean conversion
print(bool(1))     # True
print(bool(0))     # False
print(bool(""))    # False
print(bool("Hi"))  # True
```

---

## 5. Input/Output Cơ Bản

### 📤 Output với print()

```python
# Basic printing
print("Hello, World!")

# Multiple values
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Formatted output
print(f"My name is {name} and I am {age} years old")

# Print with separators
print("A", "B", "C", sep="-")  # A-B-C
print("Line 1", end=" ")
print("Line 2")  # Line 1 Line 2
```

### 📥 Input với input()

```python
# Basic input (always returns string)
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input with type conversion
age_str = input("Enter your age: ")
age = int(age_str)
print(f"You are {age} years old")

# One-liner conversion
height = float(input("Enter your height (m): "))
```

### 🔧 Ví dụ thực hành

```python
# Simple calculator
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Error: Invalid operator!"

print(f"Result: {result}")
```

---

## 📝 Tóm tắt Kiến Thức

### ✅ Những điều đã học:

1. Python là ngôn ngữ ideal cho Data Science và GIS
2. Cài đặt môi trường với Anaconda hoặc Python official
3. Python syntax cơ bản: comments, indentation, naming
4. Variables và basic data types: string, int, float, bool
5. Input/output với print() và input()

### 🎯 Kỹ năng cần thành thạo:

- [ ] Viết và chạy Python script đơn giản
- [ ] Sử dụng variables đúng cách
- [ ] Type conversion giữa các kiểu dữ liệu
- [ ] Input/output cơ bản
- [ ] Debug lỗi syntax đơn giản

### 🔗 Đọc thêm:

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python - Python Basics](https://realpython.com/python-basics/)
- [Automate the Boring Stuff - Chapter 1](https://automatetheboringstuff.com/2e/chapter1/)

---

**Tiếp theo**: Làm bài tập trong thư mục `02_Exercises/`
