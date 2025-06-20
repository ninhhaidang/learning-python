#!/usr/bin/env python3
"""
Week 2 - Exercise 2: List Methods
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 2: List Methods ===\n")

# Create the fruits list
fruits = ["apple", "banana", "orange", "apple", "grape", "banana"]
print(f"Original fruits: {fruits}")

# Count apples
apple_count = fruits.count("apple")
print(f"Number of apples: {apple_count}")

# Find position of orange
orange_position = fruits.index("orange")
print(f"Position of orange: {orange_position}")
print()

# Insert kiwi at index 2
fruits.insert(2, "kiwi")
print("After inserting kiwi at index 2:")
print(fruits)
print()

# Remove first apple
fruits.remove("apple")
print("After removing first apple:")
print(fruits)
print()

# Sort the list
fruits.sort()
print("After sorting:")
print(fruits)
