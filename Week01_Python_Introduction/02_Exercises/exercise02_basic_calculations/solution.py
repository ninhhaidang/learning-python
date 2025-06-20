"""
Exercise 02: Basic Calculations & Math - Complete Solution

This file demonstrates all mathematical operations and concepts
for Exercise 02. Study this after attempting the exercise yourself.

Key concepts demonstrated:
- Arithmetic operators
- Math module usage
- Number formatting
- Order of operations
- Real-world calculations
"""

import math

# Define variables for calculations
length = 15.5    # meters
width = 8.2      # meters
principal = 1000 # dollars
rate = 0.05      # 5% interest rate
time = 3         # years
radius = 7.5     # meters

print("=== Mathematical Calculations ===")
print()

# Task 1: Basic Arithmetic Operations
print("Basic Arithmetic:")

# Simple arithmetic
addition = 15 + 25
subtraction = 100 - 37
multiplication = 8 * 7

# Division operations
regular_division = 20 / 3
floor_division = 20 // 3
modulo_operation = 20 % 3

# Exponentiation
power_operation = 2 ** 8

# Display results with proper formatting
print(f"15 + 25 = {addition}")
print(f"100 - 37 = {subtraction}")
print(f"8 × 7 = {multiplication}")
print(f"20 ÷ 3 = {regular_division:.2f}")
print(f"20 ÷ 3 (floor) = {floor_division}")
print(f"20 mod 3 = {modulo_operation}")
print(f"2^8 = {power_operation}")

print()

# Task 2: Geometric Calculations
print("Geometric Calculations:")

# Rectangle area
rectangle_area = length * width
print(f"Rectangle Area ({length}m × {width}m) = {rectangle_area:.2f} m²")

# Circle calculations
circle_area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Circle Area (radius {radius}m) = {circle_area:.2f} m²")
print(f"Circle Circumference = {circumference:.2f} m")

print()

# Task 3: Financial Calculations
print("Financial Calculations:")

# Simple Interest: I = P × R × T
simple_interest = principal * rate * time

# Compound Interest: A = P(1 + R)^T
compound_amount = principal * (1 + rate) ** time
compound_interest = compound_amount - principal

print(f"Simple Interest: ${simple_interest:.2f}")
print(f"Compound Interest: ${compound_interest:.2f}")
print(f"Final Amount: ${compound_amount:.2f}")

print()

# Task 4: Order of Operations
print("Order of Operations:")

# Demonstrate PEMDAS/BODMAS
expression_result = (10 + 5) * 3 - 8 / 2
print(f"(10 + 5) × 3 - 8 ÷ 2 = {expression_result}")

# Show step by step
step1 = 10 + 5        # Parentheses first
step2 = step1 * 3     # Multiplication
step3 = 8 / 2         # Division
final_result = step2 - step3  # Subtraction
print(f"Step by step: ({step1}) × 3 - {step3} = {final_result}")

print()

# Bonus: Additional mathematical operations
print("🎯 Bonus Mathematical Operations:")

# More complex calculations
# Pythagorean theorem: c² = a² + b²
a, b = 3, 4
c = math.sqrt(a**2 + b**2)
print(f"Pythagorean theorem: {a}² + {b}² = {c:.2f}²")

# Area of triangle
triangle_area = 0.5 * a * b
print(f"Triangle area (base={a}, height={b}): {triangle_area:.2f}")

# Percentage calculations
score = 85
total = 100
percentage = (score / total) * 100
print(f"Percentage: {score}/{total} = {percentage:.1f}%")

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature: {celsius}°C = {fahrenheit:.1f}°F")

# Volume calculations
cube_side = 5
cube_volume = cube_side ** 3
sphere_volume = (4/3) * math.pi * radius ** 3

print(f"Cube volume (side={cube_side}): {cube_volume}")
print(f"Sphere volume (radius={radius}): {sphere_volume:.2f}")

print()

# Mathematical constants and functions
print("📊 Mathematical Constants and Functions:")
print(f"π (pi) = {math.pi:.6f}")
print(f"e (Euler's number) = {math.e:.6f}")
print(f"Square root of 16 = {math.sqrt(16)}")
print(f"Ceiling of 4.3 = {math.ceil(4.3)}")
print(f"Floor of 4.7 = {math.floor(4.7)}")
print(f"Absolute value of -5 = {abs(-5)}")

# Scientific notation
large_number = 1.23e6  # 1,230,000
small_number = 4.56e-3  # 0.00456
print(f"Large number: {large_number:,.0f}")
print(f"Small number: {small_number:.6f}")

print()
print("=== Calculations Complete ===")
print("🎯 All mathematical operations successfully demonstrated!")

# Summary of key operators used
print("\n📋 Arithmetic Operators Summary:")
print("+ : Addition")
print("- : Subtraction") 
print("* : Multiplication")
print("/ : Division (float result)")
print("//: Floor division (integer result)")
print("% : Modulo (remainder)")
print("**: Exponentiation (power)")

print("\n🧮 Ready for Exercise 03: User Input & Output!")
