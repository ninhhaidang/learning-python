# Exercise 02: Step-by-Step Guide

## 🎯 Getting Started

This guide will help you master mathematical operations in Python. Complete each step and test your code as you go.

## 📝 Step 1: Import Math Module

### What you need to do:

Import the math module to access mathematical constants like π

### How to do it:

```python
import math

# Now you can use math.pi for π
print(f"Value of π: {math.pi}")
```

### Key concepts:

- `import math` gives you access to mathematical functions
- `math.pi` provides the value of π (3.14159...)
- You can also import specific functions: `from math import pi`

---

## 📝 Step 2: Basic Arithmetic Operations

### What you need to do:

Perform addition, subtraction, multiplication, division, and more

### How to do it:

```python
# Basic operations
addition = 15 + 25
subtraction = 100 - 37
multiplication = 8 * 7

# Different types of division
regular_division = 20 / 3      # Result: 6.666...
floor_division = 20 // 3       # Result: 6 (integer part only)
modulo = 20 % 3               # Result: 2 (remainder)

# Exponentiation
power = 2 ** 8                # 2 to the power of 8

# Display results
print(f"15 + 25 = {addition}")
print(f"20 ÷ 3 = {regular_division:.2f}")
```

### Key concepts:

- `+` addition, `-` subtraction, `*` multiplication
- `/` regular division (returns float), `//` floor division (returns integer)
- `%` modulo (remainder), `**` exponentiation
- Use `:.2f` to format numbers to 2 decimal places

---

## 📝 Step 3: Geometric Calculations

### What you need to do:

Calculate areas and circumferences using formulas

### How to do it:

```python
# Rectangle area
length = 15.5
width = 8.2
rectangle_area = length * width
print(f"Rectangle Area: {rectangle_area:.2f} m²")

# Circle calculations
radius = 7.5
circle_area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Circle Area: {circle_area:.2f} m²")
print(f"Circumference: {circumference:.2f} m")
```

### Key concepts:

- Area formulas: Rectangle = length × width, Circle = π × r²
- Circumference = 2 × π × r
- Use `**` for exponentiation (radius squared = radius \*\* 2)
- Format with 2 decimal places for readability

---

## 📝 Step 4: Financial Calculations

### What you need to do:

Calculate simple and compound interest

### How to do it:

```python
# Given values
principal = 1000    # P
rate = 0.05        # R (5% = 0.05)
time = 3           # T

# Simple Interest: I = P × R × T
simple_interest = principal * rate * time

# Compound Interest: A = P(1 + R)^T
compound_amount = principal * (1 + rate) ** time
compound_interest = compound_amount - principal

print(f"Simple Interest: ${simple_interest:.2f}")
print(f"Compound Interest: ${compound_interest:.2f}")
print(f"Total Amount: ${compound_amount:.2f}")
```

### Key concepts:

- Simple Interest = Principal × Rate × Time
- Compound Amount = Principal × (1 + Rate)^Time
- Compound Interest = Compound Amount - Principal
- Use `$` symbol for currency formatting

---

## 📝 Step 5: Order of Operations

### What you need to do:

Demonstrate PEMDAS/BODMAS rules

### How to do it:

```python
# Without parentheses (following PEMDAS)
result1 = 10 + 5 * 3 - 8 / 2    # Result: 21.0
# Order: 5*3=15, 8/2=4, then 10+15-4=21

# With parentheses (controlling order)
result2 = (10 + 5) * 3 - 8 / 2  # Result: 41.0
# Order: (10+5)=15, 15*3=45, 8/2=4, then 45-4=41

print(f"Without parentheses: {result1}")
print(f"With parentheses: {result2}")
```

### Key concepts:

- Order: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
- Use parentheses to control calculation order
- Python follows standard mathematical order of operations

---

## 🧪 Testing Your Solution

### Check your calculations:

1. **15 + 25 = 40** ✓
2. **Rectangle area: 15.5 × 8.2 = 127.10** ✓
3. **Circle area: π × 7.5² ≈ 176.71** ✓
4. **Simple interest: 1000 × 0.05 × 3 = 150** ✓
5. **Order of operations: (10 + 5) × 3 - 8 ÷ 2 = 41** ✓

### Common Issues:

- **Import error**: Make sure you have `import math` at the top
- **Wrong division**: Use `/` for decimal results, `//` for integer results
- **Formatting**: Use `:.2f` for 2 decimal places
- **Order of operations**: Remember to use parentheses when needed

---

## 💡 Pro Tips

1. **Use descriptive variable names**: `rectangle_area` instead of `a`
2. **Format output clearly**: Include units (m², $, etc.)
3. **Test each calculation**: Verify your math manually
4. **Use comments**: Explain complex formulas

---

## 🎯 Next Steps

After completing this exercise:

1. Verify all your calculations match expected results
2. Try different values to test your formulas
3. Move on to Exercise 03: User Input & Output

Remember: Math is the foundation of programming - master these operations!
