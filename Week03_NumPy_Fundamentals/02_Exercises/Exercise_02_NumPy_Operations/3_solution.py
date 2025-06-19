"""
Exercise 02 Solutions: NumPy Operations
Week 03 - NumPy Fundamentals

Đáp án chi tiết cho các bài tập về NumPy Operations
"""

import numpy as np
import time

print("=" * 60)
print("EXERCISE 02 SOLUTIONS: NumPy Operations")
print("=" * 60)

# =============================================================================
# Bài 1: Phân tích Dữ liệu Bán hàng
# =============================================================================
print("\n" + "="*50)
print("BÀI 1: PHÂN TÍCH DỮ LIỆU BÁN HÀNG")
print("="*50)

np.random.seed(42)

# 1. Tạo ma trận doanh thu
revenue = np.random.uniform(50, 200, (4, 3))  # 4 quý x 3 tháng
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
months = ['T1', 'T2', 'T3']

print("Doanh thu theo quý (triệu VND):")
print(f"{'':4s}", end="")
for month in months:
    print(f"{month:>8s}", end="")
print(f"{'Tổng':>10s}")

for i, quarter in enumerate(quarters):
    quarter_total = np.sum(revenue[i])
    print(f"{quarter:4s}", end="")
    for j in range(3):
        print(f"{revenue[i,j]:8.1f}", end="")
    print(f"{quarter_total:10.1f}")

# 2. Tính tổng doanh thu mỗi quý và mỗi tháng
quarterly_totals = np.sum(revenue, axis=1)  # Tổng theo hàng (quý)
monthly_totals = np.sum(revenue, axis=0)    # Tổng theo cột (tháng)

print(f"\nTổng doanh thu mỗi quý:")
for i, quarter in enumerate(quarters):
    print(f"{quarter}: {quarterly_totals[i]:.1f} triệu")

print(f"\nTổng doanh thu mỗi tháng:")
for i, month in enumerate(months):
    print(f"{month}: {monthly_totals[i]:.1f} triệu")

# 3. Tính tăng trưởng theo quý
growth_rates = np.diff(quarterly_totals) / quarterly_totals[:-1] * 100
print(f"\nTăng trưởng theo quý:")
for i, rate in enumerate(growth_rates):
    print(f"{quarters[i]} -> {quarters[i+1]}: {rate:+.1f}%")

# 4. Áp dụng thuế 10%
after_tax = revenue * 0.9  # Doanh thu sau thuế
print(f"\nDoanh thu sau thuế 10% (triệu VND):")
print(after_tax.round(1))

# 5. Tìm tháng có doanh thu cao nhất và thấp nhất
max_position = np.unravel_index(np.argmax(revenue), revenue.shape)
min_position = np.unravel_index(np.argmin(revenue), revenue.shape)

max_revenue = revenue[max_position]
min_revenue = revenue[min_position]

print(f"\nTháng có doanh thu cao nhất: {quarters[max_position[0]]}-{months[max_position[1]]} ({max_revenue:.1f} triệu)")
print(f"Tháng có doanh thu thấp nhất: {quarters[min_position[0]]}-{months[min_position[1]]} ({min_revenue:.1f} triệu)")

# 6. So sánh với target
target = 150  # triệu VND/tháng
above_target = revenue > target
months_above_target = np.sum(above_target)
total_months = revenue.size
completion_rate = months_above_target / total_months * 100

print(f"\nSo sánh với target ({target} triệu/tháng):")
print(f"Số tháng đạt target: {months_above_target}/{total_months}")
print(f"Tỷ lệ hoàn thành: {completion_rate:.1f}%")

# =============================================================================
# Bài 2: Xử lý Dữ liệu Cảm biến
# =============================================================================
print("\n" + "="*50)
print("BÀI 2: XỬ LÝ DỮ LIỆU CẢM BIẾN")
print("="*50)

np.random.seed(42)

# 1. Tạo dữ liệu cảm biến
sensor_data = np.random.normal(25, 5, (5, 24))  # 5 sensors x 24 hours
sensor_names = [f'Sensor_{i+1}' for i in range(5)]

print("Dữ liệu cảm biến (5 sensors x 24 hours):")
for i, name in enumerate(sensor_names):
    print(f"{name}: {sensor_data[i][:6].round(1)} ... (showing first 6 hours)")

# 2. Tính nhiệt độ trung bình
hourly_avg = np.mean(sensor_data, axis=0)  # Trung bình theo giờ
sensor_avg = np.mean(sensor_data, axis=1)  # Trung bình theo cảm biến

print(f"\nNhiệt độ TB theo giờ (°C):")
print(f"Hours 0-5: {hourly_avg[:6].round(1)}")
print(f"Hours 18-23: {hourly_avg[18:].round(1)}")

print(f"\nNhiệt độ TB theo cảm biến (°C):")
for i, name in enumerate(sensor_names):
    print(f"{name}: {sensor_avg[i]:.1f}")

# 3. Tính correlation
correlation_matrix = np.corrcoef(sensor_data)
print(f"\nCorrelation matrix:")
print("       ", end="")
for i in range(5):
    print(f"S{i+1:1d}   ", end="")
print()

for i in range(5):
    print(f"S{i+1:1d}  ", end="")
    for j in range(5):
        print(f"{correlation_matrix[i,j]:5.2f}", end="")
    print()

# 4. Chuẩn hóa dữ liệu (z-score)
normalized_data = (sensor_data - np.mean(sensor_data, axis=1, keepdims=True)) / np.std(sensor_data, axis=1, keepdims=True)

print(f"\nDữ liệu chuẩn hóa - kiểm tra:")
print(f"Mean per sensor: {np.mean(normalized_data, axis=1).round(3)}")
print(f"Std per sensor: {np.std(normalized_data, axis=1).round(3)}")

# 5. Tìm outliers
outliers = np.abs(normalized_data) > 2
outlier_positions = np.where(outliers)

print(f"\nOutliers detected (|z-score| > 2): {len(outlier_positions[0])}")
for i in range(min(5, len(outlier_positions[0]))):  # Show first 5 outliers
    sensor_idx = outlier_positions[0][i]
    hour_idx = outlier_positions[1][i]
    z_score = normalized_data[sensor_idx, hour_idx]
    original_value = sensor_data[sensor_idx, hour_idx]
    print(f"{sensor_names[sensor_idx]} at hour {hour_idx}: {original_value:.1f}°C (z-score: {z_score:.2f})")

# 6. Smooth data với moving average
def moving_average(data, window=3):
    """Apply moving average with given window size"""
    return np.array([np.convolve(row, np.ones(window)/window, mode='valid') for row in data])

smoothed_data = moving_average(sensor_data, window=3)
print(f"\nSmoothed data shape: {smoothed_data.shape} (original: {sensor_data.shape})")
print(f"Reduction due to window: {sensor_data.shape[1] - smoothed_data.shape[1]} time points")

# =============================================================================
# Bài 3: Vector Operations & Broadcasting
# =============================================================================
print("\n" + "="*50)
print("BÀI 3: VECTOR OPERATIONS & BROADCASTING")
print("="*50)

np.random.seed(42)

# 1. Tạo matrix và vector
A = np.random.random((3, 4))
B = np.random.random(4)

print("Matrix A (3x4):")
print(A.round(2))
print(f"\nVector B (4,): {B.round(2)}")

# 2. Broadcasting operations
A_plus_B = A + B    # Broadcasting
A_times_B = A * B   # Element-wise multiplication
A_minus_B = A - B   # Broadcasting

print(f"\nBroadcasting results:")
print(f"A + B (broadcasting):")
print((A_plus_B).round(2))

# Performance benchmark
def numpy_operations(data, iterations=1000):
    """NumPy vectorized operations"""
    start = time.time()
    for _ in range(iterations):
        result = np.sum(data**2, axis=1)
    return time.time() - start

def python_loops(data, iterations=1000):
    """Pure Python loops"""
    start = time.time()
    for _ in range(iterations):
        result = []
        for row in data:
            row_sum = sum(x**2 for x in row)
            result.append(row_sum)
    return time.time() - start

# Benchmark with larger data
benchmark_data = np.random.random((100, 50))

numpy_time = numpy_operations(benchmark_data, 100)
python_time = python_loops(benchmark_data.tolist(), 100)

speedup = python_time / numpy_time

print(f"\nPerformance benchmark (100 iterations, 100x50 data):")
print(f"NumPy operations: {numpy_time:.4f}s")
print(f"Python loops: {python_time:.4f}s")
print(f"Speedup: {speedup:.1f}x")

print("\n" + "="*60)
print("HOÀN THÀNH EXERCISE 02!")
print("="*60)
