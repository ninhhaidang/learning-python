"""
Week 1 - Solution 2: Variables and Operations
Đáp án chi tiết cho bài tập về biến, phép toán và xử lý dữ liệu cơ bản

Author: Python Learning Course
Version: 1.0
"""

import math

# =============================================================================
# SOLUTION 1: VARIABLE PRACTICE
# =============================================================================

print("=" * 50)
print("SOLUTION 1: VARIABLE PRACTICE")
print("=" * 50)

# TODO 1.1: Tạo thông tin về một cuốn sách
book_title = "Python for Data Science"
author = "John Smith"
year_published = 2023
price = 29.99
is_available = True
pages = 350

print("Thông tin sách đã được tạo thành công!")

# TODO 1.2: In thông tin sách với nhiều cách format
print("\n--- Cách 1: f-string ---")
print(f"Sách: {book_title}")
print(f"Tác giả: {author}")
print(f"Năm xuất bản: {year_published}")
print(f"Giá: ${price}")
print(f"Có sẵn: {is_available}")
print(f"Số trang: {pages}")

print("\n--- Cách 2: .format() ---")
print("Sách: {}".format(book_title))
print("Tác giả: {}".format(author))
print("Năm xuất bản: {}".format(year_published))
print("Giá: ${:.2f}".format(price))
print("Có sẵn: {}".format(is_available))
print("Số trang: {}".format(pages))

print("\n--- Cách 3: % formatting ---")
print("Sách: %s" % book_title)
print("Tác giả: %s" % author)
print("Năm xuất bản: %d" % year_published)
print("Giá: $%.2f" % price)
print("Có sẵn: %s" % is_available)
print("Số trang: %d" % pages)

# TODO 1.3: Variable swapping
x = 100
y = 200

print(f"\nTrước khi swap: x = {x}, y = {y}")

# Cách 1: Tuple unpacking (Pythonic)
x, y = y, x

print(f"Sau khi swap: x = {x}, y = {y}")

# Cách khác (traditional):
# temp = x
# x = y  
# y = temp

# =============================================================================
# SOLUTION 2: MATHEMATICAL OPERATIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 2: MATHEMATICAL OPERATIONS")
print("=" * 50)

# TODO 2.1: Circle calculations
radius = 5

# a) Tính chu vi (2 * π * r)
circumference = 2 * math.pi * radius

# b) Tính diện tích (π * r²)
area = math.pi * radius ** 2

# c) In kết quả với 2 chữ số thập phân
print(f"Bán kính: {radius}")
print(f"Chu vi: {circumference:.2f}")
print(f"Diện tích: {area:.2f}")

# TODO 2.2: Compound interest calculator
principal = 1000  # $1000
rate = 0.05       # 5% per year
compounds_per_year = 12  # monthly compounding
years = 5

# Công thức: A = P(1 + r/n)^(nt)
amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * years)
interest_earned = amount - principal

print(f"\nVốn ban đầu: ${principal:,.2f}")
print(f"Lãi suất: {rate*100}% per year")
print(f"Ghép lãi: {compounds_per_year} lần/năm")
print(f"Thời gian: {years} năm")
print(f"Số tiền sau {years} năm: ${amount:,.2f}")
print(f"Lãi kiếm được: ${interest_earned:,.2f}")

# TODO 2.3: Distance calculator
x1, y1 = 1, 2
x2, y2 = 4, 6

# Công thức: d = √[(x₂-x₁)² + (y₂-y₁)²]
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"\nĐiểm 1: ({x1}, {y1})")
print(f"Điểm 2: ({x2}, {y2})")
print(f"Khoảng cách: {distance:.2f}")

# =============================================================================
# SOLUTION 3: STRING OPERATIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 3: STRING OPERATIONS")
print("=" * 50)

# TODO 3.1: Name processing
full_name = "  nguyen van minh  "

# a) Loại bỏ khoảng trắng và chuẩn hóa tên
cleaned_name = full_name.strip().title()
print(f"Tên gốc: '{full_name}'")
print(f"Tên chuẩn hóa: '{cleaned_name}'")

# b) Tách họ, tên đệm, tên
name_parts = cleaned_name.split()
if len(name_parts) >= 3:
    last_name = name_parts[0]
    middle_name = ' '.join(name_parts[1:-1])
    first_name = name_parts[-1]
    
    print(f"Họ: {last_name}")
    print(f"Tên đệm: {middle_name}")
    print(f"Tên: {first_name}")

# c) Tạo email từ tên
email = '.'.join(full_name.strip().lower().split()) + "@email.com"
print(f"Email: {email}")

# d) Tạo username
username = ''.join(full_name.strip().lower().split())
short_username = ''.join([part[0] for part in full_name.strip().split()])
print(f"Username: {username}")
print(f"Short username: {short_username}")

# TODO 3.2: Text analysis
text = "Python is a powerful programming language. Python is easy to learn."

# a) Đếm số từ
word_count = len(text.split())
print(f"\nText: {text}")
print(f"Số từ: {word_count}")

# b) Đếm số lần xuất hiện của từ "Python"
python_count = text.count("Python")
print(f"Số lần xuất hiện 'Python': {python_count}")

# c) Thay thế tất cả "Python" bằng "Java"
replaced_text = text.replace("Python", "Java")
print(f"Text sau khi thay thế: {replaced_text}")

# d) Kiểm tra xem text có chứa từ "programming" không
contains_programming = "programming" in text
print(f"Có chứa 'programming': {contains_programming}")

# TODO 3.3: URL processor
url = "https://www.example.com/blog/python-tutorial?id=123"

print(f"\nURL: {url}")

# a) Tách protocol
protocol = url.split("://")[0]
print(f"Protocol: {protocol}")

# b) Tách domain
domain = url.split("://")[1].split("/")[0]
print(f"Domain: {domain}")

# c) Tách path
path_start = url.find("/", 8)  # Bỏ qua "https://"
query_start = url.find("?")
if query_start == -1:
    path = url[path_start:]
else:
    path = url[path_start:query_start]
print(f"Path: {path}")

# d) Tách query parameters
if "?" in url:
    query = url.split("?")[1]
    print(f"Query: ?{query}")
else:
    print("Query: Không có")

# =============================================================================
# SOLUTION 4: DATA VALIDATION
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 4: DATA VALIDATION")
print("=" * 50)

# TODO 4.1: Email validator
email = "user@example.com"

print(f"Email để kiểm tra: {email}")

# a) Email có chứa ký tự @ không
has_at = "@" in email
print(f"Có chứa @: {has_at}")

# b) Email có ít nhất 1 dấu chấm sau @ không
if "@" in email:
    domain_part = email.split("@")[1]
    has_dot_after_at = "." in domain_part
    print(f"Có dấu chấm sau @: {has_dot_after_at}")

# c) Email không bắt đầu hoặc kết thúc bằng @ hoặc .
valid_start_end = not (email.startswith("@") or email.startswith(".") or 
                      email.endswith("@") or email.endswith("."))
print(f"Không bắt đầu/kết thúc bằng @ hoặc .: {valid_start_end}")

# d) Kết quả validation
is_valid = has_at and has_dot_after_at and valid_start_end
print(f"Email hợp lệ: {is_valid}")

# TODO 4.2: Phone number formatter
phone = "0123456789"

print(f"\nSố điện thoại: {phone}")

# a) Kiểm tra có đúng 10 chữ số không
is_valid_length = len(phone) == 10 and phone.isdigit()
print(f"Đúng 10 chữ số: {is_valid_length}")

if is_valid_length:
    # b) Format thành dạng: (012) 345-6789
    formatted1 = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print(f"Format 1: {formatted1}")
    
    # c) Format thành dạng: 012.345.6789
    formatted2 = f"{phone[:3]}.{phone[3:6]}.{phone[6:]}"
    print(f"Format 2: {formatted2}")
    
    # d) Format thành dạng: +84 12 345 6789
    formatted3 = f"+84 {phone[1:3]} {phone[3:6]} {phone[6:]}"
    print(f"Format 3: {formatted3}")

# TODO 4.3: Credit card number validator
card_number = "1234 5678 9012 3456"

print(f"\nSố thẻ: {card_number}")

# a) Loại bỏ khoảng trắng
clean_card = card_number.replace(" ", "")
print(f"Sau khi loại bỏ space: {clean_card}")

# b) Kiểm tra có đúng 16 chữ số không
is_valid_card = len(clean_card) == 16 and clean_card.isdigit()
print(f"Đúng 16 chữ số: {is_valid_card}")

# c) Ẩn 12 số đầu, chỉ hiện 4 số cuối
if is_valid_card:
    masked_card = "****-****-****-" + clean_card[-4:]
    print(f"Số thẻ ẩn: {masked_card}")

# =============================================================================
# SOLUTION 5: UNIT CONVERSION
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 5: UNIT CONVERSION")
print("=" * 50)

# TODO 5.1: Temperature conversion
celsius = 25

print(f"Nhiệt độ: {celsius}°C")

# a) Chuyển Celsius sang Fahrenheit: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"Fahrenheit: {fahrenheit}°F")

# b) Chuyển Celsius sang Kelvin: K = C + 273.15
kelvin = celsius + 273.15
print(f"Kelvin: {kelvin}K")

# TODO 5.2: Length conversion
meters = 1500

print(f"\nĐộ dài: {meters} mét")

# a) Kilometers (1 km = 1000 m)
kilometers = meters / 1000
print(f"Kilometers: {kilometers} km")

# b) Centimeters (1 m = 100 cm)
centimeters = meters * 100
print(f"Centimeters: {centimeters:,} cm")

# c) Inches (1 m = 39.37 inches)
inches = meters * 39.37
print(f"Inches: {inches:,.2f} inches")

# d) Feet (1 m = 3.281 feet)
feet = meters * 3.281
print(f"Feet: {feet:,.2f} feet")

# TODO 5.3: Currency converter
usd_amount = 100
usd_to_vnd_rate = 24000

print(f"\nSố tiền: ${usd_amount}")
print(f"Tỷ giá: 1 USD = {usd_to_vnd_rate:,} VND")

# a) Chuyển USD sang VND
vnd_amount = usd_amount * usd_to_vnd_rate
print(f"Số tiền VND: {vnd_amount:,} VND")

# b) Format số tiền VND với dấu phẩy
formatted_vnd = f"{vnd_amount:,} VND"
print(f"Số tiền formatted: {formatted_vnd}")

# c) Tính phí chuyển đổi 2% và số tiền thực nhận
fee_rate = 0.02
fee = vnd_amount * fee_rate
actual_amount = vnd_amount - fee
print(f"Phí chuyển đổi (2%): {fee:,} VND")
print(f"Số tiền thực nhận: {actual_amount:,} VND")

# =============================================================================
# SOLUTION 6: LOGICAL EXPRESSIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 6: LOGICAL EXPRESSIONS")
print("=" * 50)

# TODO 6.1: Student grade eligibility
math_score = 85
english_score = 78
science_score = 92

print(f"Điểm Toán: {math_score}")
print(f"Điểm Anh: {english_score}")
print(f"Điểm Khoa học: {science_score}")

average = (math_score + english_score + science_score) / 3
print(f"Điểm trung bình: {average:.2f}")

# Điều kiện đậu:
condition1 = average >= 80  # Điểm trung bình >= 80
condition2 = all([math_score >= 60, english_score >= 60, science_score >= 60])  # Không có môn < 60
condition3 = sum([math_score >= 80, english_score >= 80, science_score >= 80]) >= 2  # Ít nhất 2 môn >= 80

is_pass = condition1 and condition2 and condition3

print(f"Điều kiện 1 (TB >= 80): {condition1}")
print(f"Điều kiện 2 (Không có môn < 60): {condition2}")
print(f"Điều kiện 3 (Ít nhất 2 môn >= 80): {condition3}")
print(f"Kết quả: {'ĐẬU' if is_pass else 'TRƯỢT'}")

# TODO 6.2: Login system
username = "admin"
password = "secret123"
is_account_active = True
failed_attempts = 0
max_attempts = 3

print(f"\nThông tin đăng nhập:")
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Account active: {is_account_active}")
print(f"Failed attempts: {failed_attempts}/{max_attempts}")

# Kiểm tra đăng nhập
correct_credentials = (username == "admin" and password == "secret123")
account_status_ok = is_account_active
attempts_ok = failed_attempts < max_attempts

login_success = correct_credentials and account_status_ok and attempts_ok

print(f"Thông tin đúng: {correct_credentials}")
print(f"Account OK: {account_status_ok}")
print(f"Attempts OK: {attempts_ok}")
print(f"Đăng nhập: {'THÀNH CÔNG' if login_success else 'THẤT BẠI'}")

# TODO 6.3: Discount calculator
customer_age = 25
is_member = True
purchase_amount = 150
is_weekend = False

print(f"\nThông tin khách hàng:")
print(f"Tuổi: {customer_age}")
print(f"Thành viên: {is_member}")
print(f"Số tiền mua: ${purchase_amount}")
print(f"Cuối tuần: {is_weekend}")

# Tính discount
discounts = []

# Senior discount (65+): 20%
if customer_age >= 65:
    discounts.append(('Senior', 0.20))

# Member discount: 10%
if is_member:
    discounts.append(('Member', 0.10))

# Large purchase discount: 5%
if purchase_amount > 100:
    discounts.append(('Large Purchase', 0.05))

# Weekend discount: 5%
if is_weekend:
    discounts.append(('Weekend', 0.05))

# Tính tổng discount (tối đa 30%)
total_discount = sum([discount[1] for discount in discounts])
total_discount = min(total_discount, 0.30)  # Tối đa 30%

discount_amount = purchase_amount * total_discount
final_amount = purchase_amount - discount_amount

print(f"\nCác loại giảm giá:")
for name, rate in discounts:
    print(f"- {name}: {rate*100}%")

print(f"Tổng giảm giá: {total_discount*100}%")
print(f"Số tiền giảm: ${discount_amount:.2f}")
print(f"Thành tiền: ${final_amount:.2f}")

print("\n" + "=" * 50)
print("HOÀN THÀNH SOLUTION 2!")
print("=" * 50)
