# Exercise 08: Boolean Logic

## Mô tả bài tập

Học về logic Boolean, phép toán so sánh, và các phép toán logic trong Python.

## Yêu cầu

Thực hiện các nhiệm vụ sau trong file `practice.py`:

### Phần 1: Giá trị Boolean cơ bản

1. Tạo biến `is_python_fun = True`
2. Tạo biến `is_difficult = False`
3. In ra giá trị và kiểu dữ liệu của các biến

### Phần 2: Phép toán so sánh

4. Tạo `age1 = 20` và `age2 = 25`
5. So sánh `age1 == age2`
6. So sánh `age1 != age2`
7. So sánh `age1 < age2`
8. So sánh `age1 > age2`
9. So sánh `age1 <= age2`
10. So sánh `age1 >= age2`

### Phần 3: Phép toán logic

11. Tính `True and True`
12. Tính `True and False`
13. Tính `False or True`
14. Tính `False or False`
15. Tính `not True`
16. Tính `not False`

### Phần 4: Logic phức tạp

17. Tạo điều kiện: `(age1 >= 18) and (age1 <= 65)`
18. Tạo điều kiện: `(age1 < 18) or (age1 > 65)`
19. Kết hợp: `is_python_fun and not is_difficult`

### Phần 5: Truthiness và Falsiness

20. Kiểm tra `bool(1)`, `bool(0)`
21. Kiểm tra `bool("")`, `bool("hello")`
22. Kiểm tra `bool([])`, `bool([1, 2, 3])`
23. Kiểm tra `bool(None)`

## Đầu ra mong đợi

```
=== BOOLEAN CƠ BẢN ===
is_python_fun = True, type = <class 'bool'>
is_difficult = False, type = <class 'bool'>

=== PHÉP SO SÁNH ===
age1 = 20, age2 = 25
20 == 25: False
20 != 25: True
20 < 25: True
20 > 25: False
20 <= 25: True
20 >= 25: False

=== PHÉP TOÁN LOGIC ===
True and True = True
True and False = False
False or True = True
False or False = False
not True = False
not False = True

=== LOGIC PHỨC TẠP ===
Tuổi làm việc (18-65): True
Ngoài tuổi làm việc: False
Python vui và không khó: True

=== TRUTHINESS ===
bool(1) = True
bool(0) = False
bool("") = False
bool("hello") = True
bool([]) = False
bool([1, 2, 3]) = True
bool(None) = False
```

## Kiến thức cần nắm

- Giá trị Boolean: True, False
- Phép so sánh: ==, !=, <, >, <=, >=
- Phép logic: and, or, not
- Tính truthiness của các kiểu dữ liệu
- Kết hợp điều kiện logic

## Mức độ khó: ⭐⭐☆☆☆
