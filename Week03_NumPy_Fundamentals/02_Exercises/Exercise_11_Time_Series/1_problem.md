# Exercise 11: Time Series Analysis

## 🎯 Mục tiêu

- Phân tích dữ liệu chuỗi thời gian với NumPy
- Tính toán trend, seasonality và moving averages
- Thực hiện time series transformations
- Áp dụng forecasting cơ bản

## 📋 Đề bài: Time Series Analysis với NumPy

Phân tích dữ liệu bán hàng theo chuỗi thời gian để tìm ra patterns và xu hướng.

### Yêu cầu:

1. **Data generation** - Tạo synthetic time series data
2. **Trend analysis** - Phát hiện xu hướng tăng/giảm
3. **Seasonality detection** - Tìm tính chu kỳ trong dữ liệu
4. **Moving averages** - Tính MA, EMA để smooth data
5. **Simple forecasting** - Dự đoán giá trị tương lai

### Input mẫu:

```python
import numpy as np
# Generate 365 days of sales data
np.random.seed(42)
days = np.arange(365)
trend = 0.1 * days  # Linear trend
seasonal = 10 * np.sin(2 * np.pi * days / 7)  # Weekly pattern
noise = np.random.normal(0, 5, 365)
sales = 100 + trend + seasonal + noise
```

### Expected Output:

```
=== TIME SERIES ANALYSIS ===

📊 DATA OVERVIEW:
Time series length: 365 days
Sales range: [82.3, 154.8]
Mean daily sales: 118.4 units
Standard deviation: 12.8 units

📈 TREND ANALYSIS:
Linear trend coefficient: +0.097 units/day
Total growth over period: +35.4 units
Trend strength: Strong upward trend

📅 SEASONALITY DETECTION:
Weekly pattern detected: YES
Peak day: Sunday (index 6)
Trough day: Wednesday (index 3)
Seasonal amplitude: 19.8 units

📊 MOVING AVERAGES:
7-day Simple MA (last week): [145.2, 146.8, 148.1, 149.5, 150.8]
30-day Simple MA (last month): [138.4, 139.2, 140.1, 140.9, 141.8]
7-day Exponential MA (α=0.3): [147.2, 148.5, 149.3, 150.1, 151.0]

🔮 FORECASTING:
Linear regression forecast (next 7 days): [152.3, 151.8, 148.9, 146.1, 147.4, 150.2, 154.1]
Moving average forecast (next 7 days): [151.0, 151.0, 151.0, 151.0, 151.0, 151.0, 151.0]

📋 STATISTICS SUMMARY:
Autocorrelation (lag-1): 0.89
Autocorrelation (lag-7): 0.76
Data stationarity: Non-stationary (trend present)
Volatility (rolling std): 8.2 units
```

## 📚 Hướng dẫn

### Các kỹ thuật cần sử dụng:

1. **Moving Average:**

   ```
   MA(t) = (x(t) + x(t-1) + ... + x(t-n+1)) / n
   ```

2. **Exponential Moving Average:**

   ```
   EMA(t) = α * x(t) + (1-α) * EMA(t-1)
   ```

3. **Linear Trend:**

   ```
   y = a * x + b (using np.polyfit)
   ```

4. **Autocorrelation:**
   ```
   r(k) = corr(x(t), x(t-k))
   ```

### Gợi ý thực hiện:

1. Tạo synthetic data với trend + seasonality + noise
2. Sử dụng np.convolve cho moving averages
3. np.polyfit để tìm linear trend
4. np.correlate cho autocorrelation
5. Extrapolate trend cho forecasting

## ✅ Tiêu chí đánh giá

- [ ] Generate realistic time series data
- [ ] Detect và quantify trend correctly
- [ ] Identify seasonal patterns
- [ ] Implement multiple types of moving averages
- [ ] Perform basic forecasting
- [ ] Calculate autocorrelation
- [ ] Code có comment giải thích methodology
