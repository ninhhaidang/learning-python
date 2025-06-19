# Project 3: Phân tích dữ liệu NDVI và thay đổi sử dụng đất

## Mô tả project

Phân tích dữ liệu NDVI (Normalized Difference Vegetation Index) từ ảnh vệ tinh để theo dõi sự thay đổi độ che phủ th 植 vật và sử dụng đất ở Việt Nam. Sử dụng pandas để xử lý time series dữ liệu viễn thám và detect các thay đổi môi trường.

## Mục tiêu học tập

- Thành thạo xử lý satellite data với pandas
- Phân tích time series environmental data
- Detect land cover changes và deforestation patterns
- Áp dụng statistical analysis cho environmental monitoring
- Tạo environmental assessment reports

## Bối cảnh thực tế

Việt Nam đang đối mặt với những thay đổi lớn về sử dụng đất:

- Mất rừng do phát triển kinh tế và đô thị hóa
- Chuyển đổi từ rừng sang nông nghiệp
- Ảnh hưởng của biến đổi khí hậu lên vegetation
- Cần monitoring system để bảo vệ môi trường

## Yêu cầu chức năng

### Phase 1: Data Processing (25%)

1. **NDVI time series analysis**

   - Load monthly NDVI data (2015-2023)
   - Handle missing values và cloud contamination
   - Temporal filtering và smoothing
   - Quality assessment của satellite data

2. **Land cover classification**
   - NDVI-based land cover mapping
   - Forest, cropland, urban, water body classification
   - Protected vs non-protected area analysis
   - Administrative boundary integration

### Phase 2: Change Detection (30%)

1. **Vegetation trend analysis**

   - Long-term NDVI trends per land cover type
   - Seasonal pattern analysis
   - Phenology cycle extraction
   - Climate impact on vegetation

2. **Deforestation detection**

   - Significant NDVI drops identification
   - Change magnitude và duration analysis
   - Hotspot mapping và prioritization
   - Recovery pattern assessment

3. **Land use conversion tracking**
   - Forest to agriculture conversion
   - Urban expansion monitoring
   - Wetland changes detection
   - Infrastructure impact assessment

### Phase 3: Statistical Analysis (20%)

1. **Trend significance testing**

   - Mann-Kendall trend tests
   - Breakpoint detection
   - Confidence interval estimation
   - Spatial autocorrelation analysis

2. **Correlation analysis**
   - NDVI vs climate variables
   - Elevation và slope relationships
   - Socio-economic drivers
   - Policy impact assessment

### Phase 4: Environmental Indicators (15%)

1. **Vegetation health indices**

   - Vegetation Condition Index (VCI)
   - Temperature Vegetation Dryness Index (TVDI)
   - Ecosystem health scoring
   - Biodiversity proxy indicators

2. **Carbon stock estimation**
   - NDVI-based biomass estimation
   - Carbon sequestration potential
   - Deforestation carbon emissions
   - Reforestation impact quantification

### Phase 5: Reporting & Alerts (10%)

1. **Automated monitoring**
   - Real-time deforestation alerts
   - Vegetation stress warnings
   - Recovery progress tracking
   - Policy compliance monitoring

## Dataset mô tả

### NDVI time series structure

```python
ndvi_data = {
    'date': pd.date_range('2015-01-01', '2023-12-01', freq='MS'),  # Monthly
    'pixel_id': range(1, 100001),                                 # 100k pixels
    'latitude': [10.5 + i*0.001 for i in range(100000)],         # Vietnam extent
    'longitude': [106.0 + i*0.001 for i in range(100000)],
    'ndvi': [-1 to 1],                                           # NDVI values
    'land_cover': ['Forest', 'Cropland', 'Urban', 'Water', 'Grassland'],
    'protected_status': ['Protected', 'Non-protected'],
    'province': ['An Giang', 'Bà Rịa-Vũng Tàu', ...],         # 63 provinces
    'elevation': [0 to 3000],                                    # meters
    'slope': [0 to 45],                                          # degrees
    'quality_flag': ['Good', 'Cloud', 'Shadow', 'Snow']         # Data quality
}
```

### Auxiliary data

```python
# Climate data
climate_data = {
    'date': pd.date_range('2015-01-01', '2023-12-31', freq='D'),
    'province': ['An Giang', 'Bà Rịa-Vũng Tàu', ...],
    'temperature': [20 to 35],                                   # °C
    'rainfall': [0 to 500],                                      # mm/month
    'humidity': [60 to 95],                                      # %
    'drought_index': [-3 to 3]                                  # SPI
}

# Socio-economic data
socio_data = {
    'province': ['An Giang', 'Bà Rịa-Vũng Tàu', ...],
    'year': range(2015, 2024),
    'population': [500000 to 9000000],                          # people
    'gdp_per_capita': [20 to 200],                              # million VND
    'forest_policy_score': [1 to 10],                           # protection level
    'agricultural_expansion': [0 to 100]                        # km²/year
}
```

### Data challenges

- Cloud contamination (~20% of observations)
- Seasonal variations in data quality
- Mixed pixels at land cover boundaries
- Geometric corrections needed
- Different satellite sensors over time

## Deliverables

### 1. Core analysis system (`Project3_NDVI_LandUse.py`)

```python
class NDVILandUseAnalyzer:
    def __init__(self, data_path):
        # System initialization

    def load_satellite_data(self):
        # Multi-temporal NDVI loading

    def classify_land_cover(self):
        # NDVI-based classification

    def detect_changes(self):
        # Change detection algorithms

    def calculate_indicators(self):
        # Environmental health indices

    def generate_alerts(self):
        # Deforestation alert system
```

### 2. Change detection results

- **Deforestation hotspots** with coordinates và severity
- **Reforestation areas** với recovery rates
- **Land use transitions** matrix by province
- **Vegetation stress maps** during drought periods

### 3. Environmental reports

- **Annual vegetation assessment** by province
- **Deforestation impact** on carbon stocks
- **Policy effectiveness** evaluation
- **Climate change adaptation** recommendations

## Technical requirements

### Core libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, signal
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import rasterio  # For satellite data (if available)
import geopandas as gpd  # For spatial operations (if available)
```

### Key algorithms cần implement

1. `calculate_ndvi_trends()` - Time series trend analysis
2. `detect_breakpoints()` - Change point detection
3. `classify_changes()` - Change type classification
4. `calculate_vci()` - Vegetation condition index
5. `estimate_biomass()` - Carbon stock estimation

## Expected outputs

### Provincial deforestation report

```
VIETNAM FOREST MONITORING REPORT (2015-2023)
=============================================

National Summary:
• Total forest loss: 1,234,567 ha (2.3% of total forest area)
• Deforestation rate: 154,321 ha/year (decreasing trend)
• Primary forest loss: 567,890 ha (critically important)
• Reforestation: 890,123 ha (recovery efforts)

Top 5 Provinces with Highest Forest Loss:
1. Đắk Lắk: 89,432 ha (agricultural expansion)
2. Gia Lai: 76,543 ha (infrastructure development)
3. Kon Tum: 65,432 ha (logging activities)
4. Lâm Đồng: 54,321 ha (urban expansion)
5. Đắk Nông: 43,210 ha (agricultural conversion)

Protected Area Performance:
• National parks: 98.5% forest retention
• Nature reserves: 96.2% forest retention
• Non-protected areas: 91.7% forest retention

Climate Impact Analysis:
• Drought years (2016, 2020): 15% higher deforestation
• NDVI correlation with rainfall: r = 0.67
• Temperature stress threshold: >32°C for >30 days
```

### Real-time monitoring alerts

```
DEFORESTATION ALERT SYSTEM
==========================
Date: 2024-01-15

New Alerts (Last 30 days): 23 sites
High Priority: 5 sites (>100 ha loss)
Medium Priority: 12 sites (10-100 ha loss)
Low Priority: 6 sites (<10 ha loss)

Alert Details:
┌─────────────┬────────────┬──────────┬─────────────┬──────────┐
│ Province    │ Location   │ Area(ha) │ NDVI Drop   │ Priority │
├─────────────┼────────────┼──────────┼─────────────┼──────────┤
│ Đắk Lắk     │ 12.5°N     │ 245.3    │ -0.45       │ HIGH     │
│             │ 108.2°E    │          │             │          │
│ Gia Lai     │ 13.8°N     │ 89.7     │ -0.38       │ MEDIUM   │
│             │ 107.9°E    │          │             │          │
└─────────────┴────────────┴──────────┴─────────────┴──────────┘

Recommended Actions:
• Deploy field verification teams to HIGH priority sites
• Coordinate with local forest protection departments
• Update illegal logging database
• Issue public awareness notifications
```

## Đánh giá criteria

### Technical Implementation (35%)

- [ ] Robust time series processing
- [ ] Accurate change detection algorithms
- [ ] Proper statistical testing
- [ ] Efficient data handling

### Scientific Accuracy (30%)

- [ ] Valid NDVI interpretation
- [ ] Appropriate statistical methods
- [ ] Realistic threshold settings
- [ ] Climate correlation analysis

### Environmental Impact (25%)

- [ ] Meaningful change detection
- [ ] Policy-relevant insights
- [ ] Conservation recommendations
- [ ] Monitoring system effectiveness

### Documentation (10%)

- [ ] Clear methodology description
- [ ] Reproducible analysis
- [ ] User manual completion
- [ ] Scientific report quality

## Bonus challenges

### Advanced analytics

1. **Machine learning integration**

   - Random Forest for land cover classification
   - Time series forecasting with LSTM
   - Anomaly detection algorithms

2. **Spatial analysis**

   - Landscape fragmentation metrics
   - Connectivity index calculation
   - Edge effect quantification

3. **Economic valuation**
   - Ecosystem service valuation
   - Cost-benefit analysis of conservation
   - Payment for ecosystem services design

### Real-world deployment

1. **Government integration**

   - Ministry of Natural Resources reporting
   - Provincial environmental monitoring
   - International commitment tracking

2. **Public engagement**
   - Citizen science data collection
   - Community-based monitoring
   - Educational outreach programs

## Resources

### Scientific references

- NDVI methodology và applications
- Remote sensing của tropical forests
- Climate change impact on Southeast Asian ecosystems

### Technical documentation

- Pandas time series analysis
- Statistical change detection methods
- Satellite data processing workflows

---

**Note**: Project này requires understanding của remote sensing principles và environmental science. Focus on scientific rigor, policy relevance, và practical monitoring applications.

**Timeline**: 3-4 weeks for complete system development
**Difficulty**: Advanced level
