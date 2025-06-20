# 💬 Input/Output Operations

## 📖 Mục lục

1. [Output with print()](#1-output-with-print)
2. [Input with input()](#2-input-with-input)
3. [Formatting Output](#3-formatting-output)
4. [File Input/Output Basics](#4-file-inputoutput-basics)
5. [Error Handling for I/O](#5-error-handling-for-io)
6. [Interactive Programs](#6-interactive-programs)

---

## 1. Output with print()

### 📺 Basic print() Function

```python
# Simple output
print(\"Hello, World!\")
print('Python is awesome!')

# Multiple arguments
print(\"Hello\", \"World\", \"from\", \"Python\")
# Output: Hello World from Python

# Mixed data types
name = \"Alice\"
age = 25
print(\"Name:\", name, \"Age:\", age)
# Output: Name: Alice Age: 25
```

### 🎨 print() Parameters

```python
# Separator parameter
print(\"A\", \"B\", \"C\")                    # A B C (default separator: space)
print(\"A\", \"B\", \"C\", sep=\"-\")            # A-B-C
print(\"A\", \"B\", \"C\", sep=\" | \")          # A | B | C
print(\"A\", \"B\", \"C\", sep=\"\")             # ABC (no separator)

# End parameter
print(\"Hello\", end=\" \")                   # No newline at end
print(\"World\")                           # Output: Hello World (same line)

print(\"Line 1\", end=\"\\n\\n\")              # Double newline
print(\"Line 2\")

# Combined parameters
print(\"Name\", \"Age\", \"City\", sep=\", \", end=\".\\n\")
# Output: Name, Age, City.
```

### 📁 Output to Files

```python
# Print to file
with open(\"output.txt\", \"w\") as file:
    print(\"Hello, File!\", file=file)
    print(\"This goes to the file\", file=file)

# Print to both console and file
import sys
print(\"This goes to console\")
print(\"This goes to file\", file=open(\"log.txt\", \"w\"))
```

### 🎯 Advanced print() Techniques

```python
# Print without spaces between arguments
items = [\"apple\", \"banana\", \"cherry\"]
print(*items, sep=\", \")  # apple, banana, cherry

# Print with flush (immediately output)
import time
for i in range(5):
    print(f\"Count: {i}\", end=\" \", flush=True)
    time.sleep(1)
```

---

## 2. Input with input()

### ⌨️ Basic input() Function

```python
# Simple input (always returns string)
name = input(\"Enter your name: \")
print(f\"Hello, {name}!\")

# Input without prompt
user_input = input()  # Waits for user input
print(f\"You entered: {user_input}\")
```

### 🔢 Input with Type Conversion

```python
# Convert to integer
age_str = input(\"Enter your age: \")
age = int(age_str)
print(f\"Next year you'll be {age + 1}\")

# One-liner conversion
age = int(input(\"Enter your age: \"))
height = float(input(\"Enter your height in meters: \"))
is_student = input(\"Are you a student? (yes/no): \").lower() == \"yes\"

# Multiple inputs in one line
numbers = input(\"Enter three numbers separated by spaces: \").split()
num1, num2, num3 = map(int, numbers)
print(f\"Sum: {num1 + num2 + num3}\")
```

### ⚠️ Input Validation

```python
# Basic validation
while True:
    age_str = input(\"Enter your age (0-120): \")
    try:
        age = int(age_str)
        if 0 <= age <= 120:
            break
        else:
            print(\"Age must be between 0 and 120\")
    except ValueError:
        print(\"Please enter a valid number\")

print(f\"Your age is: {age}\")
```

### 🛡️ Safe Input Functions

```python
def get_int(prompt, min_val=None, max_val=None):
    \"\"\"Safely get integer input with validation\"\"\"
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f\"Value must be at least {min_val}\")
                continue
            if max_val is not None and value > max_val:
                print(f\"Value must be at most {max_val}\")
                continue
            return value
        except ValueError:
            print(\"Please enter a valid integer\")

def get_float(prompt):
    \"\"\"Safely get float input\"\"\"
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(\"Please enter a valid number\")

def get_yes_no(prompt):
    \"\"\"Get yes/no input\"\"\"
    while True:
        response = input(prompt + \" (yes/no): \").lower()
        if response in ['yes', 'y', '1', 'true']:
            return True
        elif response in ['no', 'n', '0', 'false']:
            return False
        else:
            print(\"Please enter yes or no\")

# Usage examples
age = get_int(\"Enter your age: \", 0, 120)
height = get_float(\"Enter your height: \")
is_student = get_yes_no(\"Are you a student?\")
```

---

## 3. Formatting Output

### 🎨 f-strings (Python 3.6+) - Recommended

```python
name = \"Alice\"
age = 25
height = 5.6
balance = 1234.567

# Basic f-string
print(f\"Hello, {name}!\")

# Expressions in f-strings
print(f\"Next year, {name} will be {age + 1} years old\")

# Number formatting
print(f\"Balance: ${balance:.2f}\")        # $1234.57
print(f\"Balance: ${balance:,.2f}\")       # $1,234.57
print(f\"Height: {height:.1f} feet\")     # 5.6 feet

# Alignment and padding
print(f\"Name: {name:>10}\")              # Right align in 10 chars
print(f\"Name: {name:<10}\")              # Left align in 10 chars
print(f\"Name: {name:^10}\")              # Center align in 10 chars
print(f\"Number: {42:05d}\")              # Pad with zeros: 00042

# Percentage
ratio = 0.85
print(f\"Success rate: {ratio:.1%}\")     # Success rate: 85.0%
```

### 🔧 .format() Method

```python
# Basic format
name = \"Bob\"
age = 30
print(\"Hello, {}! You are {} years old.\".format(name, age))

# Positional arguments
print(\"{0} is {1} years old. {0} lives in {2}.\".format(name, age, \"NYC\"))

# Named arguments
print(\"{name} is {age} years old.\".format(name=\"Charlie\", age=35))

# Number formatting
price = 19.99
print(\"Price: ${:.2f}\".format(price))    # Price: $19.99
```

### 📊 Advanced Formatting

```python
# Date and time formatting
from datetime import datetime
now = datetime.now()
print(f\"Current time: {now:%Y-%m-%d %H:%M:%S}\")

# Scientific notation
big_number = 1234567890
print(f\"Scientific: {big_number:.2e}\")   # 1.23e+09

# Binary, octal, hex
number = 255
print(f\"Binary: {number:b}\")            # 11111111
print(f\"Octal: {number:o}\")             # 377
print(f\"Hex: {number:x}\")               # ff
print(f\"Hex (upper): {number:X}\")       # FF

# Complex formatting
data = [(\"Alice\", 85.5), (\"Bob\", 92.3), (\"Charlie\", 78.9)]
print(\"Student Grades:\")
print(\"-\" * 20)
for name, grade in data:
    print(f\"{name:<10} {grade:>6.1f}%\")
```

---

## 4. File Input/Output Basics

### 📝 Writing to Files

```python
# Write text to file
with open(\"example.txt\", \"w\") as file:
    file.write(\"Hello, File!\\n\")
    file.write(\"This is line 2\\n\")

# Write multiple lines
lines = [\"Line 1\\n\", \"Line 2\\n\", \"Line 3\\n\"]
with open(\"multiple_lines.txt\", \"w\") as file:
    file.writelines(lines)

# Using print to write to file
with open(\"print_to_file.txt\", \"w\") as file:
    print(\"Hello from print!\", file=file)
    print(\"Another line\", file=file)
```

### 📖 Reading from Files

```python
# Read entire file
try:
    with open(\"example.txt\", \"r\") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(\"File not found!\")

# Read line by line
with open(\"example.txt\", \"r\") as file:
    for line_number, line in enumerate(file, 1):
        print(f\"Line {line_number}: {line.strip()}\")

# Read all lines into a list
with open(\"example.txt\", \"r\") as file:
    lines = file.readlines()
    print(f\"File has {len(lines)} lines\")
```

---

## 5. Error Handling for I/O

### 🛡️ Handling Input Errors

```python
def safe_input(prompt, data_type=str, validator=None):
    \"\"\"
    Safely get input with type conversion and validation

    Args:
        prompt: String to display to user
        data_type: Type to convert to (int, float, str)
        validator: Function to validate input
    \"\"\"
    while True:
        try:
            user_input = input(prompt)

            # Convert to desired type
            if data_type != str:
                converted_input = data_type(user_input)
            else:
                converted_input = user_input

            # Validate if validator function provided
            if validator and not validator(converted_input):
                print(\"Invalid input. Please try again.\")
                continue

            return converted_input

        except ValueError:
            print(f\"Please enter a valid {data_type.__name__}\")
        except KeyboardInterrupt:
            print(\"\\nProgram interrupted by user\")
            exit()

# Usage examples
age = safe_input(\"Enter age: \", int, lambda x: 0 <= x <= 120)
email = safe_input(\"Enter email: \", str, lambda x: \"@\" in x)
```

### 📁 Handling File Errors

```python
def safe_file_read(filename):
    \"\"\"Safely read file with error handling\"\"\"
    try:
        with open(filename, \"r\") as file:
            return file.read()
    except FileNotFoundError:
        print(f\"Error: File '{filename}' not found\")
        return None
    except PermissionError:
        print(f\"Error: Permission denied to read '{filename}'\")
        return None
    except Exception as e:
        print(f\"Unexpected error reading file: {e}\")
        return None

def safe_file_write(filename, content):
    \"\"\"Safely write to file with error handling\"\"\"
    try:
        with open(filename, \"w\") as file:
            file.write(content)
        print(f\"Successfully wrote to '{filename}'\")
        return True
    except PermissionError:
        print(f\"Error: Permission denied to write '{filename}'\")
        return False
    except Exception as e:
        print(f\"Unexpected error writing file: {e}\")
        return False
```

---

## 6. Interactive Programs

### 🎮 Menu-Driven Program

```python
def display_menu():
    \"\"\"Display program menu\"\"\"
    print(\"\\n\" + \"=\"*30)
    print(\"    CALCULATOR MENU\")
    print(\"=\"*30)
    print(\"1. Addition\")
    print(\"2. Subtraction\")
    print(\"3. Multiplication\")
    print(\"4. Division\")
    print(\"5. Exit\")
    print(\"-\"*30)

def get_numbers():
    \"\"\"Get two numbers from user\"\"\"
    num1 = get_float(\"Enter first number: \")
    num2 = get_float(\"Enter second number: \")
    return num1, num2

def calculator():
    \"\"\"Main calculator function\"\"\"
    while True:
        display_menu()

        choice = safe_input(\"Enter choice (1-5): \", int,
                           lambda x: 1 <= x <= 5)

        if choice == 5:
            print(\"Thank you for using the calculator!\")
            break

        num1, num2 = get_numbers()

        if choice == 1:
            result = num1 + num2
            operation = \"addition\"
        elif choice == 2:
            result = num1 - num2
            operation = \"subtraction\"
        elif choice == 3:
            result = num1 * num2
            operation = \"multiplication\"
        elif choice == 4:
            if num2 == 0:
                print(\"Error: Cannot divide by zero!\")
                continue
            result = num1 / num2
            operation = \"division\"

        print(f\"\\nResult of {operation}: {result:.2f}\")

        # Ask if user wants to continue
        if not get_yes_no(\"\\nDo another calculation?\"):
            print(\"Thank you for using the calculator!\")
            break

# Run the calculator
if __name__ == \"__main__\":
    calculator()
```

### 🔄 Data Collection Program

```python
def collect_student_data():
    \"\"\"Collect and store student information\"\"\"
    students = []

    print(\"Student Data Collection System\")
    print(\"Enter 'quit' for name to stop\\n\")

    while True:
        # Get student name
        name = input(\"Enter student name: \").strip()
        if name.lower() == 'quit':
            break

        if not name:
            print(\"Name cannot be empty. Please try again.\")
            continue

        # Get student data
        age = safe_input(\"Enter age: \", int, lambda x: 5 <= x <= 100)
        grade = safe_input(\"Enter grade (0-100): \", float,
                          lambda x: 0 <= x <= 100)

        # Store student data
        student = {
            \"name\": name,
            \"age\": age,
            \"grade\": grade
        }
        students.append(student)

        print(f\"Added {name} to the database\\n\")

    # Display summary
    if students:
        print(\"\\n\" + \"=\"*40)
        print(\"         STUDENT SUMMARY\")
        print(\"=\"*40)

        total_grade = 0
        for i, student in enumerate(students, 1):
            print(f\"{i:2d}. {student['name']:<15} Age: {student['age']:2d} Grade: {student['grade']:5.1f}\")
            total_grade += student['grade']

        average_grade = total_grade / len(students)
        print(\"-\"*40)
        print(f\"Total students: {len(students)}\")
        print(f\"Average grade: {average_grade:.1f}\")

        # Save to file
        if get_yes_no(\"Save data to file?\"):
            save_student_data(students)
    else:
        print(\"No student data collected.\")

def save_student_data(students):
    \"\"\"Save student data to file\"\"\"
    filename = \"student_data.txt\"
    try:
        with open(filename, \"w\") as file:
            file.write(\"Student Data Report\\n\")
            file.write(\"=\" * 40 + \"\\n\\n\")

            for i, student in enumerate(students, 1):
                file.write(f\"{i:2d}. Name: {student['name']:<15} \")
                file.write(f\"Age: {student['age']:2d} \")
                file.write(f\"Grade: {student['grade']:5.1f}\\n\")

            total_grade = sum(s['grade'] for s in students)
            average = total_grade / len(students)
            file.write(f\"\\nTotal students: {len(students)}\\n\")
            file.write(f\"Average grade: {average:.1f}\\n\")

        print(f\"Data saved to {filename}\")
    except Exception as e:
        print(f\"Error saving file: {e}\")

# Run the program
if __name__ == \"__main__\":
    collect_student_data()
```

---

## 🧪 Practice Exercises

### Exercise 1: Personal Information Collector

```python
\"\"\"
Create a program that collects personal information
and displays it in a formatted way
\"\"\"

def personal_info_collector():
    print(\"Personal Information Form\")
    print(\"=\" * 30)

    # Collect information
    first_name = input(\"First Name: \").strip().title()
    last_name = input(\"Last Name: \").strip().title()
    age = safe_input(\"Age: \", int, lambda x: 0 <= x <= 150)
    email = safe_input(\"Email: \", str, lambda x: \"@\" in x and \".\" in x)
    phone = input(\"Phone Number: \").strip()

    # Display formatted information
    print(\"\\n\" + \"=\" * 40)
    print(\"         INFORMATION SUMMARY\")
    print(\"=\" * 40)
    print(f\"Name:     {first_name} {last_name}\")
    print(f\"Age:      {age} years old\")
    print(f\"Email:    {email}\")
    print(f\"Phone:    {phone}\")
    print(\"=\" * 40)

personal_info_collector()
```

### Exercise 2: Simple Grade Calculator

```python
\"\"\"
Grade calculator that accepts multiple test scores
and calculates average with letter grade
\"\"\"

def grade_calculator():
    print(\"Grade Calculator\")
    print(\"Enter test scores (0-100). Enter -1 to finish.\\n\")

    scores = []
    while True:
        score = safe_input(\"Enter score: \", float,
                          lambda x: -1 <= x <= 100)
        if score == -1:
            break
        scores.append(score)
        print(f\"Added score: {score}\")

    if scores:
        average = sum(scores) / len(scores)

        # Determine letter grade
        if average >= 90:
            letter = \"A\"
        elif average >= 80:
            letter = \"B\"
        elif average >= 70:
            letter = \"C\"
        elif average >= 60:
            letter = \"D\"
        else:
            letter = \"F\"

        print(f\"\\nScores entered: {len(scores)}\")
        print(f\"Average: {average:.1f}\")
        print(f\"Letter Grade: {letter}\")
    else:
        print(\"No scores entered.\")

grade_calculator()
```

---

## 📋 I/O Operations Checklist

- [ ] Understand print() function and its parameters
- [ ] Can get user input with input() function
- [ ] Know how to convert input to different data types
- [ ] Can format output using f-strings
- [ ] Understand basic file I/O operations
- [ ] Can handle input/output errors gracefully
- [ ] Can create interactive menu-driven programs
- [ ] Can validate user input effectively
- [ ] Practice with real-world examples

---

## 🎯 Key Takeaways

1. **print()** is versatile with parameters like `sep`, `end`, and `file`
2. **input()** always returns strings - convert as needed
3. **f-strings** are the modern, preferred way to format output
4. **Always validate user input** to prevent errors
5. **Use context managers** (`with open()`) for file operations
6. **Handle exceptions** gracefully for better user experience
7. **Create helper functions** for common input validation patterns
8. **Interactive programs** make software more user-friendly

---

**Next**: Continue to `07_operators_and_expressions.md` to learn about performing operations and calculations.
