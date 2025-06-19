# 01. Pandas Introduction & Series Fundamentals

## 🎯 Mục tiêu học tập

Sau khi hoàn thành chương này, bạn sẽ:

- Hiểu được Pandas là gì và tại sao nó quan trọng trong Data Science
- Nắm vững cấu trúc dữ liệu Series và DataFrame
- Biết cách tạo và thao tác với Pandas Series
- Hiểu relationship giữa NumPy và Pandas
- Thực hiện basic operations trên Series

## 📚 Pandas là gì?

**Pandas** (Python Data Analysis Library) là thư viện mạnh mẽ nhất cho data manipulation và analysis trong Python. Nó cung cấp:

- **Data structures**: Series (1D) và DataFrame (2D)
- **Data I/O tools**: Đọc/ghi CSV, Excel, JSON, SQL, HTML...
- **Data cleaning**: Handle missing data, remove duplicates
- **Data transformation**: Grouping, merging, reshaping
- **Analysis tools**: Statistics, time series analysis

### Tại sao Pandas quan trọng?

1. **User-friendly**: Syntax dễ hiểu, tương tự SQL/Excel
2. **Performance**: Built trên NumPy, tối ưu cho big data
3. **Flexibility**: Handle heterogeneous data types
4. **Integration**: Kết hợp tốt với NumPy, Matplotlib, Scikit-learn
5. **Industry standard**: Được sử dụng rộng rãi trong Data Science

## 🔧 Cài đặt và Import

```python
# Cài đặt Pandas
pip install pandas

# Import Pandas
import pandas as pd
import numpy as np

# Kiểm tra version
print(pd.__version__)
```

## 📊 Pandas Series

**Series** là cấu trúc dữ liệu 1-dimensional với labeled data, tương tự như array nhưng có index.

### 1. Tạo Series

```python
import pandas as pd

# Từ list
series_from_list = pd.Series([1, 2, 3, 4, 5])
print(series_from_list)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Từ list với custom index
cities_population = pd.Series(
    [8900000, 1200000, 3500000],
    index=['TP.HCM', 'Đà Nẵng', 'Hà Nội']
)
print(cities_population)
# TP.HCM     8900000
# Đà Nẵng    1200000
# Hà Nội     3500000
# dtype: int64

# Từ dictionary
scores_dict = {'Toán': 8.5, 'Lý': 7.0, 'Hóa': 9.0, 'Sinh': 8.0}
scores_series = pd.Series(scores_dict)
print(scores_series)
# Toán    8.5
# Lý      7.0
# Hóa     9.0
# Sinh    8.0
# dtype: float64

# Từ NumPy array
import numpy as np
np_array = np.random.randn(5)
series_from_numpy = pd.Series(np_array, index=['A', 'B', 'C', 'D', 'E'])
print(series_from_numpy)
```

### 2. Series Attributes

```python
# Tạo series mẫu
temperatures = pd.Series([25, 28, 30, 27, 24],
                        index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                        name='Temperature')

# Các thuộc tính quan trọng
print(f"Values: {temperatures.values}")      # NumPy array
print(f"Index: {temperatures.index}")        # Index object
print(f"Name: {temperatures.name}")          # Series name
print(f"Shape: {temperatures.shape}")        # (5,)
print(f"Size: {temperatures.size}")          # 5
print(f"Dtype: {temperatures.dtype}")        # int64
print(f"Empty: {temperatures.empty}")        # False

# Statistical info
print(f"Mean: {temperatures.mean()}")        # 26.8
print(f"Max: {temperatures.max()}")          # 30
print(f"Min: {temperatures.min()}")          # 24
print(f"Std: {temperatures.std()}")          # 2.49
```

### 3. Indexing và Selection

```python
# Label-based indexing
print(temperatures['Mon'])              # 25
print(temperatures[['Mon', 'Wed']])     # Multiple selection

# Position-based indexing
print(temperatures[0])                  # 25 (first element)
print(temperatures[-1])                 # 24 (last element)
print(temperatures[1:4])                # Slice

# Boolean indexing
hot_days = temperatures[temperatures > 27]
print(hot_days)
# Tue    28
# Wed    30
# dtype: int64

# Conditions
above_average = temperatures[temperatures > temperatures.mean()]
weekend_prep = temperatures[temperatures.index.isin(['Thu', 'Fri'])]
```

### 4. Series Operations

```python
# Arithmetic operations
celsius = pd.Series([0, 20, 30, 40], index=['A', 'B', 'C', 'D'])

# Convert to Fahrenheit
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)
# A     32.0
# B     68.0
# C     86.0
# D    104.0
# dtype: float64

# Mathematical functions
import numpy as np
angles = pd.Series([0, 30, 45, 60, 90], name='degrees')
radians = np.radians(angles)
sine_values = np.sin(radians)

print(sine_values)

# String operations (for string data)
cities = pd.Series(['hà nội', 'tp.hcm', 'đà nẵng'])
cities_proper = cities.str.title()
print(cities_proper)
# 0      Hà Nội
# 1      Tp.Hcm
# 2    Đà Nẵng
# dtype: object
```

### 5. Series Methods

```python
# Sample data
exam_scores = pd.Series([85, 92, 78, 88, 95, 82, 90, 87])

# Descriptive statistics
print(exam_scores.describe())
"""
count     8.000000
mean     87.125000
std       5.815330
min      78.000000
25%      84.250000
50%      87.500000
75%      90.250000
max      95.000000
dtype: float64
"""

# Sorting
sorted_scores = exam_scores.sort_values(ascending=False)
print(sorted_scores)

# Value counts
grades = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'B', 'A'])
grade_counts = grades.value_counts()
print(grade_counts)
# A    4
# B    3
# C    1
# dtype: int64

# Unique values
print(f"Unique grades: {grades.unique()}")
print(f"Number of unique: {grades.nunique()}")

# Apply custom functions
def grade_category(score):
    if score >= 90:
        return 'Excellent'
    elif score >= 80:
        return 'Good'
    elif score >= 70:
        return 'Average'
    else:
        return 'Below Average'

categories = exam_scores.apply(grade_category)
print(categories)
```

## 🔗 Relationship với NumPy

```python
# Series được built trên NumPy
import numpy as np
import pandas as pd

# NumPy array
np_array = np.array([1, 2, 3, 4, 5])
print(f"NumPy array: {np_array}")
print(f"Type: {type(np_array)}")

# Convert to Series
series = pd.Series(np_array)
print(f"Pandas Series: {series}")
print(f"Type: {type(series)}")

# Access underlying NumPy array
underlying_array = series.values
print(f"Underlying array: {underlying_array}")
print(f"Are they same? {np.array_equal(np_array, underlying_array)}")

# NumPy operations work on Series
result = np.sqrt(series)
print(f"Square root: {result}")

# Broadcasting still works
series_2d = series.values.reshape(-1, 1) + series.values
print(f"Broadcasting result shape: {series_2d.shape}")
```

## 📊 Practical Examples

### Example 1: Vietnam Population Analysis

```python
# Vietnam major cities population (millions)
vietnam_cities = pd.Series({
    'TP. Hồ Chí Minh': 9.0,
    'Hà Nội': 8.1,
    'Hải Phòng': 2.0,
    'Đà Nẵng': 1.2,
    'Cần Thơ': 1.2,
    'Biên Hòa': 1.1,
    'Huế': 0.5,
    'Nha Trang': 0.4,
    'Buôn Ma Thuột': 0.4,
    'Vũng Tàu': 0.3
}, name='Population_Millions')

print("Vietnam Cities Population Analysis")
print("=" * 40)
print(f"Total population: {vietnam_cities.sum():.1f} million")
print(f"Average city size: {vietnam_cities.mean():.1f} million")
print(f"Largest city: {vietnam_cities.idxmax()} ({vietnam_cities.max():.1f}M)")
print(f"Smallest city: {vietnam_cities.idxmin()} ({vietnam_cities.min():.1f}M)")

# Cities with population > 1M
major_cities = vietnam_cities[vietnam_cities >= 1.0]
print(f"\\nMajor cities (≥1M): {len(major_cities)}")
print(major_cities)

# Population percentage
total_pop = vietnam_cities.sum()
percentages = (vietnam_cities / total_pop * 100).round(1)
print("\\nPopulation Distribution:")
for city, pct in percentages.items():
    print(f"{city}: {pct}%")
```

### Example 2: Monthly Sales Analysis

```python
# Monthly sales data (in millions VND)
monthly_sales = pd.Series({
    'Jan': 45.2, 'Feb': 52.1, 'Mar': 48.7, 'Apr': 55.3,
    'May': 61.8, 'Jun': 58.9, 'Jul': 67.2, 'Aug': 69.1,
    'Sep': 63.5, 'Oct': 71.3, 'Nov': 78.9, 'Dec': 82.4
}, name='Sales_Millions_VND')

print("Monthly Sales Analysis")
print("=" * 30)

# Basic statistics
print(f"Total annual sales: {monthly_sales.sum():.1f}M VND")
print(f"Average monthly sales: {monthly_sales.mean():.1f}M VND")
print(f"Best month: {monthly_sales.idxmax()} ({monthly_sales.max():.1f}M)")
print(f"Worst month: {monthly_sales.idxmin()} ({monthly_sales.min():.1f}M)")

# Growth analysis
print("\\nQuarterly Performance:")
q1 = monthly_sales[['Jan', 'Feb', 'Mar']].sum()
q2 = monthly_sales[['Apr', 'May', 'Jun']].sum()
q3 = monthly_sales[['Jul', 'Aug', 'Sep']].sum()
q4 = monthly_sales[['Oct', 'Nov', 'Dec']].sum()

quarterly_sales = pd.Series([q1, q2, q3, q4],
                           index=['Q1', 'Q2', 'Q3', 'Q4'],
                           name='Quarterly_Sales')
print(quarterly_sales)

# Month-over-month growth
mom_growth = monthly_sales.pct_change() * 100
print("\\nMonth-over-Month Growth (%):")
print(mom_growth.dropna().round(1))
```

## 🔍 Missing Data trong Series

```python
# Series with missing data
incomplete_data = pd.Series([100, None, 150, np.nan, 200, 175],
                           index=['A', 'B', 'C', 'D', 'E', 'F'])

print("Original data:")
print(incomplete_data)

# Check for missing data
print(f"\\nHas missing data? {incomplete_data.isnull().any()}")
print(f"Number of missing values: {incomplete_data.isnull().sum()}")
print(f"Number of valid values: {incomplete_data.count()}")

# Handle missing data
print("\\nFilled with mean:")
filled_mean = incomplete_data.fillna(incomplete_data.mean())
print(filled_mean)

print("\\nDrop missing values:")
dropped = incomplete_data.dropna()
print(dropped)

print("\\nForward fill:")
forward_filled = incomplete_data.fillna(method='ffill')
print(forward_filled)
```

## 💡 Best Practices

### 1. Naming Convention

```python
# Good: descriptive names
customer_ages = pd.Series([25, 30, 35, 40], name='customer_age')
monthly_revenue = pd.Series(data, name='revenue_millions_vnd')

# Avoid: unclear names
s1 = pd.Series([1, 2, 3])
data = pd.Series(some_values)
```

### 2. Index Management

```python
# Use meaningful indices
temperatures = pd.Series([25, 28, 30], index=['Monday', 'Tuesday', 'Wednesday'])

# For time series, use datetime index
dates = pd.date_range('2024-01-01', periods=3)
time_series = pd.Series([100, 110, 105], index=dates)
```

### 3. Data Validation

```python
# Always check data after creation
print(f"Data shape: {series.shape}")
print(f"Data type: {series.dtype}")
print(f"Missing values: {series.isnull().sum()}")
print(f"Memory usage: {series.memory_usage()} bytes")
```

## 🎯 Exercises

### Exercise 1: Basic Series Operations

Tạo một Series chứa điểm số của 10 học sinh và thực hiện:

1. Tính điểm trung bình
2. Tìm học sinh có điểm cao nhất/thấp nhất
3. Đếm số học sinh đạt điểm ≥ 8.0
4. Tạo Series mới với điểm được chuẩn hóa (0-10 scale)

### Exercise 2: Real-world Application

Sử dụng dữ liệu giá Bitcoin hàng ngày và:

1. Tạo Series với datetime index
2. Tính volatility (độ biến động)
3. Tìm ngày có giá cao nhất/thấp nhất
4. Tính moving average 7 ngày

### Exercise 3: Data Cleaning

Cho Series với missing data và outliers:

1. Phát hiện và đếm missing values
2. Fill missing data bằng các methods khác nhau
3. Detect outliers sử dụng IQR method
4. So sánh kết quả của các cleaning methods

---

## 📖 Tài liệu tham khảo

- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

**Tiếp theo: DataFrame Fundamentals** 📊
