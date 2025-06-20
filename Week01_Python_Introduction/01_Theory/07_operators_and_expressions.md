# ⚡ Operators and Expressions

## 📖 Mục lục

1. [Arithmetic Operators](#1-arithmetic-operators)
2. [Comparison Operators](#2-comparison-operators)
3. [Logical Operators](#3-logical-operators)
4. [Assignment Operators](#4-assignment-operators)
5. [Identity and Membership Operators](#5-identity-and-membership-operators)
6. [Operator Precedence](#6-operator-precedence)
7. [Expressions and Evaluation](#7-expressions-and-evaluation)

---

## 1. Arithmetic Operators

### 🧮 Basic Arithmetic Operations

```python
# Sample numbers for examples
a = 15
b = 4

# Addition
result = a + b        # 19
print(f\"{a} + {b} = {result}\")

# Subtraction
result = a - b        # 11
print(f\"{a} - {b} = {result}\")

# Multiplication
result = a * b        # 60
print(f\"{a} * {b} = {result}\")

# Division (float result)
result = a / b        # 3.75
print(f\"{a} / {b} = {result}\")

# Floor Division (integer result)
result = a // b       # 3
print(f\"{a} // {b} = {result}\")

# Modulus (remainder)
result = a % b        # 3
print(f\"{a} % {b} = {result}\")

# Exponentiation (power)
result = a ** b       # 50625 (15^4)
print(f\"{a} ** {b} = {result}\")
```

### 🔢 Arithmetic with Different Data Types

```python
# Integer arithmetic
int1, int2 = 10, 3
print(f\"Integer division: {int1 // int2}\")     # 3
print(f\"Integer modulus: {int1 % int2}\")      # 1

# Float arithmetic
float1, float2 = 10.5, 3.2
print(f\"Float division: {float1 / float2:.2f}\")    # 3.28
print(f\"Float modulus: {float1 % float2:.2f}\")     # 0.90

# Mixed arithmetic (int + float = float)
mixed_result = int1 + float1    # 20.5 (automatic type promotion)
print(f\"Mixed result type: {type(mixed_result)}\")  # <class 'float'>

# String repetition and concatenation
text = \"Python \"
number = 3
repeated = text * number        # \"Python Python Python \"
print(f\"String repetition: {repeated}\")

greeting = \"Hello\" + \" \" + \"World\"    # \"Hello World\"
print(f\"String concatenation: {greeting}\")
```

### 🎯 Practical Arithmetic Examples

```python
# Calculate area and perimeter of rectangle
length = 10.5
width = 6.2

area = length * width
perimeter = 2 * (length + width)

print(f\"Rectangle: {length} x {width}\")
print(f\"Area: {area:.2f} square units\")
print(f\"Perimeter: {perimeter:.2f} units\")

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f\"{celsius}°C = {fahrenheit}°F = {kelvin}K\")

# Calculate compound interest
principal = 1000
rate = 0.05        # 5% annual rate
time = 3           # 3 years

amount = principal * (1 + rate) ** time
interest = amount - principal

print(f\"Principal: ${principal:.2f}\")
print(f\"Rate: {rate*100:.1f}% per year\")
print(f\"Time: {time} years\")
print(f\"Final amount: ${amount:.2f}\")
print(f\"Interest earned: ${interest:.2f}\")
```

---

## 2. Comparison Operators

### ⚖️ Comparison Operations

```python
# Sample values
x, y = 10, 15
a, b = 5, 5

# Equal to
print(f\"{x} == {y}: {x == y}\")    # False
print(f\"{a} == {b}: {a == b}\")    # True

# Not equal to
print(f\"{x} != {y}: {x != y}\")    # True
print(f\"{a} != {b}: {a != b}\")    # False

# Less than
print(f\"{x} < {y}: {x < y}\")      # True

# Greater than
print(f\"{x} > {y}: {x > y}\")      # False

# Less than or equal to
print(f\"{a} <= {b}: {a <= b}\")    # True

# Greater than or equal to
print(f\"{x} >= {y}: {x >= y}\")    # False
```

### 🔤 String Comparisons

```python
# String comparison (lexicographic order)
str1 = \"apple\"
str2 = \"banana\"
str3 = \"Apple\"

print(f\"'{str1}' == '{str2}': {str1 == str2}\")      # False
print(f\"'{str1}' < '{str2}': {str1 < str2}\")        # True (alphabetical)
print(f\"'{str1}' == '{str3}': {str1 == str3}\")      # False (case sensitive)

# Case-insensitive comparison
print(f\"Case-insensitive: {str1.lower() == str3.lower()}\")  # True

# String length comparison
print(f\"Length comparison: {len(str1) < len(str2)}\")        # True
```

### 🔢 Comparing Different Types

```python
# Comparing numbers of different types
int_num = 5
float_num = 5.0
print(f\"{int_num} == {float_num}: {int_num == float_num}\")   # True

# Boolean comparisons
print(f\"True == 1: {True == 1}\")                           # True
print(f\"False == 0: {False == 0}\")                         # True
print(f\"True == 2: {True == 2}\")                           # False

# None comparisons
value = None
print(f\"value is None: {value is None}\")                   # True
print(f\"value == None: {value == None}\")                   # True (but 'is' preferred)
```

---

## 3. Logical Operators

### 🔗 Boolean Logic Operations

```python
# Sample boolean values
p = True
q = False
r = True

# AND operator
print(f\"{p} and {q}: {p and q}\")        # False
print(f\"{p} and {r}: {p and r}\")        # True

# OR operator
print(f\"{p} or {q}: {p or q}\")          # True
print(f\"{q} or False: {q or False}\")    # False

# NOT operator
print(f\"not {p}: {not p}\")              # False
print(f\"not {q}: {not q}\")              # True
```

### 🧠 Complex Logical Expressions

```python
# Combining multiple conditions
age = 25
has_license = True
has_insurance = True
is_employed = True

# Check if person can drive
can_drive = age >= 18 and has_license and has_insurance
print(f\"Can drive: {can_drive}\")

# Check eligibility for loan
good_credit = True
loan_eligible = (age >= 21 and is_employed) and (good_credit or has_insurance)
print(f\"Loan eligible: {loan_eligible}\")

# Complex condition with parentheses
score = 85
attendance = 90
extra_credit = True

passed = (score >= 60 and attendance >= 80) or extra_credit
print(f\"Passed course: {passed}\")
```

### 🎯 Short-Circuit Evaluation

```python
# AND short-circuit: if first is False, second isn't evaluated
def expensive_function():
    print(\"This function was called!\")
    return True

x = False
result = x and expensive_function()  # expensive_function() not called
print(f\"Result: {result}\")

# OR short-circuit: if first is True, second isn't evaluated
y = True
result = y or expensive_function()   # expensive_function() not called
print(f\"Result: {result}\")

# Practical example: safe division
def safe_divide(a, b):
    return b != 0 and a / b  # Only divide if b is not zero

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # False (division prevented)
```

### ✅ Truthy and Falsy Values in Logic

```python
# Falsy values
falsy_values = [False, 0, 0.0, \"\", [], {}, None]

for value in falsy_values:
    print(f\"{repr(value)} is falsy: {not value}\")

# Using truthy/falsy in logical operations
name = \"\"
default_name = \"Anonymous\"
display_name = name or default_name  # Use default if name is empty
print(f\"Display name: {display_name}\")

# Check if list has items
numbers = [1, 2, 3]
empty_list = []

if numbers:  # Truthy - list has items
    print(f\"Numbers list has {len(numbers)} items\")

if not empty_list:  # Falsy - list is empty
    print(\"Empty list has no items\")
```

---

## 4. Assignment Operators

### 📝 Basic Assignment

```python
# Simple assignment
x = 10
name = \"Alice\"
is_active = True

print(f\"x = {x}, name = {name}, is_active = {is_active}\")
```

### ⚡ Compound Assignment Operators

```python
# Start with a value
counter = 10
print(f\"Initial counter: {counter}\")

# Addition assignment
counter += 5        # Same as: counter = counter + 5
print(f\"After += 5: {counter}\")

# Subtraction assignment
counter -= 3        # Same as: counter = counter - 3
print(f\"After -= 3: {counter}\")

# Multiplication assignment
counter *= 2        # Same as: counter = counter * 2
print(f\"After *= 2: {counter}\")

# Division assignment
counter /= 4        # Same as: counter = counter / 4
print(f\"After /= 4: {counter}\")

# Floor division assignment
counter //= 2       # Same as: counter = counter // 2
print(f\"After //= 2: {counter}\")

# Modulus assignment
counter %= 3        # Same as: counter = counter % 3
print(f\"After %= 3: {counter}\")

# Exponentiation assignment
counter **= 3       # Same as: counter = counter ** 3
print(f\"After **= 3: {counter}\")
```

### 🎯 Practical Assignment Examples

```python
# Bank account example
balance = 1000.0
print(f\"Initial balance: ${balance:.2f}\")

# Deposit
deposit = 250.0
balance += deposit
print(f\"After deposit of ${deposit:.2f}: ${balance:.2f}\")

# Withdrawal
withdrawal = 150.0
balance -= withdrawal
print(f\"After withdrawal of ${withdrawal:.2f}: ${balance:.2f}\")

# Interest calculation
interest_rate = 0.02  # 2%
balance *= (1 + interest_rate)
print(f\"After {interest_rate*100}% interest: ${balance:.2f}\")

# String concatenation assignment
message = \"Hello\"
message += \", \"
message += \"World!\"
print(f\"Final message: {message}\")

# List operations with assignment
shopping_list = [\"milk\", \"bread\"]
shopping_list += [\"eggs\", \"butter\"]  # Extend list
print(f\"Shopping list: {shopping_list}\")
```

---

## 5. Identity and Membership Operators

### 🆔 Identity Operators (is, is not)

```python
# Identity vs Equality
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f\"a == b: {a == b}\")        # True (same content)
print(f\"a is b: {a is b}\")        # False (different objects)
print(f\"a is c: {a is c}\")        # True (same object)

print(f\"ID of a: {id(a)}\")
print(f\"ID of b: {id(b)}\")
print(f\"ID of c: {id(c)}\")

# None comparison (always use 'is')
value = None
print(f\"value is None: {value is None}\")      # Preferred
print(f\"value == None: {value == None}\")      # Works but not recommended

# Boolean identity
x = True
y = 1
print(f\"x == y: {x == y}\")        # True (equal value)
print(f\"x is y: {x is y}\")        # False (different types)
```

### 🔍 Membership Operators (in, not in)

```python
# String membership
text = \"Python Programming\"
print(f\"'Python' in text: {'Python' in text}\")           # True
print(f\"'Java' in text: {'Java' in text}\")               # False
print(f\"'python' in text: {'python' in text}\")           # False (case sensitive)

# List membership
fruits = [\"apple\", \"banana\", \"orange\", \"grape\"]
print(f\"'apple' in fruits: {'apple' in fruits}\")         # True
print(f\"'mango' not in fruits: {'mango' not in fruits}\") # True

# Dictionary membership (checks keys by default)
person = {\"name\": \"Alice\", \"age\": 25, \"city\": \"NYC\"}
print(f\"'name' in person: {'name' in person}\")           # True
print(f\"'Alice' in person: {'Alice' in person}\")         # False (not a key)
print(f\"'Alice' in person.values(): {'Alice' in person.values()}\")  # True

# Range membership
numbers = range(1, 11)  # 1 to 10
print(f\"5 in range(1, 11): {5 in numbers}\")             # True
print(f\"15 in range(1, 11): {15 in numbers}\")           # False
```

### 🎯 Practical Membership Examples

```python
# Email validation
def is_valid_email(email):
    return \"@\" in email and \".\" in email

emails = [\"user@example.com\", \"invalid-email\", \"test@domain.org\"]
for email in emails:
    print(f\"{email}: {is_valid_email(email)}\")

# Access control
admin_users = [\"alice\", \"bob\", \"charlie\"]
current_user = \"alice\"

if current_user in admin_users:
    print(f\"{current_user} has admin access\")
else:
    print(f\"{current_user} has regular access\")

# Vowel checker
def count_vowels(text):
    vowels = \"aeiouAEIOU\"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

word = \"Programming\"
print(f\"'{word}' has {count_vowels(word)} vowels\")
```

---

## 6. Operator Precedence

### 📊 Precedence Order (Highest to Lowest)

```python
# 1. Parentheses
result = (2 + 3) * 4        # 20, not 14

# 2. Exponentiation (**)
result = 2 ** 3 ** 2        # 2 ** (3 ** 2) = 2 ** 9 = 512

# 3. Unary operators (+, -, not)
result = -3 ** 2            # -(3 ** 2) = -9, not (-3) ** 2 = 9

# 4. Multiplication, Division, Floor Division, Modulus (*, /, //, %)
result = 2 + 3 * 4          # 2 + 12 = 14

# 5. Addition, Subtraction (+, -)
result = 2 * 3 + 4 * 5      # 6 + 20 = 26

# 6. Comparison operators (<, <=, >, >=, ==, !=)
result = 2 + 3 > 4          # (2 + 3) > 4 = 5 > 4 = True

# 7. Boolean operators (and, or, not)
result = True or False and False  # True or (False and False) = True
```

### 🔍 Precedence Examples

```python
# Complex expression
a, b, c = 2, 3, 4
result = a + b * c ** 2      # 2 + 3 * 16 = 2 + 48 = 50
print(f\"a + b * c ** 2 = {result}\")

# With parentheses to change order
result = (a + b) * c ** 2    # 5 * 16 = 80
print(f\"(a + b) * c ** 2 = {result}\")

# Boolean precedence
x, y, z = True, False, True
result = x or y and z        # x or (y and z) = True or False = True
print(f\"x or y and z = {result}\")

result = (x or y) and z      # (True or False) and True = True and True = True
print(f\"(x or y) and z = {result}\")

# Mixed operations
age = 25
has_license = True
income = 50000

eligible = age >= 18 and has_license and income > 30000
print(f\"Loan eligible: {eligible}\")

# Same expression with explicit parentheses for clarity
eligible = (age >= 18) and has_license and (income > 30000)
print(f\"Loan eligible (explicit): {eligible}\")
```

### 📝 Thực hành tốt nhất cho thứ tự ưu tiên

```python
# ✅ Use parentheses for clarity
result = (a + b) * (c - d)  # Clear intention

# ❌ Relying on precedence can be confusing
result = a + b * c - d      # Less clear

# ✅ Break complex expressions into steps
tax_rate = 0.08
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# ❌ Everything in one line
total = price * quantity + price * quantity * 0.08
```

---

## 7. Expressions and Evaluation

### 🧮 Simple Expressions

```python
# Arithmetic expressions
x = 5
y = 3
result = x * 2 + y ** 2     # 5 * 2 + 9 = 19

# String expressions
first_name = \"John\"
last_name = \"Doe\"
full_name = first_name + \" \" + last_name

# Boolean expressions
is_adult = age >= 18
is_senior = age >= 65
discount_eligible = is_adult and not is_senior
```

### 🔄 Complex Expressions

```python
# Mathematical formula: quadratic equation discriminant
a, b, c = 1, -5, 6  # x² - 5x + 6 = 0
discriminant = b ** 2 - 4 * a * c
print(f\"Discriminant: {discriminant}\")

# Conditional expressions (ternary operator)
age = 20
status = \"adult\" if age >= 18 else \"minor\"
print(f\"Status: {status}\")

# Complex conditional
temperature = 75
weather = \"sunny\"
activity = \"beach\" if temperature > 70 and weather == \"sunny\" else \"indoor\"
print(f\"Recommended activity: {activity}\")

# Multiple conditions in one expression
score = 85
grade = \"A\" if score >= 90 else \"B\" if score >= 80 else \"C\" if score >= 70 else \"F\"
print(f\"Grade: {grade}\")
```

### 📊 Expression Evaluation Order

```python
# Function calls in expressions
def get_x():
    print(\"Getting x\")
    return 5

def get_y():
    print(\"Getting y\")
    return 3

# Left to right evaluation
result = get_x() + get_y()  # \"Getting x\" then \"Getting y\"
print(f\"Result: {result}\")

# Short-circuit evaluation affects function calls
def expensive_check():
    print(\"Expensive check called\")
    return True

# This won't call expensive_check() because False is enough
result = False and expensive_check()
print(f\"Result: {result}\")

# This will call expensive_check() because True means we need to check the second condition
result = True and expensive_check()
print(f\"Result: {result}\")
```

---

## 🧪 Practical Applications

### Example 1: Grade Calculator with Multiple Conditions

```python
def calculate_grade(score, attendance, participation):
    \"\"\"
    Calculate final grade based on multiple criteria
    \"\"\"
    # Base grade from score
    if score >= 90:
        base_grade = \"A\"
    elif score >= 80:
        base_grade = \"B\"
    elif score >= 70:
        base_grade = \"C\"
    elif score >= 60:
        base_grade = \"D\"
    else:
        base_grade = \"F\"

    # Adjust for attendance and participation
    bonus_eligible = attendance >= 90 and participation >= 80
    penalty = attendance < 70 or participation < 50

    if penalty:
        final_grade = \"F\"  # Override with failing grade
    elif bonus_eligible and base_grade in [\"B\", \"C\", \"D\"]:
        # Bump up one letter grade
        grade_map = {\"D\": \"C\", \"C\": \"B\", \"B\": \"A\"}
        final_grade = grade_map[base_grade]
    else:
        final_grade = base_grade

    return final_grade, bonus_eligible, penalty

# Test the function
students = [
    (\"Alice\", 85, 95, 90),
    (\"Bob\", 78, 85, 75),
    (\"Charlie\", 92, 60, 85),
    (\"Diana\", 65, 95, 95)
]

for name, score, attendance, participation in students:
    grade, bonus, penalty = calculate_grade(score, attendance, participation)
    print(f\"{name}: Score={score}, Attendance={attendance}%, Participation={participation}%\")
    print(f\"  Final Grade: {grade} (Bonus: {bonus}, Penalty: {penalty})\\n\")
```

### Example 2: Shopping Cart Calculator

```python
def calculate_cart_total(items, customer_type=\"regular\", has_coupon=False):
    \"\"\"
    Calculate shopping cart total with discounts and taxes
    \"\"\"
    # Calculate subtotal
    subtotal = sum(item[\"price\"] * item[\"quantity\"] for item in items)

    # Apply customer discount
    if customer_type == \"premium\":
        discount_rate = 0.15  # 15% discount
    elif customer_type == \"member\":
        discount_rate = 0.10  # 10% discount
    else:
        discount_rate = 0.05 if subtotal > 100 else 0  # 5% for orders over $100

    # Additional coupon discount
    coupon_discount = 0.05 if has_coupon else 0

    # Total discount (but not more than 25%)
    total_discount_rate = min(discount_rate + coupon_discount, 0.25)

    # Calculate discount and apply
    discount_amount = subtotal * total_discount_rate
    discounted_total = subtotal - discount_amount

    # Calculate tax (8.5%)
    tax_rate = 0.085
    tax_amount = discounted_total * tax_rate

    # Final total
    final_total = discounted_total + tax_amount

    # Free shipping for orders over $75 after discount
    shipping = 0 if discounted_total > 75 else 5.99
    final_total += shipping

    return {
        \"subtotal\": subtotal,
        \"discount_rate\": total_discount_rate,
        \"discount_amount\": discount_amount,
        \"tax_amount\": tax_amount,
        \"shipping\": shipping,
        \"final_total\": final_total
    }

# Example cart
cart_items = [
    {\"name\": \"Laptop\", \"price\": 899.99, \"quantity\": 1},
    {\"name\": \"Mouse\", \"price\": 29.99, \"quantity\": 2},
    {\"name\": \"Keyboard\", \"price\": 79.99, \"quantity\": 1}
]

# Calculate for different customer types
customer_types = [\"regular\", \"member\", \"premium\"]

for customer_type in customer_types:
    result = calculate_cart_total(cart_items, customer_type, has_coupon=True)

    print(f\"\\n{customer_type.upper()} CUSTOMER (with coupon):\")
    print(f\"Subtotal: ${result['subtotal']:.2f}\")
    print(f\"Discount ({result['discount_rate']*100:.1f}%): -${result['discount_amount']:.2f}\")
    print(f\"Tax: ${result['tax_amount']:.2f}\")
    print(f\"Shipping: ${result['shipping']:.2f}\")
    print(f\"TOTAL: ${result['final_total']:.2f}\")
```

---

## 📋 Operators Checklist

- [ ] Understand all arithmetic operators (+, -, \*, /, //, %, \*\*)
- [ ] Know comparison operators (==, !=, <, >, <=, >=)
- [ ] Master logical operators (and, or, not)
- [ ] Use assignment operators effectively (=, +=, -=, etc.)
- [ ] Understand identity (is, is not) vs equality (==, !=)
- [ ] Know membership operators (in, not in)
- [ ] Understand operator precedence and use parentheses for clarity
- [ ] Can write complex expressions and conditional logic
- [ ] Thực hành với ứng dụng thực tế

---

## 🎯 Key Takeaways

1. **Operators** are symbols that perform operations on operands
2. **Precedence matters** - use parentheses for clarity
3. **Logical operators** use short-circuit evaluation
4. **Identity vs Equality**: `is` checks object identity, `==` checks value equality
5. **Membership operators** are powerful for checking containment
6. **Assignment operators** make code more concise
7. **Complex expressions** should be readable and well-structured
8. **Practice** with real-world scenarios builds intuition

---

**Next**: Continue to `08_debugging_and_troubleshooting.md` to learn about finding and fixing errors in your code.
