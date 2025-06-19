# 02. Pandas DataFrame Fundamentals

## 🎯 Mục tiêu học tập

Sau khi hoàn thành chương này, bạn sẽ:

- Hiểu về DataFrame structure và relationship với Series
- Biết cách tạo DataFrame từ nhiều nguồn dữ liệu khác nhau
- Thực hiện basic operations: selection, filtering, sorting
- Hiểu về row/column operations và axis concept
- Handle mixed data types trong DataFrame

## 📊 DataFrame là gì?

**DataFrame** là cấu trúc dữ liệu 2-dimensional với labeled axes (rows và columns). Có thể hiểu DataFrame như:

- **Excel spreadsheet** với named columns và indexed rows
- **SQL table** với structured data
- **Dictionary of Series** sharing the same index
- **2D NumPy array** với labels

### Key Features:

- **Heterogeneous data**: Mỗi column có thể có data type khác nhau
- **Size mutable**: Có thể thêm/xóa rows và columns
- **Labeled axes**: Row index và column names
- **Powerful indexing**: Multiple ways to select data

## 🏗️ Tạo DataFrame

### 1. Từ Dictionary

```python
import pandas as pd
import numpy as np

# Dictionary of lists
student_data = {
    'name': ['Nguyen Van A', 'Tran Thi B', 'Le Van C', 'Pham Thi D'],
    'age': [20, 21, 19, 22],
    'math_score': [8.5, 9.0, 7.5, 8.8],
    'english_score': [7.0, 8.5, 8.0, 9.2],
    'city': ['Ha Noi', 'Ho Chi Minh', 'Da Nang', 'Can Tho']
}

df_students = pd.DataFrame(student_data)
print(df_students)
"""
          name  age  math_score  english_score        city
0  Nguyen Van A   20         8.5            7.0     Ha Noi
1   Tran Thi B   21         9.0            8.5  Ho Chi Minh
2    Le Van C   19         7.5            8.0     Da Nang
3   Pham Thi D   22         8.8            9.2    Can Tho
"""

# Dictionary of Series
math_scores = pd.Series([8.5, 9.0, 7.5, 8.8], name='math')
english_scores = pd.Series([7.0, 8.5, 8.0, 9.2], name='english')

df_scores = pd.DataFrame({
    'math': math_scores,
    'english': english_scores
})
print(df_scores)
```

### 2. Từ List of Dictionaries

```python
# Real-world example: Vietnam provinces data
provinces_data = [
    {'name': 'Ha Noi', 'population': 8.1, 'area': 3358.6, 'region': 'North'},
    {'name': 'Ho Chi Minh', 'population': 9.0, 'area': 2095.0, 'region': 'South'},
    {'name': 'Da Nang', 'population': 1.2, 'area': 1285.4, 'region': 'Central'},
    {'name': 'Can Tho', 'population': 1.2, 'area': 1408.9, 'region': 'South'},
    {'name': 'Hai Phong', 'population': 2.0, 'area': 1561.8, 'region': 'North'}
]

df_provinces = pd.DataFrame(provinces_data)
print(df_provinces)

# Set custom index
df_provinces.set_index('name', inplace=True)
print(df_provinces)
```

### 3. Từ NumPy Array

```python
# Random financial data
np.random.seed(42)
stock_data = np.random.randn(5, 4) * 10 + 100  # Random around 100

df_stocks = pd.DataFrame(
    stock_data,
    columns=['VNM', 'VIC', 'VCB', 'MSN'],  # Vietnam stocks
    index=pd.date_range('2024-01-01', periods=5, freq='D')
)
print(df_stocks)
```

### 4. Từ CSV và External Sources

```python
# Reading from CSV (will cover in detail later)
# df = pd.read_csv('data.csv')

# Creating sample CSV-like data
import io

csv_data = """
product,category,price,quantity,supplier
Laptop,Electronics,15000000,50,Dell
Phone,Electronics,8000000,100,Samsung
Desk,Furniture,2000000,30,IKEA
Chair,Furniture,1500000,40,IKEA
Tablet,Electronics,6000000,25,Apple
"""

df_products = pd.read_csv(io.StringIO(csv_data))
print(df_products)
```

## 📋 DataFrame Attributes

```python
# Using our student DataFrame
print("DataFrame Info:")
print("=" * 40)
print(f"Shape: {df_students.shape}")           # (4, 5) - rows, columns
print(f"Size: {df_students.size}")             # 20 - total elements
print(f"Columns: {df_students.columns.tolist()}")
print(f"Index: {df_students.index.tolist()}")
print(f"Data types:\\n{df_students.dtypes}")

# Memory info
print(f"\\nMemory usage:")
print(df_students.info())

# Quick statistics
print(f"\\nQuick stats:")
print(df_students.describe())
```

## 🔍 Data Selection và Indexing

### 1. Column Selection

```python
# Single column (returns Series)
names = df_students['name']
print(type(names))  # <class 'pandas.core.series.Series'>
print(names)

# Multiple columns (returns DataFrame)
scores = df_students[['name', 'math_score', 'english_score']]
print(type(scores))  # <class 'pandas.core.frame.DataFrame'>
print(scores)

# Using dot notation (only for valid Python identifiers)
ages = df_students.age  # Same as df_students['age']
print(ages)
```

### 2. Row Selection

```python
# Using iloc (integer position)
first_student = df_students.iloc[0]  # Returns Series
print(first_student)

first_two_students = df_students.iloc[0:2]  # Returns DataFrame
print(first_two_students)

# Using loc (label-based)
# First, set meaningful index
df_indexed = df_students.set_index('name')
student_a = df_indexed.loc['Nguyen Van A']
print(student_a)

# Multiple rows
selected_students = df_indexed.loc[['Nguyen Van A', 'Le Van C']]
print(selected_students)
```

### 3. Boolean Indexing

```python
# Students with high math scores
high_math = df_students[df_students['math_score'] > 8.0]
print("Students with math score > 8.0:")
print(high_math)

# Multiple conditions
good_students = df_students[
    (df_students['math_score'] > 8.0) &
    (df_students['english_score'] > 8.0)
]
print("\\nStudents good at both subjects:")
print(good_students)

# String conditions
hanoi_students = df_students[df_students['city'] == 'Ha Noi']
print("\\nStudents from Ha Noi:")
print(hanoi_students)

# Using isin() for multiple values
target_cities = ['Ha Noi', 'Ho Chi Minh']
major_city_students = df_students[df_students['city'].isin(target_cities)]
print("\\nStudents from major cities:")
print(major_city_students)
```

### 4. Advanced Selection with loc và iloc

```python
# loc: [rows, columns] with labels
specific_data = df_indexed.loc['Nguyen Van A', 'math_score']
print(f"Nguyen Van A's math score: {specific_data}")

# Multiple rows and columns
subset = df_indexed.loc[
    ['Nguyen Van A', 'Tran Thi B'],
    ['age', 'math_score', 'english_score']
]
print(subset)

# iloc: [rows, columns] with positions
first_student_scores = df_students.iloc[0, [2, 3]]  # First student, math & english
print(first_student_scores)

# Slicing with iloc
subset_iloc = df_students.iloc[1:3, 1:4]  # Rows 1-2, columns 1-3
print(subset_iloc)
```

## 🔧 Basic DataFrame Operations

### 1. Adding New Columns

```python
# Calculate total score
df_students['total_score'] = df_students['math_score'] + df_students['english_score']

# Calculate average
df_students['average_score'] = df_students['total_score'] / 2

# Conditional column
df_students['grade'] = df_students['average_score'].apply(
    lambda x: 'A' if x >= 9 else 'B' if x >= 8 else 'C' if x >= 7 else 'D'
)

print(df_students)
```

### 2. Modifying Existing Data

```python
# Update specific values
df_students.loc[0, 'age'] = 21  # Update Nguyen Van A's age

# Update multiple values
df_students.loc[df_students['city'] == 'Ha Noi', 'city'] = 'Hanoi'

# Apply transformation to entire column
df_students['name'] = df_students['name'].str.upper()

print(df_students)
```

### 3. Removing Data

```python
# Drop columns
df_no_city = df_students.drop('city', axis=1)  # axis=1 for columns
df_no_multiple = df_students.drop(['total_score', 'average_score'], axis=1)

# Drop rows
df_no_first = df_students.drop(0, axis=0)  # axis=0 for rows (default)

# Drop based on condition
df_filtered = df_students[df_students['age'] >= 20].copy()

print("After removing students under 20:")
print(df_filtered)
```

## 📊 Sorting và Ranking

```python
# Sort by single column
df_sorted_math = df_students.sort_values('math_score', ascending=False)
print("Sorted by math score (descending):")
print(df_sorted_math)

# Sort by multiple columns
df_sorted_multiple = df_students.sort_values(
    ['average_score', 'age'],
    ascending=[False, True]  # Descending by score, ascending by age
)
print("\\nSorted by average score (desc) then age (asc):")
print(df_sorted_multiple)

# Sort by index
df_sorted_index = df_students.sort_index()
print("\\nSorted by index:")
print(df_sorted_index)

# Ranking
df_students['math_rank'] = df_students['math_score'].rank(ascending=False, method='min')
df_students['english_rank'] = df_students['english_score'].rank(ascending=False, method='min')

print("\\nWith rankings:")
print(df_students[['name', 'math_score', 'math_rank', 'english_score', 'english_rank']])
```

## 📈 Aggregation và Grouping Basics

```python
# Basic statistics
print("Basic Statistics:")
print("=" * 30)
print(f"Average math score: {df_students['math_score'].mean():.2f}")
print(f"Average english score: {df_students['english_score'].mean():.2f}")
print(f"Total students: {len(df_students)}")

# Aggregation functions
numeric_summary = df_students[['age', 'math_score', 'english_score']].agg({
    'age': ['mean', 'min', 'max'],
    'math_score': ['mean', 'std', 'min', 'max'],
    'english_score': ['mean', 'std', 'min', 'max']
})
print("\\nNumeric Summary:")
print(numeric_summary)
```

## 🌏 Real-World Example: Vietnam Economic Data

```python
# Create a more comprehensive dataset
vietnam_economic = pd.DataFrame({
    'province': ['Ha Noi', 'Ho Chi Minh', 'Da Nang', 'Can Tho', 'Hai Phong', 'Binh Duong'],
    'population_millions': [8.1, 9.0, 1.2, 1.2, 2.0, 2.5],
    'gdp_billion_usd': [45.2, 67.8, 8.1, 7.2, 12.5, 18.9],
    'area_km2': [3358.6, 2095.0, 1285.4, 1408.9, 1561.8, 2694.4],
    'region': ['North', 'South', 'Central', 'South', 'North', 'South'],
    'coastal': [False, False, True, False, True, False],
    'established_year': [1010, 1698, 1307, 1739, 1149, 1997]
})

print("Vietnam Economic Data Analysis")
print("=" * 40)

# Basic info
print(f"Number of provinces: {len(vietnam_economic)}")
print(f"Total population: {vietnam_economic['population_millions'].sum():.1f} million")
print(f"Total GDP: ${vietnam_economic['gdp_billion_usd'].sum():.1f} billion")

# GDP per capita
vietnam_economic['gdp_per_capita'] = (
    vietnam_economic['gdp_billion_usd'] * 1000 / vietnam_economic['population_millions']
)

# Population density
vietnam_economic['population_density'] = (
    vietnam_economic['population_millions'] * 1000000 / vietnam_economic['area_km2']
)

# Rankings
vietnam_economic['gdp_rank'] = vietnam_economic['gdp_billion_usd'].rank(ascending=False)
vietnam_economic['population_rank'] = vietnam_economic['population_millions'].rank(ascending=False)

print("\\nTop 3 provinces by GDP:")
top_gdp = vietnam_economic.nlargest(3, 'gdp_billion_usd')[['province', 'gdp_billion_usd', 'gdp_per_capita']]
print(top_gdp)

print("\\nRegional distribution:")
regional_stats = vietnam_economic.groupby('region').agg({
    'population_millions': 'sum',
    'gdp_billion_usd': 'sum',
    'province': 'count'
}).round(1)
regional_stats.columns = ['Total_Population', 'Total_GDP', 'Number_of_Provinces']
print(regional_stats)

print("\\nCoastal vs Inland:")
coastal_comparison = vietnam_economic.groupby('coastal').agg({
    'population_millions': 'mean',
    'gdp_billion_usd': 'mean',
    'gdp_per_capita': 'mean'
}).round(1)
print(coastal_comparison)
```

## 🔄 Working with Mixed Data Types

```python
# DataFrame with mixed types
mixed_data = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5],
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones'],
    'price': [25000000, 15000000, 12000000, 8000000, 3000000],
    'in_stock': [True, True, False, True, True],
    'rating': [4.5, 4.2, 4.7, 4.0, 4.3],
    'launch_date': pd.to_datetime(['2023-01-15', '2023-03-20', '2023-02-10', '2023-04-05', '2023-05-12'])
})

print("Mixed Data Types DataFrame:")
print(mixed_data.dtypes)
print("\\n", mixed_data)

# Working with different types
print("\\nString operations:")
mixed_data['product_name_upper'] = mixed_data['product_name'].str.upper()
mixed_data['name_length'] = mixed_data['product_name'].str.len()

print("\\nBoolean operations:")
available_products = mixed_data[mixed_data['in_stock'] == True]
print(f"Available products: {len(available_products)}")

print("\\nNumeric operations:")
mixed_data['price_millions'] = mixed_data['price'] / 1000000
expensive_products = mixed_data[mixed_data['price'] > 10000000]
print(f"Expensive products (>10M): {len(expensive_products)}")

print("\\nDateTime operations:")
mixed_data['days_since_launch'] = (pd.Timestamp.now() - mixed_data['launch_date']).dt.days
recent_products = mixed_data[mixed_data['days_since_launch'] < 365]
print(f"Recent products (within 1 year): {len(recent_products)}")
```

## 💡 Best Practices

### 1. DataFrame Creation

```python
# Good: explicit column specification
df = pd.DataFrame(data, columns=['col1', 'col2', 'col3'])

# Good: meaningful index
df.set_index('id', inplace=True)

# Good: appropriate data types
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')
```

### 2. Selection and Filtering

```python
# Good: use loc/iloc explicitly
value = df.loc[row_label, column_label]
subset = df.loc[condition, ['col1', 'col2']]

# Good: clear boolean conditions
condition = (df['price'] > 1000) & (df['category'] == 'Electronics')
filtered_df = df[condition]
```

### 3. Performance Tips

```python
# Use vectorized operations instead of loops
df['new_col'] = df['col1'] * df['col2']  # Good
# Avoid: for i in range(len(df)): df.loc[i, 'new_col'] = ...

# Use appropriate data types
df['category'] = df['category'].astype('category')  # Saves memory
df['id'] = df['id'].astype('int32')  # If values fit in int32
```

## 🎯 Practice Exercises

### Exercise 1: Student Management System

Tạo DataFrame cho hệ thống quản lý sinh viên và thực hiện:

1. Thêm cột GPA tính từ điểm các môn
2. Tìm top 3 sinh viên có GPA cao nhất
3. Lọc sinh viên theo năm sinh
4. Tính thống kê theo khoa

### Exercise 2: Sales Analysis

Với dữ liệu bán hàng, thực hiện:

1. Tính tổng doanh thu theo tháng
2. Tìm sản phẩm bán chạy nhất
3. Phân tích theo khu vực
4. Tạo báo cáo tóm tắt

### Exercise 3: Data Cleaning Challenge

Với DataFrame có missing data và inconsistent formats:

1. Identify data quality issues
2. Clean and standardize data
3. Handle missing values appropriately
4. Validate final results

---

## 📖 Tài liệu tham khảo

- [DataFrame User Guide](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe)
- [Indexing and Selecting Data](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Essential Basic Functionality](https://pandas.pydata.org/docs/user_guide/basics.html)

**Tiếp theo: Data Input/Output Operations** 📥📤
