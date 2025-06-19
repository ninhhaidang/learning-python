# Exercise 03: Data Loading and I/O Operations

## Mục tiêu

- Thành thạo việc đọc và ghi dữ liệu từ/ra các định dạng file khác nhau
- Hiểu cách xử lý các vấn đề thường gặp khi load dữ liệu (encoding, delimiter, missing values)
- Thực hành với dữ liệu GIS và viễn thám thực tế
- Làm quen với việc kết hợp nhiều nguồn dữ liệu

## Bài tập

### Bài 1: Xử lý dữ liệu khí tượng từ file CSV

Bạn có file CSV chứa dữ liệu khí tượng của Việt Nam với một số vấn đề về format cần xử lý.

**Yêu cầu:**

1. Đọc file CSV với các tham số phù hợp (delimiter, encoding, header)
2. Xử lý missing values và dữ liệu không hợp lệ
3. Chuyển đổi kiểu dữ liệu cho các cột thích hợp
4. Lưu dữ liệu đã xử lý ra file mới
5. Tạo báo cáo tóm tắt về chất lượng dữ liệu

**Dữ liệu mẫu (weather_data.csv):**

```csv
Station;Date;Temperature(°C);Humidity(%);Rainfall(mm);Wind_Speed(m/s);Notes
Hà Nội;2024-01-15;18.5;82;0.0;3.2;Normal
TP.HCM;2024-01-15;27.8;76;5.2;2.1;
Đà Nẵng;2024-01-15;22.4;85;12.8;4.5;Windy
Hải Phòng;2024-01-15;N/A;79;0.0;2.8;Sensor error
Cần Thơ;2024-01-15;28.1;NULL;3.4;1.9;Humidity sensor down
Huế;2024-01-15;20.9;88;-999;3.7;Invalid rainfall data
Nha Trang;2024-01-15;25.6;74;0.0;5.2;Normal
Đà Lạt;2024-01-15;16.2;92;8.5;1.5;
Vinh;2024-01-15;19.8;83;2.1;3.0;Normal
Sa Pa;2024-01-15;12.4;95;15.2;2.3;Foggy
```

**Output mẫu:**

```
Data Quality Report:
==================
Total records: 10
Missing temperature: 1 (10.0%)
Missing humidity: 1 (10.0%)
Invalid rainfall: 1 (10.0%)
Complete records: 7 (70.0%)

Cleaned data saved to: weather_cleaned.csv
```

### Bài 2: Kết hợp dữ liệu từ nhiều file Excel

Xử lý dữ liệu quan trắc môi trường từ 3 file Excel khác nhau.

**Yêu cầu:**

1. Đọc dữ liệu từ 3 sheet Excel: air_quality.xlsx (sheet: PM25, PM10, NO2)
2. Kết hợp dữ liệu từ 3 sheet thành 1 DataFrame
3. Xử lý duplicate records và missing values
4. Tính correlation matrix giữa các chỉ số ô nhiễm
5. Export kết quả ra file Excel với multiple sheets

**Cấu trúc dữ liệu:**

```
Sheet PM25:
Station_ID | Date | PM25_Value | Status
HN001 | 2024-01-15 | 35.2 | Valid
HCM001 | 2024-01-15 | 42.8 | Valid

Sheet PM10:
Station_ID | Date | PM10_Value | Status
HN001 | 2024-01-15 | 58.4 | Valid
HCM001 | 2024-01-15 | 67.2 | Valid

Sheet NO2:
Station_ID | Date | NO2_Value | Status
HN001 | 2024-01-15 | 28.5 | Valid
HCM001 | 2024-01-15 | 35.7 | Valid
```

### Bài 3: Xử lý dữ liệu JSON và API response

Làm việc với dữ liệu thời tiết từ API response format JSON.

**Yêu cầu:**

1. Parse JSON data chứa thông tin thời tiết real-time
2. Normalize nested JSON structure thành DataFrame
3. Xử lý timestamp và time zone
4. Lọc và aggregate dữ liệu theo time period
5. Save processed data sang multiple formats (CSV, JSON, Parquet)

**Dữ liệu JSON mẫu:**

```json
{
  "locations": [
    {
      "id": "VN_HN_001",
      "name": "Hà Nội",
      "coordinates": { "lat": 21.0285, "lon": 105.8542 },
      "observations": [
        {
          "timestamp": "2024-01-15T08:00:00Z",
          "weather": {
            "temperature": 18.5,
            "humidity": 82,
            "pressure": 1013.2,
            "wind": { "speed": 3.2, "direction": 45 }
          },
          "air_quality": {
            "pm25": 35.2,
            "pm10": 58.4,
            "no2": 28.5,
            "aqi": 89
          }
        }
      ]
    }
  ]
}
```

### Bài 4: Tạo và quản lý database connection

Thực hành đọc/ghi dữ liệu từ SQLite database.

**Yêu cầu:**

1. Tạo SQLite database và tables cho dữ liệu GIS
2. Import CSV data vào database
3. Thực hiện SQL queries để phân tích dữ liệu
4. Export query results thành các file format khác nhau
5. Tạo backup và restore procedures

**Schema mẫu:**

```sql
CREATE TABLE weather_stations (
    id INTEGER PRIMARY KEY,
    station_code TEXT UNIQUE,
    name TEXT,
    latitude REAL,
    longitude REAL,
    elevation REAL,
    region TEXT
);

CREATE TABLE observations (
    id INTEGER PRIMARY KEY,
    station_id INTEGER,
    observation_date DATE,
    temperature REAL,
    humidity REAL,
    rainfall REAL,
    wind_speed REAL,
    FOREIGN KEY (station_id) REFERENCES weather_stations (id)
);
```

## Hướng dẫn giải

### Bài 1 - CSV Processing:

```python
# Đọc CSV với parameters
df = pd.read_csv('weather_data.csv',
                 delimiter=';',
                 encoding='utf-8',
                 na_values=['N/A', 'NULL', -999])

# Xử lý missing values
df['Temperature(°C)'].fillna(df['Temperature(°C)'].mean(), inplace=True)

# Chuyển đổi kiểu dữ liệu
df['Date'] = pd.to_datetime(df['Date'])
df['Temperature(°C)'] = pd.to_numeric(df['Temperature(°C)'], errors='coerce')
```

### Bài 2 - Excel Multiple Sheets:

```python
# Đọc multiple sheets
pm25_df = pd.read_excel('air_quality.xlsx', sheet_name='PM25')
pm10_df = pd.read_excel('air_quality.xlsx', sheet_name='PM10')
no2_df = pd.read_excel('air_quality.xlsx', sheet_name='NO2')

# Merge dataframes
merged_df = pm25_df.merge(pm10_df, on=['Station_ID', 'Date']) \
                   .merge(no2_df, on=['Station_ID', 'Date'])
```

### Bài 3 - JSON Processing:

```python
import json
from pandas import json_normalize

# Parse JSON
with open('weather_api.json', 'r') as f:
    data = json.load(f)

# Normalize nested structure
df = json_normalize(data['locations'],
                    ['observations'],
                    ['id', 'name', ['coordinates', 'lat'], ['coordinates', 'lon']])
```

### Bài 4 - Database Operations:

```python
import sqlite3

# Connect to database
conn = sqlite3.connect('weather_data.db')

# Read from database
df = pd.read_sql_query("SELECT * FROM weather_stations", conn)

# Write to database
df.to_sql('new_table', conn, if_exists='replace', index=False)
```

## Tiêu chí đánh giá

- [ ] Đọc đúng các file với parameters phù hợp
- [ ] Xử lý missing values và dữ liệu không hợp lệ hiệu quả
- [ ] Chuyển đổi kiểu dữ liệu chính xác
- [ ] Kết hợp nhiều nguồn dữ liệu thành công
- [ ] Xử lý JSON nested structure đúng cách
- [ ] Thực hiện database operations an toàn
- [ ] Generate báo cáo chất lượng dữ liệu chi tiết
- [ ] Export dữ liệu ra đúng format yêu cầu
- [ ] Code có error handling và validation
- [ ] Tối ưu performance khi xử lý file lớn
