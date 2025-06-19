# Week 1 - Exercise 1: Python Basics

**Bài tập cơ bản về cú pháp Python và kiểu dữ liệu**

## 🎯 Mục tiêu

- Thực hành tạo và sử dụng variables
- Làm việc với các kiểu dữ liệu cơ bản
- Manipulate strings và numbers
- Áp dụng boolean logic
- Xử lý input/output

## 📝 Hướng dẫn

1. Đọc kỹ từng bài tập
2. Tạo file Python mới để viết code
3. Thực hiện từng TODO theo thứ tự
4. Chạy và kiểm tra kết quả
5. So sánh với đáp án trong thư mục `03_Solutions`

---

## Exercise 1: Variables and Data Types

### TODO 1.1: Tạo biến thông tin cá nhân

Tạo các biến sau với giá trị phù hợp:

- `student_name`: tên của bạn (string)
- `student_age`: tuổi của bạn (integer)
- `student_height`: chiều cao của bạn tính bằng mét (float)
- `is_student`: có phải là sinh viên không (boolean)

```python
# Viết code của bạn ở đây:
student_name = ?
student_age = ?
student_height = ?
is_student = ?
```

### TODO 1.2: Format và in thông tin

Sử dụng f-string để in thông tin theo mẫu:

```
Tên: [name], Tuổi: [age], Chiều cao: [height]m, Sinh viên: [is_student]
```

```python
# Viết code của bạn ở đây:
print(f"...")
```

### TODO 1.3: Kiểm tra kiểu dữ liệu

Sử dụng `type()` để in ra kiểu dữ liệu của từng biến

```python
# Viết code của bạn ở đây:
print(f"Kiểu của student_name: {type(...)}")
# Thêm cho các biến còn lại...
```

---

## Exercise 2: String Manipulation

### TODO 2.1: String methods

Cho chuỗi: `sentence = "  Python Programming is Amazing!  "`

Thực hiện các task sau:

- a) In ra sentence sau khi loại bỏ khoảng trắng đầu và cuối
- b) In ra sentence viết hoa toàn bộ
- c) In ra sentence viết thường toàn bộ
- d) In ra sentence với chữ cái đầu mỗi từ viết hoa (title case)

```python
sentence = "  Python Programming is Amazing!  "

# a) Strip whitespace
print("Stripped:", sentence....)

# b) Uppercase
print("Upper:", sentence....)

# c) Lowercase
print("Lower:", sentence....)

# d) Title case
print("Title:", sentence....)
```

### TODO 2.2: String indexing và slicing

Cho chuỗi: `text = "Data Science"`

Thực hiện:

- a) In ra ký tự đầu tiên
- b) In ra ký tự cuối cùng
- c) In ra từ "Data" (4 ký tự đầu)
- d) In ra từ "Science" (từ vị trí thứ 5 đến hết)
- e) In ra chuỗi đảo ngược

```python
text = "Data Science"

# a) First character
print("First char:", text[...])

# b) Last character
print("Last char:", text[...])

# c) "Data"
print("Data:", text[...])

# d) "Science"
print("Science:", text[...])

# e) Reversed
print("Reversed:", text[...])
```

### TODO 2.3: String search và replace

Cho chuỗi: `course = "Machine Learning with Python"`

Thực hiện:

- a) Tìm vị trí của từ "Learning"
- b) Đếm số lần xuất hiện của chữ "n"
- c) Kiểm tra xem chuỗi có bắt đầu bằng "Machine" không
- d) Thay thế "Python" bằng "R"

```python
course = "Machine Learning with Python"

# a) Find position
position = course.find("...")
print(f"Position of 'Learning': {position}")

# b) Count character
count = course.count("...")
print(f"Count of 'n': {count}")

# c) Check start
starts_with = course.startswith("...")
print(f"Starts with 'Machine': {starts_with}")

# d) Replace
replaced = course.replace("...", "...")
print(f"Replaced: {replaced}")
```

---

## Exercise 3: Numbers and Calculations

### TODO 3.1: Basic arithmetic

Cho: `a = 15`, `b = 4`

Tính và in ra kết quả của:

- a) `a + b`
- b) `a - b`
- c) `a * b`
- d) `a / b` (chia thường)
- e) `a // b` (chia lấy phần nguyên)
- f) `a % b` (chia lấy dư)
- g) `a ** b` (a mũ b)

```python
a = 15
b = 4

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
# Tiếp tục với các phép toán còn lại...
```

### TODO 3.2: Number conversion

Cho: `number_str = "123"`, `decimal_str = "45.67"`

Thực hiện:

- a) Chuyển `number_str` thành integer và in ra
- b) Chuyển `decimal_str` thành float và in ra
- c) Chuyển số 89 thành string và in ra
- d) Tính tổng của `number_str` và `decimal_str` (sau khi chuyển đổi kiểu)

```python
number_str = "123"
decimal_str = "45.67"

# a) String to int
int_value = int(...)
print(f"String to int: {int_value}")

# b) String to float
float_value = float(...)
print(f"String to float: {float_value}")

# c) Number to string
str_value = str(...)
print(f"Number to string: {str_value}")

# d) Sum after conversion
sum_result = int(...) + float(...)
print(f"Sum: {sum_result}")
```

### TODO 3.3: Temperature converter

Viết code chuyển đổi nhiệt độ từ Celsius sang Fahrenheit
Công thức: `F = (C * 9/5) + 32`

```python
celsius = 25

# Chuyển đổi
fahrenheit = ...

print(f"{celsius}°C = {fahrenheit}°F")
```

---

## Exercise 4: Boolean and Logic

### TODO 4.1: Boolean operations

Cho: `x = True`, `y = False`

Tính và in ra kết quả của:

- a) `x and y`
- b) `x or y`
- c) `not x`
- d) `not y`
- e) `(x and y) or (not x)`

```python
x = True
y = False

print(f"x and y = {x and y}")
print(f"x or y = {x or y}")
# Tiếp tục với các operations còn lại...
```

### TODO 4.2: Comparison operations

Cho: `num1 = 10`, `num2 = 20`, `num3 = 10`

Tính và in ra kết quả của:

- a) `num1 == num2`
- b) `num1 != num2`
- c) `num1 < num2`
- d) `num1 <= num3`
- e) `num2 > num1`
- f) `num1 == num3`

```python
num1 = 10
num2 = 20
num3 = 10

print(f"num1 == num2: {num1 == num2}")
print(f"num1 != num2: {num1 != num2}")
# Tiếp tục với các comparisons còn lại...
```

### TODO 4.3: Truthiness test

Kiểm tra truthiness của các giá trị sau: `[0, 1, "", "hello", [], [1, 2], None, True, False]`

```python
values_to_test = [0, 1, "", "hello", [], [1, 2], None, True, False]

print("Truthiness test:")
for value in values_to_test:
    result = bool(value)
    print(f"{repr(value):10} -> {result}")
```

---

## Exercise 5: Practical Application

### TODO 5.1: Age classifier

Viết code phân loại độ tuổi:

- 0-12: Child
- 13-19: Teenager
- 20-59: Adult
- 60+: Senior

```python
age = 25  # Thay đổi giá trị này để test

if age <= 12:
    category = "Child"
elif ...:  # Hoàn thành điều kiện
    category = "Teenager"
elif ...:  # Hoàn thành điều kiện
    category = "Adult"
else:
    category = "Senior"

print(f"Age {age} -> Category: {category}")
```

### TODO 5.2: Grade calculator

Viết code tính điểm chữ từ điểm số:

- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- <60: F

```python
score = 85  # Thay đổi giá trị này để test

if score >= 90:
    grade = 'A'
elif ...:  # Hoàn thành
    grade = 'B'
# Tiếp tục...

print(f"Score {score} -> Grade: {grade}")
```

### TODO 5.3: Simple password checker

Kiểm tra password có đáp ứng yêu cầu cơ bản:

- Độ dài ít nhất 8 ký tự
- Có ít nhất 1 chữ số
- Có ít nhất 1 chữ cái viết hoa

```python
password = "MyPass123"  # Thay đổi để test

# Kiểm tra độ dài
length_ok = len(password) >= 8

# Kiểm tra có chữ số (sử dụng loop)
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break

# Kiểm tra có chữ hoa (sử dụng loop)
has_upper = False
for char in password:
    if ...:  # Hoàn thành điều kiện
        has_upper = True
        break

print(f"Password: {password}")
print(f"Length >= 8: {length_ok}")
print(f"Has digit: {has_digit}")
print(f"Has uppercase: {has_upper}")

if length_ok and has_digit and has_upper:
    print("✓ Password is valid")
else:
    print("✗ Password is invalid")
```

---

## Exercise 6: Input/Output

### TODO 6.1: User input program

Viết chương trình:

1. Hỏi tên người dùng
2. Hỏi năm sinh
3. Tính tuổi (giả sử năm hiện tại là 2024)
4. In ra lời chào với tên và tuổi

```python
# Uncomment để test interactively:
# name = input("Nhập tên của bạn: ")
# birth_year = int(input("Nhập năm sinh: "))
# current_year = 2024
# age = current_year - birth_year
# print(f"Xin chào {name}! Bạn {age} tuổi.")

# Hoặc test với hardcoded values:
name = "Alice"
birth_year = 1995
current_year = 2024
age = ...  # Tính tuổi
print(f"Xin chào {name}! Bạn {age} tuổi.")
```

### TODO 6.2: Simple calculator

Viết calculator đơn giản:

1. Nhập số thứ nhất
2. Nhập phép toán (+, -, \*, /)
3. Nhập số thứ hai
4. Tính và in kết quả

```python
# Uncomment để test interactively:
# num1 = float(input("Nhập số thứ nhất: "))
# operator = input("Nhập phép toán (+, -, *, /): ")
# num2 = float(input("Nhập số thứ hai: "))

# Hoặc test với hardcoded values:
num1 = 10.0
operator = "+"
num2 = 5.0

print(f"Calculating: {num1} {operator} {num2}")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = ...  # Hoàn thành
elif operator == "*":
    result = ...  # Hoàn thành
elif operator == "/":
    if num2 != 0:
        result = ...  # Hoàn thành
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")
```

---

## 🎯 Checklist hoàn thành

- [ ] Exercise 1: Variables and Data Types
- [ ] Exercise 2: String Manipulation
- [ ] Exercise 3: Numbers and Calculations
- [ ] Exercise 4: Boolean and Logic
- [ ] Exercise 5: Practical Application
- [ ] Exercise 6: Input/Output

## 📚 Tài liệu tham khảo

- `01_Theory/data_types.md` - Chi tiết về kiểu dữ liệu
- `01_Theory/operators.md` - Chi tiết về operators
- `03_Solutions/solution_01_basics.py` - Đáp án chi tiết

## 💡 Tips

- Đọc error messages cẩn thận
- Test với nhiều giá trị khác nhau
- Sử dụng `print()` để debug
- Đặt tên biến có ý nghĩa
- Comment giải thích logic của bạn
