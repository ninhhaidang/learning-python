# Exercise 10: Combined Operations - Guide

## 🎯 Mục tiêu học tập

Bài tập này giúp bạn:

- Tích hợp tất cả kiến thức từ Week 1
- Xây dựng chương trình đa chức năng
- Thực hành với menu-driven program
- Áp dụng concepts vào bài toán thực tế
- Tổ chức code theo modules/functions

## 📋 Chuẩn bị

### Kiến thức cần tổng hợp:

- Variables và data types (string, int, float, bool)
- Input/output operations với `input()` và `print()`
- Arithmetic operators và calculations
- String manipulation và formatting
- Type conversions
- Boolean logic và conditions
- Code organization

### Cấu trúc chương trình:

- Menu system để lựa chọn chức năng
- Từng module xử lý một problem cụ thể
- Error handling cơ bản
- Professional output formatting

## 🚀 Hướng dẫn từng bước

### Bước 1: Thiết lập main menu

```python
def show_menu():
    print("=== Python Fundamentals Integration ===")
    print()
    print("Choose a program to run:")
    print("1. Personal Information Manager")
    print("2. Budget Calculator")
    print("3. Grade Analyzer")
    print("4. Geometry Calculator")
    print("5. Unit Converter")
    print("6. Exit")
    print()

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            personal_info_manager()
        elif choice == "2":
            budget_calculator()
        elif choice == "3":
            grade_analyzer()
        elif choice == "4":
            geometry_calculator()
        elif choice == "5":
            unit_converter()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")
        print("\n" + "="*50 + "\n")
```

### Bước 2: Module 1 - Personal Information Manager

```python
def personal_info_manager():
    print("=== PERSONAL INFORMATION MANAGER ===")

    # Collect basic info
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (cm): "))
    weight = float(input("Enter your weight (kg): "))

    # Calculations
    height_m = height / 100  # Convert to meters
    bmi = weight / (height_m ** 2)

    # Determine BMI category
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # Display results
    print(f"\n=== PROFILE FOR {name.upper()} ===")
    print(f"Age: {age} years")
    print(f"Height: {height} cm")
    print(f"Weight: {weight} kg")
    print(f"BMI: {bmi:.1f} ({bmi_category})")
```

### Bước 3: Module 2 - Budget Calculator

```python
def budget_calculator():
    print("=== BUDGET CALCULATOR ===")

    # Income input
    income_str = input("Enter your monthly income: $")
    income = float(income_str.replace(",", ""))

    # Expense categories
    print("\nEnter your expenses:")
    rent = float(input("  Rent: $"))
    food = float(input("  Food: $"))
    transport = float(input("  Transportation: $"))
    entertainment = float(input("  Entertainment: $"))
    other = float(input("  Other: $"))

    # Calculations
    total_expenses = rent + food + transport + entertainment + other
    remaining = income - total_expenses
    savings_rate = (remaining / income) * 100 if income > 0 else 0

    # Format output
    print("\n┌─────────────────────────────┐")
    print("│       BUDGET SUMMARY        │")
    print("├─────────────────────────────┤")
    print(f"│ Monthly Income: ${income:,.2f}   │")
    print(f"│ Total Expenses: ${total_expenses:,.2f}   │")
    print(f"│ Remaining: ${remaining:,.2f}        │")
    print(f"│ Savings Rate: {savings_rate:.1f}%         │")
    print("└─────────────────────────────┘")
```

### Bước 4: Module 3 - Grade Analyzer

```python
def grade_analyzer():
    print("=== GRADE ANALYZER ===")

    # Collect grades
    print("Enter your grades (0-100):")
    math_grade = float(input("Mathematics: "))
    science_grade = float(input("Science: "))
    english_grade = float(input("English: "))
    history_grade = float(input("History: "))

    # Calculations
    grades = [math_grade, science_grade, english_grade, history_grade]
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    # Determine letter grade
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Display results
    print("\n=== GRADE REPORT ===")
    print(f"Mathematics: {math_grade}")
    print(f"Science: {science_grade}")
    print(f"English: {english_grade}")
    print(f"History: {history_grade}")
    print("-" * 20)
    print(f"Average: {average:.1f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
```

### Bước 5: Module 4 - Geometry Calculator

```python
def geometry_calculator():
    print("=== GEOMETRY CALCULATOR ===")

    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    shape = input("Enter choice (1-3): ")

    if shape == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        perimeter = 2 * (length + width)
        print(f"Rectangle - Area: {area}, Perimeter: {perimeter}")

    elif shape == "2":
        radius = float(input("Enter radius: "))
        pi = 3.14159
        area = pi * radius ** 2
        circumference = 2 * pi * radius
        print(f"Circle - Area: {area:.2f}, Circumference: {circumference:.2f}")

    elif shape == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Triangle - Area: {area}")
```

### Bước 6: Module 5 - Unit Converter

```python
def unit_converter():
    print("=== UNIT CONVERTER ===")

    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Meters to Feet")
    print("3. Kilograms to Pounds")

    conversion = input("Enter choice (1-3): ")

    if conversion == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")

    elif conversion == "2":
        meters = float(input("Enter distance in meters: "))
        feet = meters * 3.28084
        print(f"{meters}m = {feet:.2f} feet")

    elif conversion == "3":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg}kg = {pounds:.2f} pounds")
```

## 💡 Kỹ thuật quan trọng

### 1. Menu-driven Programming

```python
# Sử dụng while loop cho menu chính
while True:
    # Show menu
    # Get choice
    # Process choice
    # Exit condition
```

### 2. Input Validation

```python
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
```

### 3. Professional Formatting

```python
# Sử dụng borders và alignment
print("┌─────────────────────────────┐")
print(f"│ Value: {value:<20} │")
print("└─────────────────────────────┘")
```

### 4. Code Organization

```python
# Tách từng functionality thành function riêng
def main():
    # Main program logic

def module1():
    # Specific functionality

def module2():
    # Another functionality
```

## 🔍 Common Issues & Solutions

### Issue 1: Menu không lặp lại

```python
# Wrong
choice = input("Enter choice: ")
if choice == "1":
    function1()

# Right
while True:
    choice = input("Enter choice: ")
    if choice == "1":
        function1()
    elif choice == "6":
        break
```

### Issue 2: Input validation

```python
# Add try-except cho numeric inputs
try:
    value = float(input("Enter number: "))
except ValueError:
    print("Invalid input")
    continue
```

### Issue 3: String formatting

```python
# Consistent formatting across modules
print(f"Value: ${value:,.2f}")  # Currency with commas
print(f"Percentage: {percent:.1f}%")  # One decimal
```

## ✅ Checklist hoàn thành

- [ ] Main menu hoạt động đúng
- [ ] Tất cả 5 modules được implement
- [ ] Input validation cho numeric values
- [ ] Professional output formatting
- [ ] Proper exit functionality
- [ ] Clear separation between modules
- [ ] Consistent coding style
- [ ] Comments giải thích logic

## 🎯 Thử thách nâng cao

1. **Data persistence**: Lưu results vào file
2. **Enhanced validation**: Validate all inputs thoroughly
3. **Better UI**: Colors, clear screen, better formatting
4. **More modules**: Add calculator, password generator, etc.
5. **Configuration**: Allow users to customize settings

Đây là bài tập tổng hợp quan trọng nhất Week 1! 🚀
