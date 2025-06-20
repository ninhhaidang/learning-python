# Exercise 10: GIS Basic Operations

## 🎯 Mục tiêu

- Thực hành xử lý dữ liệu không gian (spatial data) cơ bản
- Tính toán khoảng cách giữa các điểm địa lý
- Xử lý hệ tọa độ và projection
- Áp dụng NumPy trong bài toán GIS thực tế

## 📋 Đề bài: Geographic Information System Basics

Thực hiện các phép tính GIS cơ bản với dữ liệu tọa độ địa lý.

### Yêu cầu:

1. **Distance calculation** - Tính khoảng cách Euclidean và Haversine
2. **Coordinate transformation** - Chuyển đổi lat/lon sang UTM
3. **Spatial filtering** - Lọc điểm trong bounding box
4. **Nearest neighbor** - Tìm điểm gần nhất
5. **Polygon area** - Tính diện tích đa giác

### Input mẫu:

```python
import numpy as np
# Sample coordinates (latitude, longitude)
hanoi_coords = [21.0285, 105.8542]
hcm_coords = [10.8231, 106.6297]
danang_coords = [16.0471, 108.2068]
```

### Expected Output:

```
=== GIS BASIC OPERATIONS ===

📍 COORDINATES:
Hanoi: [21.0285, 105.8542]
Ho Chi Minh: [10.8231, 106.6297]
Da Nang: [16.0471, 108.2068]

📏 DISTANCE CALCULATIONS:
Euclidean Distance:
  Hanoi ↔ Ho Chi Minh: 11.24 degrees
  Hanoi ↔ Da Nang: 7.23 degrees
  Ho Chi Minh ↔ Da Nang: 6.24 degrees

Haversine Distance (Great Circle):
  Hanoi ↔ Ho Chi Minh: 1253.2 km
  Hanoi ↔ Da Nang: 760.8 km
  Ho Chi Minh ↔ Da Nang: 692.4 km

📦 BOUNDING BOX FILTERING:
Bounding box: [10°N-22°N, 105°E-109°E]
Cities within bounds: 3/3
- Hanoi: ✅
- Ho Chi Minh: ✅
- Da Nang: ✅

🎯 NEAREST NEIGHBOR:
Target point: [18.5, 107.0]
Nearest city: Da Nang (distance: 2.71 degrees)

📐 POLYGON OPERATIONS:
Triangle area (Hanoi-HCM-DaNang): 27.45 square degrees
Centroid: [15.97°N, 106.83°E]
```

## 📚 Hướng dẫn

### Công thức cần sử dụng:

1. **Euclidean Distance:**

   ```
   d = √[(lat₂-lat₁)² + (lon₂-lon₁)²]
   ```

2. **Haversine Formula:**

   ```
   a = sin²(Δφ/2) + cos φ₁ ⋅ cos φ₂ ⋅ sin²(Δλ/2)
   c = 2 ⋅ atan2(√a, √(1−a))
   d = R ⋅ c
   ```

3. **Triangle Area (Shoelace formula):**
   ```
   Area = 0.5 * |x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|
   ```

### Gợi ý thực hiện:

1. Tạo arrays cho coordinates
2. Vectorize distance calculations
3. Implement bounding box filtering với Boolean indexing
4. Sử dụng argmin cho nearest neighbor
5. Áp dụng công thức geometry cho polygon

## ✅ Tiêu chí đánh giá

- [ ] Implement cả Euclidean và Haversine distance
- [ ] Bounding box filtering chính xác
- [ ] Nearest neighbor search hiệu quả
- [ ] Polygon area calculation đúng
- [ ] Code có comment giải thích công thức
- [ ] Output format rõ ràng với đơn vị phù hợp
