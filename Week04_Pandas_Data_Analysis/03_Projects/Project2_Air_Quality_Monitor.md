# Project 2: Hệ thống giám sát chất lượng không khí thành phố

## Mô tả project

Xây dựng hệ thống phân tích và giám sát chất lượng không khí real-time cho các thành phố lớn ở Việt Nam. Sử dụng pandas để xử lý dữ liệu từ multiple sensors, API weather data, và tạo dashboard báo cáo tự động.

## Mục tiêu học tập

- Thành thạo data integration từ nhiều nguồn khác nhau
- Xử lý real-time data streams với pandas
- Áp dụng data quality control và validation
- Tạo automated reporting system

## Bối cảnh thực tế

Ô nhiễm không khí đang trở thành vấn đề nghiêm trọng tại các thành phố lớn Việt Nam:

- Hà Nội, TP.HCM thường xuyên vượt ngưỡng WHO
- PM2.5, PM10 từ giao thông và công nghiệp
- Thiếu hệ thống monitoring tích hợp
- Cần cảnh báo sớm cho cộng đồng

## Yêu cầu chức năng

### Phase 1: Data Integration (25%)

1. **Multi-source data loading**

   - Air quality sensors (PM2.5, PM10, NO2, SO2, CO, O3)
   - Weather stations (temperature, humidity, wind, pressure)
   - Traffic density APIs
   - Industrial emission reports

2. **Data synchronization và validation**
   - Handle different sampling frequencies
   - Timestamp alignment across sources
   - Data quality flags và error detection
   - Real-time data ingestion simulation

### Phase 2: Data Processing (30%)

1. **Real-time data cleaning**

   - Outlier detection và removal
   - Sensor calibration adjustments
   - Missing data interpolation
   - Quality assurance protocols

2. **Air Quality Index calculation**

   - Vietnam AQI standards implementation
   - Sub-index calculations per pollutant
   - Health risk categorization
   - Trend analysis và forecasting

3. **Spatial analysis**
   - Station-to-station correlation
   - Urban vs suburban patterns
   - Pollution hotspot identification
   - Wind direction impact analysis

### Phase 3: Alert System (20%)

1. **Threshold monitoring**

   - WHO guidelines compliance
   - Vietnam national standards
   - Health advisory thresholds
   - Trend-based early warnings

2. **Automated notifications**
   - Exceedance alerts
   - Health recommendations
   - Vulnerable group advisories
   - Emergency response triggers

### Phase 4: Analytics & Reporting (15%)

1. **Statistical analysis**

   - Daily, weekly, monthly trends
   - Seasonal patterns identification
   - Correlation with meteorology
   - Long-term health impact assessment

2. **Performance metrics**
   - Data coverage và availability
   - Sensor reliability scores
   - Prediction accuracy tracking
   - System uptime monitoring

### Phase 5: Dashboard & Visualization (10%)

1. **Real-time dashboard**
   - Current AQI display
   - Station status monitoring
   - Trend charts và heatmaps
   - Alert status indicators

## Dataset mô tả

### Multi-source data structure

```python
# Air quality sensors (5-minute intervals)
air_quality_data = {
    'timestamp': pd.date_range('2024-01-01', periods=105120, freq='5min'),
    'station_id': ['HN_AQ_001', 'HCM_AQ_002', ...],
    'pm25': [35.2, 42.8, ...],                    # μg/m³
    'pm10': [58.4, 67.2, ...],                    # μg/m³
    'no2': [28.5, 35.7, ...],                     # μg/m³
    'so2': [15.2, 18.3, ...],                     # μg/m³
    'co': [1.8, 2.3, ...],                        # mg/m³
    'o3': [89.2, 95.7, ...],                      # μg/m³
    'status': ['Valid', 'Maintenance', ...]
}

# Weather data (10-minute intervals)
weather_data = {
    'timestamp': pd.date_range('2024-01-01', periods=52560, freq='10min'),
    'station_id': ['HN_WX_001', 'HCM_WX_002', ...],
    'temperature': [18.5, 27.8, ...],             # °C
    'humidity': [82, 76, ...],                     # %
    'wind_speed': [3.2, 2.1, ...],                # m/s
    'wind_direction': [45, 120, ...],             # degrees
    'pressure': [1013.2, 1011.5, ...],           # hPa
    'visibility': [8.5, 12.3, ...]               # km
}

# Traffic data (hourly)
traffic_data = {
    'timestamp': pd.date_range('2024-01-01', periods=8760, freq='H'),
    'location_id': ['HN_TR_001', 'HCM_TR_002', ...],
    'vehicle_count': [1250, 2340, ...],           # vehicles/hour
    'average_speed': [25.5, 18.2, ...],           # km/h
    'congestion_level': ['Medium', 'High', ...]
}
```

### Data quality challenges

- ~5% sensor downtime và maintenance periods
- Different measurement frequencies across sensors
- Network connectivity issues
- Calibration drift over time
- Weather impact on sensor accuracy

## Deliverables

### 1. Core system (`Project2_Air_Quality_Monitor.py`)

```python
class AirQualityMonitor:
    def __init__(self, config_file):
        # System initialization

    def load_real_time_data(self):
        # Multi-source data ingestion

    def calculate_aqi(self):
        # Vietnam AQI calculation

    def detect_anomalies(self):
        # Real-time quality control

    def generate_alerts(self):
        # Threshold-based alerting

    def create_dashboard(self):
        # Real-time monitoring dashboard
```

### 2. Monitoring dashboard

- **Real-time AQI map** với color-coded stations
- **Trend charts** for last 24h, 7d, 30d
- **Alert panel** với current warnings
- **Data quality indicators** per station

### 3. Automated reports

- **Daily summary** email reports
- **Weekly trend** analysis
- **Monthly compliance** reporting
- **Annual air quality** assessment

## Technical requirements

### Core libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import requests  # For API data
import sqlite3  # For data storage
from scipy import stats
import plotly.express as px  # Interactive plots
```

### Key functions cần implement

1. `ingest_sensor_data()` - Real-time data collection
2. `calculate_vietnam_aqi()` - AQI computation
3. `quality_control()` - Data validation pipeline
4. `generate_alerts()` - Threshold monitoring
5. `create_dashboard()` - Visualization system

## Expected outputs

### Real-time monitoring display

```
VIETNAM AIR QUALITY MONITORING SYSTEM
=====================================
Last updated: 2024-01-15 14:30:00

Current Status:
┌─────────────┬─────────┬─────────┬──────────┬─────────┐
│ Station     │ AQI     │ PM2.5   │ Status   │ Trend   │
├─────────────┼─────────┼─────────┼──────────┼─────────┤
│ Hà Nội      │ 89      │ 35.2    │ Moderate │ ↗       │
│ TP.HCM      │ 105     │ 42.8    │ USG      │ ↗↗      │
│ Đà Nẵng     │ 72      │ 28.9    │ Moderate │ →       │
│ Hải Phòng   │ 95      │ 38.7    │ Moderate │ ↗       │
└─────────────┴─────────┴─────────┴──────────┴─────────┘

Active Alerts: 2
• TP.HCM: Unhealthy for Sensitive Groups (AQI: 105)
• Hà Nội: Trending upward - watch for exceedance

Data Quality: 94.2% (47/50 stations online)
```

### Daily summary report

```
DAILY AIR QUALITY REPORT - 2024-01-15
=====================================

Summary Statistics:
• National average AQI: 78 (Moderate)
• Stations exceeding WHO PM2.5: 32/50 (64%)
• Peak pollution hour: 08:00-09:00
• Cleanest hour: 05:00-06:00

Regional Analysis:
• Bắc Bộ: AQI 85 (↑5 from yesterday)
• Trung Bộ: AQI 68 (↓2 from yesterday)
• Nam Bộ: AQI 82 (↑8 from yesterday)

Weather Impact:
• Low wind speed contributed to accumulation
• High humidity (>85%) affected sensor readings
• Temperature inversion layer observed 06:00-08:00

Recommendations:
• Sensitive groups avoid outdoor activities 07:00-10:00
• General public limit prolonged outdoor exercise
• Consider mask usage in high-traffic areas
```

## Đánh giá criteria

### Technical Implementation (40%)

- [ ] Robust data ingestion pipeline
- [ ] Accurate AQI calculations
- [ ] Effective anomaly detection
- [ ] Reliable alert system

### Data Quality (30%)

- [ ] Comprehensive validation protocols
- [ ] Proper handling of missing data
- [ ] Statistical quality control
- [ ] Error propagation analysis

### User Interface (20%)

- [ ] Intuitive dashboard design
- [ ] Clear data visualization
- [ ] Responsive alert system
- [ ] Mobile-friendly display

### Documentation (10%)

- [ ] Technical documentation
- [ ] User manual
- [ ] API documentation
- [ ] Maintenance procedures

## Bonus challenges

### Advanced features

1. **Machine learning integration**

   - Pollution forecasting models
   - Sensor failure prediction
   - Traffic correlation analysis

2. **Mobile app integration**

   - Push notifications
   - Location-based alerts
   - Personal exposure tracking

3. **Public API development**
   - RESTful API for data access
   - Rate limiting và authentication
   - Developer documentation

### Real-world integration

1. **Government compliance**

   - Regulatory reporting formats
   - Data sharing protocols
   - Emergency response integration

2. **Public health integration**
   - Hospital admission correlation
   - Vulnerable population tracking
   - Health advisory automation

## Resources

### Air quality standards

- WHO Air Quality Guidelines
- Vietnam National Technical Regulation (QCVN)
- US EPA AQI calculation methods

### Technical references

- Pandas time series documentation
- Real-time data processing patterns
- IoT sensor data best practices

---

**Note**: Project này requires understanding của air quality science và real-time systems. Focus on data reliability, user safety, và system robustness.

**Timeline**: 2-3 weeks for complete system development
**Difficulty**: Intermediate-Advanced level
