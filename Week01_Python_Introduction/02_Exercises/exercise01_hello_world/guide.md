# Exercise 01: Step-by-Step Guide

## 🎯 Getting Started

This guide will walk you through solving Exercise 01 step by step. Try each step on your own before looking at the next one.

## 📝 Step 1: Basic Print Statements

### What you need to do:

Print "Hello, World!" and your personal information

### How to do it:

```python
# Basic print statement
print("Hello, World!")

# Print personal information
print("My name is Alice")
print("I am 25 years old")
print("My favorite color is blue")
print("I live in New York")
```

### Key concepts:

- `print()` function displays text on screen
- Text must be in quotes (single or double)
- Each print() creates a new line by default

---

## 📝 Step 2: Print with Separators

### What you need to do:

Use the `sep` parameter to change how multiple items are separated

### How to do it:

```python
# Default separator (space)
print("Name", "Age", "City")

# Custom separators
print("Alice", "25", "New York", sep=" | ")
print("Alice", "25", "New York", sep=", ")
print("Alice", "25", "New York", sep="-")
```

### Key concepts:

- `sep` parameter controls what goes between multiple arguments
- Default separator is a space " "
- You can use any string as separator

---

## 📝 Step 3: Print with Custom Endings

### What you need to do:

Use the `end` parameter to control what happens at the end of print()

### How to do it:

```python
# Print on same line
print("Hello", end=" ")
print("World")  # This will be on the same line

# Custom ending
print("First line", end="\n\n")  # Double newline
print("Second line")
```

### Key concepts:

- `end` parameter controls what's printed at the end
- Default is `\n` (newline)
- Use `end=""` to remove the newline

---

## 📝 Step 4: Formatted Output

### What you need to do:

Create nicely formatted output with borders and alignment

### How to do it:

```python
# Create borders
print("=" * 30)
print("    Personal Information")
print("=" * 30)

# Formatted content
print("Name: Alice")
print("Age: 25")
print("=" * 30)
```

### Key concepts:

- `"=" * 30` repeats the character 30 times
- You can create visual separators and borders
- Spacing helps with readability

---

## 📝 Step 5: Multiple Techniques

### What you need to do:

Show the same information using different print methods

### Technique 1 - String Concatenation:

```python
name = "Alice"
age = "25"
print("My name is " + name + " and I am " + age + " years old")
```

### Technique 2 - Multiple Arguments:

```python
print("My name is", name, "and I am", age, "years old")
```

### Technique 3 - F-strings (Advanced):

```python
print(f"My name is {name} and I am {age} years old")
```

---

## 🧪 Testing Your Solution

### Run your program and check:

1. Does it print "Hello, World!"?
2. Does it show your personal information?
3. Are different separators working?
4. Does the formatting look good?
5. Are there any error messages?

### Common Issues:

- **SyntaxError**: Check your quotes and parentheses
- **NameError**: Make sure variable names are spelled correctly
- **Formatting issues**: Check spacing and line breaks

---

## 💡 Pro Tips

1. **Use comments**: Explain what each section does
2. **Test frequently**: Run your code after each step
3. **Experiment**: Try different separators and formats
4. **Keep it simple**: Start basic, then add complexity

---

## 🎯 Next Steps

After completing this exercise:

1. Compare your solution with the provided solution.py
2. Try variations - different text, formats, etc.
3. Move on to Exercise 02: Basic Calculations

Remember: There's no single "correct" way to solve this. Focus on making your code work and understanding the concepts!
