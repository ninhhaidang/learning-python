#!/usr/bin/env python3
"""
Week 2 - Exercise 5: Basic Sets
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 5: Basic Sets ===\n")

# Create sets for math and english students
math_students = {"An", "Binh", "Chi", "Duc", "Em"}
english_students = {"Binh", "Chi", "Phong", "Giang", "Huong"}

print(f"Math students: {math_students}")
print(f"English students: {english_students}")
print()

# Find students taking both subjects (intersection)
both_subjects = math_students & english_students
print(f"Students taking both subjects: {both_subjects}")

# Find students taking only math (difference)
only_math = math_students - english_students
print(f"Students taking only Math: {only_math}")

# Find students taking only english (difference)
only_english = english_students - math_students
print(f"Students taking only English: {only_english}")

# Find all students (union)
all_students = math_students | english_students
print(f"All students: {all_students}")
print()

# Demonstrate removing duplicates from a list using set
duplicate_list = ["An", "Binh", "An", "Chi", "Binh", "Duc"]
print(f"Original list with duplicates: {duplicate_list}")

unique_students = set(duplicate_list)
print(f"After removing duplicates: {unique_students}")
