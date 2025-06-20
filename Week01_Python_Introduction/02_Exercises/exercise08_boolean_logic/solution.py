# Exercise 08: Boolean Logic - Solution

# =============================================================================
# EXERCISE 08: BOOLEAN LOGIC
# =============================================================================

print("=" * 60)
print("    EXERCISE 08: BOOLEAN LOGIC")
print("=" * 60)

# =============================================================================
# PHẦN 1: GIÁ TRỊ BOOLEAN CƠ BẢN
# =============================================================================

print("\n=== BOOLEAN CƠ BẢN ===")

# 1-2. Tạo biến boolean
is_python_fun = True
is_difficult = False

# 3. In giá trị và kiểu dữ liệu
print(f"is_python_fun = {is_python_fun}, type = {type(is_python_fun)}")
print(f"is_difficult = {is_difficult}, type = {type(is_difficult)}")

# =============================================================================
# PHẦN 2: PHÉP TOÁN SO SÁNH
# =============================================================================

print("\n=== PHÉP SO SÁNH ===")

# 4. Tạo biến tuổi
age1 = 20
age2 = 25
print(f"age1 = {age1}, age2 = {age2}")

# 5. So sánh bằng
equal_result = age1 == age2
print(f"{age1} == {age2}: {equal_result}")

# 6. So sánh khác
not_equal_result = age1 != age2
print(f"{age1} != {age2}: {not_equal_result}")

# 7. So sánh nhỏ hơn
less_than_result = age1 < age2
print(f"{age1} < {age2}: {less_than_result}")

# 8. So sánh lớn hơn
greater_than_result = age1 > age2
print(f"{age1} > {age2}: {greater_than_result}")

# 9. So sánh nhỏ hơn hoặc bằng
less_equal_result = age1 <= age2
print(f"{age1} <= {age2}: {less_equal_result}")

# 10. So sánh lớn hơn hoặc bằng
greater_equal_result = age1 >= age2
print(f"{age1} >= {age2}: {greater_equal_result}")

# =============================================================================
# PHẦN 3: PHÉP TOÁN LOGIC
# =============================================================================

print("\n=== PHÉP TOÁN LOGIC ===")

# 11. True and True
and_true_true = True and True
print(f"True and True = {and_true_true}")

# 12. True and False
and_true_false = True and False
print(f"True and False = {and_true_false}")

# 13. False or True
or_false_true = False or True
print(f"False or True = {or_false_true}")

# 14. False or False
or_false_false = False or False
print(f"False or False = {or_false_false}")

# 15. not True
not_true = not True
print(f"not True = {not_true}")

# 16. not False
not_false = not False
print(f"not False = {not_false}")

# =============================================================================
# PHẦN 4: LOGIC PHỨC TẠP
# =============================================================================

print("\n=== LOGIC PHỨC TẠP ===")

# 17. Kiểm tra tuổi làm việc (18-65)
working_age = (age1 >= 18) and (age1 <= 65)
print(f"Tuổi làm việc (18-65): {working_age}")

# 18. Ngoài tuổi làm việc
outside_working_age = (age1 < 18) or (age1 > 65)
print(f"Ngoài tuổi làm việc: {outside_working_age}")

# 19. Kết hợp điều kiện
python_good_to_learn = is_python_fun and not is_difficult
print(f"Python vui và không khó: {python_good_to_learn}")

# =============================================================================
# PHẦN 5: TRUTHINESS VÀ FALSINESS
# =============================================================================

print("\n=== TRUTHINESS ===")

# 20. Boolean từ số
bool_1 = bool(1)
bool_0 = bool(0)
print(f"bool(1) = {bool_1}")
print(f"bool(0) = {bool_0}")

# 21. Boolean từ chuỗi
bool_empty_string = bool("")
bool_hello = bool("hello")
print(f'bool("") = {bool_empty_string}')
print(f'bool("hello") = {bool_hello}')

# 22. Boolean từ list
bool_empty_list = bool([])
bool_list = bool([1, 2, 3])
print(f"bool([]) = {bool_empty_list}")
print(f"bool([1, 2, 3]) = {bool_list}")

# 23. Boolean từ None
bool_none = bool(None)
print(f"bool(None) = {bool_none}")

# =============================================================================
# BONUS: CÁC VÍ DỤ NÂNG CAO
# =============================================================================

print("\n=== BONUS: VÍ DỤ NÂNG CAO ===")

# Short-circuit evaluation
print("Short-circuit evaluation:")
print(f"True or (print không chạy): {True or print('Không in')}")

# Chaining comparisons
x = 15
chain_result = 10 < x < 20
print(f"10 < {x} < 20: {chain_result}")

# Boolean arithmetic
print(f"True + True = {True + True}")
print(f"False * 5 = {False * 5}")

# Practical examples
# Kiểm tra tên hợp lệ
name = "Alice"
valid_name = name and name.isalpha() and len(name) >= 2
print(f"'{name}' là tên hợp lệ: {valid_name}")

# Kiểm tra tuổi hợp lệ
age = 25
valid_age = isinstance(age, int) and 0 <= age <= 150
print(f"Tuổi {age} hợp lệ: {valid_age}")

# Default value với or
username = "" or "guest"
print(f"Username: {username}")

# Toggle boolean
flag = True
print(f"Flag ban đầu: {flag}")
flag = not flag
print(f"Flag sau toggle: {flag}")

# Truth table đầy đủ
print("\n=== TRUTH TABLE ===")
print("AND Truth Table:")
print(f"True  and True  = {True and True}")
print(f"True  and False = {True and False}")
print(f"False and True  = {False and True}")
print(f"False and False = {False and False}")

print("\nOR Truth Table:")
print(f"True  or True  = {True or True}")
print(f"True  or False = {True or False}")
print(f"False or True  = {False or True}")
print(f"False or False = {False or False}")

print("\nNOT Truth Table:")
print(f"not True  = {not True}")
print(f"not False = {not False}")

# Test tất cả falsy values
print("\n=== TẤT CẢ FALSY VALUES ===")
falsy_values = [False, 0, 0.0, "", [], {}, set(), None]
for value in falsy_values:
    print(f"bool({repr(value):>10}) = {bool(value)}")

# Test một số truthy values
print("\n=== MỘT SỐ TRUTHY VALUES ===")
truthy_values = [True, 1, -1, "hello", [1], {"a": 1}, {1, 2}]
for value in truthy_values:
    print(f"bool({repr(value):>10}) = {bool(value)}")

print("\n" + "=" * 60)
print("         HOÀN THÀNH BOOLEAN LOGIC!")
print("=" * 60)
