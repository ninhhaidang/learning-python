# Week 1 - Exercise 3: Operations and Expressions

**Bài tập nâng cao về phép toán, biểu thức logic và ứng dụng thực tế**

## 🎯 Mục tiêu

- Hiểu sâu về operator precedence
- Thực hành comparison chains
- Xây dựng logical expressions phức tạp
- Áp dụng bitwise operations
- Giải quyết problems thực tế

---

## Exercise 1: Operator Precedence

### TODO 1.1: Predict và verify

Dự đoán kết quả của các biểu thức sau **TRƯỚC KHI** chạy code:

```python
# Dự đoán kết quả trong comments, sau đó verify
expressions = [
    "2 + 3 * 4",           # Dự đoán: ?
    "(2 + 3) * 4",         # Dự đoán: ?
    "2 ** 3 ** 2",         # Dự đoán: ?
    "2 ** (3 ** 2)",       # Dự đoán: ?
    "(2 ** 3) ** 2",       # Dự đoán: ?
    "10 - 4 - 2",          # Dự đoán: ?
    "10 - (4 - 2)",        # Dự đoán: ?
    "5 + 3 * 2 ** 2 - 1"   # Dự đoán: ?
]

print("Verification:")
for expr in expressions:
    result = eval(expr)
    print(f"{expr:20} = {result}")
```

### TODO 1.2: Complex precedence

Tính toán step-by-step:

```python
# Phân tích: 5 + 3 * 2 ** 2 - 1
# Step 1: 2 ** 2 = ?
# Step 2: 3 * (result of step 1) = ?
# Step 3: 5 + (result of step 2) = ?
# Step 4: (result of step 3) - 1 = ?

expression = "5 + 3 * 2 ** 2 - 1"
step1 = 2 ** 2
step2 = 3 * step1
step3 = 5 + step2
step4 = step3 - 1

print(f"Expression: {expression}")
print(f"Step 1: 2 ** 2 = {step1}")
print(f"Step 2: 3 * {step1} = {step2}")
print(f"Step 3: 5 + {step2} = {step3}")
print(f"Step 4: {step3} - 1 = {step4}")
print(f"Direct calculation: {eval(expression)}")
print(f"Match: {step4 == eval(expression)}")
```

---

## Exercise 2: Comparison Chains

### TODO 2.1: Age group validation

```python
def classify_age(age):
    """Classify age using chained comparisons"""

    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 17:
        return "Teenager"
    elif 18 <= age <= 25:
        return "Young Adult"
    elif 26 <= age <= 64:
        return "Adult"
    elif age >= 65:
        return "Senior"
    else:
        return "Invalid age"

# Test với different ages
test_ages = [5, 15, 22, 45, 70, -5, 150]
for age in test_ages:
    category = classify_age(age)
    print(f"Age {age:3d}: {category}")
```

### TODO 2.2: Grade boundaries

```python
def get_grade_info(score):
    """Get grade and description using chained comparisons"""

    if 90 <= score <= 100:
        return 'A', 'Excellent'
    elif 80 <= score < 90:
        return 'B', 'Good'
    elif 70 <= score < 80:
        return 'C', 'Average'
    elif 60 <= score < 70:
        return 'D', 'Below Average'
    elif 0 <= score < 60:
        return 'F', 'Fail'
    else:
        return 'Invalid', 'Score out of range'

# Test với various scores
test_scores = [95, 87, 76, 65, 45, 105, -10]
for score in test_scores:
    grade, description = get_grade_info(score)
    print(f"Score {score:3d}: Grade {grade} ({description})")
```

### TODO 2.3: Temperature comfort zone

```python
def analyze_temperature(temp_celsius):
    """Analyze temperature comfort level"""

    if temp_celsius < 15:
        comfort = "Too Cold"
        color = "Blue"
    elif 15 <= temp_celsius < 18:
        comfort = "Cold"
        color = "Light Blue"
    elif 18 <= temp_celsius <= 25:
        comfort = "Comfortable"
        color = "Green"
    elif 25 < temp_celsius <= 30:
        comfort = "Warm"
        color = "Orange"
    else:  # temp_celsius > 30
        comfort = "Too Hot"
        color = "Red"

    return comfort, color

# Test temperatures
test_temps = [10, 16, 22, 28, 35]
for temp in test_temps:
    comfort, color = analyze_temperature(temp)
    print(f"{temp:2d}°C: {comfort:12} ({color})")
```

---

## Exercise 3: Logical Expressions

### TODO 3.1: Login validation system

```python
def validate_login(username, password, is_active, login_attempts, max_attempts):
    """Complex login validation with multiple conditions"""

    # Define valid credentials
    valid_username = "admin"
    valid_password = "secret123"

    # Check individual conditions
    username_ok = username == valid_username
    password_ok = password == valid_password
    account_active = is_active
    attempts_ok = login_attempts < max_attempts

    # Overall validation
    login_success = username_ok and password_ok and account_active and attempts_ok

    # Detailed feedback
    print(f"Login attempt for: {username}")
    print(f"Username correct: {username_ok}")
    print(f"Password correct: {password_ok}")
    print(f"Account active: {account_active}")
    print(f"Attempts OK: {attempts_ok} ({login_attempts}/{max_attempts})")
    print(f"Login result: {'SUCCESS' if login_success else 'FAILED'}")

    return login_success

# Test cases
test_cases = [
    ("admin", "secret123", True, 2, 3),    # Should succeed
    ("admin", "wrongpass", True, 1, 3),    # Wrong password
    ("wronguser", "secret123", True, 0, 3), # Wrong username
    ("admin", "secret123", False, 1, 3),   # Inactive account
    ("admin", "secret123", True, 3, 3),    # Too many attempts
]

for i, (user, pwd, active, attempts, max_att) in enumerate(test_cases, 1):
    print(f"\n--- Test Case {i} ---")
    validate_login(user, pwd, active, attempts, max_att)
```

### TODO 3.2: Scholarship eligibility

```python
def check_scholarship_eligibility(math_grade, english_grade, science_grade,
                                extracurricular, financial_need):
    """Complex scholarship eligibility check"""

    # Calculate average
    average = (math_grade + english_grade + science_grade) / 3

    # Individual conditions
    avg_requirement = average >= 85
    all_subjects_ok = math_grade >= 80 and english_grade >= 80 and science_grade >= 80
    special_circumstances = extracurricular or financial_need

    # Final eligibility
    eligible = avg_requirement and all_subjects_ok and special_circumstances

    # Detailed report
    print(f"Grades: Math={math_grade}, English={english_grade}, Science={science_grade}")
    print(f"Average: {average:.1f}")
    print(f"Average >= 85: {avg_requirement}")
    print(f"All subjects >= 80: {all_subjects_ok}")
    print(f"Extracurricular: {extracurricular}")
    print(f"Financial need: {financial_need}")
    print(f"Special circumstances: {special_circumstances}")
    print(f"Scholarship eligible: {eligible}")

    return eligible

# Test students
students = [
    (85, 90, 88, True, False),   # Good grades + extracurricular
    (95, 85, 90, False, True),   # Great grades + financial need
    (80, 85, 75, True, True),    # Science < 80
    (90, 95, 85, False, False),  # Great grades but no special circumstances
]

for i, (math, eng, sci, extra, finance) in enumerate(students, 1):
    print(f"\n--- Student {i} ---")
    check_scholarship_eligibility(math, eng, sci, extra, finance)
```

### TODO 3.3: Advanced discount system

```python
def calculate_discount(is_member, purchase_amount, is_birthday_month,
                      is_weekend, customer_age, years_member):
    """Advanced discount calculation with multiple rules"""

    # Base discounts
    member_discount = 10 if is_member else 0
    purchase_discount = 5 if purchase_amount > 100 else 0
    birthday_discount = 15 if is_birthday_month else 0
    weekend_discount = 3 if is_weekend else 0

    # Age-based discounts
    age_discount = 0
    if customer_age >= 65:
        age_discount = 20  # Senior discount
    elif customer_age <= 18:
        age_discount = 10  # Student discount

    # Loyalty bonus
    loyalty_bonus = 0
    if is_member and years_member >= 5:
        loyalty_bonus = 5

    # Calculate total discount (with maximum cap)
    total_discount = member_discount + purchase_discount + birthday_discount + \
                    weekend_discount + age_discount + loyalty_bonus

    # Apply maximum discount cap
    max_discount = 35
    final_discount = min(total_discount, max_discount)

    # Calculate amounts
    discount_amount = purchase_amount * final_discount / 100
    final_price = purchase_amount - discount_amount

    # Detailed breakdown
    print(f"Customer Profile:")
    print(f"  Age: {customer_age}, Member: {is_member}, Years: {years_member}")
    print(f"  Purchase: ${purchase_amount}, Birthday month: {is_birthday_month}")
    print(f"  Weekend: {is_weekend}")
    print(f"")
    print(f"Discount Breakdown:")
    print(f"  Member discount: {member_discount}%")
    print(f"  Purchase discount: {purchase_discount}%")
    print(f"  Birthday discount: {birthday_discount}%")
    print(f"  Weekend discount: {weekend_discount}%")
    print(f"  Age discount: {age_discount}%")
    print(f"  Loyalty bonus: {loyalty_bonus}%")
    print(f"  Total before cap: {total_discount}%")
    print(f"  Final discount: {final_discount}%")
    print(f"")
    print(f"Final Calculation:")
    print(f"  Original price: ${purchase_amount:.2f}")
    print(f"  Discount amount: ${discount_amount:.2f}")
    print(f"  Final price: ${final_price:.2f}")

    return final_price, final_discount

# Test customers
customers = [
    (True, 150, True, True, 25, 3),    # Member, birthday, weekend
    (True, 200, False, False, 70, 8),  # Senior member with loyalty
    (False, 80, False, True, 17, 0),   # Student, small purchase
    (True, 300, True, False, 45, 2),   # Large purchase, birthday
]

for i, customer_data in enumerate(customers, 1):
    print(f"\n{'='*50}")
    print(f"CUSTOMER {i}")
    print(f"{'='*50}")
    calculate_discount(*customer_data)
```

---

## Exercise 4: Bitwise Operations

### TODO 4.1: Number properties analysis

```python
def analyze_number_properties(number):
    """Analyze number properties using bitwise operations"""

    # Check if even using bitwise AND
    is_even = (number & 1) == 0

    # Check if power of 2
    # A number is power of 2 if: n > 0 and (n & (n-1)) == 0
    is_power_of_2 = number > 0 and (number & (number - 1)) == 0

    # Binary representation
    binary = bin(number)[2:]  # Remove '0b' prefix

    print(f"Number: {number}")
    print(f"Binary: {binary}")
    print(f"Even: {is_even}")
    print(f"Power of 2: {is_power_of_2}")
    print(f"Bitwise check (n & 1): {number & 1}")
    if number > 0:
        print(f"Power of 2 check (n & (n-1)): {number} & {number-1} = {number & (number-1)}")
    print("-" * 30)

# Test numbers
test_numbers = [12, 15, 8, 7, 16, 1, 0, 32]
for num in test_numbers:
    analyze_number_properties(num)
```

### TODO 4.2: Permission system

```python
# Define permission constants
READ = 1      # 001 in binary
WRITE = 2     # 010 in binary
EXECUTE = 4   # 100 in binary

def permission_demo():
    """Demonstrate bitwise permission system"""

    # Initial user permissions (READ + WRITE)
    user_permissions = READ | WRITE
    print(f"Initial permissions: {user_permissions} (binary: {bin(user_permissions)})")

    # Check individual permissions
    def has_permission(permissions, permission):
        return (permissions & permission) != 0

    print(f"Has READ: {has_permission(user_permissions, READ)}")
    print(f"Has write: {has_permission(user_permissions, WRITE)}")
    print(f"Has execute: {has_permission(user_permissions, EXECUTE)}")

    # Add execute permission
    user_permissions |= EXECUTE
    print(f"\nAfter adding EXECUTE: {user_permissions} (binary: {bin(user_permissions)})")
    print(f"Has execute: {has_permission(user_permissions, EXECUTE)}")

    # Remove write permission
    user_permissions &= ~WRITE
    print(f"\nAfter removing WRITE: {user_permissions} (binary: {bin(user_permissions)})")
    print(f"Has write: {has_permission(user_permissions, WRITE)}")

    # Check all permissions
    print(f"\nFinal permission check:")
    print(f"READ: {has_permission(user_permissions, READ)}")
    print(f"WRITE: {has_permission(user_permissions, WRITE)}")
    print(f"EXECUTE: {has_permission(user_permissions, EXECUTE)}")

permission_demo()
```

---

## Exercise 5: Advanced Applications

### TODO 5.1: Password strength analyzer

```python
def analyze_password_strength(password):
    """Comprehensive password strength analysis"""

    # Length check
    length_ok = len(password) >= 8

    # Character type checks
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

    # Calculate strength score
    score = 0
    score += 1 if length_ok else 0
    score += 1 if has_lower else 0
    score += 1 if has_upper else 0
    score += 1 if has_digit else 0
    score += 1 if has_special else 0

    # Bonus points
    if len(password) >= 12:
        score += 1  # Extra length bonus

    # Determine strength level
    if score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    else:  # score == 6
        strength = "Very Strong"

    # Detailed report
    print(f"Password: {'*' * len(password)}")
    print(f"Length ({len(password)} chars): {'✓' if length_ok else '✗'}")
    print(f"Lowercase: {'✓' if has_lower else '✗'}")
    print(f"Uppercase: {'✓' if has_upper else '✗'}")
    print(f"Digits: {'✓' if has_digit else '✗'}")
    print(f"Special chars: {'✓' if has_special else '✗'}")
    print(f"Score: {score}/6")
    print(f"Strength: {strength}")

    return score, strength

# Test passwords
passwords = [
    "password",           # Very weak
    "Password1",          # Weak
    "MyPassword123",      # Moderate
    "MyP@ssw0rd123",     # Strong
    "V3ry$tr0ng!P@ssw0rd" # Very Strong
]

for i, pwd in enumerate(passwords, 1):
    print(f"\n--- Password {i} ---")
    analyze_password_strength(pwd)
```

### TODO 5.2: BMI Calculator with categories

```python
def comprehensive_bmi_analysis(weight_kg, height_m, age, gender):
    """Comprehensive BMI analysis with age and gender considerations"""

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)

    # Standard BMI categories
    if bmi < 18.5:
        category = "Underweight"
        health_risk = "Increased risk of nutritional deficiency"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        health_risk = "Low risk"
    elif 25 <= bmi < 30:
        category = "Overweight"
        health_risk = "Moderate risk of health problems"
    else:  # bmi >= 30
        category = "Obese"
        health_risk = "High risk of health problems"

    # Age adjustments (simplified)
    age_adjusted_message = ""
    if age >= 65:
        age_adjusted_message = "Note: BMI ranges may be different for seniors"
    elif age < 18:
        age_adjusted_message = "Note: BMI calculation for children/teens needs pediatric charts"

    # Gender considerations (simplified)
    gender_note = ""
    if gender.lower() == "female":
        gender_note = "Women typically have higher body fat percentage at same BMI"
    elif gender.lower() == "male":
        gender_note = "Men typically have higher muscle mass at same BMI"

    # Recommendations
    if bmi < 18.5:
        recommendation = "Consider consulting healthcare provider about healthy weight gain"
    elif bmi >= 30:
        recommendation = "Consider consulting healthcare provider about weight management"
    elif bmi >= 25:
        recommendation = "Consider lifestyle changes: diet and exercise"
    else:
        recommendation = "Maintain current healthy lifestyle"

    # Report
    print(f"BMI Analysis Report")
    print(f"=" * 30)
    print(f"Personal Info: {age} years old, {gender}")
    print(f"Measurements: {weight_kg}kg, {height_m}m")
    print(f"BMI: {bmi:.1f}")
    print(f"Category: {category}")
    print(f"Health Risk: {health_risk}")
    print(f"Recommendation: {recommendation}")

    if age_adjusted_message:
        print(f"Age consideration: {age_adjusted_message}")
    if gender_note:
        print(f"Gender consideration: {gender_note}")

    return bmi, category

# Test cases
test_people = [
    (50, 1.60, 25, "female"),   # Underweight
    (70, 1.75, 30, "male"),     # Normal
    (85, 1.70, 45, "female"),   # Overweight
    (100, 1.65, 55, "male"),    # Obese
    (65, 1.70, 70, "female"),   # Senior
]

for i, (weight, height, age, gender) in enumerate(test_people, 1):
    print(f"\n--- Person {i} ---")
    comprehensive_bmi_analysis(weight, height, age, gender)
```

---

## 🎯 Checklist hoàn thành

- [ ] Exercise 1: Operator Precedence
- [ ] Exercise 2: Comparison Chains
- [ ] Exercise 3: Logical Expressions
- [ ] Exercise 4: Bitwise Operations
- [ ] Exercise 5: Advanced Applications

## 📚 Tài liệu tham khảo

- `01_Theory/operators.md` - Chi tiết về tất cả operators
- `03_Solutions/solution_03_operations.py` - Đáp án chi tiết

## 💡 Advanced Tips

- Sử dụng parentheses để làm rõ ý định
- Test logical expressions với truth tables
- Bitwise operations hữu ích cho flags và permissions
- Luôn validate input trong real applications
- Comment giải thích business logic phức tạp

## 🚀 Challenge

Thử implement một mini-game sử dụng tất cả concepts đã học:

- User input validation
- Complex scoring logic
- Multiple game states
- Bitwise flags cho achievements
