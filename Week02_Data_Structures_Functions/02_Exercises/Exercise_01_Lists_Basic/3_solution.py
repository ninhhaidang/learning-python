#!/usr/bin/env python3
"""
Week 2 - Exercise 1: Basic Lists
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 1: Basic Lists ===\n")

# Create lists
cities = ["Hanoi", "Ho Chi Minh", "Da Nang", "Hue", "Can Tho"]
temperatures = [25.5, 28.0, 26.5, 24.0, 27.5]

# Print first and last city information
print(f"First city: {cities[0]} ({temperatures[0]}°C)")
print(f"Last city: {cities[-1]} ({temperatures[-1]}°C)")
print()

# Change temperature of the 3rd city (index 2)
temperatures[2] = 30.0
print("After updating Da Nang temperature:")
print(f"{cities[2]}: {temperatures[2]}°C")
print()

# Add new city and temperature
cities.append("Nha Trang")
temperatures.append(29.0)

# Print final list
print("Final cities and temperatures:")
for i in range(len(cities)):
    print(f"{cities[i]}: {temperatures[i]}°C")
