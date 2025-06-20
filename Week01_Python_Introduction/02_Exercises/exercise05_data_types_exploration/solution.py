# Exercise 05: Data Types Exploration - Solution

# =============================================================================
# EXERCISE 05: DATA TYPES EXPLORATION
# =============================================================================

print("=" * 60)
print("    EXERCISE 05: DATA TYPES EXPLORATION")
print("=" * 60)

# =============================================================================
# PHẦN 1: KIỂU SỐ (NUMBERS)
# =============================================================================

print("\n=== KIỂU SỐ (NUMBERS) ===")

# 1. Integer (số nguyên)
integer_num = 42
print(f"integer_num = {integer_num}, type = {type(integer_num)}")

# 2. Float (số thực)
float_num = 3.14159
print(f"float_num = {float_num}, type = {type(float_num)}")

# 3. Scientific notation
scientific_num = 2e5  # 200000.0
print(f"scientific_num = {scientific_num}, type = {type(scientific_num)}")

# 4. Complex number (số phức)
complex_num = 3 + 4j
print(f"complex_num = {complex_num}, type = {type(complex_num)}")

# =============================================================================
# PHẦN 2: KIỂU CHUỖI (STRING)
# =============================================================================

print("\n=== KIỂU CHUỖI (STRING) ===")

# 5. Simple string
simple_string = "Hello Python"
print(f'simple_string = "{simple_string}", type = {type(simple_string)}')

# 6. Multiline string
multiline_string = """Đây là dòng 1
Đây là dòng 2
Đây là dòng 3"""
print(f"multiline_string có {len(multiline_string.splitlines())} dòng")
print(f"Nội dung:\n{multiline_string}")

# 7. Raw string (không xử lý escape characters)
raw_string = r"C:\new\text.txt"
print(f'raw_string = "{raw_string}"')

# 8. Unicode string
unicode_string = "Xin chào 🐍"
print(f'unicode_string = "{unicode_string}"')

# =============================================================================
# PHẦN 3: KIỂU BOOLEAN
# =============================================================================

print("\n=== KIỂU BOOLEAN ===")

# 9. True value
is_true = True
print(f"is_true = {is_true}")

# 10. False value
is_false = False
print(f"is_false = {is_false}")

# 11. Boolean from number
bool_from_number = bool(10)  # True (số khác 0)
print(f"bool(10) = {bool_from_number}")

# 12. Boolean from string
bool_from_string = bool("")  # False (chuỗi rỗng)
print(f'bool("") = {bool_from_string}')

# Thêm ví dụ khác
print(f"bool(0) = {bool(0)}")           # False
print(f'bool("hello") = {bool("hello")}') # True

# =============================================================================
# PHẦN 4: KIỂU DANH SÁCH (LIST)
# =============================================================================

print("\n=== KIỂU DANH SÁCH (LIST) ===")

# 13. Number list
number_list = [1, 2, 3, 4, 5]
print(f"number_list: {number_list}, length = {len(number_list)}")

# 14. Mixed list (chứa nhiều kiểu dữ liệu)
mixed_list = [1, "hello", 3.14, True, None]
print(f"mixed_list: {mixed_list}, length = {len(mixed_list)}")

# 15. Nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"nested_list: {nested_list}, length = {len(nested_list)}")

# =============================================================================
# PHẦN 5: KIỂU TUPLE
# =============================================================================

print("\n=== KIỂU TUPLE ===")

# 16. Coordinate tuple
coordinate = (10, 20)
print(f"coordinate: {coordinate}, length = {len(coordinate)}")

# 17. Single element tuple (cần dấu phẩy!)
single_tuple = (42,)
print(f"single_tuple: {single_tuple}, length = {len(single_tuple)}")

# 18. RGB color tuple
color_rgb = (255, 128, 0)
print(f"color_rgb: {color_rgb}, length = {len(color_rgb)}")

# =============================================================================
# PHẦN 6: KIỂU DICTIONARY
# =============================================================================

print("\n=== KIỂU DICTIONARY ===")

# 19. Student info dictionary
student_info = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print(f"student_info: {student_info}, length = {len(student_info)}")

# 20. Nested dictionary
nested_dict = {
    "personal": {
        "name": "Bob",
        "age": 22
    },
    "academic": {
        "major": "Math",
        "year": 3
    }
}
print(f"nested_dict: {nested_dict}")
print(f"nested_dict length = {len(nested_dict)}")

# =============================================================================
# PHẦN 7: KIỂU SET
# =============================================================================

print("\n=== KIỂU SET ===")

# 21. Unique numbers set
unique_numbers = {1, 2, 3, 4, 5}
print(f"unique_numbers: {unique_numbers}, length = {len(unique_numbers)}")

# 22. Set from list with duplicates
duplicate_list = [1, 1, 2, 2, 3, 3, 4, 5]
set_from_list = set(duplicate_list)
print(f"Original list: {duplicate_list}")
print(f"set_from_list: {set_from_list}, length = {len(set_from_list)}")

# =============================================================================
# PHẦN 8: PHÂN TÍCH VÀ SO SÁNH
# =============================================================================

print("\n=== PHÂN TÍCH KIỂU DỮ LIỆU ===")

# 23. In kiểu dữ liệu của tất cả biến
variables = [
    ("integer_num", integer_num),
    ("float_num", float_num),
    ("scientific_num", scientific_num),
    ("complex_num", complex_num),
    ("simple_string", simple_string),
    ("is_true", is_true),
    ("number_list", number_list),
    ("coordinate", coordinate),
    ("student_info", student_info),
    ("unique_numbers", unique_numbers)
]

print("Kiểu dữ liệu của các biến:")
for name, var in variables:
    print(f"- {name}: {type(var)}")

# 24. In kích thước của collections
print("\n=== KÍCH THƯỚC CÁC COLLECTION ===")
collections = [
    ("simple_string", simple_string),
    ("number_list", number_list),
    ("mixed_list", mixed_list),
    ("nested_list", nested_list),
    ("coordinate", coordinate),
    ("color_rgb", color_rgb),
    ("student_info", student_info),
    ("unique_numbers", unique_numbers)
]

for name, collection in collections:
    print(f"{name}: length = {len(collection)}")

# 25. Kiểm tra tính mutable/immutable
print("\n=== TÍNH CHẤT MUTABLE/IMMUTABLE ===")

# Immutable examples
string_example = "hello"
id_before = id(string_example)
string_example = string_example.upper()
id_after = id(string_example)
print(f"String - ID thay đổi khi 'modify': {id_before != id_after}")

tuple_example = (1, 2, 3)
print(f"Tuple - Không thể thay đổi (immutable)")

# Mutable examples
list_example = [1, 2, 3]
id_before = id(list_example)
list_example.append(4)
id_after = id(list_example)
print(f"List - ID không đổi khi modify: {id_before == id_after}")

dict_example = {"a": 1}
id_before = id(dict_example)
dict_example["b"] = 2
id_after = id(dict_example)
print(f"Dict - ID không đổi khi modify: {id_before == id_after}")

set_example = {1, 2, 3}
id_before = id(set_example)
set_example.add(4)
id_after = id(set_example)
print(f"Set - ID không đổi khi modify: {id_before == id_after}")

# =============================================================================
# BONUS: KHÁM PHÁ THÊM
# =============================================================================

print("\n=== BONUS: KHÁM PHÁ THÊM ===")

# Type checking
print("Type checking:")
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"isinstance(3.14, (int, float)): {isinstance(3.14, (int, float))}")

# Memory sharing for small integers
a = 100
b = 100
c = 1000
d = 1000
print(f"\nMemory sharing:")
print(f"Small integers (100): id(a) == id(b) = {id(a) == id(b)}")
print(f"Large integers (1000): id(c) == id(d) = {id(c) == id(d)}")

# Type conversion examples
print(f"\nType conversions:")
print(f'int("123"): {int("123")}')
print(f'float("3.14"): {float("3.14")}')
print(f'str(42): "{str(42)}"')
print(f'list((1, 2, 3)): {list((1, 2, 3))}')
print(f'tuple([1, 2, 3]): {tuple([1, 2, 3])}')

print("\n" + "=" * 60)
print("           HOÀN THÀNH DATA TYPES EXPLORATION!")
print("=" * 60)
