# Exercise 02: Pandas DataFrame

## Mục tiêu

- Thành thạo việc tạo và thao tác với pandas DataFrame
- Hiểu rõ cách truy cập, chỉnh sửa và phân tích dữ liệu dạng bảng
- Thực hành các phép toán trên DataFrame cho phân tích không gian và viễn thám
- Làm quen với các phương pháp filtering, grouping và aggregation

## Bài tập

### Bài 1: Phân tích dữ liệu ảnh vệ tinh Landsat

Bạn có dữ liệu pixel của ảnh vệ tinh Landsat với các band quang phổ khác nhau. Cần tạo DataFrame để lưu trữ và phân tích dữ liệu này.

**Yêu cầu:**

1. Tạo DataFrame với dữ liệu pixel từ 4 band: Blue (450-515nm), Green (525-600nm), Red (630-680nm), NIR (845-885nm)
2. Thêm cột Location với tọa độ (latitude, longitude)
3. Tính NDVI (Normalized Difference Vegetation Index) = (NIR - Red) / (NIR + Red)
4. Tạo cột phân loại Land Cover dựa trên NDVI: Water (<0), Bare Soil (0-0.2), Vegetation (0.2-0.8), Dense Vegetation (>0.8)
5. Thống kê số lượng pixel theo từng loại Land Cover
6. Tìm pixel có NDVI cao nhất và thấp nhất với tọa độ tương ứng

**Dữ liệu mẫu:**

```python
# 20 pixel mẫu từ ảnh Landsat
data = {
    'pixel_id': range(1, 21),
    'blue': [145, 180, 167, 156, 189, 134, 198, 123, 167, 145,
             178, 156, 134, 189, 167, 145, 178, 156, 134, 189],
    'green': [189, 234, 223, 198, 245, 167, 256, 156, 223, 189,
              234, 198, 167, 245, 223, 189, 234, 198, 167, 245],
    'red': [134, 167, 156, 145, 178, 123, 189, 112, 156, 134,
            167, 145, 123, 178, 156, 134, 167, 145, 123, 178],
    'nir': [567, 890, 823, 634, 912, 456, 934, 389, 823, 567,
            890, 634, 456, 912, 823, 567, 890, 634, 456, 912],
    'latitude': [21.0285, 21.0290, 21.0295, 21.0300, 21.0305, 21.0310, 21.0315, 21.0320, 21.0325, 21.0330,
                21.0335, 21.0340, 21.0345, 21.0350, 21.0355, 21.0360, 21.0365, 21.0370, 21.0375, 21.0380],
    'longitude': [105.8542, 105.8547, 105.8552, 105.8557, 105.8562, 105.8567, 105.8572, 105.8577, 105.8582, 105.8587,
                 105.8592, 105.8597, 105.8602, 105.8607, 105.8612, 105.8617, 105.8622, 105.8627, 105.8632, 105.8637]
}
```

### Bài 2: Phân tích dữ liệu khí tượng theo vùng

Phân tích dữ liệu nhiệt độ, độ ẩm, lượng mưa của các trạm khí tượng ở Việt Nam.

**Yêu cầu:**

1. Tạo DataFrame với dữ liệu của 15 trạm khí tượng (tên trạm, vùng, nhiệt độ TB, độ ẩm %, lượng mưa mm)
2. Thêm cột phân loại khí hậu dựa trên nhiệt độ: Lạnh (<20°C), Mát (20-25°C), Ấm (25-30°C), Nóng (>30°C)
3. Tính trung bình nhiệt độ, độ ẩm, lượng mưa theo từng vùng
4. Tìm trạm có nhiệt độ cao nhất và thấp nhất
5. Lọc các trạm có lượng mưa trên 2000mm
6. Sắp xếp theo độ ẩm giảm dần

**Dữ liệu mẫu:**

```python
weather_data = {
    'station_name': ['Hà Nội', 'TP.HCM', 'Đà Nẵng', 'Hải Phòng', 'Cần Thơ',
                    'Huế', 'Nha Trang', 'Đà Lạt', 'Vinh', 'Buôn Ma Thuột',
                    'Quy Nhon', 'Rạch Giá', 'Cà Mau', 'Sa Pa', 'Điện Biên'],
    'region': ['Bắc Bộ', 'Nam Bộ', 'Trung Bộ', 'Bắc Bộ', 'Nam Bộ',
               'Trung Bộ', 'Trung Bộ', 'Tây Nguyên', 'Trung Bộ', 'Tây Nguyên',
               'Trung Bộ', 'Nam Bộ', 'Nam Bộ', 'Bắc Bộ', 'Bắc Bộ'],
    'avg_temp': [23.6, 27.4, 25.8, 23.1, 27.0, 24.5, 26.2, 18.9, 24.2, 21.8,
                 26.4, 27.1, 26.8, 15.4, 21.5],
    'humidity': [79, 78, 81, 82, 83, 84, 76, 85, 85, 82, 77, 84, 86, 87, 81],
    'rainfall': [1678, 1949, 2505, 1943, 1635, 2815, 1361, 1804, 1956, 2391,
                 1878, 2034, 2153, 2539, 1764]
}
```

### Bài 3: Quản lý dữ liệu điểm quan trắc môi trường

Tạo hệ thống quản lý dữ liệu chất lượng không khí tại các điểm quan trắc.

**Yêu cầu:**

1. Tạo DataFrame với thông tin 12 điểm quan trắc (ID, tên địa điểm, quận/huyện, PM2.5, PM10, NO2, SO2, CO)
2. Thêm cột đánh giá chất lượng không khí theo PM2.5: Tốt (<12), Trung bình (12-35), Kém (35-55), Rất kém (>55)
3. Tính trung bình các chỉ số ô nhiễm theo quận/huyện
4. Tìm điểm có chất lượng không khí tốt nhất và tệ nhất
5. Đếm số điểm quan trắc theo từng mức chất lượng
6. Lọc các điểm có PM10 vượt ngưỡng WHO (>20 μg/m³)

**Output mẫu:**

```
Thống kê chất lượng không khí:
- Tốt: 3 điểm
- Trung bình: 5 điểm
- Kém: 3 điểm
- Rất kém: 1 điểm

Điểm tốt nhất: Công viên Thống Nhất (PM2.5: 8.5 μg/m³)
Điểm tệ nhất: Ngã tư Hàng Xanh (PM2.5: 67.2 μg/m³)
```

## Hướng dẫn giải

### Bài 1 - Phân tích ảnh vệ tinh:

- Sử dụng `pd.DataFrame()` để tạo DataFrame từ dictionary
- Dùng phép toán vector để tính NDVI: `df['ndvi'] = (df['nir'] - df['red']) / (df['nir'] + df['red'])`
- Sử dụng `pd.cut()` hoặc `np.where()` để phân loại Land Cover
- Dùng `value_counts()` để đếm số lượng theo loại
- Sử dụng `idxmax()` và `idxmin()` để tìm pixel có NDVI cao/thấp nhất

### Bài 2 - Dữ liệu khí tượng:

- Dùng `groupby()` để nhóm theo vùng và tính trung bình
- Sử dụng điều kiện logic để phân loại khí hậu
- Dùng boolean indexing để lọc dữ liệu: `df[df['rainfall'] > 2000]`
- Sử dụng `sort_values()` để sắp xếp theo cột

### Bài 3 - Quan trắc môi trường:

- Tạo function để phân loại chất lượng không khí
- Dùng `apply()` để áp dụng function lên cột
- Sử dụng `agg()` với multiple functions cho groupby
- Kết hợp điều kiện để tìm điểm tốt nhất/tệ nhất

## Tiêu chí đánh giá

- [ ] Tạo DataFrame chính xác từ dữ liệu cho trước
- [ ] Thực hiện các phép toán và tính toán đúng công thức
- [ ] Sử dụng đúng phương pháp filtering và boolean indexing
- [ ] Phân loại dữ liệu chính xác theo điều kiện
- [ ] Thống kê và tổng hợp dữ liệu đúng yêu cầu
- [ ] Tìm được các giá trị min/max với thông tin chi tiết
- [ ] Code sạch sẽ, có comment giải thích
- [ ] Kết quả output đúng định dạng và đầy đủ thông tin
