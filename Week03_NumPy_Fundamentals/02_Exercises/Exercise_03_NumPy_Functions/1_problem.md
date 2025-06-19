# Exercise 03: NumPy Functions

## Mục tiêu

- Thành thạo các hàm NumPy cho array creation và manipulation
- Sử dụng hiệu quả sorting, searching functions
- Thực hành array I/O operations
- Làm việc với random number generation

## Bài tập

### Bài 1: Quản lý Kho hàng thông minh

Xây dựng hệ thống quản lý kho hàng sử dụng NumPy.

**Yêu cầu:**

1. Tạo database sản phẩm với structured array (ID, name, price, quantity, category)
2. Implement các function: search by name, sort by price, filter by category
3. Tính inventory value và statistics
4. Save/load database từ file
5. Generate reports và visualize data

**Input mẫu:**

```python
# Sample products
products = [
    (1001, 'Laptop Dell', 15000000, 50, 'Electronics'),
    (1002, 'iPhone 15', 25000000, 30, 'Electronics'),
    (1003, 'Bàn gỗ', 2000000, 20, 'Furniture'),
    # ... more products
]
```

**Output mẫu:**

```
=== INVENTORY MANAGEMENT SYSTEM ===
Total products: 100
Total categories: 5
Total inventory value: 2,450,000,000 VND

Top 5 most expensive:
1. iPhone 15 Pro: 35,000,000 VND (qty: 15)
2. MacBook Pro: 32,000,000 VND (qty: 8)
...

Category statistics:
Electronics: 45 items, avg price: 18,500,000 VND
Furniture: 25 items, avg price: 3,200,000 VND
...

Low stock alert (<10): 12 products
Out of stock: 3 products
```

### Bài 2: Weather Data Analysis

Phân tích dữ liệu thời tiết sử dụng NumPy functions.

**Yêu cầu:**

1. Generate synthetic weather data (365 ngày)
2. Implement seasonal patterns và noise
3. Tìm extreme weather events
4. Compute moving averages và trends
5. Export data và create summary report

**Input mẫu:**

```python
# Weather parameters
base_temp = 25  # Base temperature
seasonal_amplitude = 8  # Seasonal variation
daily_noise = 3  # Random daily variation
```

**Output mẫu:**

```
=== WEATHER ANALYSIS REPORT ===
Dataset: 365 days of weather data

Temperature Statistics:
Mean: 25.2°C
Median: 25.1°C
Std: 6.8°C
Min: 8.3°C (Day 15, Winter)
Max: 41.7°C (Day 201, Summer)

Seasonal Averages:
Spring (Mar-May): 22.1°C
Summer (Jun-Aug): 31.8°C
Autumn (Sep-Nov): 24.3°C
Winter (Dec-Feb): 16.4°C

Extreme Events:
Heat waves (>35°C): 23 days
Cold snaps (<10°C): 8 days
Record high: 41.7°C
Record low: 8.3°C

Data exported to: weather_data.csv
```

### Bài 3: Advanced Array Manipulation

Thực hành các kỹ thuật array manipulation nâng cao.

**Yêu cầu:**

1. Create complex array patterns (spiral, checkerboard, gradient)
2. Implement custom sorting algorithms
3. Array reshaping và dimension manipulation
4. Performance comparison giữa các methods
5. Memory optimization techniques

**Input mẫu:**

```python
size = 100  # Array dimensions
patterns = ['spiral', 'checkerboard', 'gradient', 'random']
```

**Output mẫu:**

```
=== ARRAY MANIPULATION DEMO ===

Pattern Generation:
Spiral (100x100): Created in 0.045s
Checkerboard (100x100): Created in 0.012s
Gradient (100x100): Created in 0.008s

Sorting Performance (10000 elements):
np.sort(): 0.003s
np.argsort(): 0.004s
Custom quicksort: 0.156s
Speedup: 52x

Memory Usage:
Original array: 781.25 KB
Compressed: 156.25 KB (80% reduction)
View operations: 0 extra memory
Copy operations: 781.25 KB extra memory

Reshaping Operations:
1D -> 2D: ✓ (view)
2D -> 3D: ✓ (view)
Transpose: ✓ (view)
Flatten: ✓ (copy)
```

## Hướng dẫn giải

### Tips cho Bài 1:

- Sử dụng `np.dtype` để define structured array
- `np.sort()` và `np.argsort()` cho sorting
- Boolean indexing cho filtering
- `np.save()` và `np.load()` cho I/O
- `np.unique()` để tìm unique categories

### Tips cho Bài 2:

- `np.linspace()` cho time series
- `np.sin()` cho seasonal patterns
- `np.random.normal()` cho noise
- `np.convolve()` cho moving average
- `np.where()` cho extreme event detection

### Tips cho Bài 3:

- `np.meshgrid()` cho pattern generation
- `np.flip()`, `np.rot90()` cho transformations
- `time.time()` cho performance measurement
- `array.nbytes` cho memory usage
- Views vs copies: check `array.base`

## Tiêu chí đánh giá

- [ ] Sử dụng đúng NumPy functions cho từng task
- [ ] Code hiệu quả, tận dụng vectorization
- [ ] Xử lý được structured arrays
- [ ] Implement được I/O operations
- [ ] Performance optimization awareness
- [ ] Memory usage optimization
- [ ] Error handling và edge cases
- [ ] Clean code với proper documentation
