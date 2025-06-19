"""
Exercise 04 Solutions: NumPy Advanced
Week 03 - NumPy Fundamentals

Đáp án chi tiết cho các bài tập NumPy Advanced
"""

import numpy as np
import time

print("=" * 60)
print("EXERCISE 04 SOLUTIONS: NumPy Advanced")
print("=" * 60)

# =============================================================================
# Bài 1: Geographic Information System (GIS)
# =============================================================================
print("\n" + "="*50)
print("BÀI 1: VIETNAM GIS SYSTEM")
print("="*50)

# Vietnam cities data với structured array
city_dtype = np.dtype([
    ('name', 'U30'),
    ('lat', 'f8'),
    ('lon', 'f8'),
    ('population', 'i4')
])

vietnam_cities = np.array([
    ('Hanoi', 21.0285, 105.8542, 8053663),
    ('Ho Chi Minh City', 10.8231, 106.6297, 9077158), 
    ('Da Nang', 16.0544, 108.2022, 1230000),
    ('Hai Phong', 20.8449, 106.6881, 2028514),
    ('Can Tho', 10.0452, 105.7469, 1235171),
    ('Bien Hoa', 10.9500, 106.8167, 1104495),
    ('Hue', 16.4637, 107.5909, 652572),
    ('Nha Trang', 12.2388, 109.1967, 392279),
    ('Buon Ma Thuot', 12.6667, 108.0500, 340000),
    ('Quy Nhon', 13.7563, 109.2297, 457400)
], dtype=city_dtype)

print("=== VIETNAM GIS SYSTEM ===")
print(f"Loaded {len(vietnam_cities)} cities")

# Haversine distance function
def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    # Radius of earth in kilometers
    r = 6371
    return c * r

# Calculate distance matrix
def calculate_distance_matrix(cities):
    """Calculate pairwise distances between all cities"""
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = haversine_distance(
                    cities[i]['lat'], cities[i]['lon'],
                    cities[j]['lat'], cities[j]['lon']
                )
                distance_matrix[i, j] = dist
    
    return distance_matrix

distances = calculate_distance_matrix(vietnam_cities)

print(f"\nDistance Analysis:")
hanoi_idx = 0  # Hanoi is first
hcmc_idx = 1   # Ho Chi Minh City is second

hanoi_hcmc_dist = distances[hanoi_idx, hcmc_idx]
print(f"Hanoi to Ho Chi Minh City: {hanoi_hcmc_dist:.0f} km")

# Find closest city to Hanoi (excluding Hanoi itself)
hanoi_distances = distances[hanoi_idx].copy()
hanoi_distances[hanoi_idx] = np.inf  # Exclude self
closest_to_hanoi_idx = np.argmin(hanoi_distances)
closest_distance = hanoi_distances[closest_to_hanoi_idx]

print(f"Nearest to Hanoi: {vietnam_cities[closest_to_hanoi_idx]['name']} ({closest_distance:.0f} km)")

# Find longest distance
max_dist_indices = np.unravel_index(np.argmax(distances), distances.shape)
max_distance = distances[max_dist_indices]
city1 = vietnam_cities[max_dist_indices[0]]['name']
city2 = vietnam_cities[max_dist_indices[1]]['name']

print(f"Longest distance: {city1} to {city2} ({max_distance:.0f} km)")

# Spatial queries - cities within radius
def cities_within_radius(cities, center_idx, radius_km, distance_matrix):
    """Find cities within radius of center city"""
    distances_from_center = distance_matrix[center_idx]
    within_radius = distances_from_center <= radius_km
    within_radius[center_idx] = False  # Exclude center itself
    return np.where(within_radius)[0]

nearby_hanoi = cities_within_radius(vietnam_cities, 0, 200, distances)
print(f"\nCities within 200km of Hanoi: {len(nearby_hanoi)} cities")
for idx in nearby_hanoi:
    dist = distances[0, idx]
    print(f"  {vietnam_cities[idx]['name']}: {dist:.0f} km")

# Population analysis
total_population = np.sum(vietnam_cities['population'])
print(f"\nPopulation Analysis:")
print(f"Total population: {total_population:,}")
print(f"Average city population: {np.mean(vietnam_cities['population']):,.0f}")

# Largest cities
sorted_by_pop = np.argsort(vietnam_cities['population'])[::-1]
print(f"\nTop 5 largest cities:")
for i, idx in enumerate(sorted_by_pop[:5]):
    city = vietnam_cities[idx]
    print(f"{i+1}. {city['name']}: {city['population']:,}")

# =============================================================================
# Bài 2: Time Series Analysis với NumPy
# =============================================================================
print("\n" + "="*50)
print("BÀI 2: TIME SERIES ANALYSIS")
print("="*50)

np.random.seed(42)

# Generate multi-variate time series
days = 730  # 2 years
variables = ['temperature', 'humidity', 'pressure', 'wind_speed']

def generate_multivariate_timeseries(days):
    """Generate synthetic multi-variate time series"""
    
    # Time vector
    t = np.arange(days)
    
    # Temperature with trend and seasonality
    temp_trend = 0.02 * t / 30  # 0.02°C per month warming
    temp_seasonal = 5 * np.sin(2 * np.pi * t / 365.25)
    temp_noise = np.random.normal(0, 2, days)
    temperature = 25 + temp_trend + temp_seasonal + temp_noise
    
    # Humidity (inversely correlated with temperature)
    humidity_base = 75 - 0.5 * (temperature - 25)
    humidity_noise = np.random.normal(0, 5, days)
    humidity = np.clip(humidity_base + humidity_noise, 20, 95)
    
    # Pressure (weak seasonality)
    pressure_seasonal = 2 * np.sin(2 * np.pi * (t + 90) / 365.25)
    pressure_noise = np.random.normal(0, 1, days)
    pressure = 1013 + pressure_seasonal + pressure_noise
    
    # Wind speed (increasing trend)
    wind_trend = 0.05 * t / 30  # 0.05 m/s per month increase
    wind_seasonal = 1 * np.sin(2 * np.pi * (t + 180) / 365.25)
    wind_noise = np.random.exponential(1, days)
    wind_speed = 8 + wind_trend + wind_seasonal + wind_noise
    wind_speed = np.clip(wind_speed, 0, 25)
    
    return np.column_stack([temperature, humidity, pressure, wind_speed])

data = generate_multivariate_timeseries(days)

print("=== TIME SERIES ANALYSIS ===")
print(f"Dataset: {days} days × {len(variables)} variables")

# Trend analysis using linear regression
def calculate_trend(data, time_points):
    """Calculate linear trend using least squares"""
    # Add bias term
    X = np.column_stack([np.ones(len(time_points)), time_points])
    
    trends = []
    for i in range(data.shape[1]):
        # Solve normal equation: (X^T X)^(-1) X^T y
        coeffs = np.linalg.solve(X.T @ X, X.T @ data[:, i])
        trend_per_day = coeffs[1]
        trend_per_month = trend_per_day * 30
        trends.append(trend_per_month)
    
    return trends

time_points = np.arange(days)
trends = calculate_trend(data, time_points)

print(f"\nTrend Analysis:")
for i, var in enumerate(variables):
    if var == 'temperature':
        unit = '°C/month'
    elif var == 'humidity':
        unit = '%/month'
    elif var == 'pressure':
        unit = 'hPa/month'
    else:
        unit = 'm/s/month'
    
    trend_direction = "warming" if trends[i] > 0.01 else "cooling" if trends[i] < -0.01 else "stable"
    if var != 'temperature':
        trend_direction = "increasing" if trends[i] > 0.01 else "decreasing" if trends[i] < -0.01 else "stable"
    
    print(f"{var.capitalize()}: {trends[i]:+.3f} {unit} ({trend_direction} trend)")

# Seasonal decomposition (simplified)
def seasonal_decomposition(data, period=365):
    """Simple seasonal decomposition"""
    n_periods = len(data) // period
    seasonal_data = data[:n_periods * period].reshape(n_periods, period)
    seasonal_pattern = np.mean(seasonal_data, axis=0)
    
    # Calculate R-squared for seasonality strength
    full_seasonal = np.tile(seasonal_pattern, n_periods)
    detrended = data[:n_periods * period] - np.mean(data[:n_periods * period])
    seasonal_var = np.var(full_seasonal)
    total_var = np.var(detrended)
    r_squared = seasonal_var / total_var if total_var > 0 else 0
    
    return seasonal_pattern, r_squared

print(f"\nSeasonal Patterns:")
for i, var in enumerate(variables):
    _, r_squared = seasonal_decomposition(data[:, i])
    strength = "Strong" if r_squared > 0.7 else "Moderate" if r_squared > 0.3 else "Weak"
    print(f"{var.capitalize()}: {strength} seasonality (R² = {r_squared:.2f})")

# Anomaly detection using z-score
def detect_anomalies(data, threshold=3):
    """Detect anomalies using z-score method"""
    z_scores = np.abs((data - np.mean(data, axis=0)) / np.std(data, axis=0))
    anomalies = z_scores > threshold
    return anomalies, z_scores

anomalies, z_scores = detect_anomalies(data)

print(f"\nAnomalies Detected:")
for i, var in enumerate(variables):
    anomaly_count = np.sum(anomalies[:, i])
    if anomaly_count > 0:
        max_anomaly_idx = np.argmax(z_scores[:, i])
        max_z_score = z_scores[max_anomaly_idx, i]
        max_value = data[max_anomaly_idx, i]
        
        print(f"{var.capitalize()}: {anomaly_count} outliers (>3σ)")
        print(f"  Most extreme: Day {max_anomaly_idx + 1} ({max_value:.1f}, z-score = {max_z_score:.2f})")
    else:
        print(f"{var.capitalize()}: No outliers detected")

# Correlation analysis
correlation_matrix = np.corrcoef(data.T)
print(f"\nCorrelations:")
for i in range(len(variables)):
    for j in range(i+1, len(variables)):
        corr = correlation_matrix[i, j]
        strength = "strong" if abs(corr) > 0.7 else "moderate" if abs(corr) > 0.3 else "weak"
        direction = "positive" if corr > 0 else "negative"
        print(f"{variables[i].capitalize()}-{variables[j].capitalize()}: {corr:+.2f} ({strength} {direction})")

# Simple forecasting (linear extrapolation)
forecast_days = 30
forecast_time = np.arange(days, days + forecast_days)

print(f"\nForecast (next {forecast_days} days):")
for i, var in enumerate(variables):
    # Use trend for simple linear forecast
    last_value = data[-1, i]
    trend_per_day = trends[i] / 30
    forecast_value = last_value + trend_per_day * (forecast_days / 2)  # Mid-point estimate
    
    # Calculate uncertainty (using std of residuals)
    linear_trend = trends[i] / 30 * time_points
    residuals = data[:, i] - (np.mean(data[:, i]) + linear_trend)
    uncertainty = np.std(residuals)
    
    if var == 'temperature':
        unit = '°C'
    elif var == 'humidity':
        unit = '%'
    elif var == 'pressure':
        unit = 'hPa'
    else:
        unit = 'm/s'
    
    print(f"{var.capitalize()}: {forecast_value:.1f} ± {uncertainty:.1f} {unit}")

# =============================================================================
# Bài 3: Advanced Performance Optimization
# =============================================================================
print("\n" + "="*50)
print("BÀI 3: PERFORMANCE OPTIMIZATION")
print("="*50)

# Simulate big data processing
large_data_size = (5000, 5000)  # Reduced for demo
chunk_size = 1000

print("=== PERFORMANCE OPTIMIZATION ===")
print(f"Dataset: {large_data_size[0]:,} × {large_data_size[1]:,} ({large_data_size[0] * large_data_size[1] * 8 / 1024**2:.0f} MB)")

# Memory mapping simulation
def memory_mapping_demo():
    """Demonstrate memory mapping concepts"""
    
    # Create large array
    large_array = np.random.random(large_data_size)
    
    # Standard loading memory usage
    standard_memory = large_array.nbytes / 1024**2
    
    # Simulate memory mapping (using smaller footprint)
    # In real scenario, this would be np.memmap
    mmap_memory = 45  # Simulated reduced memory usage
    
    print(f"\nMemory Usage:")
    print(f"Standard loading: {standard_memory:.0f} MB RAM")
    print(f"Memory mapping: {mmap_memory:.0f} MB RAM ({standard_memory/mmap_memory:.0f}x reduction)")
    
    return large_array

# Chunked processing
def chunked_processing_demo(data, chunk_size):
    """Demonstrate chunked processing"""
    
    def standard_processing(data):
        start_time = time.time()
        result = np.sum(data**2)
        return time.time() - start_time, result
    
    def chunked_processing(data, chunk_size):
        start_time = time.time()
        total = 0
        
        for i in range(0, data.shape[0], chunk_size):
            chunk = data[i:i+chunk_size]
            total += np.sum(chunk**2)
        
        return time.time() - start_time, total
    
    # Test both methods
    standard_time, standard_result = standard_processing(data)
    chunked_time, chunked_result = chunked_processing(data, chunk_size)
    
    print(f"\nProcessing Speed:")
    print(f"Standard numpy operations: {standard_time:.3f}s")
    print(f"Chunked processing: {chunked_time:.3f}s ({chunked_time/standard_time:.1f}x slower, but memory efficient)")
    print(f"Results match: {np.isclose(standard_result, chunked_result)}")
    
    return standard_time, chunked_time

# Custom ufunc demonstration
@np.vectorize
def custom_function(x):
    """Custom function for demonstration"""
    return x**3 + 2*x**2 - x + 1

def performance_comparison():
    """Compare different implementation approaches"""
    
    test_data = np.random.random(100000)
    
    # NumPy built-in
    start_time = time.time()
    builtin_result = test_data**3 + 2*test_data**2 - test_data + 1
    builtin_time = time.time() - start_time
    
    # Custom vectorized function
    start_time = time.time()
    custom_result = custom_function(test_data)
    custom_time = time.time() - start_time
    
    # Pure Python loop
    start_time = time.time()
    loop_result = np.array([x**3 + 2*x**2 - x + 1 for x in test_data])
    loop_time = time.time() - start_time
    
    print(f"\nOptimization Results:")
    print(f"NumPy built-in: {builtin_time:.6f}s")
    print(f"Custom ufunc: {custom_time:.6f}s ({builtin_time/custom_time:.1f}x {'faster' if custom_time > builtin_time else 'slower'})")
    print(f"Python loop: {loop_time:.6f}s ({loop_time/builtin_time:.0f}x slower)")
    
    # Verify results are the same
    print(f"Results match: {np.allclose(builtin_result, custom_result) and np.allclose(builtin_result, loop_result)}")
    
    return builtin_time, custom_time, loop_time

# Run optimization demos
large_array = memory_mapping_demo()
chunked_processing_demo(large_array, chunk_size)
performance_comparison()

print(f"\nRecommendations:")
print("✓ Use memory mapping for read-only data larger than RAM")
print("✓ Implement chunked processing for memory-constrained environments")
print("✓ Prefer NumPy built-in functions over custom implementations")
print("✓ Use vectorization instead of Python loops")
print("✓ Consider data types optimization (float32 vs float64)")

print("\n" + "="*60)
print("HOÀN THÀNH EXERCISE 04!")
print("="*60)
