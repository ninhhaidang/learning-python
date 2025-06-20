# Exercise 06: String Manipulation - Solution

# =============================================================================
# EXERCISE 06: STRING MANIPULATION
# =============================================================================

print("=" * 60)
print("    EXERCISE 06: STRING MANIPULATION")
print("=" * 60)

# =============================================================================
# PHẦN 1: TẠO VÀ NỐI CHUỖI
# =============================================================================

print("\n=== TẠO VÀ NỐI CHUỖI ===")

# 1-2. Tạo biến tên và họ
first_name = "Nguyen"
last_name = "Van A"
print(f"Tên: {first_name}")
print(f"Họ: {last_name}")

# 3. Nối thành họ tên đầy đủ
full_name = first_name + " " + last_name
print(f"Họ tên đầy đủ: {full_name}")

# 4. Tạo lời chào
greeting = "Xin chào, " + full_name + "!"
print(f"Lời chào: {greeting}")

# =============================================================================
# PHẦN 2: ĐỊNH DẠNG CHUỖI
# =============================================================================

print("\n=== ĐỊNH DẠNG CHUỖI ===")

# 5. Biến tuổi
age = 20

# 6. F-string (Python 3.6+) - Cách hiện đại nhất
intro_f = f"Tôi tên {full_name}, {age} tuổi"
print(f"F-string: {intro_f}")

# 7. .format() method
intro_format = "Tôi tên {}, {} tuổi".format(full_name, age)
print(f"Format method: {intro_format}")

# Hoặc với named parameters
intro_format2 = "Tôi tên {name}, {age} tuổi".format(name=full_name, age=age)

# 8. % formatting (cách cũ)
intro_percent = "Tôi tên %s, %d tuổi" % (full_name, age)
print(f"% formatting: {intro_percent}")

# =============================================================================
# PHẦN 3: PHƯƠNG THỨC CHUỖI CƠ BẢN
# =============================================================================

print("\n=== PHƯƠNG THỨC CHUỖI ===")

# 9. Chuyển thành chữ hoa
upper_name = full_name.upper()
print(f"Chữ hoa: {upper_name}")

# 10. Chuyển thành chữ thường
lower_name = full_name.lower()
print(f"Chữ thường: {lower_name}")

# 11. Title case (viết hoa chữ đầu mỗi từ)
title_name = full_name.title()
print(f"Title case: {title_name}")

# 12. Đếm số ký tự
char_count = len(full_name)
print(f"Số ký tự: {char_count}")

# 13. Kiểm tra có chứa "Van" không
contains_van = "Van" in full_name
print(f"Chứa 'Van': {contains_van}")

# Bonus: thêm một số phương thức khác
print(f"Capitalize: {full_name.capitalize()}")
print(f"Swapcase: {full_name.swapcase()}")

# =============================================================================
# PHẦN 4: XỬ LÝ KHOẢNG TRẮNG
# =============================================================================

print("\n=== XỬ LÝ KHOẢNG TRẮNG ===")

# 14. Chuỗi có khoảng trắng thừa
messy_string = "   Hello World   "
print(f'Gốc: "{messy_string}"')

# 15. Loại bỏ khoảng trắng đầu và cuối
stripped = messy_string.strip()
print(f'Strip: "{stripped}"')

# 16. Loại bỏ chỉ khoảng trắng bên trái
left_stripped = messy_string.lstrip()
print(f'Lstrip: "{left_stripped}"')

# 17. Loại bỏ chỉ khoảng trắng bên phải
right_stripped = messy_string.rstrip()
print(f'Rstrip: "{right_stripped}"')

# =============================================================================
# PHẦN 5: CHIA VÀ THAY THẾ CHUỖI
# =============================================================================

print("\n=== CHIA VÀ THAY THẾ ===")

# 18. Chia chuỗi thành danh sách các từ
words = full_name.split()  # Tách theo khoảng trắng
print(f"Chia thành từ: {words}")

# Các cách split khác
words_space = full_name.split(" ")  # Tách theo space cụ thể
words_n = full_name.split("n")      # Tách theo ký tự 'n'

# 19. Thay thế "Nguyen" thành "Mr. Nguyen"
formal_name = full_name.replace("Nguyen", "Mr. Nguyen")
print(f"Thay thế: {formal_name}")

# 20. Tạo chuỗi từ danh sách với .join()
hyphenated = "-".join(words)
print(f"Join lại: {hyphenated}")

# Các ví dụ join khác
comma_separated = ", ".join(words)
print(f"Join với dấu phẩy: {comma_separated}")

# =============================================================================
# PHẦN 6: KIỂM TRA CHUỖI
# =============================================================================

print("\n=== KIỂM TRA CHUỖI ===")

# 21. Kiểm tra bắt đầu bằng "Nguyen"
starts_nguyen = full_name.startswith("Nguyen")
print(f"Bắt đầu bằng 'Nguyen': {starts_nguyen}")

# 22. Kiểm tra kết thúc bằng "A"
ends_a = full_name.endswith("A")
print(f"Kết thúc bằng 'A': {ends_a}")

# 23. Kiểm tra toàn bộ là chữ cái
is_alpha = full_name.isalpha()
print(f"Toàn chữ cái: {is_alpha} (có khoảng trắng)")

# Kiểm tra từng từ
words_alpha = [word.isalpha() for word in words]
print(f"Từng từ là chữ cái: {words_alpha}")

# 24. Kiểm tra toàn bộ là số
is_digit = full_name.isdigit()
print(f"Toàn số: {is_digit}")

# Test với chuỗi số
number_string = "12345"
print(f"'{number_string}' toàn số: {number_string.isdigit()}")

# =============================================================================
# BONUS: CÁC PHƯƠNG THỨC KHÁC
# =============================================================================

print("\n=== BONUS: CÁC PHƯƠNG THỨC KHÁC ===")

# Tìm kiếm
test_string = "Hello World Python World"
print(f"Find 'World': {test_string.find('World')}")        # Index đầu tiên
print(f"Count 'World': {test_string.count('World')}")      # Số lần xuất hiện
print(f"Replace 'World' 1 lần: {test_string.replace('World', 'Universe', 1)}")

# Kiểm tra kiểu chuỗi
test_cases = [
    ("ABC123", "isalnum"),
    ("   ", "isspace"),
    ("hello", "islower"),
    ("HELLO", "isupper"),
    ("Hello World", "istitle")
]

print("\nKiểm tra các kiểu chuỗi:")
for text, method in test_cases:
    result = getattr(text, method)()
    print(f"'{text}'.{method}(): {result}")

# String alignment
word = "Python"
print(f"\nString alignment:")
print(f"'{word}'.center(12): '{word.center(12)}'")
print(f"'{word}'.ljust(12): '{word.ljust(12)}'")
print(f"'{word}'.rjust(12): '{word.rjust(12)}'")
print(f"'{word}'.zfill(10): '{word.zfill(10)}'")

# Indexing và Slicing
print(f"\nIndexing và Slicing với '{full_name}':")
print(f"Ký tự đầu: {full_name[0]}")
print(f"Ký tự cuối: {full_name[-1]}")
print(f"3 ký tự đầu: {full_name[:3]}")
print(f"3 ký tự cuối: {full_name[-3:]}")
print(f"Từ ký tự 2-5: {full_name[2:6]}")
print(f"Reverse: {full_name[::-1]}")

# Multiple line processing
multiline_text = """Dòng 1: Hello
Dòng 2: World
Dòng 3: Python"""

print(f"\nXử lý multiline:")
lines = multiline_text.split('\n')
print(f"Số dòng: {len(lines)}")
for i, line in enumerate(lines, 1):
    print(f"  Dòng {i}: {line.strip()}")

print("\n" + "=" * 60)
print("         HOÀN THÀNH STRING MANIPULATION!")
print("=" * 60)
