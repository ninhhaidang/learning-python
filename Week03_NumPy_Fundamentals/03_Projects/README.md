# Week 03 Projects: NumPy Applications

## Project Overview

Tuần 3 tập trung vào các dự án thực tế ứng dụng NumPy trong data science và geographic analysis. Mỗi project sẽ kết hợp nhiều kỹ năng NumPy đã học.

---

## Project 1: Vietnam Weather Analysis System 🌤️

### Mô tả

Xây dựng hệ thống phân tích dữ liệu thời tiết Việt Nam sử dụng NumPy, mô phỏng dữ liệu từ 63 tỉnh thành trong 2 năm.

### Mục tiêu học tập

- Structured arrays cho dữ liệu phức tạp
- Time series analysis với NumPy
- Statistical analysis và visualization
- Array I/O operations
- Performance optimization

### Yêu cầu kỹ thuật

#### Core Features:

1. **Data Generation**: Tạo synthetic weather data

   - 63 tỉnh thành × 730 ngày × 5 parameters
   - Parameters: temperature, humidity, pressure, rainfall, wind_speed
   - Seasonal patterns + regional variations + random noise

2. **Statistical Analysis**:

   - Monthly/seasonal averages per province
   - Extreme weather detection
   - Correlation analysis between parameters
   - Trend analysis (warming/cooling trends)

3. **Geographic Analysis**:

   - North/Central/South regional comparisons
   - Coastal vs inland climate differences
   - Elevation impact simulation

4. **Reporting System**:
   - Generate comprehensive weather reports
   - Export data to CSV/NPY formats
   - Summary statistics và rankings

#### Advanced Features:

1. **Climate Pattern Detection**: Identify monsoon seasons, dry periods
2. **Anomaly Detection**: Find unusual weather events
3. **Forecasting**: Simple linear/polynomial trend extrapolation
4. **Visualization Preparation**: Format data for plotting

### Deliverables

```
Project1_Vietnam_Weather/
├── src/
│   ├── data_generator.py      # Weather data generation
│   ├── analysis_engine.py     # Statistical analysis
│   ├── geographic_analyzer.py # Regional analysis
│   ├── report_generator.py    # Report generation
│   └── main.py               # Main application
├── data/
│   ├── provinces.csv         # Province coordinates
│   ├── weather_raw.npy       # Generated weather data
│   └── weather_processed.npz # Processed results
├── outputs/
│   ├── weather_report.txt    # Text report
│   ├── statistics.csv        # Summary statistics
│   └── extremes.csv          # Extreme events
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies
```

### Sample Output

```
=== VIETNAM WEATHER ANALYSIS REPORT ===
Analysis Period: 2022-2024 (730 days)
Provinces Analyzed: 63

NATIONAL SUMMARY:
Average Temperature: 26.3°C (±4.2°C)
Average Humidity: 78.5% (±12.1%)
Average Rainfall: 4.2mm/day (±8.7mm)
Total Rainfall: 3,066mm/year

REGIONAL COMPARISON:
North (20 provinces): 23.1°C, 82.3% humidity
Central (19 provinces): 26.8°C, 76.1% humidity
South (24 provinces): 28.9°C, 77.2% humidity

EXTREME EVENTS:
Hottest day: 42.1°C (An Giang, 15/04/2023)
Coldest day: 2.3°C (Sa Pa, 28/01/2023)
Wettest day: 234mm (Quang Binh, 18/10/2023)
Longest drought: 45 days (Ninh Thuan)

CLIMATE TRENDS:
Temperature: +0.02°C/month (warming)
Rainfall: -0.3mm/month (drying trend)
Humidity: stable (±0.1%/month)
```

---

## Project 2: Satellite Image Processing Simulator 🛰️

### Mô tả

Mô phỏng xử lý ảnh vệ tinh sử dụng NumPy arrays, bao gồm land cover classification, NDVI calculation, và change detection.

### Mục tiêu học tập

- Multi-dimensional array manipulation
- Image processing techniques
- Advanced indexing và masking
- Custom functions và vectorization
- Memory optimization cho large arrays

### Yêu cầu kỹ thuật

#### Core Features:

1. **Synthetic Image Generation**:

   - Multi-spectral images (RGB + NIR bands)
   - Different land cover types (water, vegetation, urban, bare soil)
   - Realistic spatial patterns và noise

2. **Image Processing Pipeline**:

   - Radiometric correction
   - Atmospheric correction simulation
   - Band math calculations (NDVI, NDWI, etc.)
   - Image filtering và smoothing

3. **Classification System**:

   - Unsupervised classification (K-means-like)
   - Rule-based classification
   - Accuracy assessment

4. **Change Detection**:
   - Multi-temporal analysis
   - Change maps generation
   - Statistics về land cover changes

#### Advanced Features:

1. **Vegetation Analysis**: NDVI trends, biomass estimation
2. **Water Body Detection**: Automated water mapping
3. **Urban Growth Analysis**: Urban expansion simulation
4. **Performance Optimization**: Memory-efficient processing

### Deliverables

```
Project2_Satellite_Processing/
├── src/
│   ├── image_generator.py     # Synthetic image creation
│   ├── preprocessor.py        # Image preprocessing
│   ├── calculator.py          # Band math và indices
│   ├── classifier.py          # Land cover classification
│   ├── change_detector.py     # Change detection
│   └── main.py               # Main pipeline
├── data/
│   ├── scene_2022.npy        # Synthetic 2022 image
│   ├── scene_2024.npy        # Synthetic 2024 image
│   └── metadata.json         # Image metadata
├── outputs/
│   ├── ndvi_map.npy          # NDVI results
│   ├── classification.npy     # Land cover map
│   ├── change_map.npy        # Change detection
│   └── statistics.csv        # Area statistics
├── README.md
└── demo.py                   # Interactive demo
```

### Sample Output

```
=== SATELLITE IMAGE ANALYSIS RESULTS ===
Study Area: 100km × 100km (10,000 pixels)
Time Period: 2022 → 2024 (2 years)

IMAGE STATISTICS:
2022 Scene:
- Water bodies: 1,847 pixels (18.5%)
- Vegetation: 4,521 pixels (45.2%)
- Urban areas: 2,156 pixels (21.6%)
- Bare soil: 1,476 pixels (14.8%)

2024 Scene:
- Water bodies: 1,823 pixels (18.2%)
- Vegetation: 4,298 pixels (43.0%)
- Urban areas: 2,401 pixels (24.0%)
- Bare soil: 1,478 pixels (14.8%)

CHANGE DETECTION:
Urban expansion: +245 pixels (+2.4%)
Vegetation loss: -223 pixels (-2.2%)
Water loss: -24 pixels (-0.3%)

VEGETATION HEALTH:
Average NDVI: 0.67 (healthy)
NDVI trend: -0.02 (slight decline)
Stressed vegetation: 234 pixels (5.2%)

PROCESSING PERFORMANCE:
Total processing time: 2.34 seconds
Memory usage: 45.2 MB
Images processed: 2 scenes × 4 bands
```

---

## Project 3: Economic Data Dashboard với NumPy 📊

### Mô tả

Xây dựng dashboard phân tích dữ liệu kinh tế Việt Nam (GDP, inflation, trade) sử dụng NumPy cho tính toán nền.

### Mục tiêu học tập

- Time series manipulation
- Financial calculations
- Multi-dimensional data analysis
- Performance benchmarking
- Data export cho visualization

### Yêu cầu kỹ thuật

#### Core Features:

1. **Economic Indicators Simulation**:

   - GDP growth rates (63 provinces, 10 years)
   - Inflation rates, unemployment rates
   - Import/export data, FDI flows

2. **Financial Calculations**:

   - Growth rate calculations
   - Moving averages và trends
   - Correlation analysis
   - Volatility measurements

3. **Comparative Analysis**:

   - Province rankings
   - Regional performance comparison
   - Sector analysis
   - Time series forecasting

4. **Dashboard Data Preparation**:
   - Aggregation functions
   - Pivot table simulation
   - Export formats for charts

### Deliverables

```
Project3_Economic_Dashboard/
├── src/
│   ├── data_simulator.py      # Economic data generation
│   ├── calculator.py          # Financial calculations
│   ├── analyzer.py            # Comparative analysis
│   ├── dashboard_backend.py   # Dashboard data prep
│   └── main.py               # Main application
├── data/
│   ├── provinces_economic.csv # Province economic data
│   ├── indicators.npz        # Economic indicators
│   └── metadata.json         # Data dictionary
├── outputs/
│   ├── dashboard_data.json   # Dashboard ready data
│   ├── rankings.csv          # Province rankings
│   ├── trends.csv            # Trend analysis
│   └── forecast.csv          # Simple forecasts
├── README.md
└── demo_dashboard.py         # Demo dashboard
```

---

## Evaluation Criteria

### Technical Skills (40%)

- [ ] NumPy mastery: arrays, operations, functions
- [ ] Code efficiency và performance
- [ ] Memory management
- [ ] Error handling

### Problem Solving (30%)

- [ ] Algorithm design
- [ ] Data structure choices
- [ ] Optimization techniques
- [ ] Creative solutions

### Code Quality (20%)

- [ ] Clean, readable code
- [ ] Proper documentation
- [ ] Modular design
- [ ] Testing coverage

### Real-world Application (10%)

- [ ] Practical relevance
- [ ] Domain knowledge
- [ ] User experience
- [ ] Scalability considerations

---

## Submission Guidelines

### Deadline

**End of Week 3** (7 days from project assignment)

### Submission Format

1. **GitHub Repository** hoặc **ZIP file**
2. **README.md** với project overview và usage instructions
3. **Requirements.txt** với dependencies
4. **Demo script** để test functionality
5. **Brief report** (1-2 pages) về technical choices và challenges

### Presentation

- **5-minute demo** của main features
- **Q&A session** về implementation
- **Code walkthrough** của key algorithms

---

## Resources và Support

### Documentation

- [NumPy Official Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [Scientific Python Ecosystem](https://scipy.org/)

### Sample Data Sources

- Vietnam geographic data
- Weather station networks
- Economic indicators databases
- Satellite imagery examples

### Help & Support

- **Office hours**: Tuesdays, Thursdays 2-4 PM
- **Discussion forum**: Available 24/7
- **Peer collaboration**: Encouraged (with proper attribution)

---

**Good luck với projects! 🚀**
