# Control Flow: Loops và Conditional Statements

## If-Elif-Else Statements

### Cú pháp cơ bản

```python
# If statement đơn giản
age = 18
if age >= 18:
    print("You are an adult")

# If-else
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-elif-else
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")
```

### Comparison Operators

```python
# Comparison operators
x = 10
y = 20

print(x == y)   # False (equal)
print(x != y)   # True (not equal)
print(x < y)    # True (less than)
print(x > y)    # False (greater than)
print(x <= y)   # True (less than or equal)
print(x >= y)   # False (greater than or equal)

# Chaining comparisons
age = 25
if 18 <= age < 65:
    print("Working age")

# Membership operators
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is available")

if "grape" not in fruits:
    print("Grape is not available")
```

### Logical Operators

```python
# and, or, not
age = 25
has_license = True
has_car = False

# and - tất cả điều kiện phải True
if age >= 18 and has_license:
    print("Can drive")

# or - ít nhất một điều kiện True
if has_license or has_car:
    print("Transportation available")

# not - đảo ngược điều kiện
if not has_car:
    print("Need to buy a car")

# Kết hợp multiple conditions
income = 50000
credit_score = 750
employment_years = 3

if (income > 30000 and credit_score > 700) or employment_years > 5:
    print("Loan approved")
else:
    print("Loan denied")
```

### Ternary Operator

```python
# Cách viết ngắn gọn cho if-else
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# So sánh với if-else thông thường
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ví dụ khác
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(grade)  # Pass

# Nested ternary (không khuyến khích vì khó đọc)
score = 95
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # A
```

## For Loops

### Basic For Loops

```python
# Lặp qua list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Lặp qua string
for char in "Hello":
    print(char)

# Lặp qua range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Range với start và stop
for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

# Range với step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### Enumerate và Zip trong Loops

```python
# enumerate - lấy cả index và value
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# enumerate với custom start
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. orange

# zip - lặp qua multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Hanoi", "Ho Chi Minh", "Da Nang"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, lives in {city}")
```

### Nested Loops

```python
# Nested loops
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row

# Tạo multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print()  # Separator between tables
```

### List Comprehensions (Review)

```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# With condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16]

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary comprehension
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'hello': 5, 'world': 5, 'python': 6}
```

## While Loops

### Basic While Loops

```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop với user input
password = ""
while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password, try again!")
print("Access granted!")

# Infinite loop với break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    print(f"You entered: {user_input}")
```

### While vs For

```python
# Khi nào dùng while vs for

# For - khi biết trước số lần lặp
for i in range(10):
    print(i)

# While - khi không biết trước số lần lặp
import random
target = random.randint(1, 100)
guess = 0
attempts = 0

while guess != target:
    guess = random.randint(1, 100)
    attempts += 1
    print(f"Attempt {attempts}: Guessed {guess}")

print(f"Found {target} in {attempts} attempts!")
```

## Loop Control: Break, Continue, Pass

### Break Statement

```python
# Break - thoát khỏi loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 5:
        print("Found 5, stopping loop")
        break
    print(num)
# Output: 1, 2, 3, 4, Found 5, stopping loop

# Break trong nested loops
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"Breaking at i={i}, j={j}")
            break  # Chỉ break khỏi inner loop
        print(f"i={i}, j={j}")
```

### Continue Statement

```python
# Continue - bỏ qua iteration hiện tại
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num)  # Only prints odd numbers
# Output: 1, 3, 5, 7, 9

# Continue trong data processing
data = [1, 2, "invalid", 4, None, 6, "error", 8]
processed = []
for item in data:
    if not isinstance(item, (int, float)):
        continue  # Skip non-numeric data
    if item is None:
        continue  # Skip None values
    processed.append(item * 2)

print(processed)  # [2, 4, 8, 12, 16]
```

### Pass Statement

```python
# Pass - placeholder, không làm gì
for i in range(5):
    if i == 2:
        pass  # TODO: implement something later
    else:
        print(i)

# Pass trong function definition
def future_function():
    pass  # Will implement later

# Pass trong class definition
class MyClass:
    pass  # Will add methods later
```

### Else với Loops

```python
# Else với for loop - chạy nếu loop hoàn thành không bị break
numbers = [1, 2, 3, 4, 5]
target = 7

for num in numbers:
    if num == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found in the list")
# Output: 7 not found in the list

# Else với while loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed normally")
# Output: Count: 0, Count: 1, Count: 2, Loop completed normally
```

## Practical Applications

### Data Processing với Loops

```python
# Xử lý dữ liệu sinh viên
students = [
    {"name": "Alice", "scores": [85, 92, 78]},
    {"name": "Bob", "scores": [92, 88, 94]},
    {"name": "Charlie", "scores": [76, 82, 80]},
    {"name": "Diana", "scores": [95, 98, 92]}
]

# Tính GPA cho mỗi sinh viên
for student in students:
    total = sum(student["scores"])
    gpa = total / len(student["scores"])
    student["gpa"] = round(gpa, 2)
    print(f"{student['name']}: GPA = {student['gpa']}")

# Tìm sinh viên có điểm cao nhất
highest_gpa = 0
top_student = ""

for student in students:
    if student["gpa"] > highest_gpa:
        highest_gpa = student["gpa"]
        top_student = student["name"]

print(f"Top student: {top_student} with GPA {highest_gpa}")
```

### Data Validation

```python
# Validate user input
def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age (1-120): "))
            if 1 <= age <= 120:
                return age
            else:
                print("Age must be between 1 and 120")
        except ValueError:
            print("Please enter a valid number")

def get_valid_email():
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            return email
        else:
            print("Please enter a valid email address")

# Sử dụng
# age = get_valid_age()
# email = get_valid_email()
```

### Data Analysis Patterns

```python
# Phân tích dữ liệu bán hàng
sales_data = [
    {"month": "Jan", "sales": 15000, "region": "North"},
    {"month": "Jan", "sales": 18000, "region": "South"},
    {"month": "Feb", "sales": 16000, "region": "North"},
    {"month": "Feb", "sales": 19000, "region": "South"},
    {"month": "Mar", "sales": 17000, "region": "North"},
    {"month": "Mar", "sales": 20000, "region": "South"}
]

# Group by month
monthly_sales = {}
for record in sales_data:
    month = record["month"]
    sales = record["sales"]

    if month not in monthly_sales:
        monthly_sales[month] = 0
    monthly_sales[month] += sales

print("Monthly totals:")
for month, total in monthly_sales.items():
    print(f"{month}: ${total:,}")

# Group by region
regional_sales = {}
for record in sales_data:
    region = record["region"]
    sales = record["sales"]

    if region not in regional_sales:
        regional_sales[region] = []
    regional_sales[region].append(sales)

print("\nRegional analysis:")
for region, sales_list in regional_sales.items():
    avg_sales = sum(sales_list) / len(sales_list)
    print(f"{region}: Average ${avg_sales:,.2f}")
```

### Pattern Matching và Search

```python
# Tìm kiếm patterns trong data
log_entries = [
    "INFO: User login successful",
    "ERROR: Database connection failed",
    "WARNING: Low disk space",
    "INFO: User logout",
    "ERROR: File not found",
    "INFO: System startup complete"
]

# Count different log levels
log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

for entry in log_entries:
    for level in log_counts:
        if entry.startswith(level):
            log_counts[level] += 1
            break

print("Log level counts:")
for level, count in log_counts.items():
    print(f"{level}: {count}")

# Filter and process errors
print("\nError details:")
for entry in log_entries:
    if entry.startswith("ERROR"):
        error_msg = entry.split(": ", 1)[1]  # Get message after ": "
        print(f"- {error_msg}")
```

### Matrix Operations

```python
# Làm việc với matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Matrix addition
result = []
for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[i])):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

print("Matrix A + Matrix B:")
for row in result:
    print(row)

# Transpose matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = []
for j in range(len(matrix[0])):  # Number of columns
    column = []
    for i in range(len(matrix)):  # Number of rows
        column.append(matrix[i][j])
    transposed.append(column)

print("\nOriginal matrix:")
for row in matrix:
    print(row)

print("Transposed matrix:")
for row in transposed:
    print(row)
```

## Advanced Control Flow

### Exception Handling trong Loops

```python
# Xử lý errors trong data processing
data = ["1", "2", "invalid", "4", "5.5", "abc", "7"]
processed_numbers = []
errors = []

for item in data:
    try:
        number = float(item)
        processed_numbers.append(number)
    except ValueError:
        errors.append(item)
        continue

print(f"Successfully processed: {processed_numbers}")
print(f"Errors encountered: {errors}")

# Retry mechanism
import time
import random

def unreliable_operation():
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("Operation failed")
    return "Success"

max_retries = 5
for attempt in range(max_retries):
    try:
        result = unreliable_operation()
        print(f"Operation succeeded on attempt {attempt + 1}")
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        if attempt == max_retries - 1:
            print("All attempts failed")
        else:
            time.sleep(1)  # Wait before retry
```

### Performance Considerations

```python
# Hiệu quả với large datasets
import time

# Inefficient way - multiple list iterations
def process_data_slow(data):
    # Multiple passes through data
    evens = [x for x in data if x % 2 == 0]
    squares = [x**2 for x in evens]
    filtered = [x for x in squares if x > 100]
    return filtered

# Efficient way - single pass
def process_data_fast(data):
    result = []
    for x in data:
        if x % 2 == 0:  # Check if even
            square = x**2
            if square > 100:
                result.append(square)
    return result

# Test performance
large_data = list(range(100000))

start_time = time.time()
result1 = process_data_slow(large_data)
slow_time = time.time() - start_time

start_time = time.time()
result2 = process_data_fast(large_data)
fast_time = time.time() - start_time

print(f"Slow method: {slow_time:.4f} seconds")
print(f"Fast method: {fast_time:.4f} seconds")
print(f"Results equal: {result1 == result2}")
```

## Bài tập thực hành

### Bài 1: Grade Analysis System

```python
def analyze_class_performance():
    """
    Phân tích hiệu suất lớp học
    TODO:
    1. Nhập điểm của nhiều sinh viên
    2. Phân loại theo grade (A, B, C, D, F)
    3. Tính thống kê cho từng môn học
    4. Tìm sinh viên cần hỗ trợ (điểm thấp)
    5. Tạo báo cáo tổng hợp
    """
    pass
```

### Bài 2: Data Cleaning Pipeline

```python
def clean_survey_data():
    """
    Làm sạch dữ liệu survey
    TODO:
    1. Remove invalid responses
    2. Handle missing values
    3. Standardize text responses
    4. Validate numeric ranges
    5. Generate data quality report
    """
    pass
```

### Bài 3: Sales Analysis

```python
def analyze_sales_trends():
    """
    Phân tích xu hướng bán hàng
    TODO:
    1. Group sales by time periods
    2. Calculate growth rates
    3. Identify seasonal patterns
    4. Find top performing products/regions
    5. Generate trend predictions
    """
    pass
```

### Bài 4: Password Validator

```python
def create_password_validator():
    """
    Tạo validator cho password
    TODO:
    1. Check minimum length
    2. Require uppercase, lowercase, numbers
    3. Check for special characters
    4. Prevent common passwords
    5. Provide improvement suggestions
    """
    pass
```

## Tóm tắt

### Conditional Statements

- **if-elif-else**: Thực thi code based trên conditions
- **Comparison operators**: ==, !=, <, >, <=, >=
- **Logical operators**: and, or, not
- **Ternary operator**: Ngắn gọn cho simple if-else

### Loops

- **for loops**: Iterate over sequences, ranges
- **while loops**: Continue until condition is False
- **enumerate()**: Get index và value
- **zip()**: Combine multiple iterables

### Loop Control

- **break**: Exit loop immediately
- **continue**: Skip current iteration
- **pass**: Placeholder, do nothing
- **else**: Execute if loop completes normally

### Best Practices

- Use appropriate loop type cho từng situation
- Handle edge cases và errors
- Consider performance với large datasets
- Write readable code với meaningful variable names

### Common Patterns

- Data validation và cleaning
- Grouping và aggregation
- Search và filtering
- Matrix operations
- Error handling và retry logic

### Next Steps

- File I/O operations
- Working with external libraries
- Advanced data structures
- Algorithm optimization
