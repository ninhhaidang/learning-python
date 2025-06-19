# Functions trong Python

## Giới thiệu về Functions

Functions (hàm) là một khối code có thể tái sử dụng để thực hiện một tác vụ cụ thể. Functions giúp:

- Tái sử dụng code
- Tổ chức code tốt hơn
- Dễ debug và maintain
- Tạo abstraction

## Định nghĩa Functions

### Cú pháp cơ bản

```python
def function_name(parameters):
    """Docstring (optional)"""
    # Function body
    return value  # optional

# Ví dụ đơn giản
def greet():
    print("Hello, World!")

# Gọi function
greet()  # Hello, World!
```

### Function với parameters

```python
def greet_person(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    result = a + b
    return result

# Sử dụng
greet_person("Alice")  # Hello, Alice!
sum_result = add_numbers(5, 3)
print(sum_result)  # 8
```

### Function với return value

```python
def calculate_area(length, width):
    """Tính diện tích hình chữ nhật"""
    area = length * width
    return area

def get_full_name(first_name, last_name):
    """Tạo họ tên đầy đủ"""
    full_name = f"{first_name} {last_name}"
    return full_name

# Sử dụng
rectangle_area = calculate_area(10, 5)
print(f"Area: {rectangle_area}")  # Area: 50

name = get_full_name("John", "Doe")
print(name)  # John Doe
```

## Parameters và Arguments

### Positional Arguments

```python
def introduce(name, age, city):
    print(f"My name is {name}, I'm {age} years old, and I live in {city}")

# Thứ tự quan trọng
introduce("Alice", 25, "Hanoi")  # My name is Alice, I'm 25 years old, and I live in Hanoi
introduce("Hanoi", "Alice", 25)  # Sai thứ tự - kết quả không mong muốn
```

### Keyword Arguments

```python
def introduce(name, age, city):
    print(f"My name is {name}, I'm {age} years old, and I live in {city}")

# Sử dụng keyword arguments
introduce(age=25, name="Alice", city="Hanoi")  # Thứ tự không quan trọng
introduce("Bob", city="Ho Chi Minh", age=30)   # Mix positional và keyword
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

def calculate_power(base, exponent=2):
    return base ** exponent

# Sử dụng
greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!

print(calculate_power(5))    # 25 (5^2)
print(calculate_power(5, 3)) # 125 (5^3)
```

### Variable-length Arguments

```python
# *args - Variable positional arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - Variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Hanoi")
# name: Alice
# age: 25
# city: Hanoi

# Kết hợp tất cả
def flexible_function(required, default="default", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function("must_have", "optional", 1, 2, 3, name="Alice", age=25)
```

## Scope và Variables

### Local vs Global Scope

```python
# Global variable
global_var = "I'm global"

def demo_scope():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {global_var}")  # Có thể truy cập global
    print(f"Inside function: {local_var}")

demo_scope()
print(f"Outside function: {global_var}")
# print(f"Outside function: {local_var}")  # Error: local_var không tồn tại

# Modifying global variables
counter = 0

def increment():
    global counter  # Khai báo sử dụng global variable
    counter += 1

print(counter)  # 0
increment()
print(counter)  # 1
```

### Nonlocal Scope

```python
def outer_function():
    x = 10

    def inner_function():
        nonlocal x  # Truy cập biến của outer function
        x += 5
        print(f"Inner: {x}")

    print(f"Before inner: {x}")
    inner_function()
    print(f"After inner: {x}")

outer_function()
# Before inner: 10
# Inner: 15
# After inner: 15
```

## Advanced Function Concepts

### Lambda Functions

```python
# Function thông thường
def square(x):
    return x ** 2

# Lambda function (anonymous function)
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25

# Lambda với multiple parameters
add = lambda x, y: x + y
print(add(3, 7))  # 10

# Sử dụng lambda với built-in functions
numbers = [1, 2, 3, 4, 5]

# map() với lambda
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter() với lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sorted() với lambda
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(sorted_by_grade)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

### Higher-order Functions

```python
# Function nhận function khác làm parameter
def apply_operation(numbers, operation):
    result = []
    for num in numbers:
        result.append(operation(num))
    return result

def double(x):
    return x * 2

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
doubled = apply_operation(numbers, double)
squared = apply_operation(numbers, square)

print(doubled)  # [2, 4, 6, 8, 10]
print(squared)  # [1, 4, 9, 16, 25]

# Function trả về function khác
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_3 = create_multiplier(3)
times_5 = create_multiplier(5)

print(times_3(4))  # 12
print(times_5(4))  # 20
```

### Decorators (Cơ bản)

```python
# Decorator function
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# Sử dụng decorator
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before function call
# Hello!
# After function call

# Decorator với parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

## Built-in Functions hữu ích

### Map, Filter, Reduce

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() - áp dụng function cho mỗi element
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter() - lọc elements theo điều kiện
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce() - giảm list thành single value
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 15

product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
```

### Zip và Enumerate

```python
# zip() - kết hợp multiple iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Hanoi", "Ho Chi Minh", "Da Nang"]

combined = list(zip(names, ages, cities))
print(combined)  # [('Alice', 25, 'Hanoi'), ('Bob', 30, 'Ho Chi Minh'), ('Charlie', 35, 'Da Nang')]

# Unpacking với zip
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")

# enumerate() - thêm index
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# enumerate với start parameter
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. orange
```

## Functions trong Data Science

### Data Processing Functions

```python
# Hàm xử lý dữ liệu nhiệt độ
def celsius_to_fahrenheit(celsius):
    """Chuyển đổi Celsius sang Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Chuyển đổi Fahrenheit sang Celsius"""
    return (fahrenheit - 32) * 5/9

def analyze_temperatures(temps_celsius):
    """Phân tích dữ liệu nhiệt độ"""
    temps_fahrenheit = [celsius_to_fahrenheit(temp) for temp in temps_celsius]

    analysis = {
        "count": len(temps_celsius),
        "avg_celsius": sum(temps_celsius) / len(temps_celsius),
        "avg_fahrenheit": sum(temps_fahrenheit) / len(temps_fahrenheit),
        "max_celsius": max(temps_celsius),
        "min_celsius": min(temps_celsius),
        "range_celsius": max(temps_celsius) - min(temps_celsius)
    }

    return analysis

# Sử dụng
daily_temps = [22.5, 24.1, 23.8, 26.3, 25.7, 21.9, 27.2]
temp_analysis = analyze_temperatures(daily_temps)

for key, value in temp_analysis.items():
    print(f"{key}: {value:.2f}")
```

### Statistical Functions

```python
def calculate_mean(numbers):
    """Tính trung bình"""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Tính trung vị"""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        return sorted_nums[n//2]

def calculate_mode(numbers):
    """Tìm mode (giá trị xuất hiện nhiều nhất)"""
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]
    return modes[0] if len(modes) == 1 else modes

def calculate_variance(numbers):
    """Tính phương sai"""
    mean = calculate_mean(numbers)
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    return sum(squared_diffs) / len(numbers)

def calculate_std_dev(numbers):
    """Tính độ lệch chuẩn"""
    return calculate_variance(numbers) ** 0.5

# Hàm tổng hợp
def describe_data(numbers):
    """Mô tả thống kê dữ liệu"""
    return {
        "count": len(numbers),
        "mean": calculate_mean(numbers),
        "median": calculate_median(numbers),
        "mode": calculate_mode(numbers),
        "variance": calculate_variance(numbers),
        "std_dev": calculate_std_dev(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "range": max(numbers) - min(numbers)
    }

# Sử dụng
data = [23, 25, 24, 26, 23, 27, 25, 24, 26, 25]
stats = describe_data(data)

print("Data Statistics:")
for key, value in stats.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")
```

### Data Cleaning Functions

```python
def clean_numeric_data(data):
    """Làm sạch dữ liệu số"""
    cleaned = []
    for item in data:
        try:
            # Chuyển đổi sang số
            if isinstance(item, str):
                # Loại bỏ whitespace và ký tự đặc biệt
                item = item.strip().replace(',', '').replace('$', '')
                if item.lower() in ['null', 'none', 'na', '']:
                    continue  # Bỏ qua giá trị null

            num = float(item)
            if not (num != num):  # Kiểm tra NaN
                cleaned.append(num)
        except (ValueError, TypeError):
            continue  # Bỏ qua giá trị không hợp lệ

    return cleaned

def remove_outliers(data, method='iqr'):
    """Loại bỏ outliers"""
    if method == 'iqr':
        # Interquartile Range method
        sorted_data = sorted(data)
        n = len(sorted_data)
        q1 = sorted_data[n//4]
        q3 = sorted_data[3*n//4]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        return [x for x in data if lower_bound <= x <= upper_bound]

    elif method == 'zscore':
        # Z-score method (simplified)
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean)**2 for x in data) / len(data)) ** 0.5
        return [x for x in data if abs((x - mean) / std_dev) < 3]

# Test data cleaning
messy_data = ['23.5', '25.1', 'null', '22.8', '$26.30', '24.7', 'invalid', '150.0', '21.9']
cleaned = clean_numeric_data(messy_data)
print(f"Original: {messy_data}")
print(f"Cleaned: {cleaned}")

# Remove outliers
no_outliers = remove_outliers(cleaned)
print(f"No outliers: {no_outliers}")
```

## Error Handling trong Functions

```python
def safe_divide(a, b):
    """Chia an toàn với error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid data types!")
        return None

def validate_age(age):
    """Validate tuổi với custom exceptions"""
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
        return age
    except ValueError as e:
        print(f"Invalid age: {e}")
        return None

# Sử dụng
print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error: Cannot divide by zero! None

print(validate_age(25))     # 25
print(validate_age(-5))     # Invalid age: Age cannot be negative None
print(validate_age("abc"))  # Invalid age: invalid literal for int()... None
```

## Best Practices

### Function Design Principles

```python
# 1. Single Responsibility - mỗi function chỉ làm một việc
def calculate_bmi(weight, height):
    """Tính BMI"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Phân loại BMI"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# 2. Descriptive names và docstrings
def process_student_grades(grades_list, passing_grade=60):
    """
    Process student grades and return statistics.

    Args:
        grades_list (list): List of numerical grades
        passing_grade (int): Minimum grade to pass (default: 60)

    Returns:
        dict: Statistics including average, pass rate, etc.
    """
    if not grades_list:
        return {"error": "No grades provided"}

    avg_grade = sum(grades_list) / len(grades_list)
    passing_students = len([g for g in grades_list if g >= passing_grade])
    pass_rate = (passing_students / len(grades_list)) * 100

    return {
        "average": avg_grade,
        "total_students": len(grades_list),
        "passing_students": passing_students,
        "pass_rate": pass_rate
    }

# 3. Input validation
def calculate_circle_area(radius):
    """Tính diện tích hình tròn với validation"""
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    import math
    return math.pi * radius ** 2
```

## Bài tập thực hành

### Bài 1: Temperature Analysis System

```python
def create_temperature_analyzer():
    """
    Tạo hệ thống phân tích nhiệt độ
    TODO:
    1. Function convert nhiệt độ (C <-> F <-> K)
    2. Function tính thống kê (mean, median, mode, std)
    3. Function phân loại nhiệt độ (cold, mild, warm, hot)
    4. Function tìm trends (increasing, decreasing, stable)
    """
    pass
```

### Bài 2: Student Grade Management

```python
def create_grade_system():
    """
    Hệ thống quản lý điểm sinh viên
    TODO:
    1. Function calculate GPA from grades
    2. Function determine letter grade (A, B, C, D, F)
    3. Function analyze class performance
    4. Function identify students needing help
    """
    pass
```

### Bài 3: Data Cleaning Pipeline

```python
def create_data_cleaner():
    """
    Tạo pipeline làm sạch dữ liệu
    TODO:
    1. Function remove null values
    2. Function normalize text data
    3. Function detect and handle outliers
    4. Function validate data formats
    """
    pass
```

## Tóm tắt

### Key Concepts

- **Function definition**: `def` keyword, parameters, return
- **Scope**: Local, global, nonlocal
- **Arguments**: Positional, keyword, default, \*args, \*\*kwargs
- **Lambda functions**: Anonymous functions
- **Higher-order functions**: Functions as parameters/returns

### Best Practices

- Single responsibility principle
- Descriptive names và docstrings
- Input validation và error handling
- Keep functions focused và reusable

### Built-in Functions

- `map()`, `filter()`, `reduce()`
- `zip()`, `enumerate()`
- `sorted()`, `max()`, `min()`, `sum()`

### Applications

- Data processing pipelines
- Statistical calculations
- Data cleaning và validation
- Reusable analysis functions

### Next Steps

- Advanced decorators
- Generators và iterators
- Context managers
- Object-oriented programming
