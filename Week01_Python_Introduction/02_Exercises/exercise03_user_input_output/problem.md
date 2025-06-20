# Exercise 03: User Input & Output

## 🎯 Objective

Learn to interact with users through input() function, handle different data types, and create interactive programs.

## 📋 Problem Description

Create an interactive program that collects user information, performs calculations based on input, and displays formatted results.

## 📥 Input Requirements

The program should ask the user for:

- Full name
- Age (integer)
- Height in meters (float)
- Favorite color (string)
- Is student? (yes/no)
- Current year (for birth year calculation)

## 📤 Expected Output

```
=== Personal Information Collector ===

Please enter your information:
Enter your full name: Alice Johnson
Enter your age: 25
Enter your height in meters: 1.68
Enter your favorite color: Blue
Are you a student? (yes/no): no
Enter current year: 2024

=== PERSONAL PROFILE ===
┌─────────────────────────────────┐
│         PROFILE SUMMARY         │
├─────────────────────────────────┤
│ Name: Alice Johnson             │
│ Age: 25 years old               │
│ Height: 1.68 meters (5.51 feet) │
│ Favorite Color: Blue            │
│ Student Status: No              │
│ Birth Year: 1999                │
│ BMI: 22.32 (Normal)             │
└─────────────────────────────────┘

Thank you for using our system!
```

## 🎯 Specific Tasks

### Task 1: Basic User Input

- Get user's name, age, and favorite color
- Display the information back to user

### Task 2: Numeric Input with Conversion

- Get height as float
- Get age as integer
- Handle type conversion properly

### Task 3: Boolean Input Processing

- Ask yes/no question about student status
- Convert to boolean value

### Task 4: Calculations with Input

- Calculate birth year (current year - age)
- Convert height to feet (meters × 3.28084)
- Calculate BMI (weight ÷ height²) - assume weight 70kg

### Task 5: Formatted Output

- Create formatted profile display
- Use boxes, alignment, and clear labels
- Handle different data types in output

## 📚 Required Concepts

- input() function
- Type conversion (int(), float(), str())
- String methods (.lower(), .strip())
- Boolean conversion
- F-string formatting
- Input validation basics

## 💡 Hints

- input() always returns string - convert as needed
- Use .lower() to handle "Yes", "YES", "yes" consistently
- Use .strip() to remove extra spaces
- For BMI: BMI = weight(kg) ÷ height(m)²
- Feet conversion: feet = meters × 3.28084
- Handle invalid input gracefully

## 🧪 Testing Your Solution

Test with different inputs:

1. Name: "John Doe", Age: 30, Height: 1.75
2. Student: try "YES", "yes", "Y", "no", "NO"
3. Verify calculations are correct
4. Check formatting looks professional

## 📊 Difficulty Level

⭐⭐ Basic-Intermediate (Introduction to user interaction)

## ⏱️ Estimated Time

25-30 minutes
