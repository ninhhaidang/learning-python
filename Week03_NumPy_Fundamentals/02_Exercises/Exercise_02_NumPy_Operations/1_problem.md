# Exercise 02: NumPy Operations

## Mục tiêu

- Thành thạo các phép toán cơ bản với NumPy arrays
- Hiểu và áp dụng broadcasting trong NumPy
- Sử dụng universal functions (ufuncs) hiệu quả
- Thực hành các phép toán thống kê và linear algebra cơ bản

## Bài tập

### Bài 1: Phân tích Dữ liệu Bán hàng

Một cửa hàng có dữ liệu bán hàng 4 quý, mỗi quý có 3 tháng.

**Yêu cầu:**

1. Tạo ma trận doanh thu 4x3 (4 quý x 3 tháng) với giá trị từ 50-200 triệu
2. Tính tổng doanh thu mỗi quý và mỗi tháng
3. Tính tăng trưởng theo quý (so với quý trước)
4. Áp dụng thuế 10% cho tất cả doanh thu
5. Tìm tháng có doanh thu cao nhất và thấp nhất trong năm
6. So sánh doanh thu với target (150 triệu/tháng)

**Input mẫu:**

```python
import numpy as np
np.random.seed(42)
revenue = np.random.uniform(50, 200, (4, 3))  # 4 quý x 3 tháng
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
months = ['T1', 'T2', 'T3']
```

**Output mẫu:**

```
Doanh thu theo quý (triệu VND):
      T1    T2    T3   Tổng
Q1  [137.8 152.8 196.9] 487.5
Q2  [151.3 174.5 165.2] 491.0
Q3  [183.4 159.7 172.8] 515.9
Q4  [168.2 145.6 189.4] 503.2

Tăng trưởng theo quý: [0.7%, 5.1%, -2.5%]
Sau thuế 10%: [[124.0 137.5 ...]]
Tháng cao nhất: Q1-T3 (196.9 triệu)
Tháng thấp nhất: Q4-T2 (145.6 triệu)
Target completion: 87.2% (39/48 tháng đạt target)
```

### Bài 2: Xử lý Dữ liệu Cảm biến

Phân tích dữ liệu từ 5 cảm biến nhiệt độ trong 24 giờ.

**Yêu cầu:**

1. Tạo dữ liệu 5 cảm biến x 24 giờ (15°C - 35°C)
2. Tính nhiệt độ trung bình theo giờ và theo cảm biến
3. Tìm correlation giữa các cảm biến
4. Chuẩn hóa dữ liệu (z-score normalization)
5. Tìm outliers (|z-score| > 2)
6. Smooth data bằng moving average window=3

**Input mẫu:**

```python
sensor_data = np.random.normal(25, 5, (5, 24))  # 5 sensors x 24 hours
sensor_names = [f'Sensor_{i+1}' for i in range(5)]
```

**Output mẫu:**

```
Dữ liệu cảm biến (5x24):
Sensor_1: [23.4 28.1 31.2 ...]
Sensor_2: [21.8 26.5 29.7 ...]
...

Nhiệt độ TB theo giờ: [24.8 27.3 30.1 ...]
Nhiệt độ TB theo cảm biến: [25.2 24.9 25.8 24.6 25.1]

Correlation matrix:
       S1   S2   S3   S4   S5
S1  [1.00 0.12 0.08 -0.05 0.15]
...

Outliers detected: 3 measurements
Sensor_2 at hour 15: z-score = 2.34
...

Smoothed data shape: (5, 22)
```

### Bài 3: Operações Vectoriais và Broadcasting

Thực hành broadcasting và vector operations.

**Yêu cầu:**

1. Tạo matrix A(3x4) và vector B(4,)
2. Thực hiện A + B, A \* B, A - B (broadcasting)
3. Tạo meshgrid 2D và tính khoảng cách Euclidean
4. Implement các hàm: normalize, standardize, min-max scaling
5. Tính cosine similarity giữa các vectors
6. Benchmark performance: NumPy vs Python loops

**Input mẫu:**

```python
A = np.random.random((3, 4))
B = np.random.random(4)
points = np.random.random((100, 2))  # 100 điểm 2D
```

**Output mẫu:**

```
Matrix A (3x4):
[[0.37 0.95 0.73 0.60]
 [0.16 0.06 0.87 0.60]
 [0.71 0.02 0.97 0.83]]

Vector B (4,): [0.21 0.18 0.30 0.52]

Broadcasting results:
A + B: [[0.58 1.13 1.03 1.12] ...]
A * B: [[0.08 0.17 0.22 0.31] ...]
A - B: [[0.16 0.77 0.43 0.08] ...]

Distance matrix (100x100): computed
Normalized vectors: L2 norm = 1.0
Standardized: mean=0, std=1
Min-max scaled: range [0,1]

Cosine similarity matrix (3x3):
[[1.00 0.87 0.62]
 [0.87 1.00 0.45]
 [0.62 0.45 1.00]]

Performance:
NumPy operations: 0.0123s
Python loops: 0.1456s
Speedup: 11.8x
```

## Hướng dẫn giải

### Tips cho Bài 1:

- `np.sum(axis=0)` để tính tổng theo cột (tháng)
- `np.sum(axis=1)` để tính tổng theo hàng (quý)
- `np.diff()` hoặc manual calculation cho growth rate
- Broadcasting: `revenue * 0.9` áp dụng thuế
- `np.unravel_index()` để tìm vị trí max/min trong 2D array

### Tips cho Bài 2:

- `np.corrcoef()` để tính correlation matrix
- Z-score: `(data - mean) / std`
- `np.abs(z_scores) > 2` để tìm outliers
- Moving average: `np.convolve()` hoặc manual sliding window
- `np.where()` để tìm vị trí outliers

### Tips cho Bài 3:

- Broadcasting tự động work với compatible shapes
- `np.meshgrid()` tạo coordinate grid
- `np.linalg.norm()` cho vector normalization
- Cosine similarity: `dot(a,b) / (norm(a) * norm(b))`
- `time.time()` để benchmark performance

## Tiêu chí đánh giá

- [ ] Sử dụng đúng các phép toán NumPy (element-wise, reduction)
- [ ] Hiểu và áp dụng broadcasting chính xác
- [ ] Thực hiện được các phép toán thống kê cơ bản
- [ ] Code hiệu quả, tránh loops không cần thiết
- [ ] Xử lý được dữ liệu đa chiều
- [ ] Giải thích được ý nghĩa của kết quả
- [ ] Format output rõ ràng và dễ đọc
- [ ] Có validation và error handling cơ bản
