# Exercise 06: String Manipulation

## Mô tả bài tập

Học cách thao tác với chuỗi trong Python: tạo chuỗi, nối chuỗi, định dạng, và sử dụng các phương thức chuỗi cơ bản.

## Yêu cầu

Thực hiện các nhiệm vụ sau trong file `practice.py`:

### Phần 1: Tạo và nối chuỗi

1. Tạo biến `first_name` = "Nguyen"
2. Tạo biến `last_name` = "Van A"
3. Tạo `full_name` bằng cách nối `first_name` + " " + `last_name`
4. Tạo `greeting` = "Xin chào, " + `full_name` + "!"

### Phần 2: Định dạng chuỗi

5. Tạo `age` = 20
6. Sử dụng f-string để tạo `intro` = "Tôi tên {full_name}, {age} tuổi"
7. Sử dụng `.format()` để tạo cùng chuỗi trên
8. Sử dụng % formatting (cách cũ) để tạo cùng chuỗi trên

### Phần 3: Phương thức chuỗi cơ bản

9. Chuyển `full_name` thành chữ hoa (upper)
10. Chuyển `full_name` thành chữ thường (lower)
11. Chuyển `full_name` thành title case (mỗi từ viết hoa chữ đầu)
12. Đếm số ký tự trong `full_name`
13. Kiểm tra xem `full_name` có chứa "Van" không

### Phần 4: Xử lý khoảng trắng

14. Tạo `messy_string` = " Hello World "
15. Loại bỏ khoảng trắng đầu và cuối (.strip())
16. Loại bỏ chỉ khoảng trắng bên trái (.lstrip())
17. Loại bỏ chỉ khoảng trắng bên phải (.rstrip())

### Phần 5: Chia và thay thế chuỗi

18. Chia `full_name` thành danh sách các từ (.split())
19. Thay thế "Nguyen" thành "Mr. Nguyen" trong `full_name`
20. Tạo chuỗi từ danh sách với .join()

### Phần 6: Kiểm tra chuỗi

21. Kiểm tra xem chuỗi có bắt đầu bằng "Nguyen" không
22. Kiểm tra xem chuỗi có kết thúc bằng "A" không
23. Kiểm tra xem chuỗi có phải toàn bộ là chữ cái không
24. Kiểm tra xem chuỗi có phải toàn bộ là số không

## Đầu ra mong đợi

```
=== TẠO VÀ NỐI CHUỖI ===
Tên: Nguyen
Họ: Van A
Họ tên đầy đủ: Nguyen Van A
Lời chào: Xin chào, Nguyen Van A!

=== ĐỊNH DẠNG CHUỖI ===
F-string: Tôi tên Nguyen Van A, 20 tuổi
Format method: Tôi tên Nguyen Van A, 20 tuổi
% formatting: Tôi tên Nguyen Van A, 20 tuổi

=== PHƯƠNG THỨC CHUỖI ===
Chữ hoa: NGUYEN VAN A
Chữ thường: nguyen van a
Title case: Nguyen Van A
Số ký tự: 11
Chứa 'Van': True

=== XỬ LÝ KHOẢNG TRẮNG ===
Gốc: "   Hello World   "
Strip: "Hello World"
Lstrip: "Hello World   "
Rstrip: "   Hello World"

=== CHIA VÀ THAY THẾ ===
Chia thành từ: ['Nguyen', 'Van', 'A']
Thay thế: Mr. Nguyen Van A
Join lại: Nguyen-Van-A

=== KIỂM TRA CHUỖI ===
Bắt đầu bằng 'Nguyen': True
Kết thúc bằng 'A': True
Toàn chữ cái: False (có khoảng trắng)
Toàn số: False
```

## Kiến thức cần nắm

- Cách nối chuỗi (+, f-string, format, %)
- Các phương thức chuỗi: upper, lower, title, strip, split, replace, join
- Các phương thức kiểm tra: startswith, endswith, isalpha, isdigit
- Indexing và slicing chuỗi

## Mức độ khó: ⭐⭐☆☆☆
