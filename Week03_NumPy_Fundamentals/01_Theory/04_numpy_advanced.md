# NumPy Advanced Topics

## Mục lục

1. [Advanced Indexing](#advanced-indexing)
2. [Structured Arrays](#structured-arrays)
3. [Memory Layout và Performance](#memory-layout-và-performance)
4. [NumPy với Geographic Data](#numpy-với-geographic-data)
5. [Custom Functions và Vectorization](#custom-functions-và-vectorization)
6. [Integration với Other Libraries](#integration-với-other-libraries)
7. [Real-world Applications](#real-world-applications)

---

## Advanced Indexing

### 1. Boolean Indexing Advanced

```python
import numpy as np

# Tạo dữ liệu mẫu - điểm thi của students
np.random.seed(42)
scores = np.random.randint(0, 101, (100, 3))  # 100 students, 3 subjects
student_ids = np.arange(1000, 1100)  # ID từ 1000-1099

print(f"Scores shape: {scores.shape}")
print("First 5 students:")
print(scores[:5])

# Complex boolean conditions
# Students đạt >= 80 điểm ở tất cả môn
excellent_mask = np.all(scores >= 80, axis=1)
excellent_students = student_ids[excellent_mask]
print(f"\nExcellent students (all subjects >= 80): {len(excellent_students)}")
print(f"Their IDs: {excellent_students[:5]}")

# Students có ít nhất 1 môn < 50
failing_mask = np.any(scores < 50, axis=1)
failing_students = student_ids[failing_mask]
print(f"\nStudents with at least one subject < 50: {len(failing_students)}")

# Students có điểm trung bình 70-85
avg_scores = scores.mean(axis=1)
good_students = student_ids[(avg_scores >= 70) & (avg_scores <= 85)]
print(f"\nGood students (avg 70-85): {len(good_students)}")

# Conditional replacement
scores_adjusted = scores.copy()
scores_adjusted[scores_adjusted < 40] = 40  # Minimum score policy
print(f"\nAdjusted scores (min 40): {(scores_adjusted >= 40).all()}")
```

### 2. Fancy Indexing

```python
# Tạo data cho fancy indexing
data = np.random.randint(1, 100, (8, 8))
print("Original data:")
print(data)

# Select specific rows và columns
rows = [1, 3, 5]
cols = [0, 2, 4, 6]
subset = data[np.ix_(rows, cols)]  # ix_ creates open mesh
print(f"\nSubset (rows {rows}, cols {cols}):")
print(subset)

# Fancy indexing với arrays
row_indices = np.array([0, 2, 4])
col_indices = np.array([1, 3, 5])
elements = data[row_indices, col_indices]  # Diagonal elements
print(f"\nDiagonal elements: {elements}")

# Rearrange rows/columns
new_order = [7, 5, 3, 1, 6, 4, 2, 0]
reordered = data[new_order]
print("\nReordered rows:")
print(reordered)
```

### 3. Multi-dimensional Advanced Indexing

```python
# 3D array indexing
arr_3d = np.random.randint(1, 10, (4, 5, 6))
print(f"3D array shape: {arr_3d.shape}")

# Select elements từ mỗi "page"
pages = [0, 1, 2, 3]
rows = [0, 2, 4, 1]
cols = [0, 1, 2, 3]
selected = arr_3d[pages, rows, cols]
print(f"Selected elements: {selected}")

# Boolean indexing in 3D
# Tìm tất cả elements > 7
high_values = arr_3d > 7
high_positions = np.where(high_values)
print(f"\nPositions with values > 7:")
print(f"Pages: {high_positions[0][:5]}")  # First 5
print(f"Rows: {high_positions[1][:5]}")
print(f"Cols: {high_positions[2][:5]}")
print(f"Values: {arr_3d[high_values][:5]}")
```

---

## Structured Arrays

### 1. Basic Structured Arrays

```python
# Define data type cho student records
student_dtype = np.dtype([
    ('id', 'i4'),           # 4-byte integer
    ('name', 'U20'),        # Unicode string, 20 chars
    ('age', 'i1'),          # 1-byte integer
    ('gpa', 'f4'),          # 4-byte float
    ('graduated', '?')      # boolean
])

# Tạo structured array
students = np.array([
    (1001, 'Alice Johnson', 22, 3.8, True),
    (1002, 'Bob Smith', 21, 3.2, False),
    (1003, 'Carol Davis', 23, 3.9, True),
    (1004, 'David Wilson', 20, 2.8, False),
    (1005, 'Eva Brown', 22, 3.6, False)
], dtype=student_dtype)

print("Student records:")
print(students)

# Access fields
print(f"\nStudent names: {students['name']}")
print(f"GPAs: {students['gpa']}")
print(f"Graduated students: {students[students['graduated']]['name']}")

# Sort by GPA
sorted_students = np.sort(students, order='gpa')
print("\nSorted by GPA:")
for student in sorted_students:
    print(f"{student['name']}: {student['gpa']}")
```

### 2. Geographic Data với Structured Arrays

```python
# Define data type cho geographic points
point_dtype = np.dtype([
    ('id', 'i4'),
    ('lat', 'f8'),          # Latitude (double precision)
    ('lon', 'f8'),          # Longitude (double precision)
    ('elevation', 'f4'),    # Elevation in meters
    ('location_name', 'U50'),
    ('country', 'U20')
])

# Sample geographic data (Vietnam cities)
cities = np.array([
    (1, 21.0285, 105.8542, 12.0, 'Hanoi', 'Vietnam'),
    (2, 10.8231, 106.6297, 19.0, 'Ho Chi Minh City', 'Vietnam'),
    (3, 16.0544, 108.2022, 13.0, 'Da Nang', 'Vietnam'),
    (4, 21.5873, 105.8503, 1682.0, 'Sapa', 'Vietnam'),
    (5, 11.9404, 109.3439, 1500.0, 'Dalat', 'Vietnam')
], dtype=point_dtype)

print("Vietnam cities:")
for city in cities:
    print(f"{city['location_name']}: ({city['lat']:.4f}, {city['lon']:.4f}) - {city['elevation']}m")

# Calculate distances (Haversine formula simplified)
def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points on Earth"""
    R = 6371  # Earth radius in km

    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c

# Distance from Hanoi to other cities
hanoi = cities[0]
distances = []
for city in cities[1:]:
    dist = haversine_distance(hanoi['lat'], hanoi['lon'],
                             city['lat'], city['lon'])
    distances.append((city['location_name'], dist))

print(f"\nDistances from {hanoi['location_name']}:")
for name, dist in distances:
    print(f"To {name}: {dist:.1f} km")
```

---

## Memory Layout và Performance

### 1. Array Layout và Views

```python
# Row-major (C) vs Column-major (Fortran) layout
arr_c = np.arange(12).reshape(3, 4, order='C')
arr_f = np.arange(12).reshape(3, 4, order='F')

print("C-order (row-major):")
print(arr_c)
print(f"Flags: C_CONTIGUOUS={arr_c.flags['C_CONTIGUOUS']}, F_CONTIGUOUS={arr_c.flags['F_CONTIGUOUS']}")

print("\nF-order (column-major):")
print(arr_f)
print(f"Flags: C_CONTIGUOUS={arr_f.flags['C_CONTIGUOUS']}, F_CONTIGUOUS={arr_f.flags['F_CONTIGUOUS']}")

# Memory layout affects performance
import time

# Test với large array
large_arr = np.random.random((1000, 1000))

# Row access (faster for C-order)
start = time.time()
for i in range(1000):
    _ = large_arr[i, :].sum()
row_time = time.time() - start

# Column access (slower for C-order)
start = time.time()
for j in range(1000):
    _ = large_arr[:, j].sum()
col_time = time.time() - start

print(f"\nPerformance (C-order array):")
print(f"Row access time: {row_time:.4f}s")
print(f"Column access time: {col_time:.4f}s")
print(f"Ratio: {col_time/row_time:.2f}x slower")
```

### 2. Memory Optimization

```python
# Memory usage comparison
def print_memory_info(arr, name):
    print(f"{name}:")
    print(f"  Shape: {arr.shape}")
    print(f"  Dtype: {arr.dtype}")
    print(f"  Memory: {arr.nbytes / 1024:.1f} KB")
    print(f"  Items: {arr.size}")
    print()

# Different data types
big_array = np.random.randint(0, 255, (1000, 1000))

# Convert to appropriate dtype
as_uint8 = big_array.astype(np.uint8)    # 0-255 fits in uint8
as_float64 = big_array.astype(np.float64)  # Unnecessary precision

print_memory_info(big_array, "Original (int64)")
print_memory_info(as_uint8, "As uint8")
print_memory_info(as_float64, "As float64")

# Sparse data representation (concept)
# For arrays with many zeros, consider scipy.sparse
sparse_data = np.zeros((1000, 1000))
sparse_data[100:200, 100:200] = np.random.random((100, 100))

print(f"Sparse array:")
print(f"  Non-zero elements: {np.count_nonzero(sparse_data)}")
print(f"  Sparsity: {(1 - np.count_nonzero(sparse_data)/sparse_data.size)*100:.1f}%")
```

---

## NumPy với Geographic Data

### 1. Coordinate Transformations

```python
# Work với geographic coordinates
def geographic_operations():
    # Sample coordinates (lat, lon) của các điểm ở Việt Nam
    coordinates = np.array([
        [21.0285, 105.8542],  # Hanoi
        [10.8231, 106.6297],  # Ho Chi Minh City
        [16.0544, 108.2022],  # Da Nang
        [20.9633, 107.0840],  # Halong Bay
        [15.8801, 108.3380],  # Hoi An
    ])

    lats, lons = coordinates[:, 0], coordinates[:, 1]

    # Convert to radians
    lats_rad = np.radians(lats)
    lons_rad = np.radians(lons)

    # Calculate center point
    center_lat = np.mean(lats)
    center_lon = np.mean(lons)

    print(f"Center coordinates: ({center_lat:.4f}, {center_lon:.4f})")

    # Simple projection to cartesian (for small areas)
    # This is a simplified version, real projections are more complex
    R = 6371000  # Earth radius in meters

    x = R * lons_rad * np.cos(np.radians(center_lat))
    y = R * lats_rad

    print("\nProjected coordinates (meters from center):")
    for i, (name, xi, yi) in enumerate(zip(
        ['Hanoi', 'Ho Chi Minh City', 'Da Nang', 'Halong Bay', 'Hoi An'],
        x, y)):
        print(f"{name}: ({xi:.0f}, {yi:.0f})")

    return coordinates, x, y

coordinates, x, y = geographic_operations()
```

### 2. Raster Data Processing

```python
# Simulate raster data (elevation map)
def create_elevation_map():
    # Create a synthetic elevation map
    x = np.linspace(0, 100, 100)  # 100km x 100km area
    y = np.linspace(0, 100, 100)
    X, Y = np.meshgrid(x, y)

    # Create synthetic elevation with multiple peaks
    elevation = (
        500 * np.exp(-((X-30)**2 + (Y-70)**2) / 200) +  # Peak 1
        800 * np.exp(-((X-70)**2 + (Y-30)**2) / 300) +  # Peak 2
        200 * np.exp(-((X-50)**2 + (Y-50)**2) / 400) +  # Peak 3
        np.random.normal(0, 50, (100, 100))              # Noise
    )

    elevation = np.maximum(elevation, 0)  # No negative elevation

    print(f"Elevation map created: {elevation.shape}")
    print(f"Elevation range: {elevation.min():.1f}m to {elevation.max():.1f}m")

    # Calculate slope (gradient magnitude)
    grad_y, grad_x = np.gradient(elevation)
    slope = np.sqrt(grad_x**2 + grad_y**2)

    print(f"Slope range: {slope.min():.3f} to {slope.max():.3f}")

    # Find peaks (local maxima)
    from scipy.ndimage import maximum_filter
    local_maxima = elevation == maximum_filter(elevation, size=5)
    peak_positions = np.where(local_maxima & (elevation > np.percentile(elevation, 95)))

    print(f"Number of peaks found: {len(peak_positions[0])}")

    return elevation, slope, peak_positions

# Note: scipy import is just for demonstration
# In real application, you might implement maximum_filter manually
```

---

## Custom Functions và Vectorization

### 1. Creating Universal Functions (ufuncs)

```python
# Custom function cho geographic calculations
def haversine_ufunc(lat1, lon1, lat2, lon2):
    """Vectorized haversine distance calculation"""
    R = 6371  # Earth radius in km

    # Convert to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c

# Test với multiple points
origins = np.array([[21.0285, 105.8542],  # Hanoi
                   [10.8231, 106.6297]])  # Ho Chi Minh City

destinations = np.array([[16.0544, 108.2022],  # Da Nang
                        [20.9633, 107.0840],   # Halong Bay
                        [15.8801, 108.3380]])  # Hoi An

# Calculate distances from each origin to each destination
for i, (orig_lat, orig_lon) in enumerate(origins):
    origin_name = ['Hanoi', 'Ho Chi Minh City'][i]
    distances = haversine_ufunc(orig_lat, orig_lon,
                               destinations[:, 0], destinations[:, 1])

    print(f"\nDistances from {origin_name}:")
    dest_names = ['Da Nang', 'Halong Bay', 'Hoi An']
    for name, dist in zip(dest_names, distances):
        print(f"  To {name}: {dist:.1f} km")
```

### 2. Performance Comparison

```python
import time

def python_distance(lat1, lon1, lat2, lon2):
    """Pure Python implementation"""
    import math
    R = 6371

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    return R * c

# Generate test data
n_points = 1000
np.random.seed(42)
lats1 = np.random.uniform(8, 24, n_points)    # Vietnam latitude range
lons1 = np.random.uniform(102, 110, n_points)  # Vietnam longitude range
lats2 = np.random.uniform(8, 24, n_points)
lons2 = np.random.uniform(102, 110, n_points)

# NumPy vectorized version
start = time.time()
numpy_distances = haversine_ufunc(lats1, lons1, lats2, lons2)
numpy_time = time.time() - start

# Pure Python version (loop)
start = time.time()
python_distances = []
for i in range(n_points):
    dist = python_distance(lats1[i], lons1[i], lats2[i], lons2[i])
    python_distances.append(dist)
python_time = time.time() - start

print(f"Performance comparison ({n_points} calculations):")
print(f"NumPy vectorized: {numpy_time:.4f}s")
print(f"Pure Python loop: {python_time:.4f}s")
print(f"Speedup: {python_time/numpy_time:.1f}x")

# Verify results are the same
print(f"Results match: {np.allclose(numpy_distances, python_distances)}")
```

---

## Integration với Other Libraries

### 1. NumPy và Pandas Integration

```python
# Convert structured array to pandas-like operations
student_data = np.array([
    (1001, 'Alice', 22, 3.8, 'CS'),
    (1002, 'Bob', 21, 3.2, 'Math'),
    (1003, 'Carol', 23, 3.9, 'CS'),
    (1004, 'David', 20, 2.8, 'Physics'),
    (1005, 'Eva', 22, 3.6, 'Math')
], dtype=[('id', 'i4'), ('name', 'U10'), ('age', 'i1'),
          ('gpa', 'f4'), ('major', 'U10')])

print("Student data analysis with NumPy:")

# Group by major (manual implementation)
majors = np.unique(student_data['major'])
for major in majors:
    mask = student_data['major'] == major
    students_in_major = student_data[mask]
    avg_gpa = np.mean(students_in_major['gpa'])
    avg_age = np.mean(students_in_major['age'])
    count = len(students_in_major)

    print(f"{major}: {count} students, avg GPA: {avg_gpa:.2f}, avg age: {avg_age:.1f}")
```

### 2. Working với Image-like Data

```python
# Simulate satellite image processing
def process_satellite_image():
    # Simulate a 3-band satellite image (RGB or NIR, Red, Green)
    np.random.seed(42)
    height, width, bands = 100, 100, 3

    # Create synthetic image with different regions
    image = np.zeros((height, width, bands))

    # Water bodies (low values in all bands)
    water_mask = (np.random.random((height, width)) < 0.2)
    image[water_mask] = np.random.uniform(0.1, 0.3, (np.sum(water_mask), bands))

    # Vegetation (high in band 0, moderate in others - simulating NIR)
    veg_mask = (np.random.random((height, width)) < 0.4) & ~water_mask
    image[veg_mask, 0] = np.random.uniform(0.6, 0.9, np.sum(veg_mask))  # High NIR
    image[veg_mask, 1] = np.random.uniform(0.2, 0.4, np.sum(veg_mask))  # Low Red
    image[veg_mask, 2] = np.random.uniform(0.3, 0.6, np.sum(veg_mask))  # Moderate Green

    # Urban areas
    urban_mask = ~(water_mask | veg_mask)
    image[urban_mask] = np.random.uniform(0.4, 0.7, (np.sum(urban_mask), bands))

    print(f"Satellite image shape: {image.shape}")
    print(f"Water pixels: {np.sum(water_mask)}")
    print(f"Vegetation pixels: {np.sum(veg_mask)}")
    print(f"Urban pixels: {np.sum(urban_mask)}")

    # Calculate NDVI (Normalized Difference Vegetation Index)
    # NDVI = (NIR - Red) / (NIR + Red)
    nir_band = image[:, :, 0]
    red_band = image[:, :, 1]

    # Avoid division by zero
    denominator = nir_band + red_band
    ndvi = np.where(denominator != 0,
                   (nir_band - red_band) / denominator,
                   0)

    print(f"\nNDVI statistics:")
    print(f"Mean NDVI: {np.mean(ndvi):.3f}")
    print(f"NDVI range: {np.min(ndvi):.3f} to {np.max(ndvi):.3f}")

    # Classify based on NDVI
    water_classified = ndvi < 0
    vegetation_classified = ndvi > 0.3
    urban_classified = (ndvi >= 0) & (ndvi <= 0.3)

    print(f"\nClassification results:")
    print(f"Water: {np.sum(water_classified)} pixels")
    print(f"Vegetation: {np.sum(vegetation_classified)} pixels")
    print(f"Urban: {np.sum(urban_classified)} pixels")

    return image, ndvi

image, ndvi = process_satellite_image()
```

---

## Real-world Applications

### 1. Time Series Analysis

```python
# Simulate weather station data
def weather_analysis():
    # 2 years of daily data
    days = 730
    np.random.seed(42)

    # Generate synthetic weather data
    date_index = np.arange(days)

    # Temperature with seasonal variation
    temperature = (
        20 +  # Base temperature
        10 * np.sin(2 * np.pi * date_index / 365.25) +  # Seasonal
        np.random.normal(0, 3, days)  # Daily variation
    )

    # Humidity (inverse correlation with temperature)
    humidity = (
        70 -
        0.5 * (temperature - 20) +
        np.random.normal(0, 10, days)
    )
    humidity = np.clip(humidity, 0, 100)

    # Rainfall (more in summer, exponential distribution)
    seasonal_rain = 1 + 0.5 * np.sin(2 * np.pi * (date_index + 90) / 365.25)
    rainfall = np.random.exponential(seasonal_rain, days)

    print("Weather data analysis:")
    print(f"Temperature: {temperature.mean():.1f}°C ± {temperature.std():.1f}")
    print(f"Humidity: {humidity.mean():.1f}% ± {humidity.std():.1f}")
    print(f"Rainfall: {rainfall.mean():.1f}mm/day ± {rainfall.std():.1f}")

    # Monthly aggregation
    months = days // 30
    monthly_temp = temperature[:months*30].reshape(months, 30).mean(axis=1)
    monthly_rain = rainfall[:months*30].reshape(months, 30).sum(axis=1)

    print(f"\nMonthly statistics:")
    print(f"Hottest month avg: {monthly_temp.max():.1f}°C")
    print(f"Coolest month avg: {monthly_temp.min():.1f}°C")
    print(f"Wettest month: {monthly_rain.max():.1f}mm")
    print(f"Driest month: {monthly_rain.min():.1f}mm")

    # Find extreme events
    hot_days = np.where(temperature > temperature.mean() + 2*temperature.std())[0]
    cold_days = np.where(temperature < temperature.mean() - 2*temperature.std())[0]
    heavy_rain_days = np.where(rainfall > np.percentile(rainfall, 95))[0]

    print(f"\nExtreme events:")
    print(f"Very hot days (>2σ): {len(hot_days)}")
    print(f"Very cold days (<-2σ): {len(cold_days)}")
    print(f"Heavy rain days (>95th percentile): {len(heavy_rain_days)}")

    return {
        'temperature': temperature,
        'humidity': humidity,
        'rainfall': rainfall,
        'monthly_temp': monthly_temp,
        'monthly_rain': monthly_rain
    }

weather_data = weather_analysis()
```

### 2. Spatial Data Analysis

```python
# Analyze point patterns (e.g., tree locations in a forest)
def spatial_analysis():
    # Generate random points in a 1000x1000 meter area
    np.random.seed(42)
    n_points = 200

    # Create clustered points (simulate tree groves)
    n_clusters = 5
    cluster_centers = np.random.uniform(100, 900, (n_clusters, 2))

    points = []
    cluster_labels = []

    for i, center in enumerate(cluster_centers):
        # Number of points per cluster (variable)
        n_in_cluster = np.random.poisson(40)

        # Generate points around cluster center
        cluster_points = np.random.multivariate_normal(
            center, [[2500, 0], [0, 2500]], n_in_cluster
        )

        # Keep points within bounds
        valid = ((cluster_points >= 0) & (cluster_points <= 1000)).all(axis=1)
        cluster_points = cluster_points[valid]

        points.extend(cluster_points)
        cluster_labels.extend([i] * len(cluster_points))

    points = np.array(points)
    cluster_labels = np.array(cluster_labels)

    print(f"Spatial analysis of {len(points)} points:")

    # Calculate distances to nearest neighbors
    from scipy.spatial.distance import cdist

    # For demonstration, we'll implement a simple version
    def nearest_neighbor_distances(points):
        distances = []
        for i, point in enumerate(points):
            other_points = np.delete(points, i, axis=0)
            dists = np.sqrt(np.sum((other_points - point)**2, axis=1))
            distances.append(np.min(dists))
        return np.array(distances)

    # Simplified implementation (would use scipy.spatial in practice)
    nn_distances = []
    for i in range(len(points)):
        dists = np.sqrt(np.sum((points - points[i])**2, axis=1))
        dists[i] = np.inf  # Exclude self
        nn_distances.append(np.min(dists))

    nn_distances = np.array(nn_distances)

    print(f"Nearest neighbor distances:")
    print(f"  Mean: {nn_distances.mean():.1f}m")
    print(f"  Std: {nn_distances.std():.1f}m")
    print(f"  Min: {nn_distances.min():.1f}m")
    print(f"  Max: {nn_distances.max():.1f}m")

    # Calculate point density in grid cells
    grid_size = 100  # 100m grid cells
    n_cells = 1000 // grid_size

    density_grid = np.zeros((n_cells, n_cells))

    for point in points:
        grid_x = int(point[0] // grid_size)
        grid_y = int(point[1] // grid_size)
        if 0 <= grid_x < n_cells and 0 <= grid_y < n_cells:
            density_grid[grid_y, grid_x] += 1

    print(f"\nDensity analysis (per {grid_size}m x {grid_size}m cell):")
    print(f"  Mean density: {density_grid.mean():.1f} points/cell")
    print(f"  Max density: {density_grid.max():.0f} points/cell")
    print(f"  Empty cells: {np.sum(density_grid == 0)}/{n_cells**2}")

    return points, cluster_labels, density_grid

points, cluster_labels, density_grid = spatial_analysis()
```

---

## Best Practices và Tips

### 1. Performance Optimization

```python
# Performance tips
def performance_tips():
    # 1. Use appropriate data types
    large_array = np.random.randint(0, 255, (1000, 1000))

    # Bad: using default int64 for small values
    memory_heavy = large_array.astype(np.int64)

    # Good: using appropriate uint8 for 0-255 values
    memory_efficient = large_array.astype(np.uint8)

    print(f"Memory usage:")
    print(f"  int64: {memory_heavy.nbytes / 1024**2:.1f} MB")
    print(f"  uint8: {memory_efficient.nbytes / 1024**2:.1f} MB")
    print(f"  Savings: {(1 - memory_efficient.nbytes/memory_heavy.nbytes)*100:.0f}%")

    # 2. Use broadcasting instead of loops
    matrix = np.random.random((1000, 500))
    vector = np.random.random(500)

    # Bad: explicit loop
    import time
    start = time.time()
    result_loop = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        result_loop[i] = matrix[i] * vector
    loop_time = time.time() - start

    # Good: broadcasting
    start = time.time()
    result_broadcast = matrix * vector
    broadcast_time = time.time() - start

    print(f"\nBroadcasting vs loop:")
    print(f"  Loop time: {loop_time:.4f}s")
    print(f"  Broadcast time: {broadcast_time:.4f}s")
    print(f"  Speedup: {loop_time/broadcast_time:.1f}x")

    # 3. Use views instead of copies when possible
    arr = np.random.random(1000000)

    # View (no memory copy)
    view = arr[::2]
    print(f"\nView shares memory: {view.base is arr}")

    # Copy (memory duplication)
    copy = arr[::2].copy()
    print(f"Copy shares memory: {copy.base is arr}")

performance_tips()
```

### 2. Debugging Tips

```python
def debugging_tips():
    # 1. Check for NaN and infinity
    data = np.array([1, 2, np.nan, 4, np.inf, -np.inf])

    print("Data quality checks:")
    print(f"  Has NaN: {np.isnan(data).any()}")
    print(f"  Has infinity: {np.isinf(data).any()}")
    print(f"  All finite: {np.isfinite(data).all()}")

    # Clean data
    clean_data = data[np.isfinite(data)]
    print(f"  Clean data: {clean_data}")

    # 2. Array information
    arr = np.random.random((100, 50, 3))
    print(f"\nArray info:")
    print(f"  Shape: {arr.shape}")
    print(f"  Dtype: {arr.dtype}")
    print(f"  Memory: {arr.nbytes / 1024:.1f} KB")
    print(f"  C-contiguous: {arr.flags['C_CONTIGUOUS']}")
    print(f"  F-contiguous: {arr.flags['F_CONTIGUOUS']}")

    # 3. Statistical summaries for debugging
    print(f"\nStatistical summary:")
    print(f"  Min: {arr.min():.6f}")
    print(f"  Max: {arr.max():.6f}")
    print(f"  Mean: {arr.mean():.6f}")
    print(f"  Std: {arr.std():.6f}")
    print(f"  Shape consistency: {arr.shape[0] * arr.shape[1] * arr.shape[2] == arr.size}")

debugging_tips()
```

---

## Tổng kết

NumPy advanced topics bao gồm:

1. **Advanced Indexing**: Boolean và fancy indexing cho data filtering phức tạp
2. **Structured Arrays**: Làm việc với heterogeneous data
3. **Memory Management**: Tối ưu performance và memory usage
4. **Geographic Data**: Xử lý dữ liệu không gian địa lý
5. **Custom Functions**: Tạo universal functions và vectorization
6. **Integration**: Kết hợp với các thư viện khác
7. **Real-world Applications**: Ứng dụng thực tế trong phân tích dữ liệu

Những kỹ thuật này là nền tảng cho việc làm việc với:

- Dữ liệu địa lý và viễn thám
- Xử lý ảnh và signal
- Time series analysis
- Machine learning preprocessing
- Scientific computing

Trong phần tiếp theo, chúng ta sẽ ứng dụng các kiến thức NumPy vào pandas và data analysis!
