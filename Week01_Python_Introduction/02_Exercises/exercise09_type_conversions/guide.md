# Hướng dẫn: Type Conversions

## Lý thuyết cần biết

### 1. Tại sao cần Type Conversion?

- Dữ liệu đầu vào thường là string (user input, file)
- Cần chuyển đổi để thực hiện phép toán
- Định dạng output theo yêu cầu
- Tương thích giữa các kiểu dữ liệu

### 2. Các loại Type Conversion

#### Explicit Conversion (Chuyển đổi tường minh)

```python
# Programmer chủ động chuyển đổi
age_str = "25"
age_int = int(age_str)  # Explicit conversion
```

#### Implicit Conversion (Chuyển đổi ngầm)

```python
# Python tự động chuyển đổi
result = 10 + 3.5  # int + float → float (15.5)
```

### 3. Chuyển đổi cơ bản

#### String ↔ Number

```python
# String to Number
int("123")          # 123
float("3.14")       # 3.14
int("42.7")         # ERROR! Phải qua float trước
int(float("42.7"))  # 42

# Number to String
str(123)            # "123"
str(3.14)           # "3.14"
f"{42:.2f}"         # "42.00" (formatted)
```

#### Boolean Conversions

```python
# To Boolean
bool(1)             # True
bool(0)             # False
bool("")            # False (empty string)
bool("hello")       # True (non-empty string)
bool([])            # False (empty list)
bool([1])           # True (non-empty list)

# From Boolean
int(True)           # 1
int(False)          # 0
str(True)           # "True"
```

#### Collection Conversions

```python
# List ↔ Tuple
list((1, 2, 3))     # [1, 2, 3]
tuple([1, 2, 3])    # (1, 2, 3)

# Set conversions
set([1, 1, 2, 3])   # {1, 2, 3} (removes duplicates)
list({1, 2, 3})     # [1, 2, 3] (order may vary)

# String ↔ List
list("hello")       # ['h', 'e', 'l', 'l', 'o']
"".join(['h', 'i']) # "hi"
```

### 4. Base Number Conversions

#### Decimal to Other Bases

```python
# Decimal to Binary/Hex/Octal
bin(10)             # '0b1010'
hex(255)            # '0xff'
oct(8)              # '0o10'
```

#### Other Bases to Decimal

```python
# Binary to Decimal
int('1010', 2)      # 10
int('0b1010', 2)    # 10

# Hex to Decimal
int('FF', 16)       # 255
int('0xFF', 16)     # 255

# Octal to Decimal
int('10', 8)        # 8
int('0o10', 8)      # 8
```

### 5. Error Handling

#### Common Conversion Errors

```python
# ValueError: invalid literal
int("abc")          # ValueError
float("hello")      # ValueError
int("3.14")         # ValueError (use float first)

# TypeError: wrong type
len(123)            # TypeError
```

#### Safe Conversion

```python
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def is_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
```

## Các bước thực hiện

### Bước 1: String to Number

```python
# Cơ bản
num_str = "123"
num_int = int(num_str)
print(f'int("{num_str}") = {num_int}')

# Float
float_str = "3.14"
num_float = float(float_str)
print(f'float("{float_str}") = {num_float}')

# Qua float trước
complex_str = "42.0"
num_complex = int(float(complex_str))
print(f'int(float("{complex_str}")) = {num_complex}')

# Error handling
try:
    invalid = int("abc")
except ValueError as e:
    print(f'Error converting "abc": {e}')
```

### Bước 2: Number to String

```python
# Cơ bản
number = 42
str_number = str(number)
print(f'str({number}) = "{str_number}"')

# Formatted string
formatted = f"{number:.2f}"
print(f'f"{{{number}:.2f}}" = "{formatted}"')
```

### Bước 3: Boolean conversions

```python
# Test different values
test_values = [1, 0, -1, "", "hello", [], [1], {}, {"a": 1}, None]

for value in test_values:
    result = bool(value)
    print(f'bool({repr(value)}) = {result}')
```

### Bước 4: Collection conversions

```python
# List ↔ Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f'tuple({my_list}) = {my_tuple}')

back_to_list = list(my_tuple)
print(f'list({my_tuple}) = {back_to_list}')

# Remove duplicates with set
duplicates = [1, 1, 2, 2, 3]
unique = list(set(duplicates))
print(f'list(set({duplicates})) = {unique}')
```

### Bước 5: Base conversions

```python
# Decimal to other bases
decimal = 255
print(f'bin({decimal}) = {bin(decimal)}')
print(f'hex({decimal}) = {hex(decimal)}')
print(f'oct({decimal}) = {oct(decimal)}')

# Other bases to decimal
binary_str = "1010"
decimal_from_bin = int(binary_str, 2)
print(f'int("{binary_str}", 2) = {decimal_from_bin}')

hex_str = "FF"
decimal_from_hex = int(hex_str, 16)
print(f'int("{hex_str}", 16) = {decimal_from_hex}')
```

### Bước 6: Safe conversion functions

```python
def safe_int(value, default=0):
    """Safely convert to int with default value"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def is_convertible_to_int(value):
    """Check if value can be converted to int"""
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

# Test functions
test_values = ["123", "abc", "45.67", None, []]
for value in test_values:
    convertible = is_convertible_to_int(value)
    safe_result = safe_int(value, -1)
    print(f'"{value}": convertible={convertible}, safe_int={safe_result}')
```

## Lưu ý quan trọng

### 1. Type Checking

```python
# Kiểm tra kiểu trước khi convert
if isinstance(value, str):
    result = int(value)
elif isinstance(value, (int, float)):
    result = str(value)
```

### 2. Precision Loss

```python
# Mất độ chính xác khi convert
pi = 3.14159
pi_int = int(pi)        # 3 (mất phần thập phân)
pi_str = str(pi_int)    # "3" (không thể khôi phục)
```

### 3. Unicode và Encoding

```python
# String encoding
text = "Hello"
bytes_data = text.encode('utf-8')    # b'Hello'
back_to_str = bytes_data.decode('utf-8')  # "Hello"
```

### 4. Memory Considerations

```python
# Large numbers
big_int = 10**100
big_str = str(big_int)  # Very long string
# Cần cân nhắc bộ nhớ khi convert số lớn
```

## Tips & Tricks

### 1. Chained Conversions

```python
# Multiple conversions
result = str(int(float("42.7")))  # "42"
```

### 2. Default Values

```python
# Using or operator for defaults
age = int(input("Age: ") or "0")  # Default to 0 if empty
```

### 3. List Comprehensions với Conversion

```python
# Convert list of strings to integers
str_numbers = ["1", "2", "3"]
int_numbers = [int(x) for x in str_numbers]
```

### 4. Format Strings

```python
# Different format options
number = 42
formats = [
    f"{number:d}",      # "42" (decimal)
    f"{number:b}",      # "101010" (binary)
    f"{number:x}",      # "2a" (hex lowercase)
    f"{number:X}",      # "2A" (hex uppercase)
    f"{number:o}",      # "52" (octal)
]
```
