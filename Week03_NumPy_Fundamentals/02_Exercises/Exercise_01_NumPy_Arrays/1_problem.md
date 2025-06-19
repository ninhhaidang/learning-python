# Exercise 01: NumPy Arrays

## Mục tiêu

- Nắm vững cách tạo và thao tác với NumPy arrays
- Hiểu các thuộc tính cơ bản của arrays (shape, dtype, size)
- Thực hành indexing và slicing với arrays đa chiều
- Làm quen với các phép biến đổi shape cơ bản

## Bài tập

### Bài 1: Tạo và Phân tích Dữ liệu Nhiệt độ

Bạn là nhà khí tượng học và cần phân tích dữ liệu nhiệt độ của một thành phố trong 30 ngày qua.

**Yêu cầu:**

1. Tạo array chứa dữ liệu nhiệt độ ngẫu nhiên từ 18°C đến 35°C cho 30 ngày
2. Tìm ngày có nhiệt độ cao nhất và thấp nhất
3. Tính nhiệt độ trung bình, độ lệch chuẩn
4. Đếm số ngày có nhiệt độ trên 30°C
5. Tạo array boolean mask cho các ngày nóng (>30°C) và mát (<22°C)

**Input mẫu:**

```python
import numpy as np
np.random.seed(42)  # Để có kết quả reproducible
# Tạo dữ liệu nhiệt độ ở đây
```

**Output mẫu:**

```
Dữ liệu nhiệt độ 30 ngày: [23.4 28.1 31.2 ...]
Nhiệt độ cao nhất: 34.8°C (ngày 15)
Nhiệt độ thấp nhất: 18.3°C (ngày 7)
Nhiệt độ trung bình: 26.7°C
Độ lệch chuẩn: 4.2°C
Số ngày nóng (>30°C): 8 ngày
Ngày nóng: [False False True False ...]
Ngày mát: [True False False True ...]
```

### Bài 2: Ma trận Điểm Thi

Tạo và phân tích ma trận điểm thi của lớp học với 20 học sinh và 5 môn học.

**Yêu cầu:**

1. Tạo ma trận điểm ngẫu nhiên (0-100) kích thước 20x5
2. Tính điểm trung bình của mỗi học sinh
3. Tính điểm trung bình của mỗi môn học
4. Tìm học sinh có điểm trung bình cao nhất
5. Tìm môn học có điểm trung bình thấp nhất
6. Đếm số học sinh đạt điểm trung bình >= 80

**Input mẫu:**

```python
scores = np.random.randint(0, 101, (20, 5))
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
```

**Output mẫu:**

```
Ma trận điểm (20 học sinh x 5 môn):
[[85 92 78 81 88]
 [76 85 92 79 83]
 ...]

Điểm TB mỗi học sinh: [84.8 83.0 ...]
Điểm TB mỗi môn: [82.3 78.9 85.1 80.2 79.8]
Học sinh xuất sắc nhất: Học sinh #3 (TB: 89.2)
Môn khó nhất: Physics (TB: 78.9)
Số học sinh giỏi (TB >= 80): 12/20
```

### Bài 3: Xử lý Dữ liệu Hình ảnh Đơn giản

Mô phỏng xử lý một "ảnh" grayscale đơn giản.

**Yêu cầu:**

1. Tạo ma trận 10x10 đại diện cho ảnh grayscale (giá trị 0-255)
2. Áp dụng threshold: pixel > 128 = 255, ngược lại = 0
3. Tính histogram đơn giản (đếm số pixel ở các khoảng giá trị)
4. Tìm vùng sáng nhất (max 3x3 region)
5. Flip ảnh theo chiều ngang và dọc

**Input mẫu:**

```python
image = np.random.randint(0, 256, (10, 10))
```

**Output mẫu:**

```
Ảnh gốc (10x10):
[[123 234  56  78 ...]
 [ 45 198 167 234 ...]
 ...]

Ảnh sau threshold:
[[  0 255   0   0 ...]
 [  0 255 255 255 ...]
 ...]

Histogram:
[0-63]: 28 pixels
[64-127]: 23 pixels
[128-191]: 25 pixels
[192-255]: 24 pixels

Vùng sáng nhất tại (2,3): trung bình 201.2
Ảnh flip ngang: ...
Ảnh flip dọc: ...
```

## Hướng dẫn giải

### Tips cho Bài 1:

- Sử dụng `np.random.uniform(low, high, size)` để tạo nhiệt độ
- `np.argmax()` và `np.argmin()` để tìm vị trí min/max
- Boolean indexing: `temperatures > 30` tạo mask
- `np.sum(mask)` để đếm số True trong mask

### Tips cho Bài 2:

- `np.mean(axis=0)` tính trung bình theo cột (môn học)
- `np.mean(axis=1)` tính trung bình theo hàng (học sinh)
- Sử dụng indexing với argmax/argmin để lấy tên

### Tips cho Bài 3:

- `np.where(condition, value_if_true, value_if_false)` cho threshold
- Sử dụng slicing để tạo sliding window 3x3
- `np.flip()` hoặc slicing `[::-1]` để flip

## Tiêu chí đánh giá

- [ ] Tạo arrays với đúng kích thước và kiểu dữ liệu
- [ ] Sử dụng đúng các hàm NumPy cơ bản (mean, max, min, argmax, argmin)
- [ ] Áp dụng Boolean indexing và masking chính xác
- [ ] Code clean, có comment giải thích
- [ ] Kết quả đầu ra đúng format yêu cầu
- [ ] Xử lý edge cases (nếu có)
- [ ] Hiểu và giải thích được ý nghĩa của kết quả
