# Exercise 02: Dictionaries and Sets

## Mục tiêu

- Làm quen với dictionaries và sets trong Python
- Học cách tạo, truy cập và thao tác với dictionary
- Hiểu về sets và các phép toán tập hợp
- Ứng dụng dictionary và sets trong bài toán thực tế

## Bài tập

### Bài 1: Quản lý thông tin sinh viên (Dictionary)

Viết chương trình quản lý thông tin sinh viên sử dụng dictionary:

**Yêu cầu:**

1. Tạo dictionary chứa thông tin 3 sinh viên với các thông tin: mã SV, họ tên, tuổi, điểm trung bình
2. In ra thông tin tất cả sinh viên
3. Tìm và in thông tin sinh viên có điểm cao nhất
4. Thêm một sinh viên mới
5. Cập nhật điểm của một sinh viên theo mã SV
6. Xóa sinh viên có điểm thấp nhất

**Input mẫu:**

```
Dữ liệu ban đầu:
- SV001: Nguyễn Văn A, 20 tuổi, điểm: 8.5
- SV002: Trần Thị B, 19 tuổi, điểm: 7.2
- SV003: Lê Văn C, 21 tuổi, điểm: 9.1

Thêm sinh viên: SV004: Phạm Thị D, 20 tuổi, điểm: 8.8
Cập nhật điểm SV002: 8.0
```

**Output mẫu:**

```
=== THÔNG TIN TẤT CẢ SINH VIÊN ===
SV001: Nguyễn Văn A - Tuổi: 20 - Điểm: 8.5
SV002: Trần Thị B - Tuổi: 19 - Điểm: 7.2
SV003: Lê Văn C - Tuổi: 21 - Điểm: 9.1

=== SINH VIÊN CÓ ĐIỂM CAO NHẤT ===
SV003: Lê Văn C - Điểm: 9.1

=== SAU KHI THÊM SINH VIÊN MỚI ===
Đã thêm SV004: Phạm Thị D

=== SAU KHI CẬP NHẬT ĐIỂM ===
Đã cập nhật điểm SV002 thành 8.0

=== SAU KHI XÓA SINH VIÊN ĐIỂM THẤP NHẤT ===
Đã xóa SV002: Trần Thị B
```

### Bài 2: Phân tích dữ liệu bán hàng (Dictionary nâng cao)

Viết chương trình phân tích dữ liệu bán hàng của một cửa hàng:

**Yêu cầu:**

1. Tạo dictionary chứa thông tin bán hàng theo tháng
2. Tính tổng doanh thu cả năm
3. Tìm tháng có doanh thu cao nhất và thấp nhất
4. Tính doanh thu trung bình mỗi tháng
5. Liệt kê các tháng có doanh thu trên 50 triệu

**Input mẫu:**

```python
sales_data = {
    "Tháng 1": 45000000,
    "Tháng 2": 52000000,
    "Tháng 3": 48000000,
    "Tháng 4": 61000000,
    "Tháng 5": 58000000,
    "Tháng 6": 67000000,
    "Tháng 7": 72000000,
    "Tháng 8": 69000000,
    "Tháng 9": 55000000,
    "Tháng 10": 63000000,
    "Tháng 11": 71000000,
    "Tháng 12": 75000000
}
```

**Output mẫu:**

```
=== PHÂN TÍCH DOANH THU NĂM 2024 ===
Tổng doanh thu cả năm: 736,000,000 VNĐ
Doanh thu trung bình/tháng: 61,333,333 VNĐ

Tháng có doanh thu cao nhất: Tháng 12 (75,000,000 VNĐ)
Tháng có doanh thu thấp nhất: Tháng 1 (45,000,000 VNĐ)

Các tháng có doanh thu trên 50 triệu:
- Tháng 2: 52,000,000 VNĐ
- Tháng 4: 61,000,000 VNĐ
- Tháng 5: 58,000,000 VNĐ
- Tháng 6: 67,000,000 VNĐ
- Tháng 7: 72,000,000 VNĐ
- Tháng 8: 69,000,000 VNĐ
- Tháng 9: 55,000,000 VNĐ
- Tháng 10: 63,000,000 VNĐ
- Tháng 11: 71,000,000 VNĐ
- Tháng 12: 75,000,000 VNĐ
```

### Bài 3: Thao tác với Sets (Tập hợp)

Viết chương trình thực hiện các phép toán tập hợp:

**Yêu cầu:**

1. Tạo 3 sets: học sinh lớp A, lớp B, lớp C
2. Tìm học sinh có ở cả 3 lớp (giao của 3 tập hợp)
3. Tìm học sinh chỉ có ở lớp A (không có ở B và C)
4. Tìm tổng số học sinh khác nhau trong 3 lớp
5. Tìm học sinh có ở lớp A hoặc B nhưng không có ở lớp C

**Input mẫu:**

```python
class_a = {"An", "Bình", "Chi", "Dũng", "Em", "Giang"}
class_b = {"Bình", "Chi", "Hoa", "Khoa", "Linh", "An"}
class_c = {"Chi", "Dũng", "Hoa", "Nam", "Oanh", "Bình"}
```

**Output mẫu:**

```
=== THÔNG TIN CÁC LỚP ===
Lớp A: {'An', 'Bình', 'Chi', 'Dũng', 'Em', 'Giang'}
Lớp B: {'An', 'Bình', 'Chi', 'Hoa', 'Khoa', 'Linh'}
Lớp C: {'Bình', 'Chi', 'Dũng', 'Hoa', 'Nam', 'Oanh'}

=== PHÂN TÍCH TẬP HỢP ===
Học sinh có ở cả 3 lớp: {'Bình', 'Chi'}
Học sinh chỉ có ở lớp A: {'Em', 'Giang'}
Tổng số học sinh khác nhau: 10
Học sinh ở A hoặc B nhưng không ở C: {'An', 'Em', 'Giang', 'Khoa', 'Linh'}
```

### Bài 4: Đếm tần suất từ khóa

Viết chương trình đếm tần suất xuất hiện của các từ trong một đoạn văn:

**Yêu cầu:**

1. Nhập một đoạn văn bản
2. Tách các từ và đếm tần suất (không phân biệt hoa thường)
3. Loại bỏ các ký tự đặc biệt và số
4. Hiển thị top 5 từ xuất hiện nhiều nhất
5. Hiển thị các từ chỉ xuất hiện 1 lần

**Input mẫu:**

```
"Python là ngôn ngữ lập trình mạnh mẽ. Python dễ học và dễ sử dụng.
Với Python, bạn có thể phát triển ứng dụng web, mobile, AI và machine learning."
```

**Output mẫu:**

```
=== PHÂN TÍCH TẦN SUẤT TỪ KHÓA ===
Tổng số từ: 25
Số từ khác nhau: 22

Top 5 từ xuất hiện nhiều nhất:
1. python: 3 lần
2. dễ: 2 lần
3. và: 2 lần
4. là: 1 lần
5. ngôn: 1 lần

Các từ chỉ xuất hiện 1 lần:
là, ngôn, ngữ, lập, trình, mạnh, mẽ, học, sử, dụng, với, bạn, có, thể, phát, triển, ứng, dụng, web, mobile, ai, machine, learning
```

## Hướng dẫn giải

### Tips cho Dictionary:

- Sử dụng `dict.keys()`, `dict.values()`, `dict.items()` để duyệt
- Dùng `dict.get(key, default)` để tránh lỗi KeyError
- Sử dụng `max()`, `min()` với key function để tìm phần tử
- Dictionary comprehension: `{k: v for k, v in items}`

### Tips cho Sets:

- Phép giao: `set1 & set2` hoặc `set1.intersection(set2)`
- Phép hợp: `set1 | set2` hoặc `set1.union(set2)`
- Phép hiệu: `set1 - set2` hoặc `set1.difference(set2)`
- Phép hiệu đối xứng: `set1 ^ set2`

## Tiêu chí đánh giá

- [ ] Code chạy không lỗi
- [ ] Logic giải thuật đúng
- [ ] Xử lý input/output theo yêu cầu
- [ ] Code dễ đọc, có comment
- [ ] Sử dụng đúng methods của dict/set
- [ ] Xử lý edge cases (dict rỗng, key không tồn tại...)
