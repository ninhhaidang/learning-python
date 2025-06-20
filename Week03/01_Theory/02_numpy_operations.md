# 02. NumPy Mathematical Operations

## 🎯 Mục tiêu học tập

Sau khi hoàn thành chương này, bạn sẽ:

- Thực hiện các phép toán cơ bản với NumPy arrays
- Hiểu về broadcasting trong NumPy
- Sử dụng universal functions (ufuncs)
- Thực hiện phép toán thống kê trên arrays
- Làm việc với linear algebra operations

## 🧮 Arithmetic Operations

### Phép toán cơ bản

```python
import numpy as np

# Tạo arrays để demo
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Cộng, trừ, nhân, chia
print(a + b)   # [11 22 33 44]
print(a - b)   # [-9 -18 -27 -36]
print(a * b)   # [10 40 90 160]
print(a / b)   # [0.1 0.1 0.1 0.1]

# Phép toán với scalar
print(a + 5)   # [6 7 8 9]
print(a * 2)   # [2 4 6 8]
print(a ** 2)  # [1 4 9 16] (lũy thừa)

# Phép chia lấy nguyên và lấy dư
print(b // a)  # [10 10 10 10]
print(b % a)   # [0 0 0 0]
```

### Phép toán với 2D arrays

```python
# Arrays 2D
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Element-wise operations
print("Addition:")
print(matrix_a + matrix_b)
# [[ 6  8]
#  [10 12]]

print("Multiplication (element-wise):")
print(matrix_a * matrix_b)
# [[ 5 12]
#  [21 32]]

# Matrix multiplication
print("Matrix multiplication:")
print(matrix_a @ matrix_b)  # hoặc np.dot(matrix_a, matrix_b)
# [[19 22]
#  [43 50]]
```

## 📡 Broadcasting

Broadcasting cho phép NumPy thực hiện phép toán trên arrays có shape khác nhau.

### Quy tắc Broadcasting

1. Bắt đầu từ trailing dimension (dimension cuối)
2. Hai dimensions tương thích nếu:
   - Chúng bằng nhau
   - Một trong hai bằng 1

```python
# Broadcasting examples
a = np.array([[1, 2, 3],
              [4, 5, 6]])  # Shape: (2, 3)

b = np.array([10, 20, 30])  # Shape: (3,)

result = a + b  # Broadcasting: (2, 3) + (3,) -> (2, 3)
print(result)
# [[11 22 33]
#  [14 25 36]]

# Broadcasting với scalar
scalar = 5
result = a + scalar  # (2, 3) + scalar -> (2, 3)
print(result)
# [[ 6  7  8]
#  [ 9 10 11]]

# Broadcasting với column vector
c = np.array([[10],
              [20]])  # Shape: (2, 1)

result = a + c  # (2, 3) + (2, 1) -> (2, 3)
print(result)
# [[11 12 13]
#  [24 25 26]]
```

### Broadcasting không thể thực hiện

```python
# Ví dụ về broadcasting lỗi
try:
    a = np.array([[1, 2, 3]])     # (1, 3)
    b = np.array([[1], [2]])      # (2, 1)
    result = a + b                # (1, 3) + (2, 1) -> Error!
except ValueError as e:
    print(f"Broadcasting error: {e}")
```

## 🔢 Universal Functions (ufuncs)

Universal functions là các hàm hoạt động element-wise trên arrays.

### Mathematical ufuncs

```python
arr = np.array([1, 4, 9, 16, 25])

# Square root
print(np.sqrt(arr))  # [1. 2. 3. 4. 5.]

# Exponential và logarithm
print(np.exp(arr))      # e^x
print(np.log(arr))      # ln(x)
print(np.log10(arr))    # log10(x)
print(np.log2(arr))     # log2(x)

# Trigonometric functions
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(np.sin(angles))
print(np.cos(angles))
print(np.tan(angles))

# Inverse trigonometric
print(np.arcsin([0, 0.5, 1]))
print(np.arccos([1, 0.5, 0]))

# Hyperbolic functions
print(np.sinh(arr))
print(np.cosh(arr))
print(np.tanh(arr))
```

### Comparison ufuncs

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 4, 2, 4, 6])

# Element-wise comparison
print(np.equal(a, b))       # [True False False True False]
print(np.greater(a, b))     # [False False True False False]
print(np.less_equal(a, b))  # [True True False True True]

# Hoặc sử dụng operators
print(a == b)  # [True False False True False]
print(a > b)   # [False False True False False]
print(a <= b)  # [True True False True True]
```

### Logical ufuncs

```python
bool_arr1 = np.array([True, False, True, False])
bool_arr2 = np.array([True, True, False, False])

print(np.logical_and(bool_arr1, bool_arr2))  # [True False False False]
print(np.logical_or(bool_arr1, bool_arr2))   # [True True True False]
print(np.logical_not(bool_arr1))             # [False True False True]
print(np.logical_xor(bool_arr1, bool_arr2))  # [False True True False]
```

## 📊 Statistical Functions

### Aggregation functions

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Tổng các phần tử
print(np.sum(arr))        # 45
print(np.sum(arr, axis=0))  # [12 15 18] (tổng theo cột)
print(np.sum(arr, axis=1))  # [ 6 15 24] (tổng theo hàng)

# Trung bình
print(np.mean(arr))         # 5.0
print(np.mean(arr, axis=0)) # [4. 5. 6.]

# Median
print(np.median(arr))       # 5.0

# Min, Max
print(np.min(arr))          # 1
print(np.max(arr))          # 9
print(np.argmin(arr))       # 0 (index của giá trị min)
print(np.argmax(arr))       # 8 (index của giá trị max)

# Standard deviation và variance
print(np.std(arr))          # 2.581988897471611
print(np.var(arr))          # 6.666666666666667
```

### Cumulative functions

```python
arr = np.array([1, 2, 3, 4, 5])

# Cumulative sum
print(np.cumsum(arr))    # [ 1  3  6 10 15]

# Cumulative product
print(np.cumprod(arr))   # [  1   2   6  24 120]

# Differences
print(np.diff(arr))      # [1 1 1 1]
```

### Sorting và searching

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Sorting
print(np.sort(arr))           # [1 1 2 3 4 5 6 9]
print(np.argsort(arr))        # [1 3 6 0 2 4 7 5] (indices for sorted order)

# 2D sorting
arr_2d = np.array([[3, 1, 4], [1, 5, 9]])
print(np.sort(arr_2d, axis=1))  # Sort each row
# [[1 3 4]
#  [1 5 9]]

# Searching
print(np.where(arr > 4))       # (array([4, 5, 7]),) indices where condition is True
print(np.searchsorted(np.sort(arr), 5))  # 5 (position to insert 5 in sorted array)
```

## 🔢 Linear Algebra

### Basic operations

```python
# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product
print(np.dot(A, B))  # hoặc A @ B
# [[19 22]
#  [43 50]]

# Transpose
print(A.T)
# [[1 3]
#  [2 4]]

# Determinant
print(np.linalg.det(A))  # -2.0000000000000004

# Inverse
print(np.linalg.inv(A))
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Eigenvalues và eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
```

### Solving linear systems

```python
# Giải hệ phương trình Ax = b
A = np.array([[2, 1], [1, 3]])
b = np.array([1, 2])

x = np.linalg.solve(A, b)
print("Solution:", x)  # [-0.2  1.4]

# Kiểm tra kết quả
print("Verification:", np.allclose(A @ x, b))  # True
```

### Matrix decomposition

```python
# SVD (Singular Value Decomposition)
A = np.array([[1, 2], [3, 4], [5, 6]])
U, s, Vt = np.linalg.svd(A)
print("U shape:", U.shape)    # (3, 2)
print("s shape:", s.shape)    # (2,)
print("Vt shape:", Vt.shape)  # (2, 2)

# QR decomposition
A = np.array([[1, 2], [3, 4]])
Q, R = np.linalg.qr(A)
print("Q:", Q)
print("R:", R)
```

## ⚡ Performance Tips

### Vectorization

```python
import time

# Slow way (using Python loops)
def slow_multiply(arr):
    result = []
    for x in arr:
        result.append(x * 2)
    return np.array(result)

# Fast way (vectorized)
def fast_multiply(arr):
    return arr * 2

# Timing comparison
large_arr = np.random.random(1000000)

start_time = time.time()
slow_result = slow_multiply(large_arr)
slow_time = time.time() - start_time

start_time = time.time()
fast_result = fast_multiply(large_arr)
fast_time = time.time() - start_time

print(f"Slow method: {slow_time:.4f} seconds")
print(f"Fast method: {fast_time:.4f} seconds")
print(f"Speedup: {slow_time/fast_time:.1f}x")
```

### Memory efficient operations

```python
# In-place operations (modify original array)
arr = np.array([1, 2, 3, 4, 5])
arr += 10  # In-place addition
print(arr)  # [11 12 13 14 15]

# Using out parameter
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.empty_like(arr1)
np.add(arr1, arr2, out=result)  # Store result in pre-allocated array
```

## 📝 Bài tập thực hành

### Bài tập 1: Broadcasting

```python
# Tạo matrix 4x3 với giá trị random
# Trừ đi mean của từng cột (standardization)
# Hint: Sử dụng broadcasting
```

### Bài tập 2: Statistical analysis

```python
# Tạo array 2D (5x6) với giá trị random từ 0-100
# Tính:
# 1. Mean, std, min, max của toàn bộ array
# 2. Mean của từng hàng và từng cột
# 3. Tìm vị trí của giá trị lớn nhất
# 4. Đếm số phần tử > 50
```

### Bài tập 3: Linear algebra

```python
# Cho hai matrix A (3x3) và B (3x3)
# 1. Tính A @ B và B @ A
# 2. Tính determinant của A
# 3. Nếu det(A) != 0, tính inverse của A
# 4. Tính eigenvalues của A
```

## 💡 Best Practices

1. **Sử dụng vectorized operations**: Thay vì loops

```python
# Good
result = np.sum(arr * 2)
# Avoid
result = sum(x * 2 for x in arr)
```

2. **Chọn đúng axis**: Khi làm việc với multidimensional arrays

```python
# axis=0: operations along rows (down columns)
# axis=1: operations along columns (across rows)
```

3. **Memory management**: Sử dụng appropriate data types

```python
# Choose appropriate dtype to save memory
arr = np.array(data, dtype=np.float32)  # Instead of float64
```

4. **Numerical stability**: Cẩn thận với floating point operations

```python
# Use allclose for floating point comparison
np.allclose(a, b, rtol=1e-5, atol=1e-8)
```

## 🔗 Tài liệu tham khảo

- [NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
- [NumPy Linear Algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [NumPy Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [Broadcasting Rules](https://numpy.org/doc/stable/user/basics.broadcasting.html)
