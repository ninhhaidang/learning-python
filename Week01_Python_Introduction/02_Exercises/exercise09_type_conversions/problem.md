# Exercise 09: Type Conversions

## Mô tả bài tập

Học cách chuyển đổi giữa các kiểu dữ liệu khác nhau trong Python và xử lý các trường hợp lỗi chuyển đổi.

## Yêu cầu

Thực hiện các nhiệm vụ sau trong file `practice.py`:

### Phần 1: Chuyển đổi String sang Number

1. Chuyển `"123"` thành integer
2. Chuyển `"3.14"` thành float
3. Chuyển `"42.0"` thành integer (qua float trước)
4. Thử chuyển `"abc"` thành integer và xử lý lỗi

### Phần 2: Chuyển đổi Number sang String

5. Chuyển `42` thành string
6. Chuyển `3.14159` thành string
7. Chuyển `42` thành string với format 2 chữ số thập phân
8. Chuyển số âm `-25` thành string

### Phần 3: Chuyển đổi Boolean

9. Chuyển `1, 0, -1` thành boolean
10. Chuyển `"", "hello", " "` thành boolean
11. Chuyển `[], [1,2], {}, {"a":1}` thành boolean
12. Chuyển `None` thành boolean

### Phần 4: Chuyển đổi Collection Types

13. Chuyển list `[1,2,3]` thành tuple
14. Chuyển tuple `(4,5,6)` thành list
15. Chuyển list `[1,1,2,2,3]` thành set
16. Chuyển string `"hello"` thành list các ký tự

### Phần 5: Chuyển đổi số cơ số khác nhau

17. Chuyển binary `"1010"` (cơ số 2) thành decimal
18. Chuyển hexadecimal `"FF"` (cơ số 16) thành decimal
19. Chuyển decimal `255` thành binary string
20. Chuyển decimal `255` thành hexadecimal string

### Phần 6: Xử lý lỗi và validation

21. Viết function kiểm tra string có thể chuyển thành int không
22. Viết function chuyển đổi an toàn với giá trị mặc định
23. Chuyển đổi user input thành số với error handling

## Đầu ra mong đợi

```
=== STRING TO NUMBER ===
int("123") = 123, type = <class 'int'>
float("3.14") = 3.14, type = <class 'float'>
int(float("42.0")) = 42, type = <class 'int'>
"abc" không thể chuyển thành int: invalid literal

=== NUMBER TO STRING ===
str(42) = "42", type = <class 'str'>
str(3.14159) = "3.14159", type = <class 'str'>
f"{42:.2f}" = "42.00"
str(-25) = "-25"

=== BOOLEAN CONVERSIONS ===
bool(1) = True
bool(0) = False
bool(-1) = True
bool("") = False
bool("hello") = True
bool([]) = False
bool([1,2]) = True

=== COLLECTION CONVERSIONS ===
list to tuple: (1, 2, 3)
tuple to list: [4, 5, 6]
list to set: {1, 2, 3}
string to list: ['h', 'e', 'l', 'l', 'o']

=== BASE CONVERSIONS ===
Binary "1010" = 10 (decimal)
Hex "FF" = 255 (decimal)
255 = "0b11111111" (binary)
255 = "0xff" (hex)

=== ERROR HANDLING ===
is_convertible_to_int("123"): True
is_convertible_to_int("abc"): False
safe_int("123", 0): 123
safe_int("abc", 0): 0
```

## Kiến thức cần nắm

- Hàm chuyển đổi: `int()`, `float()`, `str()`, `bool()`
- Collection conversions: `list()`, `tuple()`, `set()`
- Base conversions: `bin()`, `hex()`, `int(x, base)`
- Error handling với `try-except`
- Type checking với `isinstance()`

## Mức độ khó: ⭐⭐⭐☆☆
