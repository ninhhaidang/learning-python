# Exercise 08: Weather Data Analysis

## 🎯 Mục tiêu

- Xử lý time series data với NumPy
- Thực hành aggregation và resampling techniques
- Phát hiện patterns và trends trong dữ liệu thời tiết
- Tính toán rolling statistics và seasonal analysis

## 📋 Đề bài: Phân tích Dữ liệu Thời tiết

Phân tích dữ liệu thời tiết của một thành phố trong 365 ngày (1 năm).

### Yêu cầu:

1. **Tạo time series data** cho nhiệt độ, độ ẩm, lượng mưa
2. **Monthly aggregation** tính trung bình theo tháng
3. **Rolling statistics** moving average 7 ngày, 30 ngày
4. **Seasonal analysis** tìm patterns theo mùa
5. **Extreme weather detection** phát hiện ngày bất thường
6. **Weather correlation** tương quan giữa các yếu tố

### Expected Output:

```
=== WEATHER DATA ANALYSIS ===

📊 DATASET OVERVIEW:
Period: 365 days (1 year)
Temperature range: 5.2°C to 38.7°C
Humidity range: 25% to 95%
Total rainfall: 1,245.6 mm

📅 MONTHLY STATISTICS:
Month 1 (Jan): Temp 8.5°C, Humidity 78%, Rain 95.2mm
Month 2 (Feb): Temp 12.3°C, Humidity 72%, Rain 68.5mm
Month 3 (Mar): Temp 18.9°C, Humidity 65%, Rain 45.8mm
...
Month 12 (Dec): Temp 6.8°C, Humidity 82%, Rain 108.4mm

🌡️  TEMPERATURE TRENDS:
Coldest month: January (8.5°C)
Warmest month: July (32.4°C)
Annual average: 18.7°C
Temperature volatility: 8.2°C std

💧 RAINFALL PATTERNS:
Wettest month: November (145.6mm)
Driest month: July (12.3mm)
Annual total: 1,245.6mm
Rainy days (>1mm): 156 days

📈 ROLLING AVERAGES:
7-day moving avg temp: [8.2, 8.5, 9.1, 9.8, ...]
30-day moving avg temp: [8.5, 8.7, 9.2, 9.8, ...]

⚠️  EXTREME WEATHER EVENTS:
Heatwave days (>35°C): 12 days
Cold snaps (<0°C): 5 days
Heavy rain days (>50mm): 8 days
Drought periods (>21 consecutive dry days): 2 periods

🔗 WEATHER CORRELATIONS:
Temp-Humidity correlation: -0.68 (strong negative)
Temp-Rainfall correlation: -0.23 (weak negative)
Humidity-Rainfall correlation: 0.45 (moderate positive)
```

## 💡 Hướng dẫn

### Các kỹ thuật cần sử dụng:

- `np.convolve()` cho moving averages
- `np.corrcoef()` cho correlation matrix
- Boolean indexing cho extreme weather detection
- `np.reshape()` để group data by month
- `np.percentile()` cho threshold analysis

### Gợi ý thực hiện:

1. Generate realistic weather data với seasonal patterns
2. Reshape daily data thành monthly format
3. Sử dụng sliding window cho rolling statistics
4. Define thresholds cho extreme weather events
5. Calculate correlations between weather variables

## ✅ Tiêu chí đánh giá

- [ ] Generate realistic weather time series data
- [ ] Tính toán monthly aggregations chính xác
- [ ] Implement rolling statistics với different windows
- [ ] Phát hiện extreme weather events
- [ ] Tính correlation matrix giữa các variables
- [ ] Output format có cấu trúc, thông tin đầy đủ
