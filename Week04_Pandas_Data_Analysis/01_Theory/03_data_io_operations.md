# 03. Data Input/Output Operations

## 🎯 Mục tiêu học tập

Sau khi hoàn thành chương này, bạn sẽ:

- Đọc và ghi dữ liệu từ/đến các format phổ biến (CSV, Excel, JSON)
- Hiểu về các parameters quan trọng khi import data
- Xử lý encoding issues và data type problems
- Làm việc với large datasets hiệu quả
- Connect với databases và APIs

## 📂 Overview của Data I/O

Pandas hỗ trợ rất nhiều data formats:

| Format  | Read Function       | Write Function    | Use Case                       |
| ------- | ------------------- | ----------------- | ------------------------------ |
| CSV     | `pd.read_csv()`     | `df.to_csv()`     | Most common, lightweight       |
| Excel   | `pd.read_excel()`   | `df.to_excel()`   | Business reports, spreadsheets |
| JSON    | `pd.read_json()`    | `df.to_json()`    | Web APIs, nested data          |
| SQL     | `pd.read_sql()`     | `df.to_sql()`     | Database integration           |
| Parquet | `pd.read_parquet()` | `df.to_parquet()` | Big data, analytics            |
| Pickle  | `pd.read_pickle()`  | `df.to_pickle()`  | Python objects, caching        |

## 📊 CSV Operations

### 1. Reading CSV Files

```python
import pandas as pd
import numpy as np

# Create sample CSV data
sample_csv_data = """
student_id,name,age,math_score,english_score,city,graduation_year
1,"Nguyen Van A",20,8.5,7.0,"Ha Noi",2024
2,"Tran Thi B",21,9.0,8.5,"Ho Chi Minh",2024
3,"Le Van C",19,7.5,8.0,"Da Nang",2025
4,"Pham Thi D",22,8.8,9.2,"Can Tho",2023
5,"Hoang Van E",20,6.5,7.5,"Hai Phong",2024
"""

# Save to file for demonstration
with open('sample_students.csv', 'w', encoding='utf-8') as f:
    f.write(sample_csv_data)

# Basic reading
df = pd.read_csv('sample_students.csv')
print("Basic CSV reading:")
print(df)
print(f"\\nData types:\\n{df.dtypes}")
```

### 2. Advanced CSV Reading Parameters

```python
# Reading with custom parameters
df_advanced = pd.read_csv(
    'sample_students.csv',
    index_col='student_id',          # Set student_id as index
    dtype={                          # Specify data types
        'age': 'int8',
        'math_score': 'float32',
        'english_score': 'float32',
        'graduation_year': 'int16'
    },
    parse_dates=['graduation_year'],  # Convert to datetime (if needed)
    encoding='utf-8'                 # Handle Vietnamese characters
)

print("Advanced CSV reading:")
print(df_advanced.info())
```

### 3. Handling Common CSV Issues

```python
# CSV with missing values
csv_with_missing = """
name,age,salary,department
John,25,50000,IT
Jane,,60000,HR
Bob,30,,Finance
Alice,28,55000,
Charlie,35,70000,IT
"""

with open('data_with_missing.csv', 'w') as f:
    f.write(csv_with_missing)

# Reading with missing value handling
df_missing = pd.read_csv(
    'data_with_missing.csv',
    na_values=['', 'NULL', 'N/A', 'na'],  # Additional missing value indicators
    keep_default_na=True                   # Keep default NaN values
)

print("Data with missing values:")
print(df_missing)
print(f"\\nMissing values per column:\\n{df_missing.isnull().sum()}")

# CSV with custom separators
csv_semicolon = """
name;age;city;country
Nguyen Van A;25;Ha Noi;Vietnam
Tran Thi B;30;Ho Chi Minh;Vietnam
"""

df_semicolon = pd.read_csv(
    pd.StringIO(csv_semicolon),
    sep=';'  # Custom separator
)
print("\\nCSV with semicolon separator:")
print(df_semicolon)
```

### 4. Writing CSV Files

```python
# Basic writing
df.to_csv('output_students.csv', index=False)  # Don't include index

# Advanced writing
df.to_csv(
    'output_advanced.csv',
    index=True,                    # Include index
    columns=['name', 'age', 'city'], # Select specific columns
    encoding='utf-8',              # Encoding for Vietnamese
    float_format='%.2f',           # Format floating numbers
    date_format='%Y-%m-%d'         # Date format
)

print("CSV files written successfully!")
```

## 📈 Excel Operations

### 1. Reading Excel Files

```python
# Create sample Excel data
excel_data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Price': [25000000, 15000000, 12000000, 8000000, 3000000],
    'Quantity': [50, 100, 30, 75, 200],
    'Supplier': ['Dell', 'Samsung', 'Apple', 'Apple', 'Sony']
}

df_products = pd.DataFrame(excel_data)

# Write to Excel first
df_products.to_excel('products.xlsx', index=False, sheet_name='Products')

# Read Excel file
df_from_excel = pd.read_excel('products.xlsx', sheet_name='Products')
print("Data from Excel:")
print(df_from_excel)

# Read specific columns and rows
df_partial = pd.read_excel(
    'products.xlsx',
    sheet_name='Products',
    usecols=['Product', 'Price', 'Quantity'],  # Specific columns
    skiprows=1,                                 # Skip header
    nrows=3                                     # Only first 3 data rows
)
print("\\nPartial Excel data:")
print(df_partial)
```

### 2. Multiple Sheets Operations

```python
# Create workbook with multiple sheets
with pd.ExcelWriter('multi_sheet_data.xlsx') as writer:
    # Sheet 1: Products
    df_products.to_excel(writer, sheet_name='Products', index=False)

    # Sheet 2: Sales data
    sales_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Revenue': [100000000, 120000000, 110000000, 130000000, 140000000],
        'Units_Sold': [500, 600, 550, 650, 700]
    })
    sales_data.to_excel(writer, sheet_name='Sales', index=False)

    # Sheet 3: Summary
    summary_data = pd.DataFrame({
        'Metric': ['Total Products', 'Total Revenue', 'Average Price'],
        'Value': [len(df_products), sales_data['Revenue'].sum(), df_products['Price'].mean()]
    })
    summary_data.to_excel(writer, sheet_name='Summary', index=False)

# Read all sheets
all_sheets = pd.read_excel('multi_sheet_data.xlsx', sheet_name=None)
print("Available sheets:", list(all_sheets.keys()))

# Read specific sheet
products_sheet = pd.read_excel('multi_sheet_data.xlsx', sheet_name='Products')
sales_sheet = pd.read_excel('multi_sheet_data.xlsx', sheet_name='Sales')

print("\\nProducts sheet:")
print(products_sheet.head())
print("\\nSales sheet:")
print(sales_sheet.head())
```

## 📋 JSON Operations

### 1. Reading JSON Data

```python
import json

# Sample JSON data (Vietnam cities)
json_data = '''
[
    {
        "city": "Ha Noi",
        "population": 8100000,
        "area": 3358.6,
        "coordinates": {"lat": 21.0285, "lon": 105.8542},
        "districts": ["Ba Dinh", "Hoan Kiem", "Tay Ho", "Long Bien"],
        "established": 1010
    },
    {
        "city": "Ho Chi Minh",
        "population": 9000000,
        "area": 2095.0,
        "coordinates": {"lat": 10.8231, "lon": 106.6297},
        "districts": ["District 1", "District 2", "District 3", "Binh Thanh"],
        "established": 1698
    },
    {
        "city": "Da Nang",
        "population": 1200000,
        "area": 1285.4,
        "coordinates": {"lat": 16.0471, "lon": 108.2068},
        "districts": ["Hai Chau", "Thanh Khe", "Son Tra", "Ngu Hanh Son"],
        "established": 1307
    }
]
'''

# Save JSON to file
with open('vietnam_cities.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

# Read JSON
df_cities = pd.read_json('vietnam_cities.json')
print("Cities from JSON:")
print(df_cities)
print(f"\\nData types:\\n{df_cities.dtypes}")
```

### 2. Handling Nested JSON

```python
# Normalize nested JSON data
from pandas import json_normalize

# Load and parse JSON
with open('vietnam_cities.json', 'r', encoding='utf-8') as f:
    cities_data = json.load(f)

# Normalize nested data
df_normalized = json_normalize(cities_data)
print("\\nNormalized JSON data:")
print(df_normalized)

# Flatten specific nested fields
df_coords = json_normalize(cities_data, sep='_')
print("\\nFlattened coordinates:")
print(df_coords[['city', 'coordinates_lat', 'coordinates_lon']])

# Handle arrays in JSON
df_districts = json_normalize(
    cities_data,
    record_path=['districts'],
    meta=['city', 'population'],
    meta_prefix='city_'
)
print("\\nDistricts data:")
print(df_districts.head())
```

### 3. Writing JSON

```python
# Write DataFrame to JSON
df_cities.to_json('output_cities.json', orient='records', indent=2)

# Different JSON orientations
orientations = ['records', 'index', 'values', 'split', 'table']

for orient in orientations:
    output_file = f'cities_{orient}.json'
    df_cities.to_json(output_file, orient=orient, indent=2)
    print(f"Created {output_file} with orient='{orient}'")
```

## 🗄️ Database Operations

### 1. SQLite Integration

```python
import sqlite3

# Create in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Write DataFrame to SQL
df_products.to_sql('products', conn, if_exists='replace', index=False)
df_cities.to_sql('cities', conn, if_exists='replace', index=False)

# Read from SQL
query = "SELECT * FROM products WHERE Price > 10000000"
expensive_products = pd.read_sql(query, conn)
print("Expensive products from database:")
print(expensive_products)

# More complex query
complex_query = """
SELECT
    Category,
    COUNT(*) as product_count,
    AVG(Price) as avg_price,
    SUM(Quantity) as total_quantity
FROM products
GROUP BY Category
"""
category_summary = pd.read_sql(complex_query, conn)
print("\\nCategory summary:")
print(category_summary)

conn.close()
```

### 2. MySQL/PostgreSQL Example (Mock)

```python
# This is example code - requires actual database connection
# pip install sqlalchemy pymysql

"""
from sqlalchemy import create_engine

# MySQL connection
mysql_engine = create_engine('mysql+pymysql://user:password@localhost/database')

# PostgreSQL connection
postgres_engine = create_engine('postgresql://user:password@localhost/database')

# Read from database
df = pd.read_sql('SELECT * FROM table_name', mysql_engine)

# Write to database
df.to_sql('new_table', postgres_engine, if_exists='replace', index=False)
"""

print("Database connection examples (commented out - requires setup)")
```

## 🌐 Web Data and APIs

### 1. Reading from URLs

```python
# Read CSV from URL (example)
url_csv = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"

try:
    # This would work with actual internet connection
    # df_covid = pd.read_csv(url_csv)
    # print("COVID data from URL:")
    # print(df_covid.head())
    print("URL CSV reading example (requires internet connection)")
except:
    print("Could not connect to URL")

# Read HTML tables
html_content = """
<table>
    <tr><th>Name</th><th>Age</th><th>City</th></tr>
    <tr><td>John</td><td>25</td><td>New York</td></tr>
    <tr><td>Jane</td><td>30</td><td>Los Angeles</td></tr>
    <tr><td>Bob</td><td>35</td><td>Chicago</td></tr>
</table>
"""

# Save HTML to file
with open('sample_table.html', 'w') as f:
    f.write(html_content)

# Read HTML table
tables = pd.read_html('sample_table.html')
df_html = tables[0]  # First table
print("\\nData from HTML table:")
print(df_html)
```

### 2. API Data Processing

```python
# Simulate API response
api_response_json = '''
{
    "status": "success",
    "data": [
        {"id": 1, "name": "Product A", "price": 100, "category": "Electronics"},
        {"id": 2, "name": "Product B", "price": 200, "category": "Books"},
        {"id": 3, "name": "Product C", "price": 150, "category": "Electronics"}
    ],
    "metadata": {
        "total_records": 3,
        "page": 1,
        "per_page": 10
    }
}
'''

# Parse API response
api_data = json.loads(api_response_json)
df_api = pd.json_normalize(api_data['data'])
print("\\nData from API response:")
print(df_api)

# Process metadata
metadata = api_data['metadata']
print(f"\\nAPI Metadata: {metadata}")
```

## ⚡ Performance Optimization

### 1. Efficient Data Types

```python
# Create large dataset for testing
large_data = {
    'id': range(100000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100000),
    'value': np.random.randn(100000),
    'date': pd.date_range('2020-01-01', periods=100000, freq='1min')
}

df_large = pd.DataFrame(large_data)

print("Original memory usage:")
print(df_large.memory_usage(deep=True))

# Optimize data types
df_optimized = df_large.copy()
df_optimized['id'] = df_optimized['id'].astype('int32')  # Instead of int64
df_optimized['category'] = df_optimized['category'].astype('category')  # Categorical
df_optimized['value'] = df_optimized['value'].astype('float32')  # Instead of float64

print("\\nOptimized memory usage:")
print(df_optimized.memory_usage(deep=True))

# Memory reduction
reduction = (df_large.memory_usage(deep=True).sum() -
            df_optimized.memory_usage(deep=True).sum()) / df_large.memory_usage(deep=True).sum() * 100
print(f"\\nMemory reduction: {reduction:.1f}%")
```

### 2. Chunking for Large Files

```python
# Read large CSV in chunks
def process_large_csv(filename, chunksize=10000):
    """Process large CSV file in chunks"""
    chunk_list = []

    for chunk in pd.read_csv(filename, chunksize=chunksize):
        # Process each chunk
        processed_chunk = chunk.groupby('category')['value'].mean().reset_index()
        chunk_list.append(processed_chunk)

    # Combine all chunks
    result = pd.concat(chunk_list, ignore_index=True)
    final_result = result.groupby('category')['value'].mean().reset_index()

    return final_result

# Simulate processing
print("Chunking example for large files (simulation):")
print("This technique is useful for files that don't fit in memory")
```

## 🔧 Data Quality and Validation

### 1. Validation During Import

```python
# Create data with quality issues
problematic_csv = """
name,age,salary,email
John Doe,25,50000,john@email.com
Jane Smith,thirty,60000,jane.email.com
Bob Wilson,35,seventy,bob@email.com
Alice Brown,-5,55000,alice@email.com
Charlie Davis,30,40000,charlie@email.com
"""

with open('problematic_data.csv', 'w') as f:
    f.write(problematic_csv)

# Read with error handling
try:
    df_problematic = pd.read_csv('problematic_data.csv')
    print("Raw problematic data:")
    print(df_problematic)
    print(f"\\nData types:\\n{df_problematic.dtypes}")

    # Identify issues
    print("\\nData quality issues:")
    print("- Age column has non-numeric values")
    print("- Salary column has non-numeric values")
    print("- Age has negative values")
    print("- Email format issues")

except Exception as e:
    print(f"Error reading data: {e}")

# Clean data during import
def validate_age(x):
    try:
        age = int(x)
        return age if 0 <= age <= 120 else np.nan
    except:
        return np.nan

def validate_salary(x):
    try:
        return float(x)
    except:
        return np.nan

# Apply validation
df_clean = df_problematic.copy()
df_clean['age'] = df_problematic['age'].apply(validate_age)
df_clean['salary'] = df_problematic['salary'].apply(validate_salary)

print("\\nCleaned data:")
print(df_clean)
print(f"\\nMissing values after cleaning:\\n{df_clean.isnull().sum()}")
```

## 💡 Best Practices

### 1. File Management

```python
# Good: Use context managers
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')

# Good: Specify encoding explicitly
df = pd.read_csv('file.csv', encoding='utf-8')

# Good: Handle large files efficiently
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process_chunk(chunk)
```

### 2. Data Type Optimization

```python
# Good: Specify dtypes upfront
dtypes = {
    'category_col': 'category',
    'int_col': 'int32',
    'float_col': 'float32'
}
df = pd.read_csv('file.csv', dtype=dtypes)

# Good: Convert strings to datetime
df['date_col'] = pd.to_datetime(df['date_col'])
```

### 3. Error Handling

```python
# Good: Handle potential errors
try:
    df = pd.read_csv('file.csv')
except FileNotFoundError:
    print("File not found")
except pd.errors.EmptyDataError:
    print("Empty file")
except Exception as e:
    print(f"Error: {e}")
```

## 🎯 Practice Exercises

### Exercise 1: Multi-format Data Processing

1. Đọc dữ liệu từ CSV, Excel, và JSON
2. Combine và clean data from multiple sources
3. Export cleaned data to different formats
4. Compare file sizes và loading times

### Exercise 2: Large Dataset Handling

1. Simulate working with large CSV (>1GB)
2. Use chunking to process data
3. Optimize memory usage
4. Export processed results efficiently

### Exercise 3: Web Data Integration

1. Read data from online CSV sources
2. Parse JSON from API responses
3. Combine web data with local files
4. Create automated data pipeline

---

## 📖 Tài liệu tham khảo

- [IO Tools (Text, CSV, HDF5, ...)](https://pandas.pydata.org/docs/user_guide/io.html)
- [Working with Text Data](https://pandas.pydata.org/docs/user_guide/text.html)
- [JSON Normalization](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html)

**Tiếp theo: Data Cleaning and Manipulation** 🧹
