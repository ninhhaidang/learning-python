"""
Week 1 - Solution 3: Operations and Expressions
Đáp án chi tiết cho bài tập về phép toán và biểu thức logic

Author: Python Learning Course
Version: 1.0
"""

import math

# =============================================================================
# SOLUTION 1: OPERATOR PRECEDENCE
# =============================================================================

print("=" * 50)
print("SOLUTION 1: OPERATOR PRECEDENCE")
print("=" * 50)

# TODO 1.1: Tính toán theo thứ tự ưu tiên
expressions = [
    "2 + 3 * 4",           # = 2 + 12 = 14
    "(2 + 3) * 4",         # = 5 * 4 = 20
    "2 ** 3 ** 2",         # = 2 ** 9 = 512 (right-to-left)
    "2 ** (3 ** 2)",       # = 2 ** 9 = 512
    "(2 ** 3) ** 2",       # = 8 ** 2 = 64
    "10 - 4 - 2",          # = 6 - 2 = 4 (left-to-right)
    "10 - (4 - 2)",        # = 10 - 2 = 8
    "5 + 3 * 2 ** 2 - 1"   # = 5 + 3 * 4 - 1 = 5 + 12 - 1 = 16
]

print("Kết quả tính toán:")
for expr in expressions:
    result = eval(expr)
    print(f"{expr:20} = {result}")

print("\nGiải thích thứ tự ưu tiên:")
print("1. ** (power) - right-to-left")
print("2. *, /, //, % - left-to-right")
print("3. +, - - left-to-right")
print("4. () để thay đổi thứ tự")

# =============================================================================
# SOLUTION 2: COMPARISON CHAINS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 2: COMPARISON CHAINS")
print("=" * 50)

# TODO 2.1: Age group validation
age = 25

print(f"Tuổi: {age}")

# Viết biểu thức boolean cho các nhóm tuổi
is_child = 0 <= age <= 12
is_teen = 13 <= age <= 17
is_young_adult = 18 <= age <= 25
is_adult = 26 <= age <= 64
is_senior = age >= 65

print(f"Trẻ em (0-12): {is_child}")
print(f"Thanh thiếu niên (13-17): {is_teen}")
print(f"Người trẻ (18-25): {is_young_adult}")
print(f"Người lớn (26-64): {is_adult}")
print(f"Người cao tuổi (65+): {is_senior}")

# Xác định nhóm tuổi
if is_child:
    age_group = "Trẻ em"
elif is_teen:
    age_group = "Thanh thiếu niên"
elif is_young_adult:
    age_group = "Người trẻ"
elif is_adult:
    age_group = "Người lớn"
else:
    age_group = "Người cao tuổi"

print(f"Nhóm tuổi: {age_group}")

# TODO 2.2: Grade boundaries
score = 85

print(f"\nĐiểm số: {score}")

# Chained comparisons cho từng loại điểm
is_excellent = 90 <= score <= 100
is_good = 80 <= score <= 89
is_average = 70 <= score <= 79
is_below_average = 60 <= score <= 69
is_fail = score < 60

print(f"Xuất sắc (90-100): {is_excellent}")
print(f"Khá (80-89): {is_good}")
print(f"Trung bình (70-79): {is_average}")
print(f"Yếu (60-69): {is_below_average}")
print(f"Kém (<60): {is_fail}")

# Xác định loại điểm
if is_excellent:
    grade = "A - Xuất sắc"
elif is_good:
    grade = "B - Khá"
elif is_average:
    grade = "C - Trung bình"
elif is_below_average:
    grade = "D - Yếu"
else:
    grade = "F - Kém"

print(f"Loại điểm: {grade}")

# TODO 2.3: Temperature comfort zone
temp_celsius = 22

print(f"\nNhiệt độ: {temp_celsius}°C")

# Kiểm tra các vùng nhiệt độ
is_too_cold = temp_celsius < 15
is_cold = 15 <= temp_celsius < 18
is_comfortable = 18 <= temp_celsius <= 25
is_warm = 25 < temp_celsius <= 30
is_hot = temp_celsius > 30

print(f"Quá lạnh (<15°C): {is_too_cold}")
print(f"Lạnh (15-18°C): {is_cold}")
print(f"Dễ chịu (18-25°C): {is_comfortable}")
print(f"Ấm (25-30°C): {is_warm}")
print(f"Nóng (>30°C): {is_hot}")

# Xác định cảm giác nhiệt độ
if is_too_cold:
    feeling = "Quá lạnh - Cần sưởi ấm"
elif is_cold:
    feeling = "Lạnh - Nên mặc áo ấm"
elif is_comfortable:
    feeling = "Dễ chịu - Nhiệt độ lý tưởng"
elif is_warm:
    feeling = "Ấm - Có thể bật quạt"
else:
    feeling = "Nóng - Cần điều hòa"

print(f"Cảm giác: {feeling}")

# =============================================================================
# SOLUTION 3: LOGICAL EXPRESSIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 3: LOGICAL EXPRESSIONS")
print("=" * 50)

# TODO 3.1: Login validation
username = "admin"
password = "secret123"
is_active = True
login_attempts = 2
max_attempts = 3

print(f"Username: {username}")
print(f"Password: {password}")
print(f"Account active: {is_active}")
print(f"Login attempts: {login_attempts}/{max_attempts}")

# Kiểm tra từng điều kiện
correct_username = username == "admin"
correct_password = password == "secret123"
account_active = is_active
attempts_valid = login_attempts < max_attempts

# Kết hợp tất cả điều kiện
login_success = correct_username and correct_password and account_active and attempts_valid

print(f"\nKiểm tra:")
print(f"Username đúng: {correct_username}")
print(f"Password đúng: {correct_password}")
print(f"Account active: {account_active}")
print(f"Attempts hợp lệ: {attempts_valid}")
print(f"Đăng nhập thành công: {login_success}")

# TODO 3.2: Scholarship eligibility
math_grade = 85
english_grade = 90
science_grade = 88
extracurricular_activities = True
financial_need = True

print(f"\nThông tin học sinh:")
print(f"Điểm Toán: {math_grade}")
print(f"Điểm Anh: {english_grade}")
print(f"Điểm Khoa học: {science_grade}")
print(f"Hoạt động ngoại khóa: {extracurricular_activities}")
print(f"Nhu cầu tài chính: {financial_need}")

# Tính điểm trung bình
average_grade = (math_grade + english_grade + science_grade) / 3

# Kiểm tra điều kiện học bổng
condition1 = average_grade >= 85
condition2 = all([math_grade >= 80, english_grade >= 80, science_grade >= 80])
condition3 = extracurricular_activities or financial_need

scholarship_eligible = condition1 and condition2 and condition3

print(f"\nKiểm tra điều kiện học bổng:")
print(f"Điểm trung bình: {average_grade:.2f}")
print(f"Điểm TB >= 85: {condition1}")
print(f"Tất cả môn >= 80: {condition2}")
print(f"Hoạt động ngoại khóa HOẶC nhu cầu tài chính: {condition3}")
print(f"Đủ điều kiện học bổng: {scholarship_eligible}")

# TODO 3.3: Discount calculation
is_member = True
purchase_amount = 150
is_birthday_month = False
is_weekend = True

print(f"\nThông tin mua hàng:")
print(f"Thành viên: {is_member}")
print(f"Số tiền: ${purchase_amount}")
print(f"Tháng sinh nhật: {is_birthday_month}")
print(f"Cuối tuần: {is_weekend}")

# Tính các loại giảm giá
member_discount = 0.10 if is_member else 0
purchase_discount = 0.05 if purchase_amount > 100 else 0
birthday_discount = 0.15 if is_birthday_month else 0
weekend_discount = 0.03 if is_weekend else 0

# Tổng discount (tối đa 25%)
total_discount = min(member_discount + purchase_discount + birthday_discount + weekend_discount, 0.25)

discount_amount = purchase_amount * total_discount
final_amount = purchase_amount - discount_amount

print(f"\nCác loại giảm giá:")
if is_member:
    print(f"- Member: {member_discount*100}%")
if purchase_amount > 100:
    print(f"- Large purchase: {purchase_discount*100}%")
if is_birthday_month:
    print(f"- Birthday: {birthday_discount*100}%")
if is_weekend:
    print(f"- Weekend: {weekend_discount*100}%")

print(f"Tổng giảm giá: {total_discount*100}%")
print(f"Số tiền giảm: ${discount_amount:.2f}")
print(f"Thành tiền: ${final_amount:.2f}")

# =============================================================================
# SOLUTION 4: BITWISE OPERATIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 4: BITWISE OPERATIONS")
print("=" * 50)

# TODO 4.1: Number properties
numbers_to_test = [12, 15, 8, 7, 16]

print("Kiểm tra tính chất số:")
for num in numbers_to_test:
    # a) Chẵn hay lẻ (sử dụng &)
    is_even = (num & 1) == 0
    
    # b) Có phải lũy thừa của 2 không
    # Lũy thừa của 2 có đặc điểm: n & (n-1) == 0 và n > 0
    is_power_of_2 = (num > 0) and ((num & (num - 1)) == 0)
    
    print(f"{num:2d}: Chẵn: {is_even:5}, Lũy thừa của 2: {is_power_of_2}")

# TODO 4.2: Permission system
READ = 1      # 001
WRITE = 2     # 010  
EXECUTE = 4   # 100

print(f"\nHệ thống phân quyền:")
print(f"READ = {READ} (binary: {bin(READ)})")
print(f"WRITE = {WRITE} (binary: {bin(WRITE)})")
print(f"EXECUTE = {EXECUTE} (binary: {bin(EXECUTE)})")

user_permissions = READ | WRITE  # User có quyền read và write
print(f"\nUser permissions: {user_permissions} (binary: {bin(user_permissions)})")

# Kiểm tra permissions
has_read = (user_permissions & READ) != 0
has_write = (user_permissions & WRITE) != 0
has_execute = (user_permissions & EXECUTE) != 0

print(f"\nKiểm tra quyền:")
print(f"Có quyền READ: {has_read}")
print(f"Có quyền write: {has_write}")
print(f"Có quyền execute: {has_execute}")

# Thêm quyền execute
user_permissions = user_permissions | EXECUTE
print(f"\nSau khi thêm execute: {user_permissions} (binary: {bin(user_permissions)})")

# Xóa quyền write
user_permissions = user_permissions & ~WRITE
print(f"Sau khi xóa write: {user_permissions} (binary: {bin(user_permissions)})")

# Kiểm tra lại
has_read = (user_permissions & READ) != 0
has_write = (user_permissions & WRITE) != 0
has_execute = (user_permissions & EXECUTE) != 0

print(f"\nKiểm tra quyền cuối cùng:")
print(f"Có quyền read: {has_read}")
print(f"Có quyền write: {has_write}")
print(f"Có quyền execute: {has_execute}")

# =============================================================================
# SOLUTION 5: STRING OPERATIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 5: STRING OPERATIONS")
print("=" * 50)

# TODO 5.1: Password strength checker
def check_password_strength(password):
    """Kiểm tra độ mạnh của password"""
    print(f"Kiểm tra password: '{password}'")
    
    # Các điều kiện
    min_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    print(f"  Ít nhất 8 ký tự: {min_length}")
    print(f"  Có chữ hoa: {has_upper}")
    print(f"  Có chữ thường: {has_lower}")
    print(f"  Có số: {has_digit}")
    print(f"  Có ký tự đặc biệt: {has_special}")
    
    # Tính điểm mạnh
    score = sum([min_length, has_upper, has_lower, has_digit, has_special])
    
    if score == 5:
        strength = "Rất mạnh"
    elif score >= 4:
        strength = "Mạnh"
    elif score >= 3:
        strength = "Trung bình"
    elif score >= 2:
        strength = "Yếu"
    else:
        strength = "Rất yếu"
    
    print(f"  Độ mạnh: {strength} ({score}/5)")
    print()

# Test với các password khác nhau
passwords = ["weak", "Strong123", "VeryStrong123!", "SHORT1!", "nouppercase123!"]

for pwd in passwords:
    check_password_strength(pwd)

# TODO 5.2: Email validator
def validate_email(email):
    """Validate email cơ bản"""
    print(f"Validate email: '{email}'")
    
    # Kiểm tra có chứa @ và chỉ một @
    at_count = email.count("@")
    has_single_at = at_count == 1
    
    if not has_single_at:
        print(f"  Có đúng 1 @: {has_single_at}")
        print(f"  Hợp lệ: False")
        print()
        return False
    
    # Tách local và domain
    local, domain = email.split("@")
    
    # Kiểm tra có ít nhất một dấu chấm sau @
    has_dot_in_domain = "." in domain
    
    # Không bắt đầu/kết thúc bằng @ hoặc .
    valid_start_end = not (email.startswith("@") or email.startswith(".") or 
                          email.endswith("@") or email.endswith("."))
    
    # Độ dài tối thiểu
    min_length = len(email) >= 5
    
    # Local part không rỗng
    valid_local = len(local) > 0
    
    # Domain có ít nhất 1 ký tự trước và sau dấu chấm
    valid_domain = len(domain) > 2 and not domain.startswith(".") and not domain.endswith(".")
    
    is_valid = all([has_single_at, has_dot_in_domain, valid_start_end, min_length, valid_local, valid_domain])
    
    print(f"  Có đúng 1 @: {has_single_at}")
    print(f"  Có dấu chấm trong domain: {has_dot_in_domain}")
    print(f"  Không bắt đầu/kết thúc bằng @ hoặc .: {valid_start_end}")
    print(f"  Độ dài >= 5: {min_length}")
    print(f"  Local part hợp lệ: {valid_local}")
    print(f"  Domain hợp lệ: {valid_domain}")
    print(f"  Hợp lệ: {is_valid}")
    print()
    
    return is_valid

# Test emails
emails = ["user@domain.com", "invalid", "user@", "@domain.com", "user.name@domain.co.uk"]

for email in emails:
    validate_email(email)

# TODO 5.3: Text analyzer
text = """
Python is a high-level programming language. Python is easy to learn and powerful.
Many companies use Python for data science, web development, and automation.
Python has a simple syntax that makes it beginner-friendly.
"""

print("Text analyzer:")
print(f"Text: {text.strip()}")

# a) Số từ
words = text.split()
word_count = len(words)
print(f"\nSố từ: {word_count}")

# b) Số câu (đếm dấu chấm)
sentence_count = text.count(".")
print(f"Số câu: {sentence_count}")

# c) Từ xuất hiện nhiều nhất
word_freq = {}
for word in words:
    # Loại bỏ dấu chấm và chuyển về lowercase
    clean_word = word.strip(".,!?").lower()
    word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

most_common_word = max(word_freq.items(), key=lambda x: x[1])
print(f"Từ xuất hiện nhiều nhất: '{most_common_word[0]}' ({most_common_word[1]} lần)")

# d) Thay thế "Python" bằng "Java"
replaced_text = text.replace("Python", "Java")
print(f"\nText sau khi thay thế 'Python' bằng 'Java':")
print(replaced_text.strip())

# =============================================================================
# SOLUTION 6: PRACTICAL APPLICATIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 6: PRACTICAL APPLICATIONS")
print("=" * 50)

# TODO 6.1: BMI Calculator
def calculate_bmi(weight, height):
    """Tính BMI và phân loại"""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

# Test BMI
weight = 70  # kg
height = 1.75  # m

bmi, category = calculate_bmi(weight, height)
print(f"BMI Calculator:")
print(f"Cân nặng: {weight} kg")
print(f"Chiều cao: {height} m")
print(f"BMI: {bmi:.2f}")
print(f"Phân loại: {category}")

# TODO 6.2: Tax calculator
def calculate_tax(income):
    """Tính thuế thu nhập theo bậc thang"""
    print(f"\nTính thuế cho thu nhập: {income:,} VND")
    
    tax = 0
    remaining = income
    
    # Bậc 1: 0-5M (0%)
    if remaining > 0:
        taxable = min(remaining, 5000000)
        bracket_tax = taxable * 0
        tax += bracket_tax
        remaining -= taxable
        if taxable > 0:
            print(f"Bậc 1 (0-5M): {taxable:,} × 0% = {bracket_tax:,}")
    
    # Bậc 2: 5M-10M (10%)
    if remaining > 0:
        taxable = min(remaining, 5000000)
        bracket_tax = taxable * 0.10
        tax += bracket_tax
        remaining -= taxable
        if taxable > 0:
            print(f"Bậc 2 (5M-10M): {taxable:,} × 10% = {bracket_tax:,}")
    
    # Bậc 3: 10M-18M (15%)
    if remaining > 0:
        taxable = min(remaining, 8000000)
        bracket_tax = taxable * 0.15
        tax += bracket_tax
        remaining -= taxable
        if taxable > 0:
            print(f"Bậc 3 (10M-18M): {taxable:,} × 15% = {bracket_tax:,}")
    
    # Bậc 4: 18M-32M (20%)
    if remaining > 0:
        taxable = min(remaining, 14000000)
        bracket_tax = taxable * 0.20
        tax += bracket_tax
        remaining -= taxable
        if taxable > 0:
            print(f"Bậc 4 (18M-32M): {taxable:,} × 20% = {bracket_tax:,}")
    
    # Bậc 5: >32M (25%)
    if remaining > 0:
        bracket_tax = remaining * 0.25
        tax += bracket_tax
        print(f"Bậc 5 (>32M): {remaining:,} × 25% = {bracket_tax:,}")
    
    net_income = income - tax
    tax_rate = (tax / income) * 100
    
    print(f"Tổng thuế: {tax:,} VND")
    print(f"Thu nhập sau thuế: {net_income:,} VND")
    print(f"Thuế suất hiệu lực: {tax_rate:.2f}%")
    
    return tax

# Test với thu nhập khác nhau
incomes = [3000000, 8000000, 15000000, 25000000, 40000000]

for income in incomes:
    calculate_tax(income)
    print()

# TODO 6.3: Date validator
def is_valid_date(day, month, year):
    """Kiểm tra ngày tháng hợp lệ"""
    print(f"Kiểm tra ngày: {day:02d}/{month:02d}/{year}")
    
    # Kiểm tra tháng
    if not (1 <= month <= 12):
        print(f"  Tháng không hợp lệ: {month}")
        return False
    
    # Số ngày trong mỗi tháng
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Kiểm tra năm nhuận
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap_year:
        days_in_month[1] = 29  # Tháng 2 có 29 ngày
    
    # Kiểm tra ngày
    max_day = days_in_month[month - 1]
    if not (1 <= day <= max_day):
        print(f"  Ngày không hợp lệ: {day} (tháng {month} có tối đa {max_day} ngày)")
        return False
    
    print(f"  Năm nhuận: {is_leap_year}")
    print(f"  Tháng {month} có {max_day} ngày")
    print(f"  Ngày hợp lệ: True")
    
    return True

# Test dates
test_dates = [
    (29, 2, 2024),  # Leap year
    (29, 2, 2023),  # Not leap year
    (31, 4, 2024),  # April has 30 days
    (15, 8, 2024),  # Valid date
]

print("Date validator:")
for day, month, year in test_dates:
    is_valid_date(day, month, year)
    print()

print("=" * 50)
print("HOÀN THÀNH SOLUTION 3!")
print("=" * 50)
