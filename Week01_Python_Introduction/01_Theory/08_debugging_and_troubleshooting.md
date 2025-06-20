# 🐛 Debug và khắc phục sự cố

## 📖 Mục lục

1. [Hiểu về lỗi](#1-hiểu-về-lỗi)
2. [Các lỗi Python phổ biến](#2-các-lỗi-python-phổ-biến)
3. [Đọc thông báo lỗi](#3-đọc-thông-báo-lỗi)
4. [Chiến lược Debug](#4-chiến-lược-debug)
5. [Sử dụng Python Debugger](#5-sử-dụng-python-debugger)
6. [Tính năng Debug trong IDE](#6-tính-năng-debug-trong-ide)
7. [Thực hành tốt nhất](#7-thực-hành-tốt-nhất)

---

## 1. Hiểu về lỗi

### 🎯 Các loại lỗi

#### 1. **Lỗi cú pháp** (Parsing Errors)

Code không tuân theo quy tắc cú pháp Python

```python
# Missing colon
if x == 5
    print(\"Five\")  # SyntaxError: invalid syntax

# Mismatched parentheses
print(\"Hello World\"  # SyntaxError: unexpected EOF while parsing

# Incorrect indentation
def my_function():
print(\"Hello\")  # IndentationError: expected an indented block
```

#### 2. **Lỗi thời gian chạy** (Exceptions)

Code có cú pháp đúng nhưng thất bại khi thực thi

```python
# Division by zero
result = 10 / 0  # ZeroDivisionError: division by zero

# Accessing non-existent variable
print(my_variable)  # NameError: name 'my_variable' is not defined

# Wrong data type operation
number = \"5\"
result = number + 10  # TypeError: can only concatenate str (not \"int\") to str
```

#### 3. **Logic Errors** (Bugs)

Code runs but produces incorrect results

```python
# Wrong formula
def calculate_circle_area(radius):
    # Should be: pi * radius ** 2
    return 3.14 * radius  # Logic error: missing ** 2

# Off-by-one error
def print_numbers(n):
    for i in range(n):  # Should be range(1, n+1) to print 1 to n
        print(i)  # Prints 0 to n-1 instead
```

---

## 2. Common Python Errors

### 🔴 SyntaxError and IndentationError

```python
# ❌ Missing colon
if True
    print(\"True\")
# Fix: if True:

# ❌ Mismatched quotes
message = \"Hello World'
# Fix: message = \"Hello World\"

# ❌ Wrong indentation
def greet():
print(\"Hello\")  # Should be indented
# Fix: add 4 spaces before print

# ❌ Inconsistent indentation
def calculate():
    x = 5
  y = 10  # IndentationError: unindent does not match any outer indentation level
# Fix: use consistent 4 spaces
```

### 🔴 NameError

```python
# ❌ Variable used before definition
print(username)  # NameError: name 'username' is not defined
username = \"Alice\"

# ❌ Typo in variable name
user_name = \"Bob\"
print(username)  # NameError: name 'username' is not defined
# Fix: print(user_name)

# ❌ Variable out of scope
def my_function():
    local_var = 10

print(local_var)  # NameError: name 'local_var' is not defined
# Fix: return the variable or make it global
```

### 🔴 TypeError

```python
# ❌ Wrong operation on data type
age = \"25\"
next_year = age + 1  # TypeError: can only concatenate str (not \"int\") to str
# Fix: next_year = int(age) + 1

# ❌ Wrong function arguments
def greet(name, age):
    print(f\"Hello {name}, you are {age}\")

greet(\"Alice\")  # TypeError: greet() missing 1 required positional argument: 'age'
# Fix: greet(\"Alice\", 25)

# ❌ Calling non-callable object
number = 42
result = number()  # TypeError: 'int' object is not callable
# Fix: result = number (remove parentheses)
```

### 🔴 ValueError

```python
# ❌ Invalid conversion
age = int(\"twenty\")  # ValueError: invalid literal for int() with base 10: 'twenty'
# Fix: age = int(\"20\") or use try-except

# ❌ Invalid operation
import math
result = math.sqrt(-1)  # ValueError: math domain error
# Fix: check if number is positive first

# ❌ Wrong number of values to unpack
coordinates = \"10,20,30\"
x, y = coordinates.split(\",\")  # ValueError: too many values to unpack (expected 2)
# Fix: x, y, z = coordinates.split(\",\")
```

### 🔴 IndexError and KeyError

```python
# ❌ List index out of range
fruits = [\"apple\", \"banana\"]
print(fruits[5])  # IndexError: list index out of range
# Fix: check length first or use try-except

# ❌ Dictionary key doesn't exist
person = {\"name\": \"Alice\", \"age\": 25}
print(person[\"height\"])  # KeyError: 'height'
# Fix: use person.get(\"height\", \"Not available\")

# ❌ Empty list access
numbers = []
first = numbers[0]  # IndexError: list index out of range
# Fix: check if list is not empty first
```

---

## 3. Đọc thông báo lỗi

### 📋 Cấu trúc của thông báo lỗi

```python
# Example error-producing code
def divide_numbers():
    x = 10
    y = 0
    result = x / y
    return result

divide_numbers()
```

**Kết quả lỗi:**

```
Traceback (most recent call last):
  File \"example.py\", line 6, in <module>
    divide_numbers()
  File \"example.py\", line 4, in divide_numbers
    result = x / y
ZeroDivisionError: division by zero
```

**Breaking down the error:**

1. **Traceback**: Shows the call stack (sequence of function calls)
2. **File and line**: Where the error occurred
3. **Function context**: Which function was executing
4. **Error type**: `ZeroDivisionError`
5. **Error message**: `division by zero`

### 🔍 Interpreting Different Error Formats

```python
# Example with nested function calls
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

def process_data():
    data = []  # Empty list
    average = calculate_average(data)
    return average

def main():
    result = process_data()
    print(result)

main()
```

**Kết quả lỗi:**

```
Traceback (most recent call last):
  File \"example.py\", line 13, in <module>
    main()
  File \"example.py\", line 10, in main
    result = process_data()
  File \"example.py\", line 7, in process_data
    average = calculate_average(data)
  File \"example.py\", line 4, in calculate_average
    return total / count
ZeroDivisionError: division by zero
```

**Reading the traceback:**

- Start from the bottom: The actual error
- Work upward: Follow the call chain
- Identify: Which function call led to the problem

---

## 4. Debugging Strategies

### 🔍 Print Debugging

```python
def calculate_grade(scores):
    print(f\"Input scores: {scores}\")  # Debug: Check input

    total = 0
    for score in scores:
        print(f\"Adding score: {score}, current total: {total}\")  # Debug: Check loop
        total += score

    count = len(scores)
    print(f\"Total: {total}, Count: {count}\")  # Debug: Check calculation

    if count == 0:
        print(\"Warning: No scores provided!\")  # Debug: Edge case
        return 0

    average = total / count
    print(f\"Calculated average: {average}\")  # Debug: Final result
    return average

# Test with debug output
scores = [85, 92, 78, 96]
grade = calculate_grade(scores)
print(f\"Final grade: {grade}\")
```

### 🧩 Rubber Duck Debugging

```python
# Talk through your code step by step
def find_maximum(numbers):
    \"\"\"
    Rubber duck explanation:
    1. I want to find the largest number in a list
    2. I'll start with the first number as the maximum
    3. I'll compare each other number with my current maximum
    4. If I find a larger number, I'll update my maximum
    5. At the end, I'll have the largest number
    \"\"\"

    if not numbers:  # Edge case: empty list
        return None

    max_value = numbers[0]  # Start with first number

    for number in numbers[1:]:  # Check rest of numbers
        if number > max_value:
            max_value = number

    return max_value

# Test the logic
test_numbers = [3, 7, 2, 9, 1, 5]
result = find_maximum(test_numbers)
print(f\"Maximum: {result}\")
```

### 🔬 Divide and Conquer

```python
# Break complex problems into smaller parts
def complex_calculation(data):
    # Step 1: Clean the data
    cleaned_data = clean_data(data)
    print(f\"Step 1 - Cleaned data: {cleaned_data}\")

    # Step 2: Process the data
    processed_data = process_data(cleaned_data)
    print(f\"Step 2 - Processed data: {processed_data}\")

    # Step 3: Calculate result
    result = calculate_result(processed_data)
    print(f\"Step 3 - Result: {result}\")

    return result

def clean_data(data):
    # Remove None values and convert to numbers
    cleaned = []
    for item in data:
        if item is not None:
            try:
                cleaned.append(float(item))
            except ValueError:
                print(f\"Warning: Could not convert {item} to number\")
    return cleaned

def process_data(data):
    # Apply some processing (e.g., square each number)
    return [x ** 2 for x in data]

def calculate_result(data):
    # Calculate average
    return sum(data) / len(data) if data else 0

# Test each step
test_data = [\"1\", \"2.5\", None, \"3\", \"invalid\", \"4.5\"]
result = complex_calculation(test_data)
```

### 🧪 Test with Edge Cases

```python
def safe_division(dividend, divisor):
    \"\"\"Division function that handles edge cases\"\"\"

    # Test various edge cases
    if divisor == 0:
        print(\"Error: Division by zero\")
        return None

    if dividend == 0:
        return 0

    return dividend / divisor

# Test edge cases
test_cases = [
    (10, 2),     # Normal case
    (10, 0),     # Division by zero
    (0, 5),      # Zero dividend
    (-10, 2),    # Negative numbers
    (10, -2),
    (-10, -2),
    (10.5, 2.5), # Floating point
]

for dividend, divisor in test_cases:
    result = safe_division(dividend, divisor)
    print(f\"{dividend} / {divisor} = {result}\")
```

---

## 5. Using Python Debugger

### 🐛 pdb (Python Debugger)

```python
import pdb

def buggy_function(numbers):
    total = 0
    for i, num in enumerate(numbers):
        pdb.set_trace()  # Debugger will stop here
        total += num * i  # Potential bug: multiplying by index
    return total

# Run this and use debugger commands:
# n (next line)
# s (step into)
# c (continue)
# p variable_name (print variable)
# l (list current code)
# q (quit)

numbers = [10, 20, 30]
result = buggy_function(numbers)
print(result)
```

### 🔧 Debugger Commands

```python
# Common pdb commands:

# Navigation:
# n (next) - Execute next line
# s (step) - Step into function calls
# c (continue) - Continue execution
# l (list) - Show current code
# w (where) - Show current stack trace

# Inspection:
# p <expression> - Print value of expression
# pp <expression> - Pretty print
# vars() - Show all local variables
# vars(object) - Show object's attributes

# Breakpoints:
# b <line_number> - Set breakpoint at line
# b <function_name> - Set breakpoint at function
# cl - Clear all breakpoints
# cl <line_number> - Clear specific breakpoint

def debug_example():
    x = 10
    y = 20
    pdb.set_trace()

    # Try these commands when debugger stops:
    # p x
    # p y
    # p x + y
    # vars()
    # n

    z = x + y
    result = z * 2
    return result
```

### 🎯 Conditional Breakpoints

```python
import pdb

def process_list(items):
    for i, item in enumerate(items):
        # Only break on specific condition
        if item < 0:
            pdb.set_trace()  # Debug negative numbers

        processed = item ** 2
        print(f\"Item {i}: {item} -> {processed}\")

# Test with mixed positive/negative numbers
test_items = [1, 4, -2, 9, -5, 16]
process_list(test_items)
```

---

## 6. IDE Debugging Features

### 🔧 VS Code Debugging

```python
# VS Code debugging setup:
# 1. Set breakpoints by clicking left margin
# 2. Press F5 to start debugging
# 3. Use debug console to inspect variables

def calculate_fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        # Set breakpoint here to watch values change
        next_fib = a + b
        a, b = b, next_fib

    return b

# Configure launch.json for debugging:
{
    \"version\": \"0.2.0\",
    \"configurations\": [
        {
            \"name\": \"Python: Current File\",
            \"type\": \"python\",
            \"request\": \"launch\",
            \"program\": \"${file}\",
            \"console\": \"integratedTerminal\",
            \"justMyCode\": true
        }
    ]
}
```

### 🎮 Interactive Debugging

```python
# Using VS Code debug console
def debug_interactive_example():
    numbers = [1, 2, 3, 4, 5]
    total = 0

    for num in numbers:
        # When breakpoint hits, try these in debug console:
        # numbers
        # num
        # total
        # len(numbers)
        # sum(numbers)
        total += num

    return total

result = debug_interactive_example()
```

---

## 7. Thực hành tốt nhất

### ✅ Error Prevention

```python
# 1. Input validation
def safe_square_root(number):
    \"\"\"Calculate square root with input validation\"\"\"
    if not isinstance(number, (int, float)):
        raise TypeError(\"Input must be a number\")

    if number < 0:
        raise ValueError(\"Cannot calculate square root of negative number\")

    return number ** 0.5

# 2. Use try-except for expected errors
def convert_to_int(value):
    \"\"\"Safely convert value to integer\"\"\"
    try:
        return int(value)
    except ValueError:
        print(f\"Warning: '{value}' is not a valid integer\")
        return None
    except TypeError:
        print(f\"Warning: Cannot convert {type(value)} to integer\")
        return None

# 3. Check preconditions
def calculate_average(numbers):
    \"\"\"Calculate average with precondition checks\"\"\"
    if not numbers:
        raise ValueError(\"Cannot calculate average of empty list\")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError(\"All items must be numbers\")

    return sum(numbers) / len(numbers)
```

### 🧪 Testing and Validation

```python
def test_function(func, test_cases):
    \"\"\"Test function with multiple test cases\"\"\"
    print(f\"Testing {func.__name__}:\")

    for i, (inputs, expected) in enumerate(test_cases):
        try:
            if isinstance(inputs, tuple):
                result = func(*inputs)
            else:
                result = func(inputs)

            if result == expected:
                print(f\"  Test {i+1}: ✅ PASS\")
            else:
                print(f\"  Test {i+1}: ❌ FAIL - Expected {expected}, got {result}\")

        except Exception as e:
            print(f\"  Test {i+1}: ❌ ERROR - {e}\")

# Example usage
def add_numbers(a, b):
    return a + b

test_cases = [
    ((2, 3), 5),      # Normal case
    ((0, 0), 0),      # Zero case
    ((-1, 1), 0),     # Negative numbers
    ((2.5, 1.5), 4.0) # Floating point
]

test_function(add_numbers, test_cases)
```

### 📝 Logging for Debugging

```python
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_data_with_logging(data):
    \"\"\"Process data with comprehensive logging\"\"\"
    logging.info(f\"Starting to process {len(data)} items\")

    processed_items = []
    errors = 0

    for i, item in enumerate(data):
        logging.debug(f\"Processing item {i}: {item}\")

        try:
            # Some processing that might fail
            if isinstance(item, str):
                processed = item.upper()
            elif isinstance(item, (int, float)):
                processed = item * 2
            else:
                raise TypeError(f\"Unsupported type: {type(item)}\")

            processed_items.append(processed)
            logging.debug(f\"Successfully processed item {i}: {processed}\")

        except Exception as e:
            logging.error(f\"Error processing item {i} ({item}): {e}\")
            errors += 1

    logging.info(f\"Processing complete: {len(processed_items)} successful, {errors} errors\")
    return processed_items

# Test with mixed data types
test_data = [\"hello\", 42, \"world\", 3.14, None, \"python\"]
result = process_data_with_logging(test_data)
```

### 🛡️ Defensive Programming

```python
def robust_function(data, operation=\"sum\"):
    \"\"\"
    Robust function with comprehensive error handling
    \"\"\"
    # Input validation
    if not isinstance(data, (list, tuple)):
        raise TypeError(\"Data must be a list or tuple\")

    if not data:
        logging.warning(\"Empty data provided\")
        return 0

    # Filter valid numbers
    valid_numbers = []
    for item in data:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            valid_numbers.append(item)
        else:
            logging.warning(f\"Skipping invalid item: {item} ({type(item)})\")

    if not valid_numbers:
        raise ValueError(\"No valid numbers found in data\")

    # Perform operation
    try:
        if operation == \"sum\":
            result = sum(valid_numbers)
        elif operation == \"average\":
            result = sum(valid_numbers) / len(valid_numbers)
        elif operation == \"max\":
            result = max(valid_numbers)
        elif operation == \"min\":
            result = min(valid_numbers)
        else:
            raise ValueError(f\"Unsupported operation: {operation}\")

        logging.info(f\"Operation '{operation}' completed successfully\")
        return result

    except Exception as e:
        logging.error(f\"Error during {operation} operation: {e}\")
        raise

# Test robust function
test_data = [1, 2, \"3\", 4.5, None, True, 6]
for op in [\"sum\", \"average\", \"max\", \"min\"]:
    try:
        result = robust_function(test_data, op)
        print(f\"{op.title()}: {result}\")
    except Exception as e:
        print(f\"Error in {op}: {e}\")
```

---

## 🧪 Debugging Exercises

### Exercise 1: Find and Fix Bugs

```python
# This code has several bugs - find and fix them
def calculate_student_grades(students):
    \"\"\"Calculate average grade for each student\"\"\"
    results = {}

    for student in students:
        name = student[\"name\"]
        grades = student[\"grades\"]

        # Bug 1: Division by zero for students with no grades
        average = sum(grades) / len(grades)

        # Bug 2: Wrong condition (should be >=)
        if average > 90:
            letter_grade = \"A\"
        elif average > 80:
            letter_grade = \"B\"
        elif average > 70:
            letter_grade = \"C\"
        elif average > 60:
            letter_grade = \"D\"
        else:
            letter_grade = \"F\"

        # Bug 3: Wrong key name
        results[name] = {
            \"average\": average,
            \"grade\": letter_grade
        }

    return results

# Test data with edge cases
test_students = [
    {\"name\": \"Alice\", \"grades\": [90, 85, 92]},
    {\"name\": \"Bob\", \"grades\": []},  # Empty grades
    {\"name\": \"Charlie\", \"grades\": [80, 80, 80]},  # Exactly 80
]

# This will crash - debug it!
result = calculate_student_grades(test_students)
print(result)
```

### Exercise 2: Debug Logic Error

```python
# This function should return True if a number is prime
def is_prime(n):
    \"\"\"Check if a number is prime - contains logic error\"\"\"
    if n < 2:
        return False

    # Logic error in range
    for i in range(2, n):  # Should be range(2, int(n**0.5) + 1)
        if n % i == 0:
            return False

    return True

# Test and debug
test_numbers = [2, 3, 4, 9, 17, 25, 29]
for num in test_numbers:
    result = is_prime(num)
    print(f\"{num} is prime: {result}\")
```

---

## 📋 Debugging Checklist

- [ ] Read error messages carefully and understand the traceback
- [ ] Check for common errors: syntax, indentation, naming, type mismatches
- [ ] Use print statements to trace program execution
- [ ] Test edge cases and invalid inputs
- [ ] Break complex problems into smaller parts
- [ ] Use debugger tools when print debugging isn't enough
- [ ] Write defensive code with proper error handling
- [ ] Add logging for complex applications
- [ ] Create test cases for your functions
- [ ] Practice debugging regularly to build intuition

---

## 🎯 Key Takeaways

1. **Errors are normal** - even experienced programmers make mistakes
2. **Read error messages** - they contain valuable information
3. **Start with simple debugging** - print statements often solve the problem
4. **Use systematic approaches** - divide and conquer, rubber duck debugging
5. **Learn your tools** - IDEs have powerful debugging features
6. **Write defensive code** - anticipate and handle potential errors
7. **Test thoroughly** - including edge cases and invalid inputs
8. **Practice debugging** - it's a skill that improves with experience

Remember: Good debugging skills will save you hours of frustration and make you a much more effective programmer!

---

**Congratulations!** You've completed Week01 Theory. Next, move on to the exercises in `02_Exercises/` to practice what you've learned.
