# Exercise 01: Temperature Analysis

## 🎯 Mục tiêu

- Nắm vững cách tạo NumPy arrays từ dữ liệu thực tế
- Thực hành các phép toán thống kê cơ bản (min, max, mean, std)
- Học cách sử dụng Boolean indexing và masking
- Áp dụng NumPy vào bài toán phân tích dữ liệu khí tượng

## 📋 Đề bài: Phân tích Dữ liệu Nhiệt độ

Bạn là nhà khí tượng học và cần phân tích dữ liệu nhiệt độ của một thành phố trong 30 ngày qua.

### Yêu cầu:

1. **Tạo dữ liệu nhiệt độ ngẫu nhiên** từ 18°C đến 35°C cho 30 ngày
2. **Tìm thông tin cực trị**: ngày có nhiệt độ cao nhất và thấp nhất
3. **Tính toán thống kê**: nhiệt độ trung bình, độ lệch chuẩn
4. **Phân loại ngày**: đếm số ngày có nhiệt độ trên 30°C
5. **Tạo Boolean mask**: mask cho các ngày nóng (>30°C) và mát (<22°C)

### Input mẫu:

```python
import numpy as np
np.random.seed(42)  # Để có kết quả reproducible
# Tạo dữ liệu nhiệt độ ở đây
```

### Expected Output:

```
=== PHÂN TÍCH DỮ LIỆU NHIỆT ĐỘ ===

Dữ liệu nhiệt độ 30 ngày (°C):
[23.4 28.1 31.2 19.8 25.6 33.7 21.4 18.9 29.3 32.1
 27.8 30.5 24.2 34.8 20.1 26.9 22.7 31.8 25.3 28.4
 19.5 33.2 24.8 27.1 30.9 21.6 26.3 32.4 23.7 29.8]

📊 THỐNG KÊ TỔNG QUAN:
- Nhiệt độ cao nhất: 34.8°C (ngày 14)
- Nhiệt độ thấp nhất: 18.9°C (ngày 8)
- Nhiệt độ trung bình: 26.7°C
- Độ lệch chuẩn: 4.2°C

🌡️  PHÂN LOẠI NGÀY:
- Số ngày nóng (>30°C): 8 ngày
- Số ngày mát (<22°C): 5 ngày
- Số ngày bình thường: 17 ngày

🔍 BOOLEAN MASKS:
Ngày nóng (>30°C): [False False  True False False  True False False False  True ...]
Ngày mát (<22°C): [False False False  True False False  True  True False False ...]
```

## 💡 Hướng dẫn

### Các hàm NumPy cần sử dụng:

- `np.random.uniform(low, high, size)` - tạo số ngẫu nhiên
- `np.argmax()`, `np.argmin()` - tìm vị trí min/max
- `np.mean()`, `np.std()` - tính trung bình và độ lệch chuẩn
- Boolean indexing: `array > threshold`
- `np.sum(boolean_array)` - đếm số True

### Gợi ý thực hiện:

1. Tạo array nhiệt độ bằng `np.random.uniform()`
2. Sử dụng `np.argmax()` để tìm vị trí nhiệt độ max
3. Tạo Boolean mask bằng so sánh: `temp > 30`
4. Đếm số ngày bằng `np.sum()` trên Boolean mask
5. Format output để dễ đọc

## ✅ Tiêu chí đánh giá

- [ ] Tạo đúng array nhiệt độ 30 ngày trong khoảng 18-35°C
- [ ] Tìm đúng vị trí và giá trị min/max
- [ ] Tính toán thống kê chính xác (mean, std)
- [ ] Sử dụng Boolean indexing đúng cách
- [ ] Output format rõ ràng, dễ đọc
- [ ] Code clean, có comment giải thích
