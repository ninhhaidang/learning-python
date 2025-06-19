"""
Week 1 - Solution 1: Python Basics
Đáp án chi tiết với giải thích

Lưu ý: Đây là một trong nhiều cách giải có thể. 
Quan trọng là hiểu logic và có thể giải thích được code.
"""

# =============================================================================
# SOLUTION 1: VARIABLES AND DATA TYPES
# =============================================================================

print("=" * 50)
print("SOLUTION 1: VARIABLES AND DATA TYPES")
print("=" * 50)

# TODO 1.1: Tạo các biến
student_name = "Nguyen Van A"      # String - tên sinh viên
student_age = 20                   # Integer - tuổi
student_height = 1.75              # Float - chiều cao (mét)
is_student = True                  # Boolean - có phải sinh viên

print("✓ Đã tạo các biến thành công")

# TODO 1.2: In thông tin với f-string
print(f"Tên: {student_name}, Tuổi: {student_age}, Chiều cao: {student_height}m, Sinh viên: {is_student}")

# Cách khác với .format()
print("Tên: {}, Tuổi: {}, Chiều cao: {}m, Sinh viên: {}".format(
    student_name, student_age, student_height, is_student))

# TODO 1.3: Kiểm tra kiểu dữ liệu
print(f"Kiểu của student_name: {type(student_name)}")        # <class 'str'>
print(f"Kiểu của student_age: {type(student_age)}")          # <class 'int'>
print(f"Kiểu của student_height: {type(student_height)}")    # <class 'float'>
print(f"Kiểu của is_student: {type(is_student)}")           # <class 'bool'>

# =============================================================================
# SOLUTION 2: STRING MANIPULATION
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 2: STRING MANIPULATION")
print("=" * 50)

# TODO 2.1: String methods
sentence = "  Python Programming is Amazing!  "

print("Original:", repr(sentence))  # repr() shows whitespace clearly
print("Stripped:", sentence.strip())           # Loại bỏ khoảng trắng
print("Upper:", sentence.upper())               # Viết hoa
print("Lower:", sentence.lower())               # Viết thường  
print("Title:", sentence.title())               # Title case

# TODO 2.2: String indexing và slicing
text = "Data Science"

print(f"Text: '{text}'")
print(f"Ký tự đầu: '{text[0]}'")              # 'D'
print(f"Ký tự cuối: '{text[-1]}'")            # 'e'
print(f"'Data': '{text[0:4]}'")               # 'Data'
print(f"'Science': '{text[5:]}'")             # 'Science'
print(f"Đảo ngược: '{text[::-1]}'")           # 'ecneicS ataD'

# Giải thích slicing:
# text[0:4] - từ index 0 đến 3 (không bao gồm 4)
# text[5:] - từ index 5 đến hết
# text[::-1] - bước -1 để đảo ngược

# TODO 2.3: String search và replace
course = "Machine Learning with Python"

print(f"Course: '{course}'")
print(f"Vị trí 'Learning': {course.find('Learning')}")      # 8
print(f"Số lần 'n': {course.count('n')}")                  # 4
print(f"Bắt đầu với 'Machine': {course.startswith('Machine')}")  # True
print(f"Thay Python bằng R: '{course.replace('Python', 'R')}'")

# find() returns -1 if not found, index() raises exception
# count() đếm không overlap
# startswith() và endswith() case-sensitive

# =============================================================================
# SOLUTION 3: NUMBERS AND CALCULATIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 3: NUMBERS AND CALCULATIONS")
print("=" * 50)

# TODO 3.1: Basic arithmetic
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")        # 19
print(f"a - b = {a - b}")        # 11
print(f"a * b = {a * b}")        # 60
print(f"a / b = {a / b}")        # 3.75 (float division)
print(f"a // b = {a // b}")      # 3 (floor division)
print(f"a % b = {a % b}")        # 3 (remainder)
print(f"a ** b = {a ** b}")      # 50625 (exponentiation)

# Giải thích:
# / luôn trả về float
# // trả về floor của phép chia (làm tròn xuống)
# % trả về số dư
# ** là lũy thừa, không phải ^

# TODO 3.2: Number conversion
number_str = "123"
decimal_str = "45.67"

print(f"String to int: {int(number_str)} (type: {type(int(number_str))})")
print(f"String to float: {float(decimal_str)} (type: {type(float(decimal_str))})")
print(f"Number to string: {str(89)} (type: {type(str(89))})")

# Tính tổng sau khi convert
sum_result = int(number_str) + float(decimal_str)
print(f"Tổng: {number_str} + {decimal_str} = {sum_result}")

# TODO 3.3: Temperature converter
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Có thể viết thành function để tái sử dụng:
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(f"Using function: {celsius}°C = {celsius_to_fahrenheit(celsius)}°F")

# =============================================================================
# SOLUTION 4: BOOLEAN AND LOGIC
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 4: BOOLEAN AND LOGIC")
print("=" * 50)

# TODO 4.1: Boolean operations
x = True
y = False

print(f"x = {x}, y = {y}")
print(f"x and y = {x and y}")              # False
print(f"x or y = {x or y}")                # True
print(f"not x = {not x}")                  # False
print(f"not y = {not y}")                  # True
print(f"(x and y) or (not x) = {(x and y) or (not x)}")  # False

# Giải thích:
# and: cả hai phải True
# or: ít nhất một True
# not: đảo ngược giá trị
# () để kiểm soát thứ tự thực hiện

# TODO 4.2: Comparison operations
num1 = 10
num2 = 20
num3 = 10

print(f"num1 = {num1}, num2 = {num2}, num3 = {num3}")
print(f"num1 == num2: {num1 == num2}")     # False
print(f"num1 != num2: {num1 != num2}")     # True
print(f"num1 < num2: {num1 < num2}")       # True
print(f"num1 <= num3: {num1 <= num3}")     # True
print(f"num2 > num1: {num2 > num1}")       # True
print(f"num1 == num3: {num1 == num3}")     # True

# TODO 4.3: Truthiness test
values_to_test = [0, 1, "", "hello", [], [1, 2], None, True, False]

print("Truthiness test:")
for value in values_to_test:
    print(f"{repr(value):10} -> {bool(value)}")

# Kết quả:
# 0         -> False (zero is falsy)
# 1         -> True  (non-zero is truthy)
# ''        -> False (empty string is falsy)
# 'hello'   -> True  (non-empty string is truthy)
# []        -> False (empty list is falsy)
# [1, 2]    -> True  (non-empty list is truthy)
# None      -> False (None is falsy)
# True      -> True  (obviously)
# False     -> False (obviously)

# =============================================================================
# SOLUTION 5: PRACTICAL APPLICATION
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 5: PRACTICAL APPLICATION")
print("=" * 50)

# TODO 5.1: Age classifier
age = 25

if age <= 12:
    category = "Child"
elif age <= 19:  # 13-19
    category = "Teenager"
elif age <= 59:  # 20-59
    category = "Adult"
else:  # 60+
    category = "Senior"

print(f"Age {age} -> Category: {category}")

# Giải thích:
# elif kiểm tra điều kiện tiếp theo nếu if trước đó False
# Thứ tự điều kiện quan trọng
# else bắt tất cả cases còn lại

# TODO 5.2: Grade calculator
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score {score} -> Grade: {grade}")

# TODO 5.3: Simple password checker
password = "MyPass123"

# Kiểm tra từng điều kiện
length_ok = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

# Cách đơn giản hơn cho beginners:
length_ok = len(password) >= 8
has_digit = False
has_upper = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

print(f"Password: {password}")
print(f"Length >= 8: {length_ok}")
print(f"Has digit: {has_digit}")
print(f"Has uppercase: {has_upper}")

if length_ok and has_digit and has_upper:
    print("✓ Password is valid")
else:
    print("✗ Password is invalid")

# =============================================================================
# SOLUTION 6: INPUT/OUTPUT
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 6: INPUT/OUTPUT")
print("=" * 50)

# TODO 6.1: User input (commented để không interrupt script)
print("# User input example:")
print("# name = input('Nhập tên của bạn: ')")
print("# birth_year = int(input('Nhập năm sinh: '))")
print("# current_year = 2024")
print("# age = current_year - birth_year")
print("# print(f'Xin chào {name}! Bạn {age} tuổi.')")

# Simulate với hardcoded values:
name = "Alice"
birth_year = 1995
current_year = 2024
age = current_year - birth_year
print(f"Simulation: Xin chào {name}! Bạn {age} tuổi.")

# TODO 6.2: Calculator
print("\n# Calculator example:")
num1 = 10.0
operator = "+"
num2 = 5.0

print(f"Calculating: {num1} {operator} {num2}")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")

print("\n" + "=" * 50)
print("✓ TẤT CẢ BÀI TẬP ĐÃ ĐƯỢC GIẢI!")
print("Đọc comments để hiểu logic của từng bài")
print("=" * 50)
