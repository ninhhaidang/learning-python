# 01. NumPy Introduction & Array Basics

## 🎯 Mục tiêu học tập

Sau khi hoàn thành chương này, bạn sẽ:

- Hiểu được NumPy là gì và tại sao nó quan trọng
- Biết cách cài đặt và import NumPy
- Tạo và làm việc với NumPy arrays
- Hiểu về shape, dtype và attributes của array
- Thực hiện indexing và slicing cơ bản

## 📚 NumPy là gì?

**NumPy** (Numerical Python) là thư viện cơ bản cho scientific computing trong Python. Nó cung cấp:

- **N-dimensional array object** (ndarray): Cấu trúc dữ liệu mạnh mẽ
- **Broadcasting functions**: Thực hiện phép toán trên arrays có shape khác nhau
- **Tools for integrating**: Với C/C++ và Fortran code
- **Linear algebra, Fourier transform, random number capabilities**

### Tại sao NumPy quan trọng?

1. **Performance**: Nhanh hơn Python lists 10-100 lần
2. **Memory efficient**: Sử dụng ít memory hơn
3. **Vectorization**: Thực hiện phép toán trên toàn bộ array
4. **Foundation**: Cơ sở cho pandas, scikit-learn, matplotlib...

## 🔧 Cài đặt và Import

```python
# Cài đặt NumPy
pip install numpy

# Import NumPy
import numpy as np

# Kiểm tra version
print(np.__version__)
```

## 🏗️ Tạo NumPy Arrays

### 1. Từ Python Lists

```python
# Array 1D
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)  # [1 2 3 4 5]

# Array 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# [[1 2 3]
#  [4 5 6]]

# Array 3D
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d.shape)  # (2, 2, 2)
```

### 2. Sử dụng Built-in Functions

```python
# Array với giá trị 0
zeros = np.zeros((3, 4))
print(zeros)

# Array với giá trị 1
ones = np.ones((2, 3))
print(ones)

# Array với giá trị bất kỳ
full = np.full((2, 2), 7)
print(full)

# Array với giá trị tăng dần
arange = np.arange(0, 10, 2)  # [0 2 4 6 8]
print(arange)

# Array với khoảng cách đều
linspace = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]
print(linspace)

# Identity matrix
identity = np.eye(3)
print(identity)

# Random arrays
random_arr = np.random.random((2, 3))
print(random_arr)

# Random integers
random_int = np.random.randint(0, 10, (2, 3))
print(random_int)
```

## 📊 Array Attributes

### Thuộc tính cơ bản

```python
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(f"Shape: {arr.shape}")      # (2, 4)
print(f"Size: {arr.size}")        # 8
print(f"Dimensions: {arr.ndim}")  # 2
print(f"Data type: {arr.dtype}")  # int64
print(f"Item size: {arr.itemsize}") # 8 bytes
print(f"Total bytes: {arr.nbytes}") # 64 bytes
```

### Data Types (dtype)

```python
# Các kiểu dữ liệu phổ biến
int_arr = np.array([1, 2, 3], dtype=np.int32)
float_arr = np.array([1.0, 2.0, 3.0], dtype=np.float64)
bool_arr = np.array([True, False, True], dtype=np.bool_)
string_arr = np.array(['a', 'b', 'c'], dtype=np.string_)

# Chuyển đổi kiểu dữ liệu
arr = np.array([1.7, 2.8, 3.9])
int_arr = arr.astype(np.int32)
print(int_arr)  # [1 2 3]

# Kiểm tra kiểu dữ liệu
print(arr.dtype)      # float64
print(int_arr.dtype)  # int32
```

## 🔍 Indexing và Slicing

### Indexing

```python
# 1D Array
arr_1d = np.array([0, 1, 2, 3, 4])
print(arr_1d[0])    # 0 (phần tử đầu)
print(arr_1d[-1])   # 4 (phần tử cuối)

# 2D Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[0, 0])    # 1 (hàng 0, cột 0)
print(arr_2d[1, 2])    # 6 (hàng 1, cột 2)
print(arr_2d[-1, -1])  # 9 (hàng cuối, cột cuối)

# 3D Array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d[0, 1, 1])  # 4 (khối 0, hàng 1, cột 1)
```

### Slicing

```python
# 1D Slicing
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[2:7])     # [2 3 4 5 6]
print(arr[:5])      # [0 1 2 3 4]
print(arr[5:])      # [5 6 7 8 9]
print(arr[::2])     # [0 2 4 6 8] (bước nhảy 2)
print(arr[::-1])    # [9 8 7 6 5 4 3 2 1 0] (đảo ngược)

# 2D Slicing
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr_2d[:2, :3])   # 2 hàng đầu, 3 cột đầu
print(arr_2d[1:, 2:])   # Từ hàng 1 trở đi, từ cột 2 trở đi
print(arr_2d[:, 1])     # Tất cả hàng, chỉ cột 1
print(arr_2d[0, :])     # Chỉ hàng 0, tất cả cột
```

### Boolean Indexing

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Tạo boolean mask
mask = arr > 5
print(mask)  # [False False False False False  True  True  True  True  True]

# Sử dụng mask để filter
result = arr[mask]
print(result)  # [6 7 8 9 10]

# Viết gọn hơn
result = arr[arr > 5]
print(result)  # [6 7 8 9 10]

# Với điều kiện phức tạp
result = arr[(arr > 3) & (arr < 8)]
print(result)  # [4 5 6 7]

# Với 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = arr_2d[arr_2d > 5]
print(result)  # [6 7 8 9] (trả về 1D array)
```

### Fancy Indexing

```python
arr = np.array([10, 20, 30, 40, 50])

# Sử dụng list các index
indices = [0, 2, 4]
result = arr[indices]
print(result)  # [10 30 50]

# Với 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = arr_2d[[0, 2], [1, 2]]  # (0,1) và (2,2)
print(result)  # [2 9]

# Lấy nhiều hàng
result = arr_2d[[0, 2]]
print(result)
# [[1 2 3]
#  [7 8 9]]
```

## 🔄 Thay đổi Shape của Array

### Reshape

```python
arr = np.arange(12)
print(arr)  # [0 1 2 3 4 5 6 7 8 9 10 11]

# Reshape thành 2D
arr_2d = arr.reshape(3, 4)
print(arr_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Reshape thành 3D
arr_3d = arr.reshape(2, 3, 2)
print(arr_3d.shape)  # (2, 3, 2)

# Sử dụng -1 để tự động tính toán
arr_auto = arr.reshape(4, -1)  # NumPy tự tính cột = 3
print(arr_auto.shape)  # (4, 3)
```

### Flatten và Ravel

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten (tạo copy)
flat = arr_2d.flatten()
print(flat)  # [1 2 3 4 5 6]

# Ravel (tạo view nếu có thể)
ravel = arr_2d.ravel()
print(ravel)  # [1 2 3 4 5 6]

# Kiểm tra sự khác biệt
flat[0] = 999
print(arr_2d[0, 0])  # 1 (không thay đổi)

ravel[0] = 999
print(arr_2d[0, 0])  # 999 (thay đổi)
```

### Transpose

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original:", arr.shape)  # (2, 3)

# Transpose
transposed = arr.T
print("Transposed:", transposed.shape)  # (3, 2)
print(transposed)
# [[1 4]
#  [2 5]
#  [3 6]]

# Với 3D array
arr_3d = np.random.random((2, 3, 4))
transposed_3d = arr_3d.transpose(2, 0, 1)  # (4, 2, 3)
print("3D Transposed:", transposed_3d.shape)
```

## 📝 Bài tập thực hành

### Bài tập 1: Tạo arrays

```python
# 1. Tạo array 1D từ 0 đến 20 với bước nhảy 2
# 2. Tạo array 2D 5x5 với tất cả giá trị bằng 7
# 3. Tạo identity matrix 4x4
# 4. Tạo array random 3x3 với giá trị từ 0 đến 1
```

### Bài tập 2: Thao tác với arrays

```python
# Cho array sau:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# 1. In shape, size, ndim của array
# 2. Lấy phần tử ở vị trí (1, 2)
# 3. Lấy hàng đầu tiên
# 4. Lấy cột cuối cùng
# 5. Lấy tất cả phần tử > 6
```

### Bài tập 3: Reshape và indexing

```python
# 1. Tạo array từ 1 đến 24
# 2. Reshape thành (4, 6)
# 3. Lấy 2 hàng đầu và 3 cột cuối
# 4. Flatten array về 1D
# 5. Sử dụng fancy indexing để lấy phần tử ở index [0, 5, 10, 15, 20]
```

## 💡 Tips và Best Practices

1. **Memory efficiency**: Sử dụng appropriate dtype

```python
# Thay vì float64 mặc định
arr = np.array([1, 2, 3], dtype=np.float32)
```

2. **Copy vs View**: Hiểu khi nào tạo copy, khi nào tạo view

```python
# View (shares memory)
view = arr[1:3]
# Copy (independent memory)
copy = arr[1:3].copy()
```

3. **Boolean operations**: Sử dụng & | thay vì and or

```python
# Đúng
mask = (arr > 5) & (arr < 10)
# Sai
# mask = (arr > 5) and (arr < 10)  # Lỗi!
```

4. **Vectorization**: Tận dụng sức mạnh của NumPy

```python
# Tốt
result = arr * 2
# Không tốt
result = [x * 2 for x in arr]
```

## 🔗 Tài liệu tham khảo

- [NumPy Official Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [NumPy Array Creation](https://numpy.org/doc/stable/user/basics.creation.html)
- [NumPy Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)
