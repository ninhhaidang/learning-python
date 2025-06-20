# Exercise 03: Image Processing Basics

## 🎯 Mục tiêu

- Học cách biểu diễn hình ảnh bằng NumPy arrays
- Thực hành threshold và binary operations trên ảnh
- Sử dụng slicing để trích xuất vùng ảnh
- Áp dụng các phép biến đổi cơ bản (flip, rotate)

## 📋 Đề bài: Xử lý Ảnh Grayscale Đơn giản

Mô phỏng xử lý một "ảnh" grayscale đơn giản bằng NumPy.

### Yêu cầu:

1. **Tạo ảnh grayscale** 10x10 với giá trị pixel từ 0-255
2. **Áp dụng threshold**: pixel > 128 = 255, ngược lại = 0
3. **Tính histogram**: đếm số pixel ở các khoảng giá trị
4. **Tìm vùng sáng nhất**: region 3x3 có trung bình pixel cao nhất
5. **Biến đổi ảnh**: flip theo chiều ngang và dọc

### Input mẫu:

```python
import numpy as np
np.random.seed(42)
image = np.random.randint(0, 256, (10, 10))
```

### Expected Output:

```
=== XỬ LÝ ẢNH GRAYSCALE ===

Ảnh gốc (10x10):
[[123 234  56  78 145  67 189  23 198 134]
 [ 45 198 167 234  89 156  78 123  45 189]
 [234  67 123  98 201 156  34 187 145  67]
 ...]

Ảnh sau threshold (binary):
[[  0 255   0   0 255   0 255   0 255 255]
 [  0 255 255 255   0 255   0   0   0 255]
 [255   0   0   0 255 255   0 255 255   0]
 ...]

📊 HISTOGRAM PHÂN BỐ PIXEL:
[0-63]:    28 pixels (28.0%)
[64-127]:  23 pixels (23.0%)
[128-191]: 25 pixels (25.0%)
[192-255]: 24 pixels (24.0%)

🔍 PHÂN TÍCH VÙNG:
Vùng sáng nhất (3x3) tại vị trí (2,3): trung bình 201.2
Vùng tối nhất (3x3) tại vị trí (5,1): trung bình 45.8

🔄 BIẾN ĐỔI ẢNH:
Ảnh flip ngang (horizontal flip):
[...]

Ảnh flip dọc (vertical flip):
[...]
```

## 💡 Hướng dẫn

### Các kỹ thuật NumPy cần sử dụng:

- `np.random.randint(0, 256, size)` - tạo ảnh ngẫu nhiên
- `np.where(condition, value_if_true, value_if_false)` - threshold
- Slicing để tạo histogram: `np.sum((image >= low) & (image < high))`
- Sliding window: `image[i:i+3, j:j+3]` để tạo region 3x3
- `np.flip()` hoặc slicing `[::-1]` để flip ảnh

### Gợi ý thực hiện:

1. Tạo ảnh bằng `np.random.randint()`
2. Dùng `np.where()` để áp dụng threshold
3. Tính histogram bằng Boolean indexing và `np.sum()`
4. Dùng nested loop để tìm region 3x3 sáng nhất
5. Sử dụng slicing để flip ảnh

## ✅ Tiêu chí đánh giá

- [ ] Tạo đúng ma trận ảnh 10x10 với giá trị 0-255
- [ ] Áp dụng threshold chính xác bằng np.where()
- [ ] Tính histogram đúng cho 4 khoảng giá trị
- [ ] Tìm được vùng 3x3 có trung bình cao nhất
- [ ] Thực hiện flip ảnh theo cả 2 chiều
- [ ] Output format rõ ràng, trực quan
