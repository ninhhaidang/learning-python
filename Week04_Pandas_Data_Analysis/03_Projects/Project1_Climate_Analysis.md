# Project 1: Phân tích dữ liệu khí tượng và biến đổi khí hậu Việt Nam

## Mô tả project

Dự án này yêu cầu bạn phân tích dữ liệu khí tượng dài hạn (1990-2023) để xác định xu hướng biến đổi khí hậu ở Việt Nam. Sử dụng pandas để xử lý time series data và tạo báo cáo khoa học về climate change.

## Mục tiêu học tập

- Thành thạo time series analysis với pandas
- Áp dụng statistical methods cho climate data
- Tạo insights từ long-term environmental data
- Phát triển kỹ năng data storytelling

## Bối cảnh thực tế

Biến đổi khí hậu đang ảnh hưởng nghiêm trọng đến Việt Nam với:

- Tăng nhiệt độ trung bình hàng năm
- Thay đổi patterns mưa mùa
- Tăng tần suất extreme weather events
- Ảnh hưởng đến nông nghiệp và an ninh lương thực

## Yêu cầu chức năng

### Phase 1: Data Processing (25%)

1. **Load và clean climate data** từ multiple sources

   - Temperature, rainfall, humidity data (1990-2023)
   - Handle missing values và outliers
   - Standardize data formats và units

2. **Create comprehensive time series**
   - Monthly, seasonal, annual aggregation
   - Multi-station data integration
   - Regional grouping (Bắc Bộ, Trung Bộ, Nam Bộ, Tây Nguyên)

### Phase 2: Trend Analysis (30%)

1. **Temperature trend analysis**

   - Calculate linear trends (°C/year) cho từng vùng
   - Identify warming rates và acceleration
   - Detect temperature anomalies và extreme years

2. **Precipitation pattern analysis**

   - Analyze rainfall trends và variability
   - Seasonal shift detection
   - Drought/flood frequency analysis

3. **Moving averages và smoothing**
   - 5-year, 10-year moving averages
   - Remove short-term noise
   - Highlight long-term signals

### Phase 3: Correlation Analysis (20%)

1. **Climate variables relationships**

   - Temperature vs rainfall correlation
   - Humidity trends với temperature changes
   - Regional climate coupling analysis

2. **Anomaly detection**
   - Identify unusual weather events
   - Calculate anomaly indices
   - Rank extreme years

### Phase 4: Statistical Testing (15%)

1. **Trend significance testing**

   - Mann-Kendall trend test
   - Linear regression significance
   - Confidence intervals

2. **Change point detection**
   - Identify when trends accelerated
   - Statistical breakpoint analysis

### Phase 5: Reporting (10%)

1. **Comprehensive climate report**
   - Executive summary với key findings
   - Detailed regional analysis
   - Visual data presentation
   - Future implications

## Dataset mô tả

### Cấu trúc dữ liệu

```python
climate_data = {
    'date': pd.date_range('1990-01-01', '2023-12-31', freq='MS'),  # Monthly data
    'station_id': ['HN001', 'HCM001', 'DN001', ...],              # 20 stations
    'station_name': ['Hà Nội', 'TP.HCM', 'Đà Nẵng', ...],
    'region': ['Bắc Bộ', 'Nam Bộ', 'Trung Bộ', 'Tây Nguyên'],
    'latitude': [21.0285, 10.8231, 16.0544, ...],
    'longitude': [105.8542, 106.6297, 108.2022, ...],
    'temperature': [18.5, 27.8, 22.4, ...],                       # °C
    'rainfall': [65.2, 245.8, 180.3, ...],                        # mm/month
    'humidity': [82, 76, 85, ...],                                 # %
    'pressure': [1013.2, 1011.5, 1012.8, ...],                   # hPa
    'wind_speed': [3.2, 2.1, 4.5, ...]                           # m/s
}
```

### Data quality issues

- ~3% missing values (equipment failures)
- Some outliers từ measurement errors
- Different measurement periods cho different stations
- Unit inconsistencies cần standardization

## Deliverables

### 1. Code implementation (`Project1_Climate_Analysis.py`)

```python
class ClimateAnalyzer:
    def __init__(self, data_path):
        # Initialize with data loading

    def load_and_clean_data(self):
        # Data loading và preprocessing

    def calculate_trends(self):
        # Temperature và rainfall trend analysis

    def detect_anomalies(self):
        # Extreme events detection

    def generate_report(self):
        # Comprehensive climate report
```

### 2. Analysis report

- **Executive Summary** (1 trang)
- **Methodology** (1 trang)
- **Regional Analysis** (2 trang)
- **Key Findings** (1 trang)
- **Recommendations** (1 trang)

### 3. Visualizations

- Temperature trends by region
- Rainfall anomaly maps
- Correlation heatmaps
- Extreme events timeline

## Technical requirements

### Core libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler
```

### Key functions cần implement

1. `load_climate_data()` - Multi-source data loading
2. `clean_and_validate()` - Data quality assurance
3. `calculate_linear_trends()` - Trend analysis
4. `detect_change_points()` - Statistical change detection
5. `generate_climate_report()` - Automated reporting

## Expected outputs

### Climate Change Summary

```
Vietnam Climate Change Analysis (1990-2023)
==========================================
Temperature Trends:
- National average: +0.68°C (+0.020°C/year)
- Bắc Bộ: +0.71°C (fastest warming)
- Trung Bộ: +0.65°C
- Nam Bộ: +0.62°C
- Tây Nguyên: +0.73°C

Precipitation Changes:
- National trend: -2.1% (-8.4mm/year)
- Increased variability: +15%
- More extreme events: +23%

Extreme Years:
- Hottest: 2023 (avg +1.2°C above 1990s)
- Driest: 2020 (-18% rainfall)
- Most variable: 2016-2020 period
```

## Đánh giá criteria

### Technical Implementation (40%)

- [ ] Clean code structure và documentation
- [ ] Efficient pandas operations
- [ ] Proper error handling
- [ ] Statistical methods accuracy

### Analysis Quality (35%)

- [ ] Comprehensive trend analysis
- [ ] Valid statistical testing
- [ ] Meaningful anomaly detection
- [ ] Regional comparison insights

### Presentation (25%)

- [ ] Clear data visualizations
- [ ] Well-structured report
- [ ] Scientific writing quality
- [ ] Actionable recommendations

## Bonus challenges

### Advanced analytics

1. **Seasonal decomposition** of climate signals
2. **Machine learning** trend prediction
3. **Spatial interpolation** between stations
4. **Climate index** calculation (e.g., local warming index)

### Real-world integration

1. **Compare with global datasets** (NASA GISS, NOAA)
2. **Agricultural impact** correlation
3. **Economic impact** quantification
4. **Policy recommendation** development

## Resources

### Scientific references

- IPCC Climate Change reports
- Vietnam National Climate Change Strategy
- Regional climate studies in Southeast Asia

### Technical documentation

- Pandas time series documentation
- Statistical trend analysis methods
- Climate data best practices

---

**Note**: Project này requires strong analytical thinking và scientific approach. Focus on data quality, statistical rigor, và meaningful interpretation of results.

**Timeline**: 2-3 weeks for complete implementation and analysis
**Difficulty**: Advanced level
