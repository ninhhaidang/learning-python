# Exercise 04: NumPy Advanced

## Mục tiêu

- Master advanced indexing techniques
- Làm việc với structured arrays cho real-world data
- Tối ưu hóa performance và memory usage
- Ứng dụng NumPy trong geographic data processing
- Integration NumPy với other libraries

## Bài tập

### Bài 1: Geographic Information System (GIS)

Xây dựng hệ thống GIS đơn giản cho dữ liệu Việt Nam.

**Yêu cầu:**

1. Tạo database các tỉnh/thành phố VN với coordinates
2. Implement distance calculations (Haversine formula)
3. Spatial queries: tìm điểm gần nhất, trong radius
4. Create elevation map và contour analysis
5. Route planning giữa các điểm

**Input mẫu:**

```python
# Vietnam cities data
cities = [
    ('Hanoi', 21.0285, 105.8542, 1000000),
    ('Ho Chi Minh City', 10.8231, 106.6297, 9000000),
    ('Da Nang', 16.0544, 108.2022, 1500000),
    # ... 63 provinces
]
```

**Output mẫu:**

```
=== VIETNAM GIS SYSTEM ===
Loaded 63 provinces/cities
Coverage area: 331,212 km²

Distance Analysis:
Hanoi to Ho Chi Minh City: 1,166 km
Hanoi to Da Nang: 608 km
Shortest route: Hanoi -> Vinh -> Da Nang (634 km)
Longest distance: Ca Mau to Ha Giang (1,489 km)

Spatial Queries:
Cities within 100km of Hanoi: 8 cities
Nearest to Hanoi: Hai Phong (94 km)
Population density hotspots: 5 regions identified

Elevation Analysis:
Highest point: Fansipan (3,147m)
Average elevation: 108m
Coastal provinces: 28
Mountainous provinces: 12
```

### Bài 2: Time Series Analysis với NumPy

Phân tích dữ liệu time series phức tạp.

**Yêu cầu:**

1. Generate multi-variate time series data
2. Implement trend detection algorithms
3. Seasonal decomposition
4. Anomaly detection using statistical methods
5. Forecasting với linear models

**Input mẫu:**

```python
# Multi-variate time series (2 years daily data)
variables = ['temperature', 'humidity', 'pressure', 'wind_speed']
days = 730
```

**Output mẫu:**

```
=== TIME SERIES ANALYSIS ===
Dataset: 730 days × 4 variables

Trend Analysis:
Temperature: +0.02°C/month (warming trend)
Humidity: -0.1%/month (drying trend)
Pressure: stable (±0.01 hPa/month)
Wind Speed: +0.05 m/s/month (increasing)

Seasonal Patterns:
Temperature: Strong seasonality (R² = 0.87)
Humidity: Moderate seasonality (R² = 0.54)
Pressure: Weak seasonality (R² = 0.23)

Anomalies Detected:
Temperature: 23 outliers (>3σ)
Extreme heat: Day 156 (43.2°C)
Extreme cold: Day 45 (-2.1°C)

Correlations:
Temp-Humidity: -0.65 (strong negative)
Pressure-Wind: +0.34 (moderate positive)

Forecast (next 30 days):
Temperature: 25.3°C ± 2.1°C
Humidity: 68.2% ± 8.5%
```

### Bài 3: Advanced Performance Optimization

Tối ưu hóa performance cho big data processing.

**Yêu cầu:**

1. Memory mapping cho large arrays
2. Chunked processing techniques
3. Parallel processing simulation
4. Custom ufuncs creation
5. Benchmarking và profiling

**Input mẫu:**

```python
# Big data simulation
large_data_size = (10000, 10000)  # 100M elements
chunk_size = 1000
operations = ['sum', 'mean', 'std', 'max', 'custom_func']
```

**Output mẫu:**

```
=== PERFORMANCE OPTIMIZATION ===
Dataset: 10,000 × 10,000 (800 MB)

Memory Usage:
Standard loading: 800 MB RAM
Memory mapping: 45 MB RAM (18x reduction)
Chunked processing: 8 MB RAM (100x reduction)

Processing Speed:
Standard numpy operations: 2.34s
Chunked processing: 3.67s (1.6x slower, but memory efficient)
Custom ufunc: 1.89s (1.2x faster)
Parallel simulation: 0.78s (3x faster)

Optimization Results:
✓ Memory usage reduced by 95%
✓ Processing speed improved by 3x
✓ Scalable to datasets >RAM size
✓ Custom functions 20% faster than built-in

Recommendations:
- Use memory mapping for read-only data
- Chunk size: 1000-5000 for optimal performance
- Custom ufuncs for repeated operations
- Consider moving to Dask for true parallelization
```

## Hướng dẫn giải

### Tips cho Bài 1:

- Structured arrays cho geographic data
- Haversine formula: `2*R*arcsin(sqrt(sin²(Δlat/2) + cos(lat1)*cos(lat2)*sin²(Δlon/2)))`
- `np.argmin()` cho nearest neighbor
- `np.meshgrid()` cho elevation grid
- Boolean indexing cho spatial filters

### Tips cho Bài 2:

- `np.polyfit()` cho trend fitting
- `np.fft` cho frequency analysis
- `np.corrcoef()` cho correlation matrix
- Rolling window: `np.convolve()` hoặc sliding window
- Z-score: `(x - μ) / σ` cho anomaly detection

### Tips cho Bài 3:

- `np.memmap()` cho memory mapping
- Array slicing cho chunking: `arr[start:end]`
- `np.frombuffer()` cho efficient I/O
- `@np.vectorize` cho custom ufuncs
- `time.perf_counter()` cho precise timing

## Tiêu chí đánh giá

- [ ] Advanced indexing mastery
- [ ] Structured array proficiency
- [ ] Performance optimization awareness
- [ ] Memory management skills
- [ ] Real-world problem solving
- [ ] Code scalability
- [ ] Documentation và testing
- [ ] Algorithm efficiency analysis
