"""
Exercise 01: Hello World & Print Operations - Complete Solution

This file contains a complete solution for Exercise 01.
Study this code after attempting the exercise yourself.

Key concepts demonstrated:
- Basic print() function
- Print parameters (sep, end)
- String formatting techniques
- Code organization and comments
"""

# Task 1: Basic Print Statements
print("=== Welcome to Python Programming ===")
print()  # Empty line

# Basic Hello World
print("Hello, World!")

# Personal information (replace with your own)
name = "Alice Johnson"
age = 25
favorite_color = "Blue"
city = "San Francisco"

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My favorite color is {favorite_color}")
print(f"I live in {city}")
print()

# Task 2: Print with Separators
print("Demonstrating different separators:")
print("Name", "Age", "Color", "City")  # Default separator (space)
print(name, age, favorite_color, city, sep=" | ")  # Pipe separator
print(name, age, favorite_color, city, sep=", ")   # Comma separator
print(name, age, favorite_color, city, sep=" - ")  # Dash separator
print()

# Task 3: Print with Custom Endings
print("Printing on the same line: ", end="")
print("This continues the previous line!")

print("First part", end=" >>> ")
print("Connected part", end=" >>> ")
print("Final part")
print()

# Task 4: Formatted Output with Borders
print("Personal Information Summary:")
print("-" * 50)
print(f"Name: {name:<20} | Age: {age:>3}")
print(f"Color: {favorite_color:<18} | City: {city}")
print("-" * 50)
print()

# Task 5: Multiple Print Techniques

# Technique 1: String concatenation
print("Technique 1 (String concatenation):")
print("My name is " + name + " and I am " + str(age) + " years old")

# Technique 2: Multiple arguments with custom separator
print("Technique 2 (Multiple arguments):")
print("My name is", name, "and I am", age, "years old")

# Technique 3: F-string formatting (modern Python)
print("Technique 3 (F-string formatting):")
print(f"My name is {name} and I am {age} years old")

# Technique 4: .format() method
print("Technique 4 (.format() method):")
print("My name is {} and I am {} years old".format(name, age))

print()

# Bonus: Advanced formatting
print("🎨 Advanced Formatting Showcase:")
print("═" * 60)
print(f"{'📋 STUDENT PROFILE':^60}")
print("═" * 60)
print(f"{'Name:':<15} {name}")
print(f"{'Age:':<15} {age} years")
print(f"{'Favorite Color:':<15} {favorite_color}")
print(f"{'City:':<15} {city}")
print("═" * 60)
print(f"{'Status:':<15} ✅ Profile Complete")
print("═" * 60)

print("\n=== End of Program ===")

# Additional demonstrations
print("\n🔍 Extra Learning - Print Function Features:")

# Multiple lines in one print
print("""This is a multi-line string
that spans several lines
and maintains formatting.""")

# Print to show different quote types
print('Single quotes work too!')
print("Double quotes are common")
print("""Triple quotes for
multi-line text""")

# Print special characters
print("Special characters: \\n (newline), \\t (tab)")
print("Unicode: 🐍 Python is fun! 🚀")

# Print numbers and calculations
print("Math in print:", 5 + 3, "equals", 5 + 3)
print(f"Calculation: 10 * 3 = {10 * 3}")

print("\n🎯 Exercise 01 Complete! Ready for Exercise 02.")
