# Exercise 06: Broadcasting Operations

## 🎯 Mục tiêu

- Hiểu và áp dụng broadcasting rules trong NumPy
- Thực hành vectorization để tối ưu hóa performance
- Sử dụng broadcasting cho các phép toán ma trận
- So sánh hiệu suất giữa loop và vectorized operations

## 📋 Đề bài: Broadcasting và Vectorization

Áp dụng broadcasting để thực hiện các phép toán hiệu quả trên arrays có shape khác nhau.

### Yêu cầu:

1. **Tạo data arrays** với các shape khác nhau
2. **Áp dụng broadcasting** để thực hiện phép toán element-wise
3. **Normalize data** bằng broadcasting (subtract mean, divide by std)
4. **Distance matrix** tính khoảng cách giữa các điểm
5. **Performance comparison** giữa loop và vectorized operations

### Input mẫu:

```python
import numpy as np
np.random.seed(42)
# Arrays with different shapes for broadcasting
matrix_2d = np.random.randint(1, 10, (4, 5))
vector_1d = np.random.randint(1, 5, 5)
scalar = 2
```

### Expected Output:

```
=== BROADCASTING & VECTORIZATION ===

Original 2D Matrix (4x5):
[[7 4 6 9 2]
 [6 7 4 4 7]
 [9 8 1 5 3]
 [8 1 5 9 8]]

1D Vector (5,):
[4 1 3 2 1]

Scalar: 2

🔢 BROADCASTING OPERATIONS:

1. Matrix + Vector (4x5 + 5):
[[11  5  9 11  3]
 [10  8  7  6  8]
 [13  9  4  7  4]
 [12  2  8 11  9]]

2. Matrix * Scalar (4x5 * scalar):
[[14  8 12 18  4]
 [12 14  8  8 14]
 [18 16  2 10  6]
 [16  2 10 18 16]]

📊 NORMALIZATION (Z-score):
Original mean: 5.4, std: 2.8
Normalized matrix:
[[ 0.57 -0.50  0.21  1.29 -1.21]
 [ 0.21  0.57 -0.50 -0.50  0.57]
 [ 1.29  0.93 -1.57 -0.14 -1.07]
 [ 0.93 -1.57 -0.14  1.29  0.93]]

🎯 DISTANCE MATRIX:
Points shape: (3, 2)
Distance matrix (3x3):
[[ 0.    2.83  4.47]
 [ 2.83  0.    3.16]
 [ 4.47  3.16  0.  ]]

⚡ PERFORMANCE COMPARISON:
Loop method: 0.0045 seconds
Vectorized method: 0.0003 seconds
Speedup: 15.0x faster
```

## 💡 Hướng dẫn

### Broadcasting Rules:

1. Arrays are aligned from the trailing dimension
2. Dimensions of size 1 can be broadcast
3. Missing dimensions are assumed to be size 1

### Các kỹ thuật cần sử dụng:

- `np.newaxis` hoặc `[:, np.newaxis]` để thêm dimension
- `np.subtract()`, `np.divide()` với broadcasting
- `np.linalg.norm()` cho distance calculation
- `time.time()` để đo performance

### Gợi ý thực hiện:

1. Test broadcasting rules với arrays shape khác nhau
2. Sử dụng `(data - mean) / std` pattern cho normalization
3. Dùng broadcasting để tính distance matrix hiệu quả
4. So sánh loop vs vectorized bằng timing

## ✅ Tiêu chí đánh giá

- [ ] Hiểu và áp dụng đúng broadcasting rules
- [ ] Thực hiện normalization bằng broadcasting
- [ ] Tính distance matrix hiệu quả
- [ ] So sánh performance loop vs vectorized
- [ ] Code clean, có comment giải thích broadcasting logic
- [ ] Output format rõ ràng, dễ hiểu
