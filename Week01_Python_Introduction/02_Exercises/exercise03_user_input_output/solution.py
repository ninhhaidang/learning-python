"""
Exercise 03: User Input & Output - Complete Solution

This file contains a complete solution for Exercise 03.
Study this code after attempting the exercise yourself.

Key concepts demonstrated:
- input() function usage
- Type conversion (int(), float(), str())
- String processing methods
- Boolean input handling
- Formatted output with f-strings
- Basic calculations with user input
"""

print("=== Personal Information Collector ===")
print()
print("Please enter your information:")

# Task 1: Basic User Input
# Get user's basic information
full_name = input("Enter your full name: ").strip()
age_str = input("Enter your age: ").strip()
height_str = input("Enter your height in meters: ").strip()
favorite_color = input("Enter your favorite color: ").strip()
student_input = input("Are you a student? (yes/no): ").strip().lower()
current_year_str = input("Enter current year: ").strip()

# Task 2: Numeric Input with Conversion
# Convert string inputs to appropriate numeric types
try:
    age = int(age_str)
    height_meters = float(height_str)
    current_year = int(current_year_str)
except ValueError:
    print("Error: Please enter valid numeric values!")
    exit()

# Task 3: Boolean Input Processing
# Convert yes/no input to boolean
if student_input in ['yes', 'y', 'true', '1']:
    is_student = True
    student_status = "Yes"
elif student_input in ['no', 'n', 'false', '0']:
    is_student = False
    student_status = "No"
else:
    print("Invalid student status input. Assuming 'No'.")
    is_student = False
    student_status = "No"

# Task 4: Calculations with Input
# Calculate derived information
birth_year = current_year - age
height_feet = height_meters * 3.28084

# Calculate BMI (assuming weight of 70kg as mentioned in problem)
weight_kg = 70  # Assumed weight for BMI calculation
bmi = weight_kg / (height_meters ** 2)

# Determine BMI category
if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

# Task 5: Formatted Output
# Display formatted profile
print()
print("=== PERSONAL PROFILE ===")
print("┌─────────────────────────────────┐")
print("│         PROFILE SUMMARY         │")
print("├─────────────────────────────────┤")
print(f"│ Name: {full_name:<23} │")
print(f"│ Age: {age} years old{'':<15} │")
print(f"│ Height: {height_meters} meters ({height_feet:.2f} feet) │")
print(f"│ Favorite Color: {favorite_color:<15} │")
print(f"│ Student Status: {student_status:<15} │")
print(f"│ Birth Year: {birth_year:<19} │")
print(f"│ BMI: {bmi:.2f} ({bmi_category}){'':<13} │")
print("└─────────────────────────────────┘")
print()
print("Thank you for using our system!")

# Additional demonstrations of input/output concepts
print()
print("=== ADDITIONAL INPUT/OUTPUT DEMONSTRATIONS ===")

# Demonstration 1: Multiple inputs on same line
print("\n1. Multiple inputs with split():")
print("Enter three numbers separated by spaces:")
try:
    numbers_input = input("Numbers: ")
    num1, num2, num3 = map(int, numbers_input.split())
    print(f"You entered: {num1}, {num2}, {num3}")
    print(f"Sum: {num1 + num2 + num3}")
except ValueError:
    print("Invalid input for numbers.")

# Demonstration 2: Input validation loop
print("\n2. Input validation:")
while True:
    grade_input = input("Enter your grade (A, B, C, D, F): ").upper().strip()
    if grade_input in ['A', 'B', 'C', 'D', 'F']:
        print(f"Valid grade entered: {grade_input}")
        break
    else:
        print("Invalid grade. Please enter A, B, C, D, or F.")

# Demonstration 3: Password input (simulated)
print("\n3. Secure input simulation:")
password = input("Enter a password: ")
print(f"Password length: {len(password)} characters")
print("Password hidden: " + "*" * len(password))

# Demonstration 4: Formatted output variations
print("\n4. Different output formatting styles:")
name = "John"
score = 85.67
percentage = 0.8567

print(f"Right aligned: {name:>10}")
print(f"Left aligned: {name:<10}")
print(f"Center aligned: {name:^10}")
print(f"Decimal places: {score:.1f}")
print(f"Percentage: {percentage:.1%}")
print(f"Scientific notation: {score:.2e}")

# Demonstration 5: Multi-line input
print("\n5. Multi-line input:")
print("Enter a short description (end with empty line):")
description_lines = []
while True:
    line = input()
    if line == "":
        break
    description_lines.append(line)

if description_lines:
    print("Your description:")
    for i, line in enumerate(description_lines, 1):
        print(f"{i}. {line}")

print()
print("=== END OF EXERCISE 03 ===")
