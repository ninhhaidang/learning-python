#!/usr/bin/env python3
"""
Week 2 - Exercise 4: Basic Dictionaries
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 4: Basic Dictionaries ===\n")

# Create student dictionary
student = {
    "name": "Nguyen Van A",
    "age": 20,
    "major": "Computer Science",
    "university": "VNU"
}

# Print initial student information
print("Student Information:")
for key, value in student.items():
    print(f"{key.title()}: {value}")
print()

# Add grade to the dictionary
student["grade"] = 8.5
print("After adding grade:")
for key, value in student.items():
    print(f"{key.title()}: {value}")
print()

# Update age
student["age"] = 21
print("After updating age to 21:")
for key, value in student.items():
    print(f"{key.title()}: {value}")
print()

# Remove university key
del student["university"]
print("After removing university:")
for key, value in student.items():
    print(f"{key.title()}: {value}")
print()

# Show dictionary methods
print(f"Dictionary keys: {student.keys()}")
print(f"Dictionary values: {student.values()}")
