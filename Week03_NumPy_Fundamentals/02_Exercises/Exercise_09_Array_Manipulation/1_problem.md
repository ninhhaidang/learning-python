# Exercise 09: Array Manipulation Advanced

## 🎯 Mục tiêu

- Thành thạo các advanced array operations
- Sử dụng reshape, stack, concatenate hiệu quả
- Thực hành fancy indexing và advanced slicing
- Xử lý multi-dimensional arrays trong thực tế

## 📋 Đề bài: Advanced Array Manipulation

Thực hiện các thao tác nâng cao với arrays để xử lý dữ liệu đa chiều.

### Yêu cầu:

1. **Array reshaping** và dimension manipulation
2. **Stacking operations** (vstack, hstack, dstack)
3. **Fancy indexing** với multiple conditions
4. **Advanced slicing** patterns
5. **Array broadcasting** trong multi-dimensional context

### Input mẫu:

```python
import numpy as np
np.random.seed(42)
# Create test arrays
arr_1d = np.arange(12)
arr_2d = np.random.randint(1, 10, (3, 4))
arr_3d = np.random.randint(1, 5, (2, 3, 4))
```

### Expected Output:

```
=== ADVANCED ARRAY MANIPULATION ===

📊 RESHAPING OPERATIONS:
Original 1D (12,): [0 1 2 3 4 5 6 7 8 9 10 11]
Reshaped to (3,4):
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

Reshaped to (2,6):
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]

🔗 STACKING OPERATIONS:
Array A (3x4): [[7 4 6 9] [2 6 7 4] [4 7 9 8]]
Array B (3x4): [[1 5 9 8] [8 1 5 9] [8 9 2 6]]

Vertical stack (6x4):
[[7 4 6 9]
 [2 6 7 4]
 [4 7 9 8]
 [1 5 9 8]
 [8 1 5 9]
 [8 9 2 6]]

Horizontal stack (3x8):
[[7 4 6 9 1 5 9 8]
 [2 6 7 4 8 1 5 9]
 [4 7 9 8 8 9 2 6]]

🎯 FANCY INDEXING:
Original array: [7 4 6 9 2 6 7 4 4 7 9 8]
Indices [0, 2, 5, 8]: [7 6 6 4]
Boolean mask (>6): [7 9 7 7 9 8]

📐 ADVANCED SLICING:
3D Array shape: (2, 3, 4)
Slice [:, 1, :]: Extract middle rows from all matrices
Slice [0, :, ::2]: First matrix, all rows, every 2nd column

🔄 ARRAY CONCATENATION:
Concatenate along axis 0: Shape (6, 4)
Concatenate along axis 1: Shape (3, 8)

💡 PERFORMANCE TIPS:
- Use views instead of copies when possible
- Leverage broadcasting for efficient operations
- Choose appropriate axis for operations
```

## � Hướng dẫn

### Các kỹ thuật cần sử dụng:

- `np.reshape()`, `arr.reshape()` - thay đổi shape
- `np.vstack()`, `np.hstack()`, `np.dstack()` - stacking
- `arr[indices]` - fancy indexing
- `arr[start:stop:step]` - advanced slicing
- `np.concatenate()` - concatenation theo axis

### Gợi ý thực hiện:

1. Tạo arrays với các shapes khác nhau
2. Thực hành reshape với -1 parameter
3. So sánh vstack vs concatenate axis=0
4. Sử dụng Boolean indexing kết hợp fancy indexing
5. Test memory efficiency của views vs copies

## ✅ Tiêu chí đánh giá

- [ ] Sử dụng đúng reshape operations với -1 parameter
- [ ] Thực hiện stacking theo multiple axes
- [ ] Áp dụng fancy indexing với Boolean conditions
- [ ] Demonstrate advanced slicing patterns
- [ ] Code có comment giải thích từng technique
- [ ] Output format rõ ràng, demo đầy đủ các operations
