# Exercise 05: Sensor Data Processing

## 🎯 Mục tiêu

- Xử lý dữ liệu từ nhiều cảm biến
- Thực hành interpolation và filtering
- Phát hiện anomalies trong dữ liệu
- Tính toán rolling statistics

## 📋 Đề bài: Xử lý Dữ liệu Cảm biến

Xử lý dữ liệu từ 5 cảm biến nhiệt độ trong 24 giờ (mỗi giờ 1 đo).

### Yêu cầu:

1. Tạo dữ liệu 5 cảm biến x 24 giờ
2. Tìm và xử lý missing values (NaN)
3. Tính moving average 3 giờ
4. Phát hiện outliers (|value - mean| > 2\*std)
5. Tính correlation giữa các cảm biến

### Expected Output:

```
=== XỬ LÝ DỮ LIỆU CẢNH BÁO ===

Dữ liệu 5 cảm biến x 24 giờ:
Sensor_1: [23.4 24.1 nan 25.6 ...]
Sensor_2: [22.8 23.5 24.2 nan ...]
...

📊 THỐNG KÊ:
- Missing values: 8/120 (6.7%)
- Outliers detected: 3 values
- Average temperature: 24.2°C

🔗 CORRELATION MATRIX:
Sensor correlations: [0.85 0.72 0.91 ...]
```

## ✅ Tiêu chí đánh giá

- [ ] Xử lý missing values với np.isnan()
- [ ] Tính rolling average chính xác
- [ ] Phát hiện outliers bằng statistical methods
- [ ] Tính correlation matrix
