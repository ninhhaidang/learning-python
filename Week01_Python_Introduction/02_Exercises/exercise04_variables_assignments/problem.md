# Exercise 04: Variables & Assignments

## Mô tả bài tập

Học cách khai báo, gán giá trị và sử dụng biến trong Python. Hiểu về quy tắc đặt tên biến và các loại gán giá trị khác nhau.

## Yêu cầu

Thực hiện các nhiệm vụ sau trong file `practice.py`:

### Phần 1: Khai báo biến cơ bản

1. Tạo biến `student_name` và gán tên của bạn
2. Tạo biến `age` và gán tuổi của bạn
3. Tạo biến `height` và gán chiều cao của bạn (đơn vị: cm)
4. Tạo biến `is_student` và gán giá trị `True`

### Phần 2: Gán giá trị từ biến khác

5. Tạo biến `birth_year` = năm hiện tại (2024) - tuổi
6. Tạo biến `height_in_meters` = chiều cao / 100
7. Tạo biến `full_info` = kết hợp tên và tuổi thành một chuỗi

### Phần 3: Gán nhiều biến cùng lúc

8. Gán `x, y, z = 10, 20, 30` trên một dòng
9. Gán `a = b = c = 100` (cùng giá trị)
10. Hoán đổi giá trị: `num1 = 5, num2 = 10`, sau đó hoán đổi chúng

### Phần 4: In kết quả

11. In tất cả các biến đã tạo với định dạng đẹp
12. In loại dữ liệu của từng biến
13. In địa chỉ bộ nhớ của các biến số

## Đầu ra mong đợi

```
=== THÔNG TIN CÁ NHÂN ===
Tên: [Tên của bạn]
Tuổi: [Tuổi] năm
Chiều cao: [Chiều cao] cm ([Chiều cao/100] m)
Năm sinh: [Năm sinh]
Là sinh viên: True
Thông tin đầy đủ: [Tên] - [Tuổi] tuổi

=== CÁC BIẾN SỐ ===
x = 10, y = 20, z = 30
a = b = c = 100

=== HOÁN ĐỔI GIÁ TRỊ ===
Trước: num1 = 5, num2 = 10
Sau: num1 = 10, num2 = 5

=== THÔNG TIN KỸ THUẬT ===
Kiểu dữ liệu:
- student_name: <class 'str'>
- age: <class 'int'>
- height: <class 'int'>
...
```

## Kiến thức cần nắm

- Quy tắc đặt tên biến trong Python
- Các cách gán giá trị cho biến
- Hàm `type()` để kiểm tra kiểu dữ liệu
- Hàm `id()` để xem địa chỉ bộ nhớ
- Kỹ thuật hoán đổi giá trị

## Mức độ khó: ⭐⭐☆☆☆
