# Exercise 07: Number Operations

## Mô tả bài tập

Học cách thực hiện các phép toán cơ bản và nâng cao với số trong Python: cộng, trừ, nhân, chia, lũy thừa, modulo, và sử dụng các hàm toán học.

## Yêu cầu

Thực hiện các nhiệm vụ sau trong file `practice.py`:

### Phần 1: Phép toán cơ bản

1. Tạo `a = 15` và `b = 4`
2. Tính tổng: `a + b`
3. Tính hiệu: `a - b`
4. Tính tích: `a * b`
5. Tính thương (chia thực): `a / b`
6. Tính chia lấy phần nguyên: `a // b`
7. Tính phần dư: `a % b`
8. Tính lũy thừa: `a ** b`

### Phần 2: Thứ tự ưu tiên phép toán

9. Tính `2 + 3 * 4` (không dùng ngoặc)
10. Tính `(2 + 3) * 4` (có ngoặc)
11. Tính `10 - 6 / 2 + 1`
12. Tính `2 ** 3 ** 2` (lũy thừa liên tiếp)

### Phần 3: Làm việc với số thực

13. Tạo `pi = 3.14159` và `radius = 5`
14. Tính diện tích hình tròn: `pi * radius ** 2`
15. Tính chu vi hình tròn: `2 * pi * radius`
16. Làm tròn diện tích đến 2 chữ số thập phân

### Phần 4: Hàm toán học built-in

17. Tìm giá trị tuyệt đối của `-25`
18. Tìm giá trị lớn nhất trong `[10, 5, 8, 20, 3]`
19. Tìm giá trị nhỏ nhất trong `[10, 5, 8, 20, 3]`
20. Tính tổng của list `[1, 2, 3, 4, 5]`
21. Làm tròn `3.7` và `3.2`

### Phần 5: Số học với module math

22. Import module math
23. Tính `math.sqrt(16)` (căn bậc 2)
24. Tính `math.ceil(3.2)` (làm tròn lên)
25. Tính `math.floor(3.8)` (làm tròn xuống)
26. Tính `math.sin(math.pi/2)` (sin 90 độ)

### Phần 6: Ứng dụng thực tế

27. Tính BMI: weight = 70kg, height = 1.75m
28. Chuyển đổi nhiệt độ: 25°C sang °F
29. Tính lãi kép: 1,000,000 VND, lãi suất 5%/năm, 3 năm
30. Tính khoảng cách 2 điểm: (0,0) và (3,4)

## Đầu ra mong đợi

```
=== PHÉP TOÁN CƠ BẢN ===
a = 15, b = 4
Tổng: 15 + 4 = 19
Hiệu: 15 - 4 = 11
Tích: 15 * 4 = 60
Thương: 15 / 4 = 3.75
Chia nguyên: 15 // 4 = 3
Phần dư: 15 % 4 = 3
Lũy thừa: 15 ** 4 = 50625

=== THỨ TỰ ƯU TIÊN ===
2 + 3 * 4 = 14
(2 + 3) * 4 = 20
10 - 6 / 2 + 1 = 8.0
2 ** 3 ** 2 = 512

=== SỐ THỰC ===
Pi = 3.14159, bán kính = 5
Diện tích = 78.54
Chu vi = 31.42
Diện tích làm tròn = 78.54

=== HÀM TOÁN HỌC ===
abs(-25) = 25
max([10, 5, 8, 20, 3]) = 20
min([10, 5, 8, 20, 3]) = 3
sum([1, 2, 3, 4, 5]) = 15
round(3.7) = 4, round(3.2) = 3

=== MODULE MATH ===
sqrt(16) = 4.0
ceil(3.2) = 4
floor(3.8) = 3
sin(π/2) = 1.0

=== ỨNG DỤNG THỰC TẾ ===
BMI = 22.86 (Bình thường)
25°C = 77.0°F
Lãi kép sau 3 năm: 1,157,625 VND
Khoảng cách 2 điểm: 5.0
```

## Kiến thức cần nắm

- Các phép toán cơ bản: +, -, \*, /, //, %, \*\*
- Thứ tự ưu tiên phép toán
- Hàm built-in: abs, max, min, sum, round
- Module math: sqrt, ceil, floor, sin, cos, pi
- Làm việc với số thực và độ chính xác

## Mức độ khó: ⭐⭐☆☆☆
