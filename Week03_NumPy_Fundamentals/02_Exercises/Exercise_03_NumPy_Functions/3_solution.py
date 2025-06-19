"""
Exercise 03 Solutions: NumPy Functions
Week 03 - NumPy Fundamentals

Đáp án chi tiết cho các bài tập về NumPy Functions và Array Manipulation
"""

import numpy as np
import time

print("=" * 60)
print("EXERCISE 03 SOLUTIONS: NumPy Functions")
print("=" * 60)

# =============================================================================
# Bài 1: Quản lý Kho hàng thông minh
# =============================================================================
print("\n" + "="*50)
print("BÀI 1: QUẢN LÝ KHO HÀNG THÔNG MINH")
print("="*50)

# 1. Tạo database sản phẩm với structured array
product_dtype = np.dtype([
    ('id', 'i4'),
    ('name', 'U30'),
    ('price', 'f8'),
    ('quantity', 'i4'),
    ('category', 'U20')
])

# Sample products data
products_data = [
    (1001, 'Laptop Dell Inspiron', 15000000, 50, 'Electronics'),
    (1002, 'iPhone 15', 25000000, 30, 'Electronics'),
    (1003, 'Samsung Galaxy S24', 22000000, 25, 'Electronics'),
    (1004, 'Bàn gỗ văn phòng', 2000000, 20, 'Furniture'),
    (1005, 'Ghế ergonomic', 3500000, 15, 'Furniture'),
    (1006, 'MacBook Pro M3', 35000000, 10, 'Electronics'),
    (1007, 'Tủ sách gỗ', 4500000, 12, 'Furniture'),
    (1008, 'Máy in Canon', 8000000, 8, 'Electronics'),
    (1009, 'Bàn ăn 6 chỗ', 6000000, 5, 'Furniture'),
    (1010, 'Sofa 3 chỗ', 12000000, 3, 'Furniture')
]

products = np.array(products_data, dtype=product_dtype)

print("=== INVENTORY MANAGEMENT SYSTEM ===")
print(f"Total products: {len(products)}")

# Tính tổng giá trị kho
total_value = np.sum(products['price'] * products['quantity'])
print(f"Total inventory value: {total_value:,.0f} VND")

# 2. Search functions
def search_by_name(products, keyword):
    """Search products by name keyword"""
    mask = np.char.find(products['name'].astype(str), keyword) >= 0
    return products[mask]

def sort_by_price(products, ascending=True):
    """Sort products by price"""
    if ascending:
        return np.sort(products, order='price')
    else:
        return np.sort(products, order='price')[::-1]

def filter_by_category(products, category):
    """Filter products by category"""
    return products[products['category'] == category]

# Test search functions
print(f"\nSearch results for 'iPhone':")
iphone_products = search_by_name(products, 'iPhone')
for product in iphone_products:
    print(f"  {product['name']}: {product['price']:,.0f} VND")

# 3. Tính statistics
categories = np.unique(products['category'])
print(f"\nCategory Statistics:")
for category in categories:
    cat_products = filter_by_category(products, category)
    avg_price = np.mean(cat_products['price'])
    total_qty = np.sum(cat_products['quantity'])
    print(f"{category}: {len(cat_products)} items, avg price: {avg_price:,.0f} VND, total qty: {total_qty}")

# Top 5 most expensive
expensive_products = sort_by_price(products, ascending=False)[:5]
print(f"\nTop 5 most expensive:")
for i, product in enumerate(expensive_products, 1):
    print(f"{i}. {product['name']}: {product['price']:,.0f} VND (qty: {product['quantity']})")

# Low stock alert
low_stock = products[products['quantity'] < 10]
print(f"\nLow stock alert (<10): {len(low_stock)} products")
for product in low_stock:
    print(f"  {product['name']}: {product['quantity']} units")

# 4. Save/Load operations
print(f"\nSaving inventory data...")
np.save('inventory_data.npy', products)
print("Data saved to inventory_data.npy")

# Load and verify
loaded_products = np.load('inventory_data.npy')
print(f"Loaded {len(loaded_products)} products successfully")

# =============================================================================
# Bài 2: Weather Data Analysis
# =============================================================================
print("\n" + "="*50)
print("BÀI 2: WEATHER DATA ANALYSIS")
print("="*50)

np.random.seed(42)

# 1. Generate synthetic weather data
def generate_weather_data(days=365, base_temp=25, seasonal_amplitude=8, daily_noise=3):
    """Generate realistic weather data with seasonal patterns"""
    
    # Time array (day of year)
    time = np.arange(days)
    
    # Seasonal temperature pattern (sine wave)
    seasonal_temp = base_temp + seasonal_amplitude * np.sin(2 * np.pi * (time - 80) / 365)
    
    # Add daily noise
    daily_variation = np.random.normal(0, daily_noise, days)
    temperature = seasonal_temp + daily_variation
    
    # Humidity (inverse relationship with temperature)
    humidity = 85 - 0.8 * (temperature - base_temp) + np.random.normal(0, 5, days)
    humidity = np.clip(humidity, 30, 95)  # Realistic range
    
    # Rainfall (more in certain seasons)
    rain_probability = 0.3 + 0.2 * np.sin(2 * np.pi * (time + 30) / 365)
    rainfall = np.where(np.random.random(days) < rain_probability,
                       np.random.exponential(5), 0)
    
    # Wind speed
    wind_speed = 5 + 3 * np.sin(2 * np.pi * time / 365) + np.random.exponential(2, days)
    wind_speed = np.clip(wind_speed, 0, 25)
    
    return {
        'temperature': temperature,
        'humidity': humidity,
        'rainfall': rainfall,
        'wind_speed': wind_speed,
        'day': time + 1
    }

weather_data = generate_weather_data(365)

print("=== WEATHER ANALYSIS REPORT ===")
print("Dataset: 365 days of weather data")

# 2. Basic statistics
temp = weather_data['temperature']
humidity = weather_data['humidity']
rainfall = weather_data['rainfall']

print(f"\nTemperature Statistics:")
print(f"Mean: {np.mean(temp):.1f}°C")
print(f"Median: {np.median(temp):.1f}°C")
print(f"Std: {np.std(temp):.1f}°C")
print(f"Min: {np.min(temp):.1f}°C (Day {np.argmin(temp)+1})")
print(f"Max: {np.max(temp):.1f}°C (Day {np.argmax(temp)+1})")

# 3. Seasonal analysis
def get_season_mask(day, season):
    """Get boolean mask for season"""
    if season == 'Spring':
        return (day >= 60) & (day < 152)  # Mar-May
    elif season == 'Summer':
        return (day >= 152) & (day < 244)  # Jun-Aug  
    elif season == 'Autumn':
        return (day >= 244) & (day < 335)  # Sep-Nov
    else:  # Winter
        return (day >= 335) | (day < 60)  # Dec-Feb

seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
print(f"\nSeasonal Averages:")
for season in seasons:
    mask = get_season_mask(weather_data['day'], season)
    avg_temp = np.mean(temp[mask])
    print(f"{season}: {avg_temp:.1f}°C")

# 4. Extreme events
heat_waves = temp > 35
cold_snaps = temp < 10
heavy_rain = rainfall > 20

print(f"\nExtreme Events:")
print(f"Heat waves (>35°C): {np.sum(heat_waves)} days")
print(f"Cold snaps (<10°C): {np.sum(cold_snaps)} days")
print(f"Heavy rain (>20mm): {np.sum(heavy_rain)} days")
print(f"Record high: {np.max(temp):.1f}°C")
print(f"Record low: {np.min(temp):.1f}°C")

# 5. Export data
weather_export = np.column_stack([
    weather_data['day'],
    weather_data['temperature'],
    weather_data['humidity'], 
    weather_data['rainfall'],
    weather_data['wind_speed']
])

np.savetxt('weather_data.csv', weather_export, 
           delimiter=',',
           header='Day,Temperature,Humidity,Rainfall,WindSpeed',
           comments='')

print(f"\nData exported to: weather_data.csv")

# =============================================================================
# Bài 3: Advanced Array Manipulation
# =============================================================================
print("\n" + "="*50)
print("BÀI 3: ADVANCED ARRAY MANIPULATION")
print("="*50)

size = 50  # Reduced for demo

# 1. Pattern generation
def create_spiral(size):
    """Create spiral pattern"""
    arr = np.zeros((size, size))
    x, y = size // 2, size // 2
    dx, dy = 0, -1
    
    for i in range(size**2):
        arr[x, y] = i
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        
    return arr

def create_checkerboard(size):
    """Create checkerboard pattern"""
    arr = np.zeros((size, size))
    arr[1::2, ::2] = 1
    arr[::2, 1::2] = 1
    return arr

def create_gradient(size):
    """Create gradient pattern"""
    x = np.linspace(0, 1, size)
    y = np.linspace(0, 1, size)
    X, Y = np.meshgrid(x, y)
    return np.sqrt(X**2 + Y**2)

print("=== ARRAY MANIPULATION DEMO ===")

# Test pattern generation
start_time = time.time()
spiral = create_spiral(size)
spiral_time = time.time() - start_time

start_time = time.time()
checkerboard = create_checkerboard(size)
checker_time = time.time() - start_time

start_time = time.time()
gradient = create_gradient(size)
gradient_time = time.time() - start_time

print(f"\nPattern Generation:")
print(f"Spiral ({size}x{size}): Created in {spiral_time:.6f}s")
print(f"Checkerboard ({size}x{size}): Created in {checker_time:.6f}s")
print(f"Gradient ({size}x{size}): Created in {gradient_time:.6f}s")

# 2. Sorting performance
test_array = np.random.random(10000)

start_time = time.time()
np_sorted = np.sort(test_array.copy())
numpy_time = time.time() - start_time

start_time = time.time()
py_sorted = sorted(test_array.copy())
python_time = time.time() - start_time

speedup = python_time / numpy_time

print(f"\nSorting Performance (10000 elements):")
print(f"np.sort(): {numpy_time:.6f}s")
print(f"Python sorted(): {python_time:.6f}s")
print(f"Speedup: {speedup:.1f}x")

# 3. Memory usage analysis
original_array = np.random.random((100, 100))
print(f"\nMemory Usage:")
print(f"Original array: {original_array.nbytes / 1024:.2f} KB")

# Views vs copies
view = original_array[::2, ::2]  # Strided view
copy = original_array[::2, ::2].copy()  # Explicit copy

print(f"View operations: {0 if view.base is original_array else view.nbytes/1024:.2f} KB extra")
print(f"Copy operations: {copy.nbytes/1024:.2f} KB extra")

# 4. Reshaping operations
print(f"\nReshaping Operations:")
flat = original_array.flatten()
print(f"1D -> 2D: ✓ ({'view' if flat.base is None else 'copy'})")

reshaped = original_array.reshape(50, 200)
print(f"2D reshape: ✓ ({'view' if reshaped.base is original_array else 'copy'})")

transposed = original_array.T
print(f"Transpose: ✓ ({'view' if transposed.base is original_array else 'copy'})")

print("\n" + "="*60)
print("HOÀN THÀNH EXERCISE 03!")
print("="*60)
