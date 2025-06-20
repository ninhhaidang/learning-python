# Exercise 09: Type Conversions - Solution

# =============================================================================
# EXERCISE 09: TYPE CONVERSIONS
# =============================================================================

print("=" * 60)
print("    EXERCISE 09: TYPE CONVERSIONS")
print("=" * 60)

# =============================================================================
# PHẦN 1: CHUYỂN ĐỔI STRING SANG NUMBER
# =============================================================================

print("\n=== STRING TO NUMBER ===")

# 1. String to integer
str_123 = "123"
int_123 = int(str_123)
print(f'int("{str_123}") = {int_123}, type = {type(int_123)}')

# 2. String to float
str_314 = "3.14"
float_314 = float(str_314)
print(f'float("{str_314}") = {float_314}, type = {type(float_314)}')

# 3. String through float to int
str_42 = "42.0"
int_42 = int(float(str_42))
print(f'int(float("{str_42}")) = {int_42}, type = {type(int_42)}')

# 4. Error handling
str_abc = "abc"
try:
    int_abc = int(str_abc)
    print(f'int("{str_abc}") = {int_abc}')
except ValueError as e:
    print(f'"{str_abc}" không thể chuyển thành int: {e}')

# =============================================================================
# PHẦN 2: CHUYỂN ĐỔI NUMBER SANG STRING
# =============================================================================

print("\n=== NUMBER TO STRING ===")

# 5. Integer to string
num_42 = 42
str_42_result = str(num_42)
print(f'str({num_42}) = "{str_42_result}", type = {type(str_42_result)}')

# 6. Float to string
num_pi = 3.14159
str_pi = str(num_pi)
print(f'str({num_pi}) = "{str_pi}", type = {type(str_pi)}')

# 7. Formatted number to string
formatted_42 = f"{num_42:.2f}"
print(f'f"{{{num_42}:.2f}}" = "{formatted_42}"')

# 8. Negative number to string
num_neg = -25
str_neg = str(num_neg)
print(f'str({num_neg}) = "{str_neg}"')

# =============================================================================
# PHẦN 3: CHUYỂN ĐỔI BOOLEAN
# =============================================================================

print("\n=== BOOLEAN CONVERSIONS ===")

# 9. Numbers to boolean
numbers_to_bool = [1, 0, -1]
for num in numbers_to_bool:
    bool_result = bool(num)
    print(f'bool({num}) = {bool_result}')

# 10. Strings to boolean
strings_to_bool = ["", "hello", " "]
for string in strings_to_bool:
    bool_result = bool(string)
    print(f'bool("{string}") = {bool_result}')

# 11. Collections to boolean
collections_to_bool = [
    ([], "empty list"),
    ([1, 2], "non-empty list"),
    ({}, "empty dict"),
    ({"a": 1}, "non-empty dict")
]
for collection, description in collections_to_bool:
    bool_result = bool(collection)
    print(f'bool({description}) = {bool_result}')

# 12. None to boolean
none_to_bool = bool(None)
print(f'bool(None) = {none_to_bool}')

# =============================================================================
# PHẦN 4: CHUYỂN ĐỔI COLLECTION TYPES
# =============================================================================

print("\n=== COLLECTION CONVERSIONS ===")

# 13. List to tuple
list_123 = [1, 2, 3]
tuple_123 = tuple(list_123)
print(f'list to tuple: {list_123} → {tuple_123}')

# 14. Tuple to list
tuple_456 = (4, 5, 6)
list_456 = list(tuple_456)
print(f'tuple to list: {tuple_456} → {list_456}')

# 15. List to set (removes duplicates)
list_duplicates = [1, 1, 2, 2, 3]
set_unique = set(list_duplicates)
print(f'list to set: {list_duplicates} → {set_unique}')

# 16. String to list of characters
string_hello = "hello"
list_chars = list(string_hello)
print(f'string to list: "{string_hello}" → {list_chars}')

# =============================================================================
# PHẦN 5: CHUYỂN ĐỔI SỐ CƠ SỐ KHÁC NHAU
# =============================================================================

print("\n=== BASE CONVERSIONS ===")

# 17. Binary to decimal
binary_str = "1010"
decimal_from_bin = int(binary_str, 2)
print(f'Binary "{binary_str}" = {decimal_from_bin} (decimal)')

# 18. Hexadecimal to decimal
hex_str = "FF"
decimal_from_hex = int(hex_str, 16)
print(f'Hex "{hex_str}" = {decimal_from_hex} (decimal)')

# 19. Decimal to binary string
decimal_255 = 255
binary_255 = bin(decimal_255)
print(f'{decimal_255} = "{binary_255}" (binary)')

# 20. Decimal to hexadecimal string
hex_255 = hex(decimal_255)
print(f'{decimal_255} = "{hex_255}" (hex)')

# Bonus: Octal conversion
octal_255 = oct(decimal_255)
print(f'{decimal_255} = "{octal_255}" (octal)')

# =============================================================================
# PHẦN 6: XỬ LÝ LỖI VÀ VALIDATION
# =============================================================================

print("\n=== ERROR HANDLING ===")

# 21. Function kiểm tra string có thể chuyển thành int
def is_convertible_to_int(value):
    """Kiểm tra xem giá trị có thể chuyển thành int không"""
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

# Test function
test_values_int = ["123", "abc", "45.67", "0", "-5"]
for value in test_values_int:
    result = is_convertible_to_int(value)
    print(f'is_convertible_to_int("{value}"): {result}')

# 22. Function chuyển đổi an toàn với giá trị mặc định
def safe_int(value, default=0):
    """Chuyển đổi an toàn sang int với giá trị mặc định"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Test safe conversion
test_values_safe = ["123", "abc", "45.67", None, []]
for value in test_values_safe:
    result = safe_int(value, -1)
    print(f'safe_int({repr(value)}, -1): {result}')

# 23. Chuyển đổi user input với error handling
def get_user_age():
    """Mô phỏng input từ user với error handling"""
    # Mô phỏng các input khác nhau
    mock_inputs = ["25", "abc", "30.5", "", "  20  "]
    
    for mock_input in mock_inputs:
        print(f'\nMô phỏng input: "{mock_input}"')
        try:
            # Xử lý input
            cleaned_input = mock_input.strip()
            if not cleaned_input:
                print("Input rỗng, sử dụng default age = 0")
                age = 0
            else:
                age = int(float(cleaned_input))  # Qua float để xử lý "30.5"
                print(f"Tuổi hợp lệ: {age}")
        except ValueError:
            print(f'Input "{mock_input}" không hợp lệ, sử dụng default age = 0')
            age = 0

get_user_age()

# =============================================================================
# BONUS: CÁC CHUYỂN ĐỔI NÂNG CAO
# =============================================================================

print("\n=== BONUS: CHUYỂN ĐỔI NÂNG CAO ===")

# Complex number conversions
complex_num = 3 + 4j
print(f"Complex number: {complex_num}")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")
print(f"Absolute value: {abs(complex_num)}")

# Bytes conversions
text = "Hello Python"
bytes_data = text.encode('utf-8')
back_to_text = bytes_data.decode('utf-8')
print(f'Text to bytes: "{text}" → {bytes_data}')
print(f'Bytes to text: {bytes_data} → "{back_to_text}"')

# Multiple conversions in one line
chained_conversion = str(int(float("42.7")))
print(f'Chained: str(int(float("42.7"))) = "{chained_conversion}"')

# List comprehension với conversion
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = [int(x) for x in str_numbers]
print(f'List conversion: {str_numbers} → {int_numbers}')

# Dictionary với type conversion
mixed_dict = {"age": "25", "height": "175.5", "name": "Alice"}
converted_dict = {
    k: (int(v) if v.isdigit() else float(v) if v.replace('.', '').isdigit() else v)
    for k, v in mixed_dict.items()
}
print(f'Dict conversion: {mixed_dict} → {converted_dict}')

# Format string examples
number = 42
print(f"\nFormat examples for {number}:")
print(f"Decimal: {number:d}")
print(f"Binary: {number:b}")
print(f"Hex (lower): {number:x}")
print(f"Hex (upper): {number:X}")
print(f"Octal: {number:o}")
print(f"With padding: {number:08d}")

# Type checking before conversion
def smart_convert(value):
    """Smart conversion dựa trên type của input"""
    if isinstance(value, str):
        if value.isdigit():
            return int(value)
        elif value.replace('.', '').replace('-', '').isdigit():
            return float(value)
        else:
            return value
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, bool):
        return int(value)
    else:
        return str(value)

# Test smart convert
smart_test = ["123", "3.14", "-5", "hello", 42, 3.14, True, [1, 2, 3]]
for item in smart_test:
    result = smart_convert(item)
    print(f'smart_convert({repr(item)}) = {repr(result)} ({type(result).__name__})')

print("\n" + "=" * 60)
print("        HOÀN THÀNH TYPE CONVERSIONS!")
print("=" * 60)
