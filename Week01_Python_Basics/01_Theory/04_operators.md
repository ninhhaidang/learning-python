# Operators (Toán Tử) trong Python

## 1. Arithmetic Operators (Toán Tử Số Học)

### 1.1 Basic Arithmetic

```python
a = 10
b = 3

# Phép toán cơ bản
print(a + b)    # 13 - Cộng
print(a - b)    # 7  - Trừ
print(a * b)    # 30 - Nhân
print(a / b)    # 3.333... - Chia (kết quả luôn là float)
print(a // b)   # 3  - Chia lấy phần nguyên
print(a % b)    # 1  - Chia lấy dư
print(a ** b)   # 1000 - Lũy thừa (10^3)
```

### 1.2 Division Types

```python
# Regular division vs Floor division
print(10 / 3)    # 3.3333333333333335
print(10 // 3)   # 3

print(-10 / 3)   # -3.3333333333333335
print(-10 // 3)  # -4 (floor towards negative infinity)

# Modulo with negative numbers
print(10 % 3)    # 1
print(-10 % 3)   # 2
print(10 % -3)   # -2
```

### 1.3 Order of Operations (PEMDAS)

```python
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
result = 2 + 3 * 4      # 14 (not 20)
result = (2 + 3) * 4    # 20
result = 2 ** 3 ** 2    # 512 (2^(3^2), not (2^3)^2)
result = 2 ** (3 ** 2)  # 512
result = (2 ** 3) ** 2  # 64

# Complex expression
result = 5 + 2 * 3 ** 2 - 4 / 2  # 5 + 2*9 - 2 = 21
```

## 2. Assignment Operators (Toán Tử Gán)

### 2.1 Basic Assignment

```python
x = 10        # Simple assignment
y = x         # Copy value
z = x = y = 5 # Multiple assignment
```

### 2.2 Compound Assignment

```python
x = 10

# Compound assignment operators
x += 5    # x = x + 5  -> 15
x -= 3    # x = x - 3  -> 12
x *= 2    # x = x * 2  -> 24
x /= 4    # x = x / 4  -> 6.0
x //= 2   # x = x // 2 -> 3.0
x %= 2    # x = x % 2  -> 1.0
x **= 3   # x = x ** 3 -> 1.0
```

### 2.3 Multiple Assignment

```python
# Unpacking assignment
a, b = 1, 2
print(a, b)  # 1 2

# Swapping variables
a, b = b, a
print(a, b)  # 2 1

# With lists
numbers = [1, 2, 3]
x, y, z = numbers
print(x, y, z)  # 1 2 3
```

## 3. Comparison Operators (Toán Tử So Sánh)

### 3.1 Basic Comparisons

```python
a = 10
b = 5

print(a == b)    # False - Bằng
print(a != b)    # True  - Không bằng
print(a > b)     # True  - Lớn hơn
print(a < b)     # False - Nhỏ hơn
print(a >= b)    # True  - Lớn hơn hoặc bằng
print(a <= b)    # False - Nhỏ hơn hoặc bằng
```

### 3.2 Chained Comparisons

```python
age = 25

# Chained comparison
if 18 <= age <= 65:
    print("Working age")

# Equivalent to:
if age >= 18 and age <= 65:
    print("Working age")

# Multiple chaining
x = 5
if 0 < x < 10 < 20:
    print("x is between 0 and 10, and 10 is less than 20")
```

### 3.3 Comparing Different Types

```python
# Numbers
print(5 == 5.0)     # True - same value
print(5 is 5.0)     # False - different types

# Strings
print("hello" == "hello")   # True
print("Hello" == "hello")   # False - case sensitive

# Boolean
print(True == 1)    # True
print(False == 0)   # True
print(True is 1)    # False - different types
```

## 4. Logical Operators (Toán Tử Logic)

### 4.1 Basic Logical Operations

```python
a = True
b = False

print(a and b)    # False - AND: cả hai phải True
print(a or b)     # True  - OR: một trong hai True
print(not a)      # False - NOT: đảo ngược
print(not b)      # True
```

### 4.2 Truth Tables

```python
# AND truth table
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# OR truth table
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

### 4.3 Short-Circuit Evaluation

```python
# AND short-circuit: nếu left False, không evaluate right
x = False and print("This won't print")  # print không được gọi

# OR short-circuit: nếu left True, không evaluate right
y = True or print("This won't print")    # print không được gọi

# Practical example
def expensive_operation():
    print("Doing expensive calculation...")
    return True

x = 5
# Chỉ gọi expensive_operation nếu x > 10
if x > 10 and expensive_operation():
    print("Both conditions met")
```

### 4.4 Logical with Non-Boolean Values

```python
# Truthy và Falsy values
print(1 and 2)      # 2 (both truthy, returns last)
print(0 and 2)      # 0 (first is falsy)
print(1 or 2)       # 1 (first is truthy)
print(0 or 2)       # 2 (first is falsy, returns second)

# Practical use
name = input("Enter name: ") or "Anonymous"
print(f"Hello, {name}")  # "Anonymous" if empty input
```

## 5. Identity Operators (Toán Tử Định Danh)

### 5.1 is vs ==

```python
# == compares values
# is compares identity (memory location)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True - same content
print(a is b)    # False - different objects
print(a is c)    # True - same object

# With numbers (Python optimizes small integers)
x = 5
y = 5
print(x is y)    # True (Python reuses small integers)

x = 1000
y = 1000
print(x is y)    # False (large integers are separate objects)
```

### 5.2 is not

```python
a = None
b = 0

print(a is not b)        # True
print(a is not None)     # False

# Best practice: always use 'is' with None
if value is None:
    print("No value")

if value is not None:
    print("Has value")
```

## 6. Membership Operators (Toán Tử Thành Viên)

### 6.1 in và not in

```python
# With strings
text = "Python Programming"
print("Python" in text)      # True
print("Java" in text)        # False
print("java" not in text)    # True

# With lists
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)          # True
print(6 not in numbers)      # True

# With dictionaries (checks keys)
person = {"name": "Alice", "age": 30}
print("name" in person)      # True
print("Alice" in person)     # False (checks keys, not values)
```

### 6.2 Practical Examples

```python
# Validate input
valid_options = ["yes", "no", "maybe"]
user_input = input("Choose (yes/no/maybe): ").lower()

if user_input in valid_options:
    print(f"You chose: {user_input}")
else:
    print("Invalid option")

# Check vowels
vowels = "aeiou"
letter = input("Enter a letter: ").lower()

if letter in vowels:
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
```

## 7. Bitwise Operators (Toán Tử Bit)

### 7.1 Basic Bitwise Operations

```python
a = 60   # 111100 in binary
b = 13   # 001101 in binary

print(a & b)    # 12 - AND: 001100
print(a | b)    # 61 - OR:  111101
print(a ^ b)    # 49 - XOR: 110001
print(~a)       # -61 - NOT: complement
print(a << 2)   # 240 - Left shift: 11110000
print(a >> 2)   # 15 - Right shift: 1111
```

### 7.2 Practical Uses

```python
# Check if number is even
def is_even(n):
    return (n & 1) == 0

print(is_even(4))   # True
print(is_even(5))   # False

# Set/clear bits (advanced usage)
flags = 0b00000000

# Set bit at position 2
flags |= (1 << 2)   # 0b00000100

# Check if bit at position 2 is set
if flags & (1 << 2):
    print("Bit 2 is set")
```

## 8. Operator Precedence (Thứ Tự Ưu Tiên)

```python
# From highest to lowest precedence:
# 1. () - Parentheses
# 2. ** - Exponentiation
# 3. +x, -x, ~x - Unary operators
# 4. *, /, //, % - Multiplication, Division, Modulo
# 5. +, - - Addition, Subtraction
# 6. <<, >> - Bitwise shifts
# 7. & - Bitwise AND
# 8. ^ - Bitwise XOR
# 9. | - Bitwise OR
# 10. ==, !=, <, <=, >, >=, is, is not, in, not in - Comparisons
# 11. not - Boolean NOT
# 12. and - Boolean AND
# 13. or - Boolean OR

# Examples with precedence
result = 5 + 3 * 2      # 11 (not 16)
result = 2 ** 3 ** 2    # 512 (2^(3^2))
result = not False and True  # True
result = 5 < 3 or 4 > 2     # True

# Use parentheses for clarity
result = (5 + 3) * 2    # 16
result = (2 ** 3) ** 2  # 64
result = not (False and True)  # True
```

## 9. Practical Examples

### Example 1: Grade Calculator

```python
def calculate_grade(score):
    """Calculate letter grade from numeric score"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Test với different scores
scores = [95, 87, 76, 65, 45]
for score in scores:
    grade = calculate_grade(score)
    print(f"Score: {score} -> Grade: {grade}")
```

### Example 2: Password Validator

```python
def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password too short"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    if not (has_upper and has_lower and has_digit and has_special):
        return False, "Password must contain uppercase, lowercase, digit, and special character"

    return True, "Password is strong"

# Test passwords
passwords = ["weak", "StrongPass123!", "nodigit!", "NOLOWER123!"]
for pwd in passwords:
    valid, message = validate_password(pwd)
    print(f"'{pwd}': {message}")
```

### Example 3: Temperature Range Checker

```python
def check_temperature_range(temp, unit='C'):
    """Check if temperature is in comfortable range"""
    if unit.upper() == 'F':
        # Convert Fahrenheit to Celsius
        temp = (temp - 32) * 5/9

    # Comfortable range: 18-24°C
    if 18 <= temp <= 24:
        return "Comfortable"
    elif temp < 18:
        return "Too cold"
    else:
        return "Too hot"

# Test temperatures
temperatures = [
    (20, 'C'), (75, 'F'), (10, 'C'), (85, 'F')
]

for temp, unit in temperatures:
    status = check_temperature_range(temp, unit)
    print(f"{temp}°{unit}: {status}")
```

## 10. Common Mistakes và Best Practices

### Common Mistakes:

```python
# Mistake 1: Assignment vs Comparison
x = 5
if x = 10:  # SyntaxError - should be ==
    print("Equal")

# Mistake 2: Floating point comparison
if 0.1 + 0.2 == 0.3:  # False due to floating point precision
    print("Equal")
# Better:
if abs((0.1 + 0.2) - 0.3) < 1e-9:
    print("Equal")

# Mistake 3: Chained comparisons misunderstanding
if False == False in [False]:  # True (unexpected!)
# Better: use parentheses
if (False == False) in [False]:  # False
if False == (False in [False]):  # True
```

### Best Practices:

```python
# Use parentheses for clarity
result = (a + b) * (c - d)  # Clear intention

# Use appropriate operators
if value is None:           # Good for None checks
    pass

if name == "":              # Good for empty string
    pass

# Chain comparisons when appropriate
if 0 <= age <= 120:         # Clear range check
    pass

# Use compound assignment
count += 1                  # Better than count = count + 1

# Use truthiness appropriately
if items:                   # Good for checking non-empty
    process(items)

if not error_message:       # Good for checking empty string
    continue_processing()
```

## Bài Tập Thực Hành

1. Viết calculator với tất cả arithmetic operators
2. Tạo age group classifier sử dụng comparison operators
3. Build logical expression để validate form input
4. Practice operator precedence với complex expressions
5. Implement simple encryption sử dụng bitwise operators
