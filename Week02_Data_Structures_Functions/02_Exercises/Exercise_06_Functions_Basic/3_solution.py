#!/usr/bin/env python3
"""
Week 2 - Exercise 6: Basic Functions
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 6: Basic Functions ===\n")

# Define basic arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Define calculate function
def calculate(operation, num1, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        return "Invalid operation!"

# Test all functions
print("=== Testing Basic Calculator Functions ===\n")

# Test individual functions
print(f"Addition: 15 + 7 = {add(15, 7)}")
print(f"Subtraction: 15 - 7 = {subtract(15, 7)}")
print(f"Multiplication: 15 * 7 = {multiply(15, 7)}")
print(f"Division: 15 / 7 = {divide(15, 7):.2f}")
print()

# Test calculate function
print("Testing calculate function:")
print(f"calculate('+', 10, 5) = {calculate('+', 10, 5)}")
print(f"calculate('-', 10, 5) = {calculate('-', 10, 5)}")
print(f"calculate('*', 10, 5) = {calculate('*', 10, 5)}")
print(f"calculate('/', 10, 5) = {calculate('/', 10, 5)}")
print()

# Test error handling
print("Error handling:")
print(f"Division by zero: {divide(10, 0)}")
