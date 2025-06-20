# Exercise 02: Grade Matrix Analysis

## 🎯 Mục tiêu

- Thực hành tạo và thao tác với ma trận 2D trong NumPy
- Học cách tính toán thống kê theo axis (hàng/cột)
- Sử dụng argmax/argmin để tìm vị trí cực trị
- Áp dụng Boolean indexing trong phân tích điểm số

## 📋 Đề bài: Ma trận Điểm Thi

Tạo và phân tích ma trận điểm thi của lớp học với 20 học sinh và 5 môn học.

### Yêu cầu:

1. **Tạo ma trận điểm** ngẫu nhiên (0-100) kích thước 20x5
2. **Phân tích theo học sinh**: tính điểm trung bình của mỗi học sinh
3. **Phân tích theo môn học**: tính điểm trung bình của mỗi môn
4. **Tìm học sinh xuất sắc**: học sinh có điểm trung bình cao nhất
5. **Tìm môn khó nhất**: môn học có điểm trung bình thấp nhất
6. **Phân loại học sinh**: đếm số học sinh đạt điểm trung bình >= 80

### Input mẫu:

```python
import numpy as np
np.random.seed(42)
scores = np.random.randint(0, 101, (20, 5))
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
```

### Expected Output:

```
=== PHÂN TÍCH MA TRẬN ĐIỂM THI ===

Ma trận điểm (20 học sinh x 5 môn):
[[85 92 78 81 88]
 [76 85 92 79 83]
 [91 73 84 88 76]
 ...]

📊 THỐNG KÊ THEO HỌC SINH:
Học sinh #1: 84.8 điểm
Học sinh #2: 83.0 điểm
Học sinh #3: 82.4 điểm
...

📚 THỐNG KÊ THEO MÔN HỌC:
Math: 82.3 điểm
Physics: 78.9 điểm
Chemistry: 85.1 điểm
Biology: 80.2 điểm
English: 79.8 điểm

🏆 THÔNG TIN NỔI BẬT:
- Học sinh xuất sắc nhất: Học sinh #7 (TB: 89.2 điểm)
- Môn khó nhất: Physics (TB: 78.9 điểm)
- Môn dễ nhất: Chemistry (TB: 85.1 điểm)

📈 PHÂN LOẠI HỌC SINH:
- Số học sinh giỏi (TB >= 80): 12/20 học sinh
- Tỷ lệ đạt: 60.0%
```

## 💡 Hướng dẫn

### Các hàm NumPy cần sử dụng:

- `np.random.randint(low, high, size)` - tạo số nguyên ngẫu nhiên
- `np.mean(axis=0)` - tính trung bình theo cột (môn học)
- `np.mean(axis=1)` - tính trung bình theo hàng (học sinh)
- `np.argmax()`, `np.argmin()` - tìm vị trí max/min
- Boolean indexing: `array >= threshold`

### Gợi ý thực hiện:

1. Tạo ma trận điểm bằng `np.random.randint()`
2. Dùng `axis=1` để tính TB theo học sinh, `axis=0` cho môn học
3. Sử dụng `np.argmax()` để tìm học sinh giỏi nhất
4. Tạo Boolean mask để đếm học sinh giỏi
5. Format output có thứ tự, dễ đọc

## ✅ Tiêu chí đánh giá

- [ ] Tạo đúng ma trận 20x5 với điểm 0-100
- [ ] Tính toán thống kê theo đúng axis (học sinh/môn học)
- [ ] Tìm đúng vị trí và giá trị cực trị
- [ ] Sử dụng Boolean indexing để phân loại
- [ ] Output format có cấu trúc, thông tin đầy đủ
- [ ] Code có comment và dễ hiểu
