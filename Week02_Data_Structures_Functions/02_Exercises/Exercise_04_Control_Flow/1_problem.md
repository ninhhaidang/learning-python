# Exercise 04: Control Flow

## Mục tiêu

- Thành thạo các cấu trúc điều khiển: if/elif/else, for, while
- Hiểu về nested loops và break/continue
- Ứng dụng control flow để giải quyết bài toán thực tế
- Kết hợp control flow với data structures

## Bài tập

### Bài 1: Hệ thống phân loại và thống kê

Viết chương trình phân loại học sinh theo nhiều tiêu chí:

**Yêu cầu:**

1. Nhập danh sách học sinh với thông tin: tên, tuổi, điểm toán, điểm văn, điểm anh
2. Phân loại theo học lực (điểm TB): Xuất sắc >9, Giỏi >8, Khá >6.5, TB >5, Yếu ≤5
3. Phân loại theo độ tuổi: Nhỏ tuổi <18, Bình thường 18-20, Lớn tuổi >20
4. Tìm học sinh giỏi toàn diện (tất cả môn >8)
5. Thống kê số lượng học sinh theo từng loại
6. Hiển thị top 3 học sinh có điểm cao nhất

**Input mẫu:**

```python
students = [
    {"name": "Nguyễn Văn A", "age": 18, "math": 8.5, "literature": 7.5, "english": 9.0},
    {"name": "Trần Thị B", "age": 19, "math": 9.2, "literature": 8.8, "english": 8.5},
    {"name": "Lê Văn C", "age": 17, "math": 6.0, "literature": 7.0, "english": 6.5},
    {"name": "Phạm Thị D", "age": 21, "math": 9.5, "literature": 9.0, "english": 9.2},
    {"name": "Hoàng Văn E", "age": 18, "math": 5.0, "literature": 4.5, "english": 5.5}
]
```

**Output mẫu:**

```
=== HỆ THỐNG PHÂN LOẠI HỌC SINH ===

=== DANH SÁCH CHI TIẾT ===
1. Nguyễn Văn A (18 tuổi) - ĐTB: 8.33 - Học lực: Giỏi - Độ tuổi: Bình thường
2. Trần Thị B (19 tuổi) - ĐTB: 8.83 - Học lực: Giỏi - Độ tuổi: Bình thường
3. Lê Văn C (17 tuổi) - ĐTB: 6.50 - Học lực: Trung bình - Độ tuổi: Nhỏ tuổi
4. Phạm Thị D (21 tuổi) - ĐTB: 9.23 - Học lực: Xuất sắc - Độ tuổi: Lớn tuổi
5. Hoàng Văn E (18 tuổi) - ĐTB: 5.00 - Học lực: Trung bình - Độ tuổi: Bình thường

=== THỐNG KÊ THEO HỌC LỰC ===
- Xuất sắc: 1 học sinh (20.0%)
- Giỏi: 2 học sinh (40.0%)
- Khá: 0 học sinh (0.0%)
- Trung bình: 2 học sinh (40.0%)
- Yếu: 0 học sinh (0.0%)

=== HỌC SINH GIỎI TOÀN DIỆN ===
- Phạm Thị D: Toán 9.5, Văn 9.0, Anh 9.2

=== TOP 3 HỌC SINH ĐIỂM CAO NHẤT ===
1. Phạm Thị D - ĐTB: 9.23
2. Trần Thị B - ĐTB: 8.83
3. Nguyễn Văn A - ĐTB: 8.33
```

### Bài 2: Quản lý kho hàng với vòng lặp

Viết chương trình quản lý kho hàng:

**Yêu cầu:**

1. Menu lựa chọn: Thêm hàng, Bán hàng, Kiểm tra tồn kho, Thống kê, Thoát
2. Thêm hàng: nhập mã, tên, số lượng, giá
3. Bán hàng: kiểm tra tồn kho, cập nhật số lượng, tính tiền
4. Kiểm tra cảnh báo hàng sắp hết (tồn kho < 10)
5. Thống kê: tổng giá trị kho, mặt hàng bán chạy nhất
6. Chương trình chạy liên tục cho đến khi user chọn thoát

**Output mẫu:**

```
=== HỆ THỐNG QUẢN LÝ KHO HÀNG ===

MENU CHÍNH:
1. Thêm hàng hóa
2. Bán hàng
3. Kiểm tra tồn kho
4. Thống kê kho hàng
5. Thoát chương trình

Lựa chọn của bạn: 1

=== THÊM HÀNG HÓA ===
Mã hàng: SP001
Tên hàng: Bút bi
Số lượng: 50
Giá bán: 5000
Đã thêm thành công!

Lựa chọn của bạn: 2

=== BÁN HÀNG ===
Mã hàng: SP001
Số lượng bán: 15
Bán thành công! Tồn kho còn lại: 35
Tổng tiền: 75,000 VNĐ

=== CẢNH BÁO TỒN KHO ===
Các mặt hàng sắp hết:
- SP002: Tập vở (còn 8 chiếc)
```

### Bài 3: Trò chơi Rắn săn mồi (Snake Game Logic)

Viết logic cơ bản cho game rắn săn mồi:

**Yêu cầu:**

1. Tạo bàn chơi 10x10 với tọa độ
2. Rắn bắt đầu tại vị trí (5,5) với độ dài 3
3. Tạo mồi ngẫu nhiên trên bàn chơi
4. Di chuyển rắn theo 4 hướng (W/A/S/D)
5. Kiểm tra va chạm với tường hoặc thân rắn
6. Khi ăn mồi: tăng độ dài, tạo mồi mới, tăng điểm
7. Game kết thúc khi va chạm

**Output mẫu:**

```
=== SNAKE GAME ===
Điểm: 0 | Độ dài rắn: 3

  0 1 2 3 4 5 6 7 8 9
0 . . . . . . . . . .
1 . . . . . . . . . .
2 . . . . . . . . . .
3 . . . . . F . . . .  <- F: Food (mồi)
4 . . . . . . . . . .
5 . . . S S S . . . .  <- S: Snake (rắn)
6 . . . . . . . . . .
7 . . . . . . . . . .
8 . . . . . . . . . .
9 . . . . . . . . . .

Nhập hướng di chuyển (W/A/S/D): W

Điểm: 0 | Độ dài rắn: 3

  0 1 2 3 4 5 6 7 8 9
0 . . . . . . . . . .
1 . . . . . . . . . .
2 . . . . . . . . . .
3 . . . . . F . . . .
4 . . . . . S . . . .  <- Rắn di chuyển lên
5 . . . . . S . . . .
6 . . . . . S . . . .
7 . . . . . . . . . .
8 . . . . . . . . . .
9 . . . . . . . . . .
```

### Bài 4: Thuật toán sắp xếp và tìm kiếm

Implement các thuật toán cơ bản:

**Yêu cầu:**

1. Bubble Sort: sắp xếp mảng bằng bubble sort
2. Selection Sort: sắp xếp bằng selection sort
3. Linear Search: tìm kiếm tuyến tính
4. Binary Search: tìm kiếm nhị phân (mảng đã sắp xếp)
5. So sánh hiệu suất các thuật toán
6. Hiển thị từng bước thực hiện

**Input mẫu:**

```python
numbers = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
search_value = 22
```

**Output mẫu:**

```
=== THUẬT TOÁN SẮP XẾP VÀ TÌM KIẾM ===

Mảng ban đầu: [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]

=== BUBBLE SORT ===
Bước 1: [34, 25, 12, 22, 11, 64, 88, 76, 50, 42, 90]
Bước 2: [25, 12, 22, 11, 34, 64, 76, 50, 42, 88, 90]
...
Kết quả: [11, 12, 22, 25, 34, 42, 50, 64, 76, 88, 90]
Số lần so sánh: 45

=== SELECTION SORT ===
Bước 1: [11, 34, 25, 12, 22, 64, 90, 88, 76, 50, 42]
Bước 2: [11, 12, 25, 34, 22, 64, 90, 88, 76, 50, 42]
...
Kết quả: [11, 12, 22, 25, 34, 42, 50, 64, 76, 88, 90]
Số lần so sánh: 55

=== TÌM KIẾM ===
Tìm số 22:
- Linear Search: Tìm thấy tại vị trí 2 (3 lần so sánh)
- Binary Search: Tìm thấy tại vị trí 2 (2 lần so sánh)
```

### Bài 5: Máy ATM mô phỏng

Viết chương trình mô phỏng máy ATM:

**Yêu cầu:**

1. Đăng nhập với PIN (3 lần thử)
2. Menu: Kiểm tra số dư, Rút tiền, Gửi tiền, Chuyển khoản, Đổi PIN, Thoát
3. Kiểm tra số dư tài khoản
4. Rút tiền: kiểm tra số dư, mệnh giá tiền
5. Gửi tiền: cập nhật số dư
6. Chuyển khoản: kiểm tra tài khoản đích
7. Đổi PIN: xác nhận PIN cũ
8. Ghi log giao dịch

**Output mẫu:**

```
=== CHÀO MỪNG ĐẾN ATM TECHBANK ===

Nhập số thẻ: 1234567890
Nhập mã PIN: ****

Đăng nhập thành công!
Xin chào, Nguyễn Văn A

MENU CHÍNH:
1. Kiểm tra số dư
2. Rút tiền
3. Gửi tiền
4. Chuyển khoản
5. Đổi mã PIN
6. Lịch sử giao dịch
7. Thoát

Lựa chọn: 2

=== RÚT TIỀN ===
Số dư hiện tại: 2,500,000 VNĐ

Chọn mệnh giá:
1. 100,000 VNĐ
2. 200,000 VNĐ
3. 500,000 VNĐ
4. 1,000,000 VNĐ
5. Nhập số tiền khác

Lựa chọn: 3

Bạn đã rút 500,000 VNĐ
Số dư còn lại: 2,000,000 VNĐ
Cảm ơn bạn đã sử dụng dịch vụ!

[2024-03-15 14:30:25] Rút tiền: -500,000 VNĐ
```

## Hướng dẫn giải

### Tips cho Control Flow:

- Sử dụng `break` để thoát khỏi vòng lặp
- Sử dụng `continue` để bỏ qua iteration hiện tại
- Nested loops cho các bài toán 2D (matrix, game board)
- `while True:` cho menu chương trình
- `for...else:` để xử lý khi không tìm thấy

### Pattern thường dùng:

```python
# Menu loop
while True:
    choice = input("Lựa chọn: ")
    if choice == "0":
        break
    elif choice == "1":
        # xử lý
    else:
        print("Lựa chọn không hợp lệ")

# Validation loop
while True:
    value = input("Nhập giá trị: ")
    if validate(value):
        break
    print("Giá trị không hợp lệ, thử lại!")
```

## Tiêu chí đánh giá

- [ ] Sử dụng đúng cấu trúc điều khiển
- [ ] Logic xử lý chính xác
- [ ] Xử lý input validation
- [ ] Code dễ đọc, có comment
- [ ] Không có infinite loop
- [ ] Xử lý edge cases
- [ ] Performance tốt cho thuật toán
