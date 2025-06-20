# Hướng dẫn: Data Types Exploration

## Lý thuyết cần biết

### 1. Hệ thống kiểu dữ liệu trong Python

Python có các kiểu dữ liệu cơ bản sau:

#### A. Kiểu số (Numeric Types)

```python
# Integer (số nguyên)
age = 25
negative = -10
large_num = 1_000_000  # Có thể dùng underscore để dễ đọc

# Float (số thực)
pi = 3.14159
temperature = -5.5
scientific = 2.5e3  # 2500.0 (scientific notation)

# Complex (số phức)
z = 3 + 4j
```

#### B. Kiểu chuỗi (String)

```python
# Chuỗi đơn giản
name = "Python"
message = 'Hello World'

# Chuỗi nhiều dòng
text = """
Đây là chuỗi
nhiều dòng
"""

# Raw string (không xử lý escape characters)
path = r"C:\new\folder\text.txt"

# Unicode
greeting = "Xin chào 🐍"
```

#### C. Kiểu Boolean

```python
is_active = True
is_finished = False

# Chuyển đổi sang Boolean
bool(1)      # True
bool(0)      # False
bool("")     # False (chuỗi rỗng)
bool("hi")   # True
bool([])     # False (list rỗng)
bool([1])    # True
```

#### D. Collection Types

**List (Danh sách - Mutable)**

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]
```

**Tuple (Bộ - Immutable)**

```python
point = (10, 20)
single = (42,)  # Cần dấu phẩy cho tuple 1 phần tử
rgb = (255, 128, 0)
```

**Dictionary (Từ điển - Mutable)**

```python
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 90, 88]
}
```

**Set (Tập hợp - Mutable)**

```python
unique = {1, 2, 3, 4, 5}
from_list = set([1, 1, 2, 2, 3])  # {1, 2, 3}
```

### 2. Mutable vs Immutable

#### Immutable (Không thể thay đổi)

- int, float, complex, str, tuple, bool
- Khi "thay đổi", Python tạo object mới

```python
x = 10
id_before = id(x)
x = 20
id_after = id(x)
# id_before != id_after
```

#### Mutable (Có thể thay đổi)

- list, dict, set
- Có thể thay đổi nội dung mà không tạo object mới

```python
my_list = [1, 2, 3]
id_before = id(my_list)
my_list.append(4)
id_after = id(my_list)
# id_before == id_after
```

## Các bước thực hiện

### Bước 1: Khám phá kiểu số

```python
# Các loại số
integer_num = 42
float_num = 3.14159
scientific_num = 2e5      # 200000.0
complex_num = 3 + 4j

# Kiểm tra kiểu
print(f"integer_num: {integer_num}, type: {type(integer_num)}")
print(f"float_num: {float_num}, type: {type(float_num)}")
print(f"scientific_num: {scientific_num}, type: {type(scientific_num)}")
print(f"complex_num: {complex_num}, type: {type(complex_num)}")
```

### Bước 2: Khám phá chuỗi

```python
simple_string = "Hello Python"
multiline_string = """Dòng 1
Dòng 2
Dòng 3"""
raw_string = r"C:\new\text.txt"
unicode_string = "Xin chào 🐍"

print(f"simple_string: {simple_string}")
print(f"multiline_string có {len(multiline_string.splitlines())} dòng")
print(f"raw_string: {raw_string}")
print(f"unicode_string: {unicode_string}")
```

### Bước 3: Khám phá Boolean

```python
is_true = True
is_false = False
bool_from_number = bool(10)    # True
bool_from_string = bool("")    # False

print(f"is_true: {is_true}")
print(f"is_false: {is_false}")
print(f"bool(10): {bool_from_number}")
print(f"bool(''): {bool_from_string}")
```

### Bước 4: Khám phá Collections

```python
# List
number_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]

# Tuple
coordinate = (10, 20)
single_tuple = (42,)
color_rgb = (255, 128, 0)

# Dictionary
student_info = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Set
unique_numbers = {1, 2, 3, 4, 5}
set_from_list = set([1, 1, 2, 2, 3, 3])  # {1, 2, 3}
```

### Bước 5: Phân tích tính chất

```python
# Kiểm tra độ dài
collections = [
    ("number_list", number_list),
    ("mixed_list", mixed_list),
    ("nested_list", nested_list),
    ("coordinate", coordinate),
    ("student_info", student_info),
    ("unique_numbers", unique_numbers)
]

for name, collection in collections:
    print(f"{name}: {collection}, length = {len(collection)}")
```

## Lưu ý quan trọng

### 1. Type Checking

```python
# Kiểm tra kiểu chính xác
type(42) == int          # True
isinstance(42, int)      # True (preferred)

# Kiểm tra nhiều kiểu
isinstance(42, (int, float))  # True
```

### 2. Memory Efficiency

```python
# Python cache số nhỏ (-5 đến 256)
a = 100
b = 100
print(id(a) == id(b))    # True

a = 1000
b = 1000
print(id(a) == id(b))    # False (có thể)
```

### 3. Duck Typing

```python
# "If it walks like a duck, quacks like a duck, it's a duck"
def print_length(obj):
    try:
        print(len(obj))
    except TypeError:
        print("Object doesn't have length")
```

## Tips & Tricks

### 1. Type Conversion

```python
# String to Number
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

# Number to String
age = 25
age_str = str(age)

# List/Tuple conversion
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
```

### 2. Collection Tricks

```python
# Unpacking
point = (10, 20)
x, y = point

# List comprehension preview
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Dictionary comprehension preview
word_lengths = {word: len(word) for word in ["hi", "hello", "python"]}
```

### 3. Debugging Types

```python
def debug_variable(var, name):
    print(f"{name}:")
    print(f"  Value: {var}")
    print(f"  Type: {type(var)}")
    print(f"  ID: {id(var)}")
    if hasattr(var, '__len__'):
        print(f"  Length: {len(var)}")
    print()
```
