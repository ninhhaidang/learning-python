# Exercise 04: Data Analysis with Pandas

## Mục tiêu

- Thành thạo các kỹ thuật phân tích dữ liệu nâng cao với Pandas
- Thực hành groupby, pivot table, và time series analysis
- Áp dụng statistical analysis cho dữ liệu địa lý và viễn thám
- Tạo insights và visualization từ dữ liệu thực tế

## Bài tập

### Bài 1: Phân tích xu hướng biến đổi khí hậu

Phân tích dữ liệu nhiệt độ dài hạn để xác định xu hướng biến đổi khí hậu ở Việt Nam.

**Yêu cầu:**

1. Phân tích xu hướng nhiệt độ trung bình theo năm (1990-2023)
2. Tính moving average 5 năm và 10 năm
3. Xác định các năm có nhiệt độ extreme (cao nhất, thấp nhất)
4. So sánh xu hướng giữa các vùng miền
5. Tính correlation giữa nhiệt độ và lượng mưa
6. Detect anomaly patterns trong dữ liệu

**Dữ liệu mẫu:**

```python
import pandas as pd
import numpy as np

# Tạo time series data
years = range(1990, 2024)
regions = ['Bắc Bộ', 'Trung Bộ', 'Nam Bộ', 'Tây Nguyên']

data = []
np.random.seed(42)
for year in years:
    for region in regions:
        # Simulate climate change trend (+0.02°C per year)
        base_temp = {'Bắc Bộ': 23.5, 'Trung Bộ': 25.2, 'Nam Bộ': 27.1, 'Tây Nguyên': 21.8}[region]
        trend_temp = base_temp + (year - 1990) * 0.02 + np.random.normal(0, 0.8)

        rainfall = np.random.normal(1800, 300) + (year - 1990) * np.random.normal(-2, 5)

        data.append({
            'year': year,
            'region': region,
            'avg_temperature': round(trend_temp, 1),
            'total_rainfall': round(max(rainfall, 800), 1),
            'extreme_events': np.random.poisson(2)
        })

climate_df = pd.DataFrame(data)
```

**Output mẫu:**

```
Climate Change Analysis Report:
==============================
Temperature Trend (1990-2023):
- Bắc Bộ: +0.68°C (+0.020°C/year)
- Trung Bộ: +0.71°C (+0.021°C/year)
- Nam Bộ: +0.64°C (+0.019°C/year)
- Tây Nguyên: +0.73°C (+0.022°C/year)

Extreme Years:
- Hottest: 2023 (Tây Nguyên: 22.8°C)
- Coolest: 1991 (Tây Nguyên: 21.1°C)

Temperature-Rainfall Correlation: -0.23 (weak negative)
```

### Bài 2: Phân tích chất lượng không khí theo thời gian

Phân tích dữ liệu chất lượng không khí theo giờ, ngày, tháng để tìm patterns.

**Yêu cầu:**

1. Tạo time series với dữ liệu hourly PM2.5, PM10, NO2
2. Phân tích patterns theo giờ trong ngày và ngày trong tuần
3. Tính rolling statistics (mean, std, percentiles)
4. Identify peak pollution periods
5. Compare weekday vs weekend patterns
6. Seasonal decomposition của time series

**Dữ liệu mẫu:**

```python
# Tạo hourly air quality data for 6 months
date_range = pd.date_range('2024-01-01', '2024-06-30', freq='H')
locations = ['Hà Nội', 'TP.HCM', 'Đà Nẵng']

data = []
for timestamp in date_range:
    for location in locations:
        # Simulate daily and weekly patterns
        hour_factor = 1 + 0.3 * np.sin(2 * np.pi * timestamp.hour / 24)
        weekend_factor = 0.7 if timestamp.weekday() >= 5 else 1.0

        base_pm25 = {'Hà Nội': 35, 'TP.HCM': 42, 'Đà Nẵng': 28}[location]
        pm25 = max(5, base_pm25 * hour_factor * weekend_factor + np.random.normal(0, 8))

        data.append({
            'timestamp': timestamp,
            'location': location,
            'pm25': round(pm25, 1),
            'pm10': round(pm25 * 1.6 + np.random.normal(0, 5), 1),
            'no2': round(pm25 * 0.8 + np.random.normal(0, 3), 1)
        })

air_quality_df = pd.DataFrame(data)
```

### Bài 3: Phân tích dữ liệu NDVI từ ảnh vệ tinh

Phân tích sự thay đổi độ che phủ th 植植 vật qua thời gian bằng chỉ số NDVI.

**Yêu cầu:**

1. Tính NDVI trung bình theo tháng cho từng loại land cover
2. Phân tích seasonal patterns của vegetation
3. Detect deforestation events (NDVI drops significantly)
4. Compare NDVI trends between protected and non-protected areas
5. Calculate vegetation recovery rate after disturbances
6. Create vegetation health index

**Dữ liệu mẫu:**

```python
# Monthly NDVI data for different land cover types
months = pd.date_range('2020-01-01', '2023-12-01', freq='MS')
land_covers = ['Forest', 'Cropland', 'Urban', 'Water', 'Grassland']
protected_status = ['Protected', 'Non-protected']

ndvi_data = []
for month in months:
    for land_cover in land_covers:
        for status in protected_status:
            # Simulate seasonal NDVI patterns
            seasonal_factor = 0.2 * np.sin(2 * np.pi * month.month / 12)

            base_ndvi = {
                'Forest': 0.8, 'Cropland': 0.6, 'Urban': 0.2,
                'Water': -0.1, 'Grassland': 0.5
            }[land_cover]

            protection_factor = 0.1 if status == 'Protected' else 0
            trend_factor = -0.02 if land_cover == 'Forest' and status == 'Non-protected' else 0

            ndvi = base_ndvi + seasonal_factor + protection_factor + \
                   trend_factor * (month.year - 2020) + np.random.normal(0, 0.05)

            ndvi_data.append({
                'date': month,
                'land_cover': land_cover,
                'protected_status': status,
                'ndvi': round(max(-1, min(1, ndvi)), 3),
                'area_km2': np.random.uniform(100, 1000)
            })

ndvi_df = pd.DataFrame(ndvi_data)
```

### Bài 4: Phân tích kinh tế-xã hội từ dữ liệu không gian

Phân tích mối quan hệ giữa các chỉ số kinh tế xã hội và môi trường.

**Yêu cầu:**

1. Phân tích correlation giữa GDP, dân số và ô nhiễm
2. Clustering các tỉnh thành theo đặc điểm kinh tế-môi trường
3. Tính Environmental Kuznets Curve
4. Predict pollution levels based on economic indicators
5. Identify outliers và investigate causes
6. Create composite sustainability index

**Dữ liệu mẫu:**

```python
provinces = [
    'Hà Nội', 'TP.HCM', 'Hải Phòng', 'Đà Nẵng', 'Cần Thơ',
    'Bắc Ninh', 'Bình Dương', 'Đồng Nai', 'Khánh Hòa', 'Lâm Đồng',
    'Thanh Hóa', 'Nghệ An', 'Thừa Thiên Huế', 'Quảng Nam', 'Gia Lai'
]

socio_economic_data = []
for province in provinces:
    # Generate realistic socio-economic indicators
    gdp_per_capita = np.random.uniform(30, 180) * 1000000  # VND
    population = np.random.uniform(0.5, 9) * 1000000  # people
    urban_rate = np.random.uniform(20, 95)  # percentage

    # Pollution tends to increase with economic activity
    pollution_factor = (gdp_per_capita / 1000000) * 0.3 + (urban_rate / 100) * 0.4
    pm25 = max(15, pollution_factor * 50 + np.random.normal(0, 10))

    socio_economic_data.append({
        'province': province,
        'gdp_per_capita': round(gdp_per_capita),
        'population': round(population),
        'urban_rate': round(urban_rate, 1),
        'pm25_avg': round(pm25, 1),
        'forest_cover': round(np.random.uniform(20, 80), 1),
        'water_quality_index': round(np.random.uniform(60, 95), 1)
    })

socio_df = pd.DataFrame(socio_economic_data)
```

## Hướng dẫn giải

### Bài 1 - Climate Trend Analysis:

```python
# Calculate temperature trend
def calculate_trend(df, column):
    years = df['year'].values
    temps = df[column].values
    slope = np.polyfit(years, temps, 1)[0]
    return slope

# Group by region and calculate trends
trends = climate_df.groupby('region').apply(
    lambda x: calculate_trend(x, 'avg_temperature')
)

# Moving averages
climate_df['temp_ma5'] = climate_df.groupby('region')['avg_temperature'] \
                                  .rolling(window=5).mean().reset_index(drop=True)
```

### Bài 2 - Air Quality Time Series:

```python
# Set datetime index
air_quality_df.set_index('timestamp', inplace=True)

# Hourly patterns
hourly_pattern = air_quality_df.groupby([air_quality_df.index.hour, 'location']) \
                               .agg({'pm25': ['mean', 'std']})

# Weekend vs weekday
air_quality_df['is_weekend'] = air_quality_df.index.weekday >= 5
weekend_comparison = air_quality_df.groupby(['location', 'is_weekend'])['pm25'].mean()
```

### Bài 3 - NDVI Analysis:

```python
# Seasonal decomposition
from statsmodels.tsa.seasonal import seasonal_decompose

for land_cover in ndvi_df['land_cover'].unique():
    subset = ndvi_df[ndvi_df['land_cover'] == land_cover].set_index('date')
    decomposition = seasonal_decompose(subset['ndvi'], model='additive', period=12)
```

### Bài 4 - Socio-Economic Analysis:

```python
# Correlation analysis
correlation_matrix = socio_df[['gdp_per_capita', 'population', 'urban_rate',
                              'pm25_avg', 'forest_cover']].corr()

# Clustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

features = ['gdp_per_capita', 'urban_rate', 'pm25_avg', 'forest_cover']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(socio_df[features])

kmeans = KMeans(n_clusters=3, random_state=42)
socio_df['cluster'] = kmeans.fit_predict(scaled_features)
```

## Tiêu chí đánh giá

- [ ] Thực hiện time series analysis chính xác
- [ ] Tính toán statistical measures và trends đúng
- [ ] Identify patterns và anomalies hiệu quả
- [ ] Sử dụng groupby và aggregation functions thành thạo
- [ ] Phân tích correlation và relationships đúng cách
- [ ] Apply advanced analysis techniques (clustering, decomposition)
- [ ] Generate meaningful insights từ dữ liệu
- [ ] Create comprehensive analysis reports
- [ ] Validate kết quả và handle edge cases
- [ ] Code có structure rõ ràng và reproducible
