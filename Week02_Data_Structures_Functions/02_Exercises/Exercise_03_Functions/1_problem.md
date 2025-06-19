# Exercise 03: Functions

## Mục tiêu

- Học cách định nghĩa và sử dụng functions trong Python
- Hiểu về parameters, arguments, return values
- Làm quen với scope và local/global variables
- Ứng dụng functions để tổ chức code hiệu quả

## Bài tập

### Bài 1: Máy tính cơ bản với Functions

Viết chương trình máy tính sử dụng functions:

**Yêu cầu:**

1. Tạo các function: `add()`, `subtract()`, `multiply()`, `divide()`
2. Function `calculate()` nhận operator và 2 số, gọi function tương ứng
3. Function `get_input()` để nhập dữ liệu từ user
4. Function `display_menu()` hiển thị menu
5. Xử lý lỗi chia cho 0

**Input mẫu:**

```
Chọn phép toán:
1. Cộng (+)
2. Trừ (-)
3. Nhân (*)
4. Chia (/)
Lựa chọn: 1
Nhập số thứ nhất: 15
Nhập số thứ hai: 7
```

**Output mẫu:**

```
=== MÁY TÍNH CƠ BẢN ===
Chọn phép toán:
1. Cộng (+)
2. Trừ (-)
3. Nhân (*)
4. Chia (/)
Lựa chọn: 1

Nhập số thứ nhất: 15
Nhập số thứ hai: 7

Kết quả: 15 + 7 = 22
```

### Bài 2: Hệ thống quản lý điểm số

Viết chương trình quản lý điểm số học sinh:

**Yêu cầu:**

1. Function `input_scores()`: nhập danh sách điểm
2. Function `calculate_average()`: tính điểm trung bình
3. Function `find_max_min()`: tìm điểm cao nhất và thấp nhất
4. Function `classify_grade()`: phân loại học lực (Giỏi ≥8.5, Khá ≥7.0, TB ≥5.0, Yếu <5.0)
5. Function `count_by_grade()`: đếm số học sinh theo từng loại
6. Function `display_statistics()`: hiển thị thống kê tổng hợp

**Input mẫu:**

```python
scores = [8.5, 7.2, 9.1, 6.8, 5.5, 8.8, 7.9, 4.2, 9.5, 6.1]
```

**Output mẫu:**

```
=== THỐNG KÊ ĐIỂM SỐ LỚP HỌC ===
Danh sách điểm: [8.5, 7.2, 9.1, 6.8, 5.5, 8.8, 7.9, 4.2, 9.5, 6.1]
Số học sinh: 10

Điểm trung bình: 7.36
Điểm cao nhất: 9.5
Điểm thấp nhất: 4.2

Phân loại học lực:
- Giỏi (≥8.5): 3 học sinh (30.0%)
- Khá (≥7.0): 3 học sinh (30.0%)
- Trung bình (≥5.0): 3 học sinh (30.0%)
- Yếu (<5.0): 1 học sinh (10.0%)
```

### Bài 3: Chuyển đổi và xử lý chuỗi

Viết các function xử lý chuỗi:

**Yêu cầu:**

1. Function `reverse_string()`: đảo ngược chuỗi
2. Function `count_words()`: đếm số từ trong chuỗi
3. Function `capitalize_words()`: viết hoa chữ cái đầu mỗi từ
4. Function `remove_duplicates()`: loại bỏ từ trùng lặp
5. Function `find_longest_word()`: tìm từ dài nhất
6. Function `count_character_frequency()`: đếm tần suất ký tự

**Input mẫu:**

```
text = "python programming is fun and python is powerful"
```

**Output mẫu:**

```
=== XỬ LÝ CHUỖI ===
Chuỗi gốc: "python programming is fun and python is powerful"

Chuỗi đảo ngược: "lufrewop si nohtyp dna nuf si gnimmargorp nohtyp"
Số từ: 8
Viết hoa chữ cái đầu: "Python Programming Is Fun And Python Is Powerful"
Loại bỏ từ trùng: "python programming is fun and powerful"
Từ dài nhất: "programming" (11 ký tự)

Tần suất ký tự (top 5):
- ' ': 7 lần
- 'n': 6 lần
- 'o': 4 lần
- 'p': 4 lần
- 'r': 4 lần
```

### Bài 4: Hệ thống tính lương (Functions với tham số)

Viết chương trình tính lương nhân viên:

**Yêu cầu:**

1. Function `calculate_basic_salary()`: tính lương cơ bản
2. Function `calculate_overtime()`: tính lương làm thêm giờ
3. Function `calculate_bonus()`: tính thưởng theo hiệu suất
4. Function `calculate_tax()`: tính thuế thu nhập
5. Function `calculate_net_salary()`: tính lương thực lãnh
6. Function `generate_payslip()`: tạo phiếu lương

**Công thức:**

- Lương cơ bản = số giờ làm việc × đơn giá giờ
- Lương làm thêm = (giờ làm thêm × đơn giá giờ × 1.5) nếu > 40 giờ/tuần
- Thưởng = lương cơ bản × % hiệu suất
- Thuế = (lương tổng - 11,000,000) × 10% nếu lương > 11 triệu
- Lương thực lãnh = lương tổng + thưởng - thuế

**Input mẫu:**

```
Nhân viên: Nguyễn Văn A
Số giờ làm việc: 45
Đơn giá giờ: 50,000 VNĐ
Hiệu suất: 15% (0.15)
```

**Output mẫu:**

```
=== PHIẾU LƯƠNG THÁNG 3/2024 ===
Nhân viên: Nguyễn Văn A

CHI TIẾT TÍNH LƯƠNG:
- Giờ làm việc cơ bản: 40 giờ
- Giờ làm thêm: 5 giờ
- Đơn giá giờ: 50,000 VNĐ

THÀNH PHẦN LƯƠNG:
- Lương cơ bản: 2,000,000 VNĐ
- Lương làm thêm: 375,000 VNĐ
- Thưởng hiệu suất (15%): 356,250 VNĐ
- Tổng thu nhập: 2,731,250 VNĐ

KHẤU TRỪ:
- Thuế thu nhập cá nhân: 0 VNĐ

LƯƠNG THỰC LÃNH: 2,731,250 VNĐ
```

### Bài 5: Game đoán số (Functions và logic)

Viết game đoán số sử dụng functions:

**Yêu cầu:**

1. Function `generate_random_number()`: tạo số ngẫu nhiên
2. Function `get_user_guess()`: nhận input từ user
3. Function `check_guess()`: kiểm tra và đưa ra gợi ý
4. Function `display_result()`: hiển thị kết quả
5. Function `play_again()`: hỏi chơi lại
6. Function `show_statistics()`: hiển thị thống kê

**Output mẫu:**

```
=== GAME ĐOÁN SỐ ===
Tôi đã nghĩ ra một số từ 1 đến 100.
Bạn có 7 lần đoán!

Lần đoán 1: Nhập số: 50
Số bạn đoán lớn hơn số tôi nghĩ!

Lần đoán 2: Nhập số: 25
Số bạn đoán nhỏ hơn số tôi nghĩ!

Lần đoán 3: Nhập số: 37
Số bạn đoán nhỏ hơn số tôi nghĩ!

Lần đoán 4: Nhập số: 43
Chúc mừng! Bạn đã đoán đúng số 43 sau 4 lần!

THỐNG KÊ:
- Số lần chơi: 1
- Tỷ lệ thắng: 100%
- Số lần đoán trung bình: 4.0
```

## Hướng dẫn giải

### Tips cho Functions:

- Sử dụng docstring để mô tả function
- Chia nhỏ logic phức tạp thành nhiều function
- Sử dụng default parameters: `def func(x, y=10)`
- Return multiple values: `return a, b, c`
- Kiểm tra input validation trong function

### Cấu trúc function tốt:

```python
def function_name(parameters):
    """
    Mô tả function
    Args: mô tả parameters
    Returns: mô tả giá trị trả về
    """
    # Logic xử lý
    return result
```

## Tiêu chí đánh giá

- [ ] Functions được định nghĩa đúng cú pháp
- [ ] Logic xử lý trong function chính xác
- [ ] Sử dụng parameters và return values hợp lý
- [ ] Code được tổ chức tốt, dễ đọc
- [ ] Có docstring mô tả function
- [ ] Xử lý edge cases và validation input
- [ ] Không có code trùng lặp (DRY principle)
