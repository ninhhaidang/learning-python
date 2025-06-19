# NumPy Functions và Array Manipulation

## Mục lục

1. [Array Creation Functions](#array-creation-functions)
2. [Shape Manipulation](#shape-manipulation)
3. [Array Joining và Splitting](#array-joining-và-splitting)
4. [Sorting và Searching](#sorting-và-searching)
5. [Array I/O Operations](#array-io-operations)
6. [Random Number Generation](#random-number-generation)
7. [Practical Examples](#practical-examples)

---

## Array Creation Functions

### 1. Zeros, Ones, Empty

```python
import numpy as np

# Tạo array với giá trị 0
zeros = np.zeros((3, 4))
print("Zeros array:")
print(zeros)

# Tạo array với giá trị 1
ones = np.ones((2, 3), dtype=int)
print("\nOnes array:")
print(ones)

# Tạo array rỗng (không khởi tạo giá trị)
empty = np.empty((2, 2))
print("\nEmpty array:")
print(empty)

# Tạo array với giá trị tùy chỉnh
full = np.full((3, 3), 7)
print("\nFull array with 7:")
print(full)
```

### 2. Range Functions

```python
# arange - tương tự range() của Python
arr1 = np.arange(10)          # 0 đến 9
arr2 = np.arange(1, 11)       # 1 đến 10
arr3 = np.arange(0, 20, 2)    # 0 đến 19, bước nhảy 2

print("arange(10):", arr1)
print("arange(1, 11):", arr2)
print("arange(0, 20, 2):", arr3)

# linspace - chia đều khoảng
linear = np.linspace(0, 10, 5)  # 5 số từ 0 đến 10
print("linspace(0, 10, 5):", linear)

# logspace - chia theo log
log_space = np.logspace(0, 2, 5)  # 5 số từ 10^0 đến 10^2
print("logspace(0, 2, 5):", log_space)
```

### 3. Identity và Eye

```python
# Ma trận đơn vị
identity = np.identity(4)
print("Identity matrix:")
print(identity)

# Ma trận với đường chéo tùy chỉnh
eye = np.eye(4, k=1)  # k=1: đường chéo trên chính
print("\nEye matrix (k=1):")
print(eye)

# Tạo ma trận chéo từ array
diag_array = np.array([1, 2, 3, 4])
diagonal = np.diag(diag_array)
print("\nDiagonal matrix:")
print(diagonal)
```

---

## Shape Manipulation

### 1. Reshape và Resize

```python
# Tạo array 1D
arr = np.arange(12)
print("Original array:", arr)

# Reshape - thay đổi shape nhưng không thay đổi dữ liệu
reshaped = arr.reshape(3, 4)
print("\nReshaped to (3, 4):")
print(reshaped)

# Reshape với -1 (tự động tính toán)
auto_reshape = arr.reshape(4, -1)  # 4 hàng, tự động tính cột
print("\nAuto reshape (4, -1):")
print(auto_reshape)

# Flatten - chuyển về 1D
flattened = reshaped.flatten()
print("\nFlattened:", flattened)

# Ravel - tương tự flatten nhưng trả về view nếu có thể
raveled = reshaped.ravel()
print("Raveled:", raveled)
```

### 2. Transpose và Swapaxes

```python
# Tạo ma trận 3x4
matrix = np.arange(12).reshape(3, 4)
print("Original matrix (3x4):")
print(matrix)

# Transpose - hoán vị ma trận
transposed = matrix.T
# Hoặc: transposed = np.transpose(matrix)
print("\nTransposed (4x3):")
print(transposed)

# Swapaxes - hoán đổi 2 axes
arr_3d = np.arange(24).reshape(2, 3, 4)
swapped = np.swapaxes(arr_3d, 0, 2)
print(f"\nOriginal shape: {arr_3d.shape}")
print(f"After swapaxes(0, 2): {swapped.shape}")
```

---

## Array Joining và Splitting

### 1. Concatenate và Stack

```python
# Tạo 2 arrays để nối
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)

# Concatenate theo axis=0 (hàng)
concat_rows = np.concatenate([arr1, arr2], axis=0)
print("\nConcatenate axis=0:")
print(concat_rows)

# Concatenate theo axis=1 (cột)
concat_cols = np.concatenate([arr1, arr2], axis=1)
print("\nConcatenate axis=1:")
print(concat_cols)

# Stack - tạo dimension mới
stacked = np.stack([arr1, arr2], axis=0)
print(f"\nStacked shape: {stacked.shape}")
print("Stacked array:")
print(stacked)

# Vstack và Hstack
vstacked = np.vstack([arr1, arr2])  # Vertical stack
hstacked = np.hstack([arr1, arr2])  # Horizontal stack

print("\nVstack:")
print(vstacked)
print("\nHstack:")
print(hstacked)
```

### 2. Split Operations

```python
# Tạo array để split
big_array = np.arange(16).reshape(4, 4)
print("Original array:")
print(big_array)

# Split theo hàng
row_splits = np.split(big_array, 2, axis=0)
print("\nSplit into 2 parts (rows):")
for i, part in enumerate(row_splits):
    print(f"Part {i+1}:")
    print(part)

# Split theo cột
col_splits = np.split(big_array, 4, axis=1)
print("\nSplit into 4 parts (columns):")
for i, part in enumerate(col_splits):
    print(f"Part {i+1}:")
    print(part)

# Vsplit và Hsplit
vsplit_parts = np.vsplit(big_array, 2)
hsplit_parts = np.hsplit(big_array, 2)
```

---

## Sorting và Searching

### 1. Sorting Functions

```python
# Tạo array ngẫu nhiên
np.random.seed(42)
arr = np.random.randint(1, 20, 10)
print("Original array:", arr)

# Sort - sắp xếp
sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)

# Argsort - trả về indices của thứ tự sắp xếp
sort_indices = np.argsort(arr)
print("Sort indices:", sort_indices)
print("Verify:", arr[sort_indices])

# Sort 2D array
matrix = np.random.randint(1, 10, (3, 4))
print("\nOriginal matrix:")
print(matrix)

# Sort theo axis=0 (cột)
sorted_cols = np.sort(matrix, axis=0)
print("\nSorted by columns:")
print(sorted_cols)

# Sort theo axis=1 (hàng)
sorted_rows = np.sort(matrix, axis=1)
print("\nSorted by rows:")
print(sorted_rows)
```

### 2. Searching Functions

```python
# Tạo array để tìm kiếm
arr = np.array([1, 3, 5, 7, 9, 11, 13])
print("Array:", arr)

# Searchsorted - tìm vị trí để chèn
pos = np.searchsorted(arr, 6)
print(f"Position to insert 6: {pos}")

# Where - tìm elements thỏa mãn điều kiện
condition_indices = np.where(arr > 7)
print(f"Indices where arr > 7: {condition_indices[0]}")
print(f"Values: {arr[condition_indices]}")

# Nonzero - tìm elements khác 0
zero_array = np.array([0, 1, 0, 3, 0, 5])
nonzero_indices = np.nonzero(zero_array)
print(f"\nNonzero indices: {nonzero_indices[0]}")
print(f"Nonzero values: {zero_array[nonzero_indices]}")

# Argmax và Argmin
max_index = np.argmax(arr)
min_index = np.argmin(arr)
print(f"\nMax value index: {max_index}, value: {arr[max_index]}")
print(f"Min value index: {min_index}, value: {arr[min_index]}")
```

---

## Array I/O Operations

### 1. Save và Load Binary

```python
# Tạo array để lưu
data = np.random.random((5, 3))
print("Data to save:")
print(data)

# Lưu dưới dạng .npy
np.save('data_array.npy', data)
print("\nSaved to data_array.npy")

# Load lại
loaded_data = np.load('data_array.npy')
print("\nLoaded data:")
print(loaded_data)

# Verify
print(f"\nArrays equal: {np.array_equal(data, loaded_data)}")

# Lưu nhiều arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
np.savez('multiple_arrays.npz', first=arr1, second=arr2)

# Load nhiều arrays
loaded = np.load('multiple_arrays.npz')
print(f"\nLoaded arrays: {list(loaded.keys())}")
print(f"First: {loaded['first']}")
print(f"Second: {loaded['second']}")
```

### 2. Text File Operations

```python
# Tạo data để lưu dưới dạng text
matrix = np.array([[1.1, 2.2, 3.3],
                   [4.4, 5.5, 6.6],
                   [7.7, 8.8, 9.9]])

# Lưu dưới dạng text file
np.savetxt('data.txt', matrix, fmt='%.2f', delimiter=',')
print("Saved to data.txt")

# Load từ text file
loaded_matrix = np.loadtxt('data.txt', delimiter=',')
print("\nLoaded from text:")
print(loaded_matrix)

# Genfromtxt - mạnh hơn loadtxt
# Có thể xử lý missing values, headers, etc.
data_with_header = """# Temperature data
25.5,26.1,24.8
27.2,25.9,26.5
24.1,25.0,26.8"""

with open('temp_data.txt', 'w') as f:
    f.write(data_with_header)

temp_data = np.genfromtxt('temp_data.txt', delimiter=',', skip_header=1)
print("\nTemperature data:")
print(temp_data)
```

---

## Random Number Generation

### 1. Random Module

```python
# Set seed để có kết quả reproducible
np.random.seed(42)

# Random float từ 0 đến 1
random_floats = np.random.random((3, 3))
print("Random floats [0, 1):")
print(random_floats)

# Random integers
random_ints = np.random.randint(1, 11, size=(2, 5))
print("\nRandom integers [1, 10]:")
print(random_ints)

# Random choice từ array
choices = np.array(['A', 'B', 'C', 'D'])
selected = np.random.choice(choices, size=8, replace=True)
print(f"\nRandom choices: {selected}")

# Random choice với probability
probabilities = [0.4, 0.3, 0.2, 0.1]
weighted_choice = np.random.choice(choices, size=10, p=probabilities)
print(f"Weighted choices: {weighted_choice}")

# Shuffle array
arr_to_shuffle = np.arange(10)
print(f"\nOriginal: {arr_to_shuffle}")
np.random.shuffle(arr_to_shuffle)
print(f"Shuffled: {arr_to_shuffle}")
```

### 2. Statistical Distributions

```python
# Normal distribution
normal_data = np.random.normal(loc=0, scale=1, size=1000)
print(f"Normal distribution - Mean: {normal_data.mean():.2f}, Std: {normal_data.std():.2f}")

# Uniform distribution
uniform_data = np.random.uniform(low=0, high=10, size=100)
print(f"Uniform [0, 10) - Min: {uniform_data.min():.2f}, Max: {uniform_data.max():.2f}")

# Binomial distribution
binomial_data = np.random.binomial(n=10, p=0.3, size=100)
print(f"Binomial (n=10, p=0.3) - Mean: {binomial_data.mean():.2f}")

# Poisson distribution
poisson_data = np.random.poisson(lam=3, size=100)
print(f"Poisson (λ=3) - Mean: {poisson_data.mean():.2f}")
```

---

## Practical Examples

### Example 1: Data Preprocessing

```python
# Simulate một dataset
np.random.seed(42)
data = np.random.normal(100, 15, (1000, 5))  # 1000 samples, 5 features

print(f"Dataset shape: {data.shape}")
print(f"Original mean: {data.mean(axis=0)}")
print(f"Original std: {data.std(axis=0)}")

# Standardization (Z-score normalization)
standardized = (data - data.mean(axis=0)) / data.std(axis=0)
print(f"\nAfter standardization:")
print(f"Mean: {standardized.mean(axis=0)}")
print(f"Std: {standardized.std(axis=0)}")

# Min-Max normalization
min_vals = data.min(axis=0)
max_vals = data.max(axis=0)
normalized = (data - min_vals) / (max_vals - min_vals)
print(f"\nAfter min-max normalization:")
print(f"Min: {normalized.min(axis=0)}")
print(f"Max: {normalized.max(axis=0)}")
```

### Example 2: Image Processing Simulation

```python
# Tạo "image" đơn giản (grayscale)
image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)
print("Original image:")
print(image)

# Thresholding
threshold = 128
binary_image = np.where(image > threshold, 255, 0)
print(f"\nBinary image (threshold={threshold}):")
print(binary_image.astype(np.uint8))

# Simple blur (3x3 average filter)
padded = np.pad(image, 1, mode='edge')
blurred = np.zeros_like(image)

for i in range(1, padded.shape[0]-1):
    for j in range(1, padded.shape[1]-1):
        window = padded[i-1:i+2, j-1:j+2]
        blurred[i-1, j-1] = window.mean()

print(f"\nBlurred image:")
print(blurred.astype(np.uint8))
```

### Example 3: Statistical Analysis

```python
# Simulate điểm thi của students
np.random.seed(42)
math_scores = np.random.normal(75, 12, 100)
english_scores = np.random.normal(78, 10, 100)

print("Math scores statistics:")
print(f"Mean: {math_scores.mean():.2f}")
print(f"Median: {np.median(math_scores):.2f}")
print(f"Std: {math_scores.std():.2f}")
print(f"Min: {math_scores.min():.2f}")
print(f"Max: {math_scores.max():.2f}")

print("\nEnglish scores statistics:")
print(f"Mean: {english_scores.mean():.2f}")
print(f"Median: {np.median(english_scores):.2f}")
print(f"Std: {english_scores.std():.2f}")

# Correlation
correlation = np.corrcoef(math_scores, english_scores)[0, 1]
print(f"\nCorrelation between Math and English: {correlation:.3f}")

# Students pass both subjects (>= 60)
pass_math = math_scores >= 60
pass_english = english_scores >= 60
pass_both = pass_math & pass_english

print(f"\nPass rates:")
print(f"Math: {pass_math.sum()}/100 ({pass_math.mean()*100:.1f}%)")
print(f"English: {pass_english.sum()}/100 ({pass_english.mean()*100:.1f}%)")
print(f"Both: {pass_both.sum()}/100 ({pass_both.mean()*100:.1f}%)")
```

---

## Bài tập thực hành

### Bài tập 1: Array Creation và Manipulation

```python
# TODO: Hoàn thành các task sau

# 1. Tạo ma trận 5x5 với viền là 1 và bên trong là 0
# Kết quả mong đợi:
# [[1 1 1 1 1]
#  [1 0 0 0 1]
#  [1 0 0 0 1]
#  [1 0 0 0 1]
#  [1 1 1 1 1]]

# 2. Tạo ma trận chess board 8x8 (0 và 1 xen kẽ)

# 3. Tạo array 1D từ 0 đến 100, sau đó reshape thành 10x10
#    và tính tổng của mỗi hàng
```

### Bài tập 2: Data Processing

```python
# TODO: Xử lý dữ liệu nhiệt độ

# 1. Tạo dữ liệu nhiệt độ 30 ngày (random từ 20-35°C)
# 2. Tìm ngày có nhiệt độ cao nhất và thấp nhất
# 3. Tính nhiệt độ trung bình của từng tuần (4 tuần đầu)
# 4. Thay thế các ngày có nhiệt độ > 32°C bằng 32°C
# 5. Lưu dữ liệu vào file và load lại
```

### Bài tập 3: Advanced Operations

```python
# TODO: Phân tích dữ liệu bán hàng

# 1. Tạo dữ liệu bán hàng: 12 tháng x 4 tuần x 7 ngày
# 2. Tính doanh thu theo tháng, theo tuần, theo ngày trong tuần
# 3. Tìm tháng có doanh thu cao nhất
# 4. Tính tăng trưởng theo tháng (month-over-month)
# 5. Tạo báo cáo tóm tắt
```

---

## Tips và Best Practices

### 1. Memory Efficiency

```python
# Sử dụng dtype phù hợp
small_ints = np.array([1, 2, 3], dtype=np.int8)    # 1 byte per element
large_ints = np.array([1, 2, 3], dtype=np.int64)   # 8 bytes per element

print(f"int8 size: {small_ints.nbytes} bytes")
print(f"int64 size: {large_ints.nbytes} bytes")

# Sử dụng views thay vì copies khi có thể
arr = np.arange(100)
view = arr[::2]      # View - không copy dữ liệu
copy = arr[::2].copy()  # Explicit copy

print(f"Original array id: {id(arr)}")
print(f"View shares data: {view.base is arr}")
print(f"Copy shares data: {copy.base is arr}")
```

### 2. Broadcasting Tips

```python
# Hiểu broadcasting để viết code hiệu quả
matrix = np.random.random((1000, 500))
row_means = matrix.mean(axis=1, keepdims=True)  # Shape: (1000, 1)

# Efficient: broadcasting
centered = matrix - row_means

# Inefficient: explicit loop
# centered = np.zeros_like(matrix)
# for i in range(matrix.shape[0]):
#     centered[i] = matrix[i] - row_means[i]
```

### 3. Error Handling

```python
# Xử lý division by zero
arr = np.array([1, 2, 0, 4])
result = np.divide(10, arr, out=np.zeros_like(arr, dtype=float), where=(arr!=0))
print(f"Safe division: {result}")

# Xử lý invalid values
data = np.array([1, 2, np.nan, 4, np.inf])
clean_data = data[np.isfinite(data)]
print(f"Clean data: {clean_data}")
```

Trong phần tiếp theo, chúng ta sẽ học về các kỹ thuật NumPy nâng cao!
