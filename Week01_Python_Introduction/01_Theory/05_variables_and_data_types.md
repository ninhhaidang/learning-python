# 📊 Variables and Data Types

## 📖 Mục lục

1. [Variables Fundamentals](#1-variables-fundamentals)
2. [Numeric Data Types](#2-numeric-data-types)
3. [String Data Type](#3-string-data-type)
4. [Boolean Data Type](#4-boolean-data-type)
5. [Type Conversion](#5-type-conversion)
6. [Variable Scope](#6-variable-scope)
7. [Memory Management](#7-memory-management)

---

## 1. Variables Fundamentals

### 🗃️ What are Variables?

Variables are **named containers** that store data values. Think of them as labeled boxes where you can put different types of information.

```python
# Creating variables (assignment)
name = \"Alice\"        # String variable
age = 25              # Integer variable
height = 5.6          # Float variable
is_student = True     # Boolean variable

# Variables can be reassigned
age = 26              # Now age has a new value
print(age)            # Output: 26
```

### 🏷️ Variable Naming Rules

#### ✅ Valid Variable Names:

```python
# Good examples
username = \"john_doe\"
first_name = \"John\"
lastName = \"Doe\"      # camelCase (less common in Python)
age2 = 25
_private = \"hidden\"
MAX_SIZE = 100
counter = 0
user_123 = \"valid\"
```

#### ❌ Invalid Variable Names:

```python
# These will cause SyntaxError
2name = \"invalid\"        # Can't start with number
first-name = \"invalid\"    # Hyphens not allowed
my name = \"invalid\"       # Spaces not allowed
class = \"invalid\"         # Can't use Python keywords
@username = \"invalid\"     # Special characters not allowed
```

### 🎯 Thực hành tốt nhất đặt tên

```python
# ✅ Descriptive names
user_age = 25
total_price = 99.99
is_logged_in = True

# ❌ Poor names
x = 25                    # What does x represent?
data = 99.99             # Too generic
flag = True              # What kind of flag?

# ✅ Constants (UPPERCASE)
PI = 3.14159
MAX_ATTEMPTS = 3
DEFAULT_COLOR = \"blue\"

# ✅ Boolean variables (use is_, has_, can_)
is_valid = True
has_permission = False
can_edit = True
```

### 🔄 Multiple Assignment

```python
# Assign same value to multiple variables
x = y = z = 0
print(x, y, z)  # Output: 0 0 0

# Assign different values in one line
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3

# Swap variables
x, y = 10, 20
x, y = y, x  # Swap values
print(x, y)  # Output: 20 10
```

---

## 2. Numeric Data Types

### 🔢 Integers (int)

```python
# Positive integers
age = 25
year = 2024

# Negative integers
temperature = -10
debt = -5000

# Zero
count = 0

# Large integers (Python handles automatically)
big_number = 123456789012345678901234567890
print(type(big_number))  # <class 'int'>

# Different number bases
binary = 0b1010      # Binary (base 2) = 10 in decimal
octal = 0o12         # Octal (base 8) = 10 in decimal
hexadecimal = 0xA    # Hexadecimal (base 16) = 10 in decimal
```

### 🔢 Floating Point Numbers (float)

```python
# Decimal numbers
height = 5.9
price = 19.99
temperature = 98.6

# Scientific notation
speed_of_light = 3e8      # 3 × 10^8
small_number = 1.5e-4     # 1.5 × 10^-4

# Special float values
positive_infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(positive_infinity)  # inf
print(negative_infinity)  # -inf
print(not_a_number)      # nan
```

### 🔢 Complex Numbers (complex)

```python
# Complex numbers (real + imaginary)
z1 = 3 + 4j
z2 = complex(2, 5)  # 2 + 5j

print(z1.real)      # 3.0 (real part)
print(z1.imag)      # 4.0 (imaginary part)
print(abs(z1))      # 5.0 (magnitude)
```

### 🧮 Numeric Operations

```python
# Basic arithmetic
a, b = 10, 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.3333333333333335
floor_division = a // b # 3 (integer division)
modulus = a % b         # 1 (remainder)
exponentiation = a ** b # 1000 (10^3)

# Order of operations (PEMDAS)
result = 2 + 3 * 4 ** 2  # 2 + 3 * 16 = 2 + 48 = 50
result_with_parentheses = (2 + 3) * 4 ** 2  # 5 * 16 = 80
```

---

## 3. String Data Type

### 📝 Creating Strings

```python
# Single quotes
name = 'Alice'
message = 'Hello, World!'

# Double quotes
name = \"Bob\"
message = \"Python is awesome!\"

# Triple quotes (multiline strings)
long_text = \"\"\"
This is a multiline string.
It can span multiple lines.
Very useful for documentation.
\"\"\"

poem = '''
Roses are red,
Violets are blue,
Python is great,
And so are you!
'''
```

### 🔤 String Operations

```python
first_name = \"John\"
last_name = \"Doe\"

# String concatenation
full_name = first_name + \" \" + last_name
print(full_name)  # \"John Doe\"

# String repetition
stars = \"*\" * 10
print(stars)  # \"**********\"

# String length
name_length = len(full_name)
print(name_length)  # 8

# String indexing (0-based)
first_char = full_name[0]    # \"J\"
last_char = full_name[-1]    # \"e\"

# String slicing
first_three = full_name[0:3]  # \"Joh\"
last_three = full_name[-3:]   # \"Doe\"
```

### 🎨 String Formatting

```python
name = \"Alice\"
age = 25
height = 5.6

# f-strings (Python 3.6+) - Recommended
message = f\"My name is {name}, I'm {age} years old and {height} feet tall.\"

# .format() method
message = \"My name is {}, I'm {} years old and {} feet tall.\".format(name, age, height)

# Named placeholders
message = \"My name is {n}, I'm {a} years old and {h} feet tall.\".format(n=name, a=age, h=height)

# % formatting (older style)
message = \"My name is %s, I'm %d years old and %.1f feet tall.\" % (name, age, height)

# Advanced f-string formatting
price = 19.99
print(f\"Price: ${price:.2f}\")  # Price: $19.99
print(f\"Name: {name:>10}\")     # Right-align in 10 characters
```

### 🛠️ String Methods

```python
text = \"  Hello, World!  \"

# Case methods
print(text.upper())         # \"  HELLO, WORLD!  \"
print(text.lower())         # \"  hello, world!  \"
print(text.title())         # \"  Hello, World!  \"
print(text.capitalize())    # \"  hello, world!  \"

# Whitespace methods
print(text.strip())         # \"Hello, World!\"
print(text.lstrip())        # \"Hello, World!  \"
print(text.rstrip())        # \"  Hello, World!\"

# Search and replace
print(text.replace(\"World\", \"Python\"))  # \"  Hello, Python!  \"
print(text.find(\"World\"))                # 9 (index of \"World\")
print(text.count(\"l\"))                   # 3 (number of 'l' characters)

# Check methods
email = \"user@example.com\"
print(email.startswith(\"user\"))     # True
print(email.endswith(\".com\"))       # True
print(\"123\".isdigit())             # True
print(\"abc\".isalpha())             # True
print(\"abc123\".isalnum())          # True
```

### 🔤 Escape Characters

```python
# Common escape characters
print(\"Hello\\nWorld\")        # New line
print(\"Hello\\tWorld\")        # Tab
print(\"He said \\\"Hello\\\"\")    # Quotes inside string
print(\"Path: C:\\\\Users\\\\Name\") # Backslash

# Raw strings (ignore escape characters)
path = r\"C:\\Users\\Name\\Documents\"
print(path)  # C:\\Users\\Name\\Documents
```

---

## 4. Boolean Data Type

### ✅ Boolean Values

```python
# Boolean literals
is_active = True
is_complete = False

# Boolean from expressions
age = 18
is_adult = age >= 18      # True
has_license = False
can_drive = is_adult and has_license  # False
```

### 🔄 Boolean Operations

```python
# Logical operators
print(True and False)     # False
print(True or False)      # True
print(not True)           # False
print(not False)          # True

# Combining logical operators
a, b, c = True, False, True
result = a and (b or c)   # True and (False or True) = True and True = True

# Comparison operators return booleans
x, y = 5, 10
print(x == y)    # False (equal)
print(x != y)    # True (not equal)
print(x < y)     # True (less than)
print(x <= y)    # True (less than or equal)
print(x > y)     # False (greater than)
print(x >= y)    # False (greater than or equal)
```

### 🎯 Truthy and Falsy Values

```python
# Falsy values (evaluate to False)
print(bool(False))     # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(\"\"))        # False (empty string)
print(bool([]))        # False (empty list)
print(bool({}))        # False (empty dictionary)
print(bool(None))      # False

# Truthy values (evaluate to True)
print(bool(True))      # True
print(bool(1))         # True
print(bool(-1))        # True
print(bool(\"hello\"))   # True
print(bool([1, 2, 3])) # True
print(bool({\"key\": \"value\"}))  # True
```

---

## 5. Type Conversion

### 🔄 Implicit Type Conversion (Automatic)

```python
# Python automatically converts types when needed
num_int = 10
num_float = 3.14

result = num_int + num_float  # int + float = float
print(result)      # 13.14
print(type(result))  # <class 'float'>
```

### 🔄 Explicit Type Conversion (Manual)

```python
# Convert to integer
print(int(3.14))        # 3 (truncates decimal)
print(int(\"42\"))        # 42
print(int(\"101\", 2))    # 5 (binary to decimal)
print(int(True))        # 1
print(int(False))       # 0

# Convert to float
print(float(42))        # 42.0
print(float(\"3.14\"))    # 3.14
print(float(\"inf\"))     # inf

# Convert to string
print(str(42))          # \"42\"
print(str(3.14))        # \"3.14\"
print(str(True))        # \"True\"

# Convert to boolean
print(bool(1))          # True
print(bool(0))          # False
print(bool(\"hello\"))    # True
print(bool(\"\"))         # False
```

### ⚠️ Type Conversion Errors

```python
# These will raise ValueError
try:
    int(\"hello\")        # ValueError: invalid literal
    float(\"not_a_number\")  # ValueError: could not convert
except ValueError as e:
    print(f\"Error: {e}\")

# Safe conversion with error handling
def safe_int(value, default=0):
    try:
        return int(value)
    except ValueError:
        return default

print(safe_int(\"42\"))     # 42
print(safe_int(\"hello\"))  # 0 (default)
```

---

## 6. Variable Scope

### 🌍 Global vs Local Variables

```python
# Global variable
global_var = \"I'm global\"

def my_function():
    # Local variable
    local_var = \"I'm local\"
    print(global_var)  # Can access global
    print(local_var)   # Can access local

my_function()
print(global_var)    # Can access global
# print(local_var)   # NameError: not defined outside function
```

### 🔧 Global Keyword

```python
counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify global variable
    counter += 1

def get_counter():
    return counter  # Can read global without 'global' keyword

increment()
print(get_counter())  # 1
```

---

## 7. Memory Management

### 🧠 Object Identity and References

```python
# Variables are references to objects
a = 5
b = 5
print(id(a))      # Memory address
print(id(b))      # Same address (Python optimizes small integers)
print(a is b)     # True (same object)

# Different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1))  # Different address
print(id(list2))  # Different address
print(list1 is list2)     # False (different objects)
print(list1 == list2)     # True (same content)
```

### 📊 Type Checking

```python
# Check variable type
age = 25
name = \"Alice\"

print(type(age))           # <class 'int'>
print(type(name))          # <class 'str'>
print(isinstance(age, int))      # True
print(isinstance(name, str))     # True
print(isinstance(age, (int, float)))  # True (check multiple types)
```

---

## 🧪 Practical Examples

### Example 1: Personal Information System

```python
\"\"\"
Personal Information Management System
Demonstrates variables and data types
\"\"\"

# Personal information
first_name = \"John\"
last_name = \"Doe\"
age = 28
height = 5.9  # feet
is_employed = True
salary = 75000.0

# Calculated fields
full_name = first_name + \" \" + last_name
height_cm = height * 30.48  # Convert feet to cm
is_adult = age >= 18

# Display information
print(\"=== PERSONAL INFORMATION ====\")
print(f\"Name: {full_name}\")
print(f\"Age: {age} years old\")
print(f\"Height: {height} feet ({height_cm:.1f} cm)\")
print(f\"Employment Status: {'Employed' if is_employed else 'Unemployed'}\")
if is_employed:
    print(f\"Salary: ${salary:,.2f}\")
print(f\"Adult: {'Yes' if is_adult else 'No'}\")

# Type information
print(\"\\n=== TYPE INFORMATION ====\")
print(f\"first_name type: {type(first_name)}\")
print(f\"age type: {type(age)}\")
print(f\"height type: {type(height)}\")
print(f\"is_employed type: {type(is_employed)}\")
```

### Example 2: Calculator Variables

```python
\"\"\"
Simple Calculator using Variables
\"\"\"

# Input numbers
num1 = 15.5
num2 = 4.2

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
power = num1 ** num2

# Display results
print(f\"{num1} + {num2} = {addition}\")
print(f\"{num1} - {num2} = {subtraction}\")
print(f\"{num1} * {num2} = {multiplication}\")
print(f\"{num1} / {num2} = {division:.2f}\")
print(f\"{num1} ^ {num2} = {power:.2f}\")

# Type conversions
print(f\"\\nInteger part of {num1}: {int(num1)}\")
print(f\"String representation: '{str(num1)}'\")
print(f\"Boolean value of {num1}: {bool(num1)}\")
```

---

## 📋 Variables and Data Types Checklist

- [ ] Understand variable assignment and naming rules
- [ ] Know the four basic data types: int, float, str, bool
- [ ] Can perform operations on each data type
- [ ] Understand type conversion (explicit and implicit)
- [ ] Know how to check variable types
- [ ] Understand variable scope (global vs local)
- [ ] Can use f-strings for string formatting
- [ ] Understand truthy/falsy values
- [ ] Can handle type conversion errors
- [ ] Practice with real-world examples

---

## 🎯 Key Takeaways

1. **Variables are containers** for storing data values
2. **Python is dynamically typed** - variable types are determined at runtime
3. **Use descriptive names** for better code readability
4. **Understand the four basic types**: integers, floats, strings, booleans
5. **Type conversion** is often necessary when working with user input
6. **F-strings** are the modern way to format strings in Python
7. **Variable scope** affects where variables can be accessed
8. **Practice with real examples** to solidify understanding

---

**Next**: Continue to `06_input_output_operations.md` to learn about interacting with users.
