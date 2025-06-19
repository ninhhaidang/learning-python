# Kiểu Dữ Liệu Cơ Bản Python

## 1. Numbers (Số)

Python có 3 kiểu số chính:

### 1.1 Integer (Số nguyên)

```python
# Số nguyên dương và âm
age = 25
temperature = -10
year = 2024

# Số lớn (Python tự động xử lý)
big_number = 123456789012345678901234567890
print(big_number)  # Python không giới hạn kích thước
```

### 1.2 Float (Số thực)

```python
# Số thập phân
height = 1.75
pi = 3.14159
temperature = 36.5

# Scientific notation
speed_of_light = 3e8  # 3 * 10^8
planck_constant = 6.626e-34
```

### 1.3 Complex (Số phức)

```python
# Số phức cho tính toán khoa học
z1 = 3 + 4j
z2 = complex(2, 5)  # 2 + 5j

print(z1.real)  # 3.0 - phần thực
print(z1.imag)  # 4.0 - phần ảo
```

### Number Operations:

```python
# Type conversion
x = 5
y = 2.5

print(int(y))      # 2 - chuyển float sang int
print(float(x))    # 5.0 - chuyển int sang float
print(str(x))      # "5" - chuyển number sang string

# Check type
print(type(x))     # <class 'int'>
print(type(y))     # <class 'float'>
print(isinstance(x, int))  # True
```

## 2. Strings (Chuỗi)

Strings là sequence của characters.

### 2.1 String Creation

```python
# Nhiều cách tạo string
name = "John"
message = 'Hello World'
long_text = """This is a
multi-line
string"""

# Empty string
empty = ""
also_empty = str()
```

### 2.2 String Indexing và Slicing

```python
text = "Python Programming"

# Indexing (bắt đầu từ 0)
print(text[0])     # 'P' - ký tự đầu
print(text[-1])    # 'g' - ký tự cuối
print(text[-2])    # 'n' - ký tự gần cuối

# Slicing [start:end:step]
print(text[0:6])   # 'Python'
print(text[7:])    # 'Programming'
print(text[:6])    # 'Python'
print(text[::2])   # 'Pto rgamn' - mỗi 2 ký tự
print(text[::-1])  # 'gnimmargorP nohtyP' - đảo ngược
```

### 2.3 String Methods

```python
text = "  Python Programming  "

# Case methods
print(text.lower())      # '  python programming  '
print(text.upper())      # '  PYTHON PROGRAMMING  '
print(text.title())      # '  Python Programming  '
print(text.capitalize()) # '  python programming  '

# Whitespace methods
print(text.strip())      # 'Python Programming'
print(text.lstrip())     # 'Python Programming  '
print(text.rstrip())     # '  Python Programming'

# Search methods
print(text.find('Python'))    # 2 - vị trí tìm thấy
print(text.count('r'))        # 2 - số lần xuất hiện
print(text.startswith('  P')) # True
print(text.endswith('g  '))   # True

# Replace
print(text.replace('Python', 'Java'))  # '  Java Programming  '
```

### 2.4 String Formatting

```python
name = "Alice"
age = 30
score = 95.67

# f-strings (Python 3.6+) - Recommended
message = f"Name: {name}, Age: {age}, Score: {score:.2f}"
print(message)  # Name: Alice, Age: 30, Score: 95.67

# .format() method
message = "Name: {}, Age: {}, Score: {:.2f}".format(name, age, score)
print(message)

# % formatting (old style)
message = "Name: %s, Age: %d, Score: %.2f" % (name, age, score)
print(message)
```

### 2.5 Escape Characters

```python
# Common escape characters
print("Hello\nWorld")     # New line
print("Hello\tWorld")     # Tab
print("Hello\\World")     # Backslash
print("Say \"Hello\"")    # Quote marks
print('It\'s Python')     # Apostrophe

# Raw strings (ignore escape characters)
path = r"C:\Users\name\Documents"
print(path)  # C:\Users\name\Documents
```

## 3. Boolean (Logic)

Boolean values: `True` và `False`

### 3.1 Boolean Creation

```python
# Direct assignment
is_student = True
is_working = False

# From comparisons
age = 20
is_adult = age >= 18  # True
is_teenager = 13 <= age <= 19  # True

# From functions
text = "Python"
is_empty = len(text) == 0  # False
```

### 3.2 Boolean Operations

```python
a = True
b = False

# Logical operators
print(a and b)    # False - cả hai phải True
print(a or b)     # True - một trong hai True
print(not a)      # False - đảo ngược

# Short-circuit evaluation
print(True or print("This won't execute"))   # True
print(False and print("This won't execute")) # False
```

### 3.3 Truthiness và Falsiness

```python
# Falsy values (được coi là False)
falsy_values = [
    False,      # Boolean False
    0,          # Zero integer
    0.0,        # Zero float
    "",         # Empty string
    [],         # Empty list
    {},         # Empty dictionary
    None        # None type
]

# Truthy values (được coi là True)
truthy_values = [
    True,       # Boolean True
    1,          # Non-zero numbers
    -1,
    "text",     # Non-empty strings
    [1, 2],     # Non-empty collections
    {"key": "value"}
]

# Testing truthiness
if "Python":
    print("Non-empty string is truthy")  # This will execute

if not "":
    print("Empty string is falsy")       # This will execute
```

## 4. None Type

`None` là special value đại diện cho "nothing" hoặc "null".

```python
# None assignment
result = None
data = None

# Check for None
if result is None:
    print("No result yet")

if result is not None:
    print("We have a result")

# None vs False vs 0 vs ""
print(None == False)  # False
print(None == 0)      # False
print(None == "")     # False
print(None is None)   # True
```

## 5. Type Checking và Conversion

### 5.1 Type Checking

```python
# type() function
x = 42
print(type(x))          # <class 'int'>
print(type(x).__name__) # 'int'

# isinstance() function (recommended)
print(isinstance(x, int))       # True
print(isinstance(x, (int, float))) # True - check multiple types
```

### 5.2 Type Conversion

```python
# String to numbers
text_num = "123"
integer = int(text_num)        # 123
floating = float(text_num)     # 123.0

# Numbers to string
number = 456
text = str(number)             # "456"

# Boolean conversion
print(bool(1))     # True
print(bool(0))     # False
print(bool(""))    # False
print(bool("hi"))  # True

# Handle conversion errors
try:
    result = int("abc")  # This will raise ValueError
except ValueError:
    print("Cannot convert 'abc' to integer")
```

## 6. Practical Examples

### Example 1: User Input Processing

```python
# Get user input and process
name = input("Enter your name: ").strip().title()
age_str = input("Enter your age: ")

try:
    age = int(age_str)
    is_adult = age >= 18

    print(f"Hello {name}!")
    print(f"You are {age} years old.")
    print(f"Adult status: {is_adult}")

except ValueError:
    print("Please enter a valid age number.")
```

### Example 2: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# Example usage
temp_c = 25.0
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.1f}°F")
```

### Example 3: Data Validation

```python
def validate_email(email):
    """Simple email validation"""
    if not isinstance(email, str):
        return False

    email = email.strip().lower()

    # Basic checks
    if len(email) == 0:
        return False
    if "@" not in email:
        return False
    if email.count("@") != 1:
        return False
    if "." not in email.split("@")[1]:
        return False

    return True

# Test validation
emails = ["user@example.com", "invalid.email", "", "test@domain.co.uk"]
for email in emails:
    print(f"{email}: {validate_email(email)}")
```

## 7. Common Mistakes và Best Practices

### Common Mistakes:

```python
# Mistake 1: Confusing assignment and comparison
x = 5
if x = 10:  # SyntaxError - should be ==
    print("Equal")

# Mistake 2: Float precision issues
print(0.1 + 0.2 == 0.3)  # False (!)
print(round(0.1 + 0.2, 10))  # 0.3000000001

# Mistake 3: String immutability
text = "Hello"
text[0] = "h"  # TypeError - strings are immutable
```

### Best Practices:

```python
# Use descriptive variable names
user_age = 25  # Good
a = 25         # Bad

# Use appropriate data types
is_valid = True   # Good for boolean
is_valid = 1      # Works but not clear

# Use f-strings for formatting
name = "Alice"
message = f"Hello, {name}!"  # Good
message = "Hello, " + name + "!"  # Works but verbose

# Check types when necessary
def process_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Expected number")
    return value * 2
```

## Bài Tập Thực Hành

1. Tạo variables cho thông tin cá nhân (tên, tuổi, chiều cao)
2. Thực hiện các phép toán với numbers
3. Manipulate strings: slice, format, search
4. Write boolean expressions cho different conditions
5. Practice type conversion với error handling
