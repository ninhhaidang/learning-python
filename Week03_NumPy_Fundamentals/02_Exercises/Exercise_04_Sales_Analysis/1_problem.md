# Exercise 04: Sales Data Analysis

## 🎯 Mục tiêu

- Thành thạo các phép toán cơ bản với NumPy arrays
- Hiểu và áp dụng broadcasting trong NumPy
- Thực hành tính toán tăng trưởng và so sánh với target
- Sử dụng NumPy cho phân tích dữ liệu kinh doanh

## 📋 Đề bài: Phân tích Dữ liệu Bán hàng

Một cửa hàng có dữ liệu bán hàng 4 quý, mỗi quý có 3 tháng.

### Yêu cầu:

1. **Tạo ma trận doanh thu** 4x3 (4 quý x 3 tháng) với giá trị từ 50-200 triệu
2. **Tính tổng doanh thu** mỗi quý và mỗi tháng
3. **Tính tăng trưởng** theo quý (so với quý trước)
4. **Áp dụng thuế 10%** cho tất cả doanh thu
5. **Tìm tháng cao/thấp nhất** trong năm
6. **So sánh với target** (150 triệu/tháng)

### Expected Output:

```
=== PHÂN TÍCH DỮ LIỆU BÁN HÀNG ===

Doanh thu theo quý (triệu VND):
      T1    T2    T3   Tổng
Q1  [137.8 152.8 196.9] 487.5
Q2  [156.4 103.2 185.7] 445.3
Q3  [142.9 134.5 167.8] 445.2
Q4  [89.7  156.2 198.1] 444.0

📊 TỔNG KẾT THEO QUÝ:
Q1: 487.5 triệu
Q2: 445.3 triệu (-8.7%)
Q3: 445.2 triệu (-0.0%)
Q4: 444.0 triệu (-0.3%)

📊 TỔNG KẾT THEO THÁNG:
Tháng 1: 526.8 triệu
Tháng 2: 546.7 triệu
Tháng 3: 748.5 triệu

💰 SAU THUẾ (10%):
Doanh thu sau thuế: 1953.7 triệu
Thuế phải nộp: 217.1 triệu

🎯 SO SÁNH TARGET (150 triệu/tháng):
Số tháng đạt target: 8/12 tháng
Tỷ lệ đạt: 66.7%
```

## ✅ Tiêu chí đánh giá

- [ ] Tạo đúng ma trận 4x3 với doanh thu hợp lý
- [ ] Tính toán thống kê theo axis chính xác
- [ ] Tính đúng tỷ lệ tăng trưởng
- [ ] Áp dụng broadcasting để tính thuế
- [ ] So sánh với target bằng Boolean indexing
