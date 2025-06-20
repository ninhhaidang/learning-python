# Exercise 02: Basic Calculations & Math

## 🎯 Objective

Learn to perform mathematical operations in Python using arithmetic operators and understand order of operations.

## 📋 Problem Description

Create a Python program that performs various mathematical calculations and displays the results in a clear, formatted way.

## 📥 Input Requirements

No user input required. Use the following values in your calculations:

- Length: 15.5 meters
- Width: 8.2 meters
- Principal amount: $1000
- Interest rate: 5% (0.05)
- Time period: 3 years
- Circle radius: 7.5 meters

## 📤 Expected Output

```
=== Mathematical Calculations ===

Basic Arithmetic:
15 + 25 = 40
100 - 37 = 63
8 × 7 = 56
20 ÷ 3 = 6.67
20 ÷ 3 (floor) = 6
20 mod 3 = 2
2^8 = 256

Geometric Calculations:
Rectangle Area (15.5m × 8.2m) = 127.10 m²
Circle Area (radius 7.5m) = 176.71 m²
Circle Circumference = 47.12 m

Financial Calculations:
Simple Interest: $150.00
Compound Interest: $157.63
Final Amount: $1157.63

Order of Operations:
(10 + 5) × 3 - 8 ÷ 2 = 41.0
```

## 🎯 Specific Tasks

### Task 1: Basic Arithmetic Operations

- Addition, subtraction, multiplication
- Regular division, floor division, modulo
- Exponentiation

### Task 2: Geometric Calculations

- Rectangle area (length × width)
- Circle area (π × r²)
- Circle circumference (2 × π × r)

### Task 3: Financial Calculations

- Simple interest: P × R × T
- Compound interest: P × (1 + R)^T - P
- Total amount calculation

### Task 4: Order of Operations

- Demonstrate PEMDAS/BODMAS rules
- Use parentheses to control calculation order

### Task 5: Number Formatting

- Display monetary values with 2 decimal places
- Display areas with 2 decimal places
- Show clear labels for all calculations

## 📚 Required Concepts

- Arithmetic operators (+, -, \*, /, //, %, \*\*)
- Order of operations
- Variable assignment
- Number formatting
- Mathematical constants (π)

## 💡 Hints

- Use `import math` for π (math.pi)
- Use f-strings for formatting: `{value:.2f}`
- Remember operator precedence: \*_ > _, /, //, % > +, -
- Use parentheses to group operations
- Store intermediate results in variables for clarity

## 🧪 Testing Your Solution

Verify your calculations:

1. 15 + 25 should equal 40
2. Rectangle area: 15.5 × 8.2 = 127.10
3. Circle area: π × 7.5² ≈ 176.71
4. Simple interest: 1000 × 0.05 × 3 = 150
5. Order of operations result should be 41.0

## 📊 Difficulty Level

⭐ Basic (Introduction to math operations)

## ⏱️ Estimated Time

20-25 minutes
