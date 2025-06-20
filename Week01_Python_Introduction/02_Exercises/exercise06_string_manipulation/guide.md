# Hướng dẫn: String Manipulation

## Lý thuyết cần biết

### 1. Chuỗi trong Python

- Chuỗi (string) là kiểu dữ liệu **immutable**
- Được bao bởi dấu nháy đơn `'` hoặc nháy đôi `"`
- Hỗ trợ Unicode đầy đủ

### 2. Các cách tạo chuỗi

#### Chuỗi đơn giản

```python
single_quote = 'Hello'
double_quote = "World"
mixed = "It's a beautiful day"
```

#### Chuỗi nhiều dòng

```python
multiline = """
Dòng 1
Dòng 2
Dòng 3
"""

# Hoặc
multiline2 = "Dòng 1\nDòng 2\nDòng 3"
```

#### Raw string

```python
# Không xử lý escape characters
path = r"C:\new\folder\file.txt"
regex = r"\d+\.\d+"
```

### 3. Nối chuỗi

#### Sử dụng toán tử +

```python
first = "Hello"
second = "World"
result = first + " " + second  # "Hello World"
```

#### Sử dụng f-string (Python 3.6+) - **Khuyến khích**

```python
name = "Alice"
age = 25
message = f"Tôi tên {name}, {age} tuổi"
```

#### Sử dụng .format()

```python
message = "Tôi tên {}, {} tuổi".format(name, age)
# Hoặc với index
message = "Tôi tên {0}, {1} tuổi".format(name, age)
# Hoặc với keyword
message = "Tôi tên {name}, {age} tuổi".format(name=name, age=age)
```

#### Sử dụng % formatting (cách cũ)

```python
message = "Tôi tên %s, %d tuổi" % (name, age)
```

### 4. Phương thức chuỗi quan trọng

#### Thay đổi case

```python
text = "Hello World"
text.upper()        # "HELLO WORLD"
text.lower()        # "hello world"
text.title()        # "Hello World"
text.capitalize()   # "Hello world"
text.swapcase()     # "hELLO wORLD"
```

#### Xử lý khoảng trắng

```python
messy = "   Hello World   "
messy.strip()       # "Hello World"
messy.lstrip()      # "Hello World   "
messy.rstrip()      # "   Hello World"
```

#### Chia và nối

```python
text = "apple,banana,cherry"
fruits = text.split(",")        # ["apple", "banana", "cherry"]
joined = "-".join(fruits)       # "apple-banana-cherry"
```

#### Thay thế

```python
text = "Hello World"
new_text = text.replace("World", "Python")  # "Hello Python"
```

#### Tìm kiếm

```python
text = "Hello World"
text.find("World")      # 6 (index của "World")
text.find("xyz")        # -1 (không tìm thấy)
text.index("World")     # 6 (giống find nhưng raise exception nếu không có)
text.count("l")         # 3 (đếm số lần xuất hiện)
```

### 5. Kiểm tra chuỗi

#### Kiểm tra nội dung

```python
text = "Hello World"
text.startswith("Hello")    # True
text.endswith("World")      # True
"World" in text             # True
"xyz" in text               # False
```

#### Kiểm tra kiểu ký tự

```python
"123".isdigit()         # True
"abc".isalpha()         # True
"abc123".isalnum()      # True
"   ".isspace()         # True
"Hello World".islower() # False
"HELLO".isupper()       # True
```

### 6. Indexing và Slicing

#### Indexing

```python
text = "Python"
text[0]     # 'P'
text[-1]    # 'n' (từ cuối)
```

#### Slicing

```python
text = "Python"
text[1:4]   # 'yth'
text[:3]    # 'Pyt'
text[2:]    # 'thon'
text[::-1]  # 'nohtyP' (reverse)
```

## Các bước thực hiện

### Bước 1: Tạo và nối chuỗi cơ bản

```python
first_name = "Nguyen"
last_name = "Van A"
full_name = first_name + " " + last_name
greeting = "Xin chào, " + full_name + "!"
```

### Bước 2: Thực hành định dạng

```python
age = 20

# F-string (modern)
intro_f = f"Tôi tên {full_name}, {age} tuổi"

# Format method
intro_format = "Tôi tên {}, {} tuổi".format(full_name, age)

# % formatting (legacy)
intro_percent = "Tôi tên %s, %d tuổi" % (full_name, age)
```

### Bước 3: Sử dụng phương thức chuỗi

```python
# Case conversion
upper_name = full_name.upper()
lower_name = full_name.lower()
title_name = full_name.title()

# Thông tin chuỗi
length = len(full_name)
contains_van = "Van" in full_name
```

### Bước 4: Xử lý khoảng trắng

```python
messy_string = "   Hello World   "
clean = messy_string.strip()
left_clean = messy_string.lstrip()
right_clean = messy_string.rstrip()
```

### Bước 5: Chia và ghép

```python
# Chia chuỗi
words = full_name.split()  # Split by whitespace
words = full_name.split(" ")  # Split by space explicitly

# Thay thế
formal_name = full_name.replace("Nguyen", "Mr. Nguyen")

# Ghép lại
hyphenated = "-".join(words)
```

### Bước 6: Kiểm tra chuỗi

```python
starts_with_nguyen = full_name.startswith("Nguyen")
ends_with_a = full_name.endswith("A")
is_alpha = full_name.isalpha()  # False vì có space
is_digit = full_name.isdigit()  # False
```

## Lưu ý quan trọng

### 1. Immutability

```python
text = "hello"
text.upper()    # Trả về "HELLO"
print(text)     # Vẫn là "hello" (không thay đổi)

# Muốn thay đổi phải gán lại
text = text.upper()
```

### 2. Escape Characters

```python
# Các ký tự đặc biệt
newline = "Dòng 1\nDòng 2"
tab = "Cột 1\tCột 2"
quote = "Anh ấy nói \"Hello\""
backslash = "Path: C:\\folder"

# Raw string để tránh escape
path = r"C:\new\folder"
```

### 3. Unicode Support

```python
# Python 3 hỗ trợ Unicode tự nhiên
vietnamese = "Xin chào Việt Nam"
emoji = "Python 🐍 is awesome! 😍"
```

### 4. Performance Tips

```python
# Tránh nối chuỗi trong vòng lặp
# ❌ Không tốt
result = ""
for i in range(1000):
    result += str(i)

# ✅ Tốt hơn
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)

# ✅ Hoặc dùng f-string
numbers = [str(i) for i in range(1000)]
result = "".join(numbers)
```

## Tips & Tricks

### 1. Multiple replacements

```python
text = "Hello World World"
# Thay thế tất cả
text.replace("World", "Python")  # "Hello Python Python"
# Thay thế 1 lần đầu
text.replace("World", "Python", 1)  # "Hello Python World"
```

### 2. String alignment

```python
text = "Python"
text.center(10)     # "  Python  "
text.ljust(10)      # "Python    "
text.rjust(10)      # "    Python"
text.zfill(10)      # "0000Python"
```

### 3. Case insensitive operations

```python
text1 = "Hello"
text2 = "hello"
text1.lower() == text2.lower()  # True
```

### 4. String validation

```python
def is_valid_name(name):
    return (name.isalpha() and
            len(name) >= 2 and
            name.istitle())
```
