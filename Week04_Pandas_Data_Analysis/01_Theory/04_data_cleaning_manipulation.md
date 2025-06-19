# 04. Data Cleaning and Manipulation

## 🎯 Mục tiêu học tập

Sau khi hoàn thành chương này, bạn sẽ:

- Phát hiện và xử lý missing data hiệu quả
- Clean và standardize messy data
- Handle duplicates và outliers
- Transform và reshape data structures
- Perform advanced filtering và selection operations
- Merge và join multiple datasets

## 🧹 Missing Data Handling

### 1. Detecting Missing Data

```python
import pandas as pd
import numpy as np

# Create dataset with missing values
data_with_missing = {
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Nguyen Van A', 'Tran Thi B', None, 'Le Van D', 'Pham Thi E', '', 'Hoang Van G', 'Do Thi H'],
    'age': [20, 21, np.nan, 19, 22, 20, None, 18],
    'math_score': [8.5, 9.0, 7.5, np.nan, 8.8, 7.0, 9.2, 8.0],
    'english_score': [7.0, 8.5, np.nan, 8.0, 9.2, np.nan, 8.8, 7.5],
    'city': ['Ha Noi', 'Ho Chi Minh', 'Da Nang', '', 'Can Tho', 'Hai Phong', None, 'Hue'],
    'phone': ['0123456789', '0987654321', 'N/A', '0111222333', '', '0999888777', 'NULL', '0333444555']
}

df = pd.DataFrame(data_with_missing)
print("Dataset with missing values:")
print(df)

# Detect missing values
print("\\n=== MISSING DATA ANALYSIS ===")
print(f"Dataset shape: {df.shape}")
print(f"\\nMissing values per column:")
print(df.isnull().sum())

print(f"\\nMissing values percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage.round(2))

# Visualize missing data pattern
print(f"\\nRows with any missing data: {df.isnull().any(axis=1).sum()}")
print(f"Rows with all data complete: {df.notnull().all(axis=1).sum()}")

# Detailed missing data info
print(f"\\nMissing data info by row:")
for idx, row in df.iterrows():
    missing_cols = row[row.isnull()].index.tolist()
    if missing_cols:
        print(f"Row {idx}: Missing {missing_cols}")
```

### 2. Handling Different Types of Missing Values

```python
# Replace various representations of missing data
df_clean = df.copy()

# Replace empty strings and 'N/A', 'NULL' with NaN
replacements = ['', 'N/A', 'NULL', 'n/a', 'null', 'None']
df_clean = df_clean.replace(replacements, np.nan)

print("After standardizing missing values:")
print(df_clean.isnull().sum())

# Identify patterns in missing data
print("\\n=== MISSING DATA PATTERNS ===")

# Students missing both math and english scores
both_scores_missing = df_clean['math_score'].isnull() & df_clean['english_score'].isnull()
print(f"Students missing both scores: {both_scores_missing.sum()}")

# Students with complete academic data
academic_complete = df_clean[['math_score', 'english_score']].notnull().all(axis=1)
print(f"Students with complete academic data: {academic_complete.sum()}")
```

### 3. Missing Data Strategies

```python
# Strategy 1: Drop missing data
print("=== STRATEGY 1: DROPPING MISSING DATA ===")

# Drop rows with any missing values
df_dropna_any = df_clean.dropna()
print(f"Drop any missing - Remaining rows: {len(df_dropna_any)}")

# Drop rows with all missing values
df_dropna_all = df_clean.dropna(how='all')
print(f"Drop all missing - Remaining rows: {len(df_dropna_all)}")

# Drop rows missing critical columns
df_dropna_subset = df_clean.dropna(subset=['name', 'age'])
print(f"Drop missing name/age - Remaining rows: {len(df_dropna_subset)}")

# Drop columns with too many missing values
threshold = 0.5  # Drop columns with >50% missing
df_drop_cols = df_clean.loc[:, df_clean.isnull().mean() < threshold]
print(f"Columns remaining after threshold: {list(df_drop_cols.columns)}")

# Strategy 2: Fill missing data
print("\\n=== STRATEGY 2: FILLING MISSING DATA ===")

df_filled = df_clean.copy()

# Fill with constants
df_filled['city'] = df_filled['city'].fillna('Unknown')
df_filled['phone'] = df_filled['phone'].fillna('Not provided')

# Fill with statistics
df_filled['age'] = df_filled['age'].fillna(df_filled['age'].median())
df_filled['math_score'] = df_filled['math_score'].fillna(df_filled['math_score'].mean())
df_filled['english_score'] = df_filled['english_score'].fillna(df_filled['english_score'].mean())

# Forward fill and backward fill
df_filled['name'] = df_filled['name'].fillna(method='ffill')  # Forward fill

print("After filling missing values:")
print(df_filled.isnull().sum())
print("\\nFilled dataset:")
print(df_filled)
```

### 4. Advanced Missing Data Techniques

```python
# Conditional filling based on other columns
df_advanced = df_clean.copy()

# Fill missing scores based on city averages
city_math_avg = df_advanced.groupby('city')['math_score'].mean()
city_english_avg = df_advanced.groupby('city')['english_score'].mean()

print("City-based averages for missing data imputation:")
print("Math scores by city:")
print(city_math_avg.dropna())

# Custom filling function
def smart_fill_score(row, score_col, city_averages):
    if pd.isnull(row[score_col]) and not pd.isnull(row['city']):
        if row['city'] in city_averages:
            return city_averages[row['city']]
    return row[score_col]

# Apply smart filling
for idx, row in df_advanced.iterrows():
    if pd.isnull(df_advanced.loc[idx, 'math_score']):
        df_advanced.loc[idx, 'math_score'] = smart_fill_score(row, 'math_score', city_math_avg)

print("\\nAfter smart filling:")
print(df_advanced[['name', 'city', 'math_score', 'english_score']])
```

## 🔍 Data Cleaning and Standardization

### 1. String Data Cleaning

```python
# Create messy string data
messy_data = {
    'company': ['  VINAMILK  ', 'vietcombank', 'FPT Software', '  TECHCOMBANK  ', 'vingroup'],
    'industry': ['Food & Beverage', 'banking', 'TECHNOLOGY', 'Banking', 'real estate'],
    'revenue': ['100,000M', '50000M', 'N/A', '75,500M', '200000M'],
    'employees': ['15,000', '25000', '40,000', '12000', '50,000'],
    'website': ['www.vinamilk.com.vn', 'vietcombank.com.vn', 'fpt.com.vn', 'techcombank.com.vn', 'vingroup.net']
}

df_messy = pd.DataFrame(messy_data)
print("Messy string data:")
print(df_messy)

# Clean string data
df_clean_str = df_messy.copy()

# 1. Clean company names
df_clean_str['company'] = df_clean_str['company'].str.strip().str.title()

# 2. Standardize industry names
industry_mapping = {
    'food & beverage': 'Food & Beverage',
    'banking': 'Banking',
    'technology': 'Technology',
    'real estate': 'Real Estate'
}
df_clean_str['industry'] = df_clean_str['industry'].str.lower().map(industry_mapping)

# 3. Clean numeric data in strings
def clean_revenue(revenue_str):
    if pd.isnull(revenue_str) or revenue_str == 'N/A':
        return np.nan
    # Remove commas and 'M', convert to float
    return float(revenue_str.replace(',', '').replace('M', ''))

def clean_employees(emp_str):
    if pd.isnull(emp_str):
        return np.nan
    return int(emp_str.replace(',', ''))

df_clean_str['revenue_millions'] = df_clean_str['revenue'].apply(clean_revenue)
df_clean_str['employees_count'] = df_clean_str['employees'].apply(clean_employees)

# 4. Standardize website URLs
df_clean_str['website'] = df_clean_str['website'].apply(
    lambda x: f"https://{x}" if not x.startswith('http') else x
)

print("\\nCleaned string data:")
print(df_clean_str)
```

### 2. Data Type Conversion

```python
# Mixed data types example
mixed_data = {
    'order_id': ['ORD001', 'ORD002', 'ORD003', 'ORD004'],
    'date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18'],
    'amount': ['1500000', '2300000', '850000', '1200000'],
    'quantity': ['2', '1', '3', '2'],
    'discount': ['0.05', '0.10', '0.00', '0.08'],
    'customer_type': ['VIP', 'Regular', 'VIP', 'Regular']
}

df_mixed = pd.DataFrame(mixed_data)
print("Original data types:")
print(df_mixed.dtypes)

# Convert data types
df_converted = df_mixed.copy()

# Convert to appropriate types
df_converted['date'] = pd.to_datetime(df_converted['date'])
df_converted['amount'] = df_converted['amount'].astype('int64')
df_converted['quantity'] = df_converted['quantity'].astype('int32')
df_converted['discount'] = df_converted['discount'].astype('float64')
df_converted['customer_type'] = df_converted['customer_type'].astype('category')

print("\\nConverted data types:")
print(df_converted.dtypes)

# Add derived columns
df_converted['total_amount'] = df_converted['amount'] * df_converted['quantity']
df_converted['discounted_amount'] = df_converted['total_amount'] * (1 - df_converted['discount'])
df_converted['day_of_week'] = df_converted['date'].dt.day_name()
df_converted['month'] = df_converted['date'].dt.month

print("\\nFinal dataset with derived columns:")
print(df_converted)
```

## 🎯 Filtering and Selection

### 1. Advanced Boolean Indexing

```python
# Sales data for filtering examples
sales_data = {
    'salesperson': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'region': ['North', 'South', 'North', 'Central', 'South', 'North', 'Central', 'South'],
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone'],
    'quantity': [5, 8, 3, 7, 12, 2, 9, 6],
    'unit_price': [25000000, 15000000, 12000000, 25000000, 15000000, 12000000, 25000000, 15000000],
    'sales_date': pd.date_range('2024-01-01', periods=8, freq='D'),
    'experience_years': [3, 5, 2, 8, 1, 6, 4, 7]
}

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = df_sales['quantity'] * df_sales['unit_price']

print("Sales dataset:")
print(df_sales)

# Advanced filtering
print("\\n=== ADVANCED FILTERING ===")

# Multiple conditions with AND
high_value_north = df_sales[
    (df_sales['total_revenue'] > 100000000) &
    (df_sales['region'] == 'North')
]
print("High value sales in North region:")
print(high_value_north[['salesperson', 'product', 'total_revenue']])

# Multiple conditions with OR
laptop_or_experienced = df_sales[
    (df_sales['product'] == 'Laptop') |
    (df_sales['experience_years'] > 5)
]
print(f"\\nLaptop sales or experienced salespeople: {len(laptop_or_experienced)} records")

# String filtering
phone_sellers = df_sales[df_sales['product'].str.contains('Phone', case=False)]
print(f"\\nPhone sellers: {phone_sellers['salesperson'].tolist()}")

# Numeric range filtering
mid_experience = df_sales[df_sales['experience_years'].between(3, 6)]
print(f"\\nMid-experience salespeople: {mid_experience['salesperson'].tolist()}")

# Date range filtering
recent_sales = df_sales[df_sales['sales_date'] >= '2024-01-05']
print(f"\\nRecent sales (from Jan 5): {len(recent_sales)} records")
```

### 2. Query Method

```python
# Using query method for cleaner syntax
print("\\n=== USING QUERY METHOD ===")

# Simple queries
high_revenue = df_sales.query('total_revenue > 150000000')
print(f"High revenue sales: {len(high_revenue)} records")

# Complex queries
complex_query = df_sales.query(
    'region in ["North", "South"] and experience_years >= 3 and total_revenue > 50000000'
)
print(f"Complex query results: {len(complex_query)} records")

# Using variables in queries
min_revenue = 100000000
target_regions = ['North', 'Central']

variable_query = df_sales.query(
    'total_revenue >= @min_revenue and region in @target_regions'
)
print(f"Variable query results: {len(variable_query)} records")
```

## 🔄 Data Transformation and Reshaping

### 1. Pivot Tables and Reshaping

```python
# Create sales summary data
summary_data = {
    'month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Mar', 'Mar', 'Mar'],
    'region': ['North', 'South', 'Central', 'North', 'South', 'Central', 'North', 'South', 'Central'],
    'product': ['Laptop', 'Laptop', 'Laptop', 'Phone', 'Phone', 'Phone', 'Tablet', 'Tablet', 'Tablet'],
    'sales': [100, 150, 80, 200, 180, 120, 60, 90, 70],
    'units': [4, 6, 3, 20, 18, 12, 5, 7, 6]
}

df_summary = pd.DataFrame(summary_data)
print("Original sales summary:")
print(df_summary)

# Create pivot table
pivot_sales = df_summary.pivot_table(
    values='sales',
    index='month',
    columns='region',
    aggfunc='sum',
    fill_value=0
)
print("\\nPivot table - Sales by Month and Region:")
print(pivot_sales)

# Multi-level pivot
multi_pivot = df_summary.pivot_table(
    values=['sales', 'units'],
    index='month',
    columns=['region', 'product'],
    aggfunc='sum',
    fill_value=0
)
print("\\nMulti-level pivot table:")
print(multi_pivot)

# Melt (unpivot) data
melted = pd.melt(
    df_summary,
    id_vars=['month', 'region'],
    value_vars=['sales', 'units'],
    var_name='metric',
    value_name='value'
)
print("\\nMelted data:")
print(melted.head(10))
```

### 2. Groupby Operations

```python
# Advanced groupby operations
print("\\n=== GROUPBY OPERATIONS ===")

# Basic grouping
region_stats = df_sales.groupby('region').agg({
    'total_revenue': ['sum', 'mean', 'count'],
    'quantity': 'sum',
    'experience_years': 'mean'
}).round(2)

print("Region statistics:")
print(region_stats)

# Multiple grouping
product_region_stats = df_sales.groupby(['product', 'region']).agg({
    'total_revenue': 'sum',
    'quantity': 'sum'
}).reset_index()

print("\\nProduct-Region statistics:")
print(product_region_stats)

# Custom aggregation functions
def revenue_per_unit(group):
    return (group['total_revenue'] / group['quantity']).mean()

custom_stats = df_sales.groupby('region').apply(revenue_per_unit)
print("\\nAverage revenue per unit by region:")
print(custom_stats)

# Transform (keep original shape)
df_sales['region_avg_revenue'] = df_sales.groupby('region')['total_revenue'].transform('mean')
df_sales['revenue_vs_region_avg'] = df_sales['total_revenue'] / df_sales['region_avg_revenue']

print("\\nWith region comparisons:")
print(df_sales[['salesperson', 'region', 'total_revenue', 'region_avg_revenue', 'revenue_vs_region_avg']])
```

## 🔗 Merging and Joining Data

### 1. Combining DataFrames

```python
# Create related datasets
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Nguyen Van A', 'Tran Thi B', 'Le Van C', 'Pham Thi D', 'Hoang Van E'],
    'city': ['Ha Noi', 'Ho Chi Minh', 'Da Nang', 'Can Tho', 'Hai Phong'],
    'segment': ['Premium', 'Standard', 'Premium', 'Standard', 'Premium']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106],
    'customer_id': [1, 2, 2, 3, 4, 6],  # Note: customer_id 6 doesn't exist in customers
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet'],
    'amount': [25000000, 15000000, 12000000, 25000000, 15000000, 12000000],
    'order_date': pd.date_range('2024-01-01', periods=6, freq='D')
})

print("Customers:")
print(customers)
print("\\nOrders:")
print(orders)

# Different types of joins
print("\\n=== DIFFERENT JOIN TYPES ===")

# Inner join (only matching records)
inner_join = pd.merge(customers, orders, on='customer_id', how='inner')
print(f"Inner join: {len(inner_join)} records")
print(inner_join)

# Left join (all customers, matching orders)
left_join = pd.merge(customers, orders, on='customer_id', how='left')
print(f"\\nLeft join: {len(left_join)} records")
print(left_join)

# Right join (all orders, matching customers)
right_join = pd.merge(customers, orders, on='customer_id', how='right')
print(f"\\nRight join: {len(right_join)} records")
print(right_join)

# Outer join (all records from both)
outer_join = pd.merge(customers, orders, on='customer_id', how='outer')
print(f"\\nOuter join: {len(outer_join)} records")
print(outer_join)
```

### 2. Advanced Merging Scenarios

```python
# Different column names
customers_alt = customers.rename(columns={'customer_id': 'cust_id'})
orders_alt = orders.rename(columns={'customer_id': 'cust_id'})

# Merge with different column names
merged_alt = pd.merge(customers_alt, orders_alt, on='cust_id')
print("\\nMerge with renamed columns:")
print(merged_alt.head())

# Multiple join keys
product_info = pd.DataFrame({
    'product': ['Laptop', 'Phone', 'Tablet'],
    'category': ['Electronics', 'Electronics', 'Electronics'],
    'cost': [20000000, 12000000, 9000000],
    'margin': [0.25, 0.25, 0.33]
})

# Three-way merge
complete_data = pd.merge(
    pd.merge(customers, orders, on='customer_id'),
    product_info,
    on='product'
)

complete_data['profit'] = complete_data['amount'] * complete_data['margin']

print("\\nThree-way merge with profit calculation:")
print(complete_data[['name', 'product', 'amount', 'profit']])
```

## 🚿 Duplicate Handling

```python
# Create data with duplicates
duplicate_data = pd.DataFrame({
    'name': ['John', 'Jane', 'John', 'Bob', 'Jane', 'Alice', 'Bob'],
    'age': [25, 30, 25, 35, 30, 28, 35],
    'city': ['NY', 'LA', 'NY', 'Chicago', 'LA', 'Boston', 'Chicago'],
    'salary': [50000, 60000, 50000, 70000, 65000, 55000, 70000]
})

print("Data with duplicates:")
print(duplicate_data)

# Identify duplicates
print(f"\\nDuplicate rows: {duplicate_data.duplicated().sum()}")
print("\\nDuplicate status:")
print(duplicate_data.duplicated())

# Find specific duplicates
print("\\nExact duplicate rows:")
print(duplicate_data[duplicate_data.duplicated()])

# Remove duplicates
print("\\n=== REMOVING DUPLICATES ===")

# Remove exact duplicates
no_exact_dupes = duplicate_data.drop_duplicates()
print(f"After removing exact duplicates: {len(no_exact_dupes)} rows")

# Remove duplicates based on subset of columns
no_name_dupes = duplicate_data.drop_duplicates(subset=['name'], keep='first')
print(f"After removing name duplicates (keep first): {len(no_name_dupes)} rows")
print(no_name_dupes)

# Keep last occurrence
no_name_dupes_last = duplicate_data.drop_duplicates(subset=['name'], keep='last')
print(f"\\nAfter removing name duplicates (keep last): {len(no_name_dupes_last)} rows")
print(no_name_dupes_last)
```

## 💡 Best Practices

### 1. Data Cleaning Pipeline

```python
def clean_data_pipeline(df):
    """Comprehensive data cleaning pipeline"""
    print("Starting data cleaning pipeline...")

    # 1. Initial assessment
    print(f"Initial shape: {df.shape}")
    print(f"Missing values: {df.isnull().sum().sum()}")

    # 2. Handle missing values
    # Fill or drop based on business logic

    # 3. Standardize strings
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].str.strip()

    # 4. Remove duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate rows")

    # 5. Data type optimization
    # Convert to appropriate types

    print(f"Final shape: {df.shape}")
    return df

# Example usage
# cleaned_df = clean_data_pipeline(raw_df)
```

### 2. Memory-Efficient Operations

```python
# Good: Process in chunks for large datasets
def process_large_dataframe(df, chunk_size=10000):
    results = []
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i+chunk_size]
        processed_chunk = chunk.groupby('category').sum()
        results.append(processed_chunk)
    return pd.concat(results)

# Good: Use categorical data for repeated strings
df['category'] = df['category'].astype('category')

# Good: Use appropriate numeric types
df['small_int'] = df['small_int'].astype('int8')  # If values fit
```

## 🎯 Practice Exercises

### Exercise 1: Complete Data Cleaning

1. Load messy dataset with mixed data types
2. Identify and handle all missing values
3. Clean and standardize string columns
4. Remove duplicates and outliers
5. Export cleaned dataset

### Exercise 2: Sales Data Analysis

1. Combine multiple sales datasets
2. Handle missing customer information
3. Calculate derived metrics (profit, margins)
4. Create summary reports by region/product
5. Identify data quality issues

### Exercise 3: Survey Data Processing

1. Clean survey responses with inconsistent formats
2. Handle multiple choice and text responses
3. Standardize categorical variables
4. Create analysis-ready dataset
5. Generate data quality report

---

## 📖 Tài liệu tham khảo

- [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Merge, join, concatenate](https://pandas.pydata.org/docs/user_guide/merging.html)
- [Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html)
- [Group by operations](https://pandas.pydata.org/docs/user_guide/groupby.html)

**Tiếp theo: Statistical Analysis và Advanced Operations** 📊
