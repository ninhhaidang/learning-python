# 📝 Python Syntax Basics

## 📖 Mục lục

1. [Python Code Structure](#1-python-code-structure)
2. [Indentation Rules](#2-i#### Cài đặt VS Code:

````json
{
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "python.formatting.provider": "black"
}on-rules)
3. [Comments and Documentation](#3-comments-and-documentation)
4. [Keywords and Identifiers](#4-keywords-and-identifiers)
5. [Case Sensitivity](#5-case-sensitivity)
6. [Line Continuation](#6-line-continuation)
7. [Statement Types](#7-statement-types)

---

## 1. Python Code Structure

### 🏗️ Basic Program Structure

```python
#!/usr/bin/env python3
\"\"\"
Module docstring: Mô tả chức năng của file
Author: Your Name
Date: YYYY-MM-DD
\"\"\"

# Import statements
import math
import datetime

# Global constants
PI = 3.14159
MAX_SIZE = 100

# Global variables
counter = 0

# Function definitions
def greet(name):
    \"\"\"Function to greet a person\"\"\"
    return f\"Hello, {name}!\"

# Class definitions
class Student:
    \"\"\"A simple student class\"\"\"
    def __init__(self, name):
        self.name = name

# Main execution
if __name__ == \"__main__\":
    # Main program logic here
    print(\"Program started\")
    message = greet(\"Python Learner\")
    print(message)
````

### 📋 Structure Explanation

1. **Shebang line** (`#!/usr/bin/env python3`): Tells system which interpreter to use
2. **Module docstring**: Describes what the file does
3. **Import statements**: External libraries and modules
4. **Constants**: Values that don't change (UPPERCASE naming)
5. **Global variables**: Variables used throughout the program
6. **Functions**: Reusable blocks of code
7. **Classes**: Object-oriented programming constructs
8. **Main execution**: Code that runs when file is executed directly

---

## 2. Indentation Rules

### 📏 The Golden Rule of Python

**Python uses indentation to define code blocks** (not curly braces `{}` like other languages)

### ✅ Correct Indentation

```python
# If statement
if True:
    print(\"This is indented\")    # 4 spaces
    print(\"This too\")            # 4 spaces

# Function definition
def my_function():
    print(\"Inside function\")     # 4 spaces
    if True:
        print(\"Nested indent\")   # 8 spaces (4 + 4)

# Loops
for i in range(3):
    print(f\"Number: {i}\")        # 4 spaces
    if i == 1:
        print(\"Special case\")    # 8 spaces
```

### ❌ Incorrect Indentation

```python
# IndentationError examples
if True:
print(\"No indentation\")  # ERROR: Expected indent

if True:
    print(\"Good\")
  print(\"Bad indent\")     # ERROR: Inconsistent indent

def function():
    print(\"Line 1\")       # 4 spaces
        print(\"Line 2\")   # 8 spaces - ERROR: Unexpected indent
```

### 🎯 Thực hành tốt nhất cho thụt đầu dòng

1. **Use 4 spaces** (PEP 8 standard)
2. **Be consistent** throughout your code
3. **Never mix tabs and spaces**
4. **Set your editor** to show spaces/tabs
5. **Use automatic formatting** tools

### ⚙️ Editor Configuration

#### VS Code settings:

```json
{
    \"editor.tabSize\": 4,
    \"editor.insertSpaces\": true,
    \"python.formatting.provider\": \"black\"
}
```

---

## 3. Comments and Documentation

### 💬 Single-line Comments

```python
# This is a single-line comment
print(\"Hello\")  # Comment at end of line

# You can use multiple single-line comments
# to create a block of explanation
# like this paragraph
```

### 📖 Multi-line Comments

```python
\"\"\"
This is a multi-line comment
using triple quotes.
It can span multiple lines.
\"\"\"

'''
You can also use single quotes
for multi-line comments.
Both work the same way.
'''
```

### 📚 Docstrings

```python
def calculate_area(radius):
    \"\"\"
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The area of the circle

    Example:
        >>> calculate_area(5)
        78.53975
    \"\"\"
    return 3.14159 * radius ** 2

class Rectangle:
    \"\"\"
    A class to represent a rectangle.

    Attributes:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    \"\"\"

    def __init__(self, width, height):
        \"\"\"Initialize rectangle with width and height.\"\"\"
        self.width = width
        self.height = height
```

### 🎯 Thực hành tốt nhất cho comment

#### ✅ Good Comments:

```python
# Calculate compound interest
final_amount = principal * (1 + rate) ** time

# Handle edge case: empty list
if not items:
    return default_value

# TODO: Optimize this algorithm for large datasets
result = slow_function(data)
```

#### ❌ Bad Comments:

```python
# Add 1 to x
x = x + 1  # This comment doesn't add value

# This variable stores the name
name = \"John\"  # Obvious from the code

# Loop through numbers
for i in range(10):  # Comment doesn't explain WHY
    print(i)
```

---

## 4. Keywords and Identifiers

### 🔒 Python Keywords (Reserved Words)

```python
# These words have special meaning in Python - cannot be used as variable names
False    class    finally  is       return
None     continue for      lambda   try
True     def      from     nonlocal while
and      del      global   not      with
as       elif     if       or       yield
assert   else     import   pass
break    except   in       raise
```

### 📝 Valid Identifiers (Variable Names)

```python
# Valid identifiers
name = \"John\"
age_in_years = 25
firstName = \"Jane\"  # camelCase
last_name = \"Doe\"   # snake_case (recommended)
_private = \"hidden\"  # Leading underscore
counter2 = 0          # Numbers allowed (not at start)
MAX_SIZE = 100        # Constants in UPPERCASE

# Invalid identifiers - These will cause errors
2name = \"Invalid\"      # Can't start with number
first-name = \"Invalid\"  # Hyphens not allowed
class = \"Invalid\"       # Can't use keywords
first name = \"Invalid\"   # Spaces not allowed
```

### 🎯 Naming Conventions (PEP 8)

```python
# Variables and functions: snake_case
user_name = \"alice\"
def calculate_total():
    pass

# Constants: UPPERCASE_WITH_UNDERSCORES
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

# Classes: PascalCase
class StudentRecord:
    pass

# Private variables: leading underscore
_internal_value = 42

# \"Magic\" methods: double underscores
def __init__(self):
    pass
```

---

## 5. Case Sensitivity

### 🔤 Python is Case Sensitive

```python
# These are all different variables
name = \"John\"
Name = \"Jane\"
NAME = \"Bob\"

print(name)  # \"John\"
print(Name)  # \"Jane\"
print(NAME)  # \"Bob\"

# Functions are also case sensitive
def greet():
    return \"Hello\"

def Greet():  # Different function
    return \"Hi\"

print(greet())  # \"Hello\"
print(Greet())  # \"Hi\"
```

### ⚠️ Common Case Sensitivity Errors

```python
# Built-in functions
print(\"Hello\")   # Correct
Print(\"Hello\")   # NameError: 'Print' is not defined

# Keywords
if True:           # Correct
    print(\"True\")

If True:           # NameError: 'If' is not defined
    print(\"True\")

# Variables
myVar = 5
print(myvar)       # NameError: 'myvar' is not defined
```

---

## 6. Line Continuation

### 🔗 Explicit Line Continuation

```python
# Using backslash for long lines
total = first_value + second_value + third_value + \
        fourth_value + fifth_value

# Better: use parentheses (preferred)
total = (first_value + second_value + third_value +
         fourth_value + fifth_value)

# Function calls with many parameters
result = some_function(parameter1, parameter2,
                      parameter3, parameter4,
                      parameter5)
```

### 📦 Implicit Line Continuation

```python
# Lists
fruits = [\"apple\", \"banana\", \"cherry\",
          \"date\", \"elderberry\", \"fig\"]

# Dictionaries
person = {\"name\": \"John\",
          \"age\": 30,
          \"city\": \"New York\"}

# Function definitions
def long_function_name(parameter_one, parameter_two,
                      parameter_three, parameter_four):
    pass
```

---

## 7. Statement Types

### 📋 Simple Statements

```python
# Assignment
x = 5
name = \"Alice\"

# Expression
x + y
len(\"Hello\")

# Function call
print(\"Hello\")

# Import
import math

# Pass (do nothing)
pass

# Break and continue (in loops)
break
continue

# Return (in functions)
return value
```

### 🏗️ Compound Statements

```python
# If statement
if condition:
    # statement block
    pass

# For loop
for item in sequence:
    # statement block
    pass

# While loop
while condition:
    # statement block
    pass

# Function definition
def function_name():
    # statement block
    pass

# Class definition
class ClassName:
    # statement block
    pass

# Try-except
try:
    # statement block
    pass
except Exception:
    # statement block
    pass
```

### 📝 Multiple Statements on One Line

```python
# Using semicolon (not recommended)
x = 5; y = 10; print(x + y)

# Better: separate lines
x = 5
y = 10
print(x + y)

# Exception: related simple assignments
x, y = 5, 10  # Tuple unpacking is okay
```

---

## 🧪 Ví dụ thực hành

### Ví dụ 1: Kiểm tra cú pháp

```python
\"\"\"
Practice: Fix the syntax errors in this code
\"\"\"

# Original (with errors):
# def calculate area(radius):
# PI = 3.14159
# area = pi * radius ** 2
# Return area

# Fixed version:
def calculate_area(radius):
    \"\"\"Calculate area of a circle\"\"\"
    PI = 3.14159
    area = PI * radius ** 2  # Fixed: PI not pi
    return area              # Fixed: return not Return

# Test the function
result = calculate_area(5)
print(f\"Area: {result}\")
```

### Ví dụ 2: Cấu trúc code sạch

```python
\"\"\"
Ví dụ về code Python có cấu trúc tốt
\"\"\"

# Constants
GREETING_MESSAGE = \"Welcome to Python!\"
MAX_ATTEMPTS = 3

def main():
    \"\"\"Main program function\"\"\"
    # Display welcome message
    print(GREETING_MESSAGE)

    # Get user input
    user_name = input(\"Enter your name: \")

    # Process and display result
    personalized_greeting = create_greeting(user_name)
    print(personalized_greeting)

def create_greeting(name):
    \"\"\"Create personalized greeting\"\"\"
    if name:
        return f\"Hello, {name}! Nice to meet you.\"
    else:
        return \"Hello, stranger!\"

# Run main program
if __name__ == \"__main__\":
    main()
```

---

## 📋 Syntax Checklist

- [ ] Use 4 spaces for indentation consistently
- [ ] Add meaningful comments and docstrings
- [ ] Use snake_case for variables and functions
- [ ] Use PascalCase for classes
- [ ] Use UPPERCASE for constants
- [ ] Avoid using Python keywords as identifiers
- [ ] Remember Python is case-sensitive
- [ ] Use parentheses for long line continuation
- [ ] Structure code logically (imports, constants, functions, main)
- [ ] End files with newline character

---

## 🔧 Debugging Syntax Errors

### Thông báo lỗi phổ biến:

```python
# SyntaxError: invalid syntax
# Thường do thiếu ngoặc đơn, dấu ngoặc kép, hoặc dấu hai chấm

# IndentationError: expected an indented block
# Thiếu indentation sau if, for, def, v.v.

# IndentationError: unexpected indent
# Thừa hoặc không nhất quán indentation

# NameError: name 'X' is not defined
# Biến được sử dụng trước khi định nghĩa hoặc viết sai tên
```

### 🛠️ Mẹo Debug:

1. **Đọc thông báo lỗi cẩn thận** - chúng chỉ ra dòng và vấn đề
2. **Kiểm tra indentation** - sử dụng tính năng hiển thị khoảng trắng của editor
3. **Xác minh dấu ngoặc kép khớp** và dấu ngoặc đơn
4. **Check spelling** of variable names and functions
5. **Use a linter** like pylint or flake8

---

**Next**: Continue to `05_variables_and_data_types.md` to learn about storing and manipulating data.
