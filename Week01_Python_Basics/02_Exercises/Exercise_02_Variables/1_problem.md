# Week 1 - Exercise 2: Variables and Operations

**Bài tập nâng cao về biến, phép toán và xử lý dữ liệu**

## 🎯 Mục tiêu

- Thực hành làm việc với variables phức tạp
- Áp dụng mathematical operations trong thực tế
- String processing và validation
- Logic expressions và decision making
- Unit conversion và practical calculations

---

## Exercise 1: Variable Practice

### TODO 1.1: Thông tin sách

Tạo các biến cho thông tin một cuốn sách:

- `book_title`: "Python for Data Science"
- `author`: "John Smith"
- `year_published`: 2023
- `price`: 29.99
- `is_available`: True
- `pages`: 350

```python
# Tạo các biến:
book_title = ?
author = ?
year_published = ?
price = ?
is_available = ?
pages = ?
```

### TODO 1.2: Multiple formatting methods

In thông tin sách sử dụng 3 cách format khác nhau:

**a) F-string:**

```python
print(f"Book: {book_title} by {author}")
print(f"Published: {year_published}, Price: ${price}")
print(f"Pages: {pages}, Available: {is_available}")
```

**b) .format() method:**

```python
print("Book: {} by {}".format(..., ...))
# Hoàn thành cho các dòng còn lại
```

**c) % formatting:**

```python
print("Book: %s by %s" % (..., ...))
# Hoàn thành cho các dòng còn lại
```

### TODO 1.3: Variable swapping

Hoán đổi giá trị của 2 biến sử dụng tuple unpacking:

```python
x = 100
y = 200

print(f"Trước khi swap: x = {x}, y = {y}")

# Swap using tuple unpacking
x, y = ..., ...

print(f"Sau khi swap: x = {x}, y = {y}")
```

---

## Exercise 2: Mathematical Operations

### TODO 2.1: Circle calculations

Cho bán kính hình tròn, tính chu vi và diện tích:

```python
import math

radius = 5

# a) Chu vi = 2 * π * r
circumference = 2 * math.pi * ...

# b) Diện tích = π * r²
area = math.pi * ... ** 2

# c) In kết quả với 2 chữ số thập phân
print(f"Radius: {radius}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")
```

### TODO 2.2: Compound interest calculator

Tính lãi kép với công thức: `A = P(1 + r/n)^(nt)`

- P = principal (số tiền gốc)
- r = annual interest rate (lãi suất hàng năm)
- n = compounds per year (số lần ghép lãi/năm)
- t = time in years (số năm)

```python
principal = 1000        # $1000
rate = 0.05            # 5% per year
compounds_per_year = 12 # monthly compounding
years = 5

# Tính toán
amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * years)

# Tính lãi thu được
interest_earned = amount - principal

print(f"Principal: ${principal}")
print(f"Amount after {years} years: ${amount:.2f}")
print(f"Interest earned: ${interest_earned:.2f}")
```

### TODO 2.3: Distance calculator

Tính khoảng cách giữa 2 điểm trong hệ tọa độ:
Công thức: `d = √[(x₂-x₁)² + (y₂-y₁)²]`

```python
x1, y1 = 1, 2
x2, y2 = 4, 6

# Tính khoảng cách
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Distance: {distance:.2f}")
```

---

## Exercise 3: String Operations

### TODO 3.1: Name processing

Cho: `full_name = "  nguyen van minh  "`

```python
full_name = "  nguyen van minh  "

# a) Chuẩn hóa tên (loại bỏ khoảng trắng, Title Case)
clean_name = full_name.strip().title()
print(f"Clean name: {clean_name}")

# b) Tách họ, tên đệm, tên
name_parts = clean_name.split()
ho = name_parts[0]
ten_dem = name_parts[1]
ten = name_parts[2]
print(f"Họ: {ho}, Tên đệm: {ten_dem}, Tên: {ten}")

# c) Tạo email từ tên
email = clean_name.lower().replace(" ", ".") + "@email.com"
print(f"Email: {email}")

# d) Tạo username (viết tắt)
username = ho[0].lower() + ten_dem[0].lower() + ten[0].lower()
print(f"Username: {username}")
```

### TODO 3.2: Text analysis

Cho: `text = "Python is a powerful programming language. Python is easy to learn."`

```python
text = "Python is a powerful programming language. Python is easy to learn."

# a) Đếm số từ
word_count = len(text.split())
print(f"Word count: {word_count}")

# b) Đếm số lần xuất hiện "Python"
python_count = text.count("Python")
print(f"'Python' appears: {python_count} times")

# c) Thay thế "Python" bằng "Java"
replaced_text = text.replace("Python", "Java")
print(f"Replaced: {replaced_text}")

# d) Kiểm tra có chứa "programming"
contains_programming = "programming" in text
print(f"Contains 'programming': {contains_programming}")
```

### TODO 3.3: URL processor

Cho: `url = "https://www.example.com/blog/python-tutorial?id=123"`

```python
url = "https://www.example.com/blog/python-tutorial?id=123"

# a) Tách protocol
protocol = url.split("://")[0]
print(f"Protocol: {protocol}")

# b) Tách domain
domain_part = url.split("://")[1]
domain = domain_part.split("/")[0]
print(f"Domain: {domain}")

# c) Tách path
path_start = url.find("/", url.find("://") + 3)
query_start = url.find("?")
if query_start != -1:
    path = url[path_start:query_start]
else:
    path = url[path_start:]
print(f"Path: {path}")

# d) Tách query parameters
if "?" in url:
    query = url.split("?")[1]
    print(f"Query: {query}")
else:
    print("No query parameters")
```

---

## Exercise 4: Data Validation

### TODO 4.1: Email validator

```python
def validate_email(email):
    """Basic email validation"""
    email = email.strip()

    # a) Có chứa @ không
    has_at = "@" in email

    # b) Chỉ có 1 ký tự @
    at_count = email.count("@")

    # c) Có ít nhất 1 dấu chấm sau @
    if has_at:
        domain_part = email.split("@")[1]
        has_dot_in_domain = "." in domain_part
    else:
        has_dot_in_domain = False

    # d) Không bắt đầu/kết thúc bằng @ hoặc .
    invalid_start_end = email.startswith("@") or email.startswith(".") or \
                       email.endswith("@") or email.endswith(".")

    # Kết quả validation
    is_valid = has_at and at_count == 1 and has_dot_in_domain and not invalid_start_end

    return is_valid

# Test
test_emails = ["user@example.com", "invalid", "user@", "@domain.com"]
for email in test_emails:
    result = validate_email(email)
    print(f"'{email}': {'Valid' if result else 'Invalid'}")
```

### TODO 4.2: Phone number formatter

```python
phone = "0123456789"

# a) Kiểm tra có đúng 10 chữ số
is_valid_length = len(phone) == 10 and phone.isdigit()
print(f"Valid length: {is_valid_length}")

if is_valid_length:
    # b) Format: (012) 345-6789
    format1 = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print(f"Format 1: {format1}")

    # c) Format: 012.345.6789
    format2 = f"{phone[:3]}.{phone[3:6]}.{phone[6:]}"
    print(f"Format 2: {format2}")

    # d) Format: +84 12 345 6789 (chuyển 0 thành +84)
    if phone.startswith("0"):
        intl_phone = "+84 " + phone[1:3] + " " + phone[3:6] + " " + phone[6:]
        print(f"International: {intl_phone}")
```

### TODO 4.3: Credit card number validator (basic)

```python
card_number = "1234 5678 9012 3456"

# a) Loại bỏ khoảng trắng
clean_number = card_number.replace(" ", "")
print(f"Clean number: {clean_number}")

# b) Kiểm tra có đúng 16 chữ số
is_valid = len(clean_number) == 16 and clean_number.isdigit()
print(f"Valid format: {is_valid}")

# c) Mask number (ẩn 12 số đầu)
if is_valid:
    masked = "****-****-****-" + clean_number[-4:]
    print(f"Masked: {masked}")
```

---

## Exercise 5: Unit Conversion

### TODO 5.1: Temperature conversion

```python
celsius = 25

# a) Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# b) Celsius to Kelvin
kelvin = celsius + 273.15
print(f"{celsius}°C = {kelvin}K")

# c) Summary
print(f"Temperature conversions for {celsius}°C:")
print(f"  Fahrenheit: {fahrenheit}°F")
print(f"  Kelvin: {kelvin}K")
```

### TODO 5.2: Length conversion

```python
meters = 1500

# a) To kilometers
kilometers = meters / 1000
print(f"{meters}m = {kilometers}km")

# b) To centimeters
centimeters = meters * 100
print(f"{meters}m = {centimeters}cm")

# c) To inches
inches = meters * 39.37
print(f"{meters}m = {inches:.2f} inches")

# d) To feet
feet = meters * 3.281
print(f"{meters}m = {feet:.2f} feet")
```

### TODO 5.3: Currency converter

```python
usd_amount = 100
usd_to_vnd_rate = 24000

# a) Convert USD to VND
vnd_amount = usd_amount * usd_to_vnd_rate
print(f"${usd_amount} = {vnd_amount:,} VND")

# b) Calculate 2% conversion fee
fee_rate = 0.02
fee_amount = vnd_amount * fee_rate
final_amount = vnd_amount - fee_amount

print(f"Conversion fee (2%): {fee_amount:,.0f} VND")
print(f"Final amount received: {final_amount:,.0f} VND")
```

---

## Exercise 6: Logical Expressions

### TODO 6.1: Student grade eligibility

```python
math_score = 85
english_score = 78
science_score = 92

# Tính điểm trung bình
average = (math_score + english_score + science_score) / 3

# Điều kiện đậu:
condition1 = average >= 80                    # Điểm TB >= 80
condition2 = math_score >= 60 and english_score >= 60 and science_score >= 60  # Không môn nào < 60
condition3 = (math_score >= 80) + (english_score >= 80) + (science_score >= 80) >= 2  # Ít nhất 2 môn >= 80

passed = condition1 and condition2 and condition3

print(f"Math: {math_score}, English: {english_score}, Science: {science_score}")
print(f"Average: {average:.1f}")
print(f"Condition 1 (Average >= 80): {condition1}")
print(f"Condition 2 (No subject < 60): {condition2}")
print(f"Condition 3 (At least 2 subjects >= 80): {condition3}")
print(f"Final result: {'PASSED' if passed else 'FAILED'}")
```

### TODO 6.2: Login system

```python
username = "admin"
password = "secret123"
is_account_active = True
failed_attempts = 0
max_attempts = 3

# Input credentials (simulate)
input_username = "admin"
input_password = "secret123"

# Check login conditions
correct_credentials = (input_username == username) and (input_password == password)
account_active = is_account_active
attempts_ok = failed_attempts < max_attempts

login_success = correct_credentials and account_active and attempts_ok

print(f"Username correct: {input_username == username}")
print(f"Password correct: {input_password == password}")
print(f"Account active: {account_active}")
print(f"Attempts OK: {attempts_ok} ({failed_attempts}/{max_attempts})")
print(f"Login success: {login_success}")
```

### TODO 6.3: Discount calculator

```python
customer_age = 25
is_member = True
purchase_amount = 150
is_weekend = False

# Calculate discount
senior_discount = 20 if customer_age >= 65 else 0
member_discount = 10 if is_member else 0
purchase_discount = 5 if purchase_amount > 100 else 0
weekend_discount = 5 if is_weekend else 0

# Total discount (max 30%)
total_discount = min(senior_discount + member_discount + purchase_discount + weekend_discount, 30)

# Calculate final price
discount_amount = purchase_amount * total_discount / 100
final_price = purchase_amount - discount_amount

print(f"Customer age: {customer_age}")
print(f"Member: {is_member}")
print(f"Purchase amount: ${purchase_amount}")
print(f"Weekend: {is_weekend}")
print(f"")
print(f"Senior discount: {senior_discount}%")
print(f"Member discount: {member_discount}%")
print(f"Purchase discount: {purchase_discount}%")
print(f"Weekend discount: {weekend_discount}%")
print(f"Total discount: {total_discount}%")
print(f"")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Final price: ${final_price:.2f}")
```

---

## 🎯 Checklist hoàn thành

- [ ] Exercise 1: Variable Practice
- [ ] Exercise 2: Mathematical Operations
- [ ] Exercise 3: String Operations
- [ ] Exercise 4: Data Validation
- [ ] Exercise 5: Unit Conversion
- [ ] Exercise 6: Logical Expressions

## 📚 Tài liệu tham khảo

- `01_Theory/operators.md` - Chi tiết về operators
- `01_Theory/data_types.md` - Chi tiết về string methods
- `03_Solutions/solution_02_variables.py` - Đáp án chi tiết

## 💡 Tips nâng cao

- Sử dụng constants cho magic numbers
- Validate input trước khi xử lý
- Format output cho người dùng dễ đọc
- Comment giải thích business logic
- Test với edge cases
