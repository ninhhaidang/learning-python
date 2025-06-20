#!/usr/bin/env python3
"""
Week 1 - Exercise 5: Input and Output
Solution File

Author: Course Instructor
Date: 2024
"""

# Ask user for length and width using input()
length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Print results with proper formatting
print(f"Rectangle dimensions: {length:.2f} x {width:.2f}")
print(f"Area: {area:.2f} square units")
print(f"Perimeter: {perimeter:.2f} units")
