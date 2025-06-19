# Project 1: Vietnam Weather Analysis System 🌤️

## Mục tiêu Project

Xây dựng hệ thống phân tích dữ liệu thời tiết Việt Nam sử dụng NumPy, mô phỏng dữ liệu từ 63 tỉnh thành trong 2 năm.

## Yêu cầu Kỹ thuật

### Phase 1: Data Generation (25 điểm)

**File: `data_generator.py`**

1. **Province Data Setup**

   - Tạo structured array cho 63 tỉnh thành
   - Fields: province_name, region, latitude, longitude, elevation
   - Sử dụng real coordinates của các tỉnh Việt Nam

2. **Weather Data Generation**

   - 730 ngày × 63 tỉnh × 5 parameters
   - Parameters: temperature, humidity, pressure, rainfall, wind_speed
   - Áp dụng seasonal patterns và regional variations

3. **Data Validation**
   - Check data ranges (temperature: -5°C to 45°C)
   - Ensure no missing values
   - Validate array shapes và dtypes

### Phase 2: Statistical Analysis (30 điểm)

**File: `analysis_engine.py`**

1. **Descriptive Statistics**

   - Mean, median, std, min, max cho từng parameter
   - Monthly và seasonal aggregations
   - Percentile calculations (5th, 25th, 75th, 95th)

2. **Extreme Weather Detection**

   - Identify heatwaves (temp > 35°C for 3+ consecutive days)
   - Cold spells (temp < 10°C for 2+ consecutive days)
   - Heavy rainfall events (>50mm/day)

3. **Trend Analysis**
   - Linear trend fitting cho temperature data
   - Year-over-year comparisons
   - Seasonal cycle analysis

### Phase 3: Geographic Analysis (25 điểm)

**File: `geographic_analyzer.py`**

1. **Regional Comparisons**

   - North (20 tỉnh), Central (19 tỉnh), South (24 tỉnh)
   - Average conditions per region
   - Regional weather pattern differences

2. **Elevation Impact**

   - Correlation between elevation và temperature
   - Highland vs lowland climate analysis

3. **Coastal vs Inland**
   - Classify provinces as coastal/inland
   - Compare humidity và temperature patterns

### Phase 4: Reporting System (20 điểm)

**File: `report_generator.py`**

1. **Text Reports**

   - National weather summary
   - Regional comparisons
   - Extreme events listing
   - Monthly statistics tables

2. **Data Export**

   - CSV exports cho charts
   - NPZ files cho processed data
   - JSON summary cho dashboards

3. **Performance Metrics**
   - Processing time measurement
   - Memory usage optimization
   - Data compression ratios

## Deliverables

### Required Files

```
Project1_Vietnam_Weather/
├── src/
│   ├── data_generator.py      # Weather data generation
│   ├── analysis_engine.py     # Statistical analysis
│   ├── geographic_analyzer.py # Regional analysis
│   ├── report_generator.py    # Report generation
│   └── main.py               # Main application
├── data/
│   ├── provinces.csv         # Province information
│   ├── weather_raw.npy       # Generated weather data
│   └── weather_processed.npz # Processed results
├── outputs/
│   ├── weather_report.txt    # Text report
│   ├── statistics.csv        # Summary statistics
│   └── extremes.csv          # Extreme events
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies
```

### Sample Code Structure

**main.py:**

```python
import numpy as np
from src.data_generator import WeatherDataGenerator
from src.analysis_engine import WeatherAnalyzer
from src.geographic_analyzer import GeographicAnalyzer
from src.report_generator import ReportGenerator

def main():
    print("=== VIETNAM WEATHER ANALYSIS SYSTEM ===")

    # 1. Generate weather data
    generator = WeatherDataGenerator()
    weather_data = generator.generate_synthetic_data()

    # 2. Perform statistical analysis
    analyzer = WeatherAnalyzer(weather_data)
    statistics = analyzer.compute_statistics()

    # 3. Geographic analysis
    geo_analyzer = GeographicAnalyzer(weather_data)
    regional_stats = geo_analyzer.regional_analysis()

    # 4. Generate reports
    reporter = ReportGenerator()
    reporter.generate_all_reports(statistics, regional_stats)

    print("Analysis complete! Check outputs/ folder for results.")

if __name__ == "__main__":
    main()
```

## Grading Rubric

### Technical Implementation (60%)

- **Data Generation (15%)**: Correct array structures, realistic data
- **Statistical Analysis (20%)**: Accurate calculations, proper NumPy usage
- **Geographic Analysis (15%)**: Regional insights, correlation analysis
- **Code Quality (10%)**: Clean code, documentation, error handling

### Functionality (30%)

- **Core Features (20%)**: All required functions working
- **Advanced Features (10%)**: Creative extensions, optimizations

### Documentation (10%)

- **README (5%)**: Clear project overview và usage
- **Code Comments (5%)**: Well-documented functions

## Timeline

- **Week 3, Day 1-2**: Data generation và basic analysis
- **Week 3, Day 3-4**: Geographic analysis và advanced statistics
- **Week 3, Day 5-6**: Report generation và optimization
- **Week 3, Day 7**: Final testing và documentation

## Sample Output

```
=== VIETNAM WEATHER ANALYSIS REPORT ===
Analysis Period: 2022-2024 (730 days)
Provinces Analyzed: 63

NATIONAL SUMMARY:
Average Temperature: 26.3°C (±4.2°C)
Average Humidity: 78.5% (±12.1%)
Average Rainfall: 4.2mm/day (±8.7mm)
Total Annual Rainfall: 1,533mm

REGIONAL COMPARISON:
North (20 provinces): 23.1°C avg, 82.3% humidity
Central (19 provinces): 26.8°C avg, 76.1% humidity
South (24 provinces): 28.9°C avg, 77.2% humidity

EXTREME EVENTS DETECTED:
- 12 heatwave episodes (avg duration: 4.2 days)
- 8 cold spell episodes (avg duration: 2.8 days)
- 156 heavy rainfall events (>50mm/day)

TOP 5 HOTTEST PROVINCES:
1. An Giang: 29.4°C average
2. Kiên Giang: 29.1°C average
3. Cà Mau: 28.9°C average
4. Đồng Tháp: 28.7°C average
5. Long An: 28.6°C average

PERFORMANCE METRICS:
- Data generation: 0.34 seconds
- Analysis processing: 1.23 seconds
- Report generation: 0.45 seconds
- Total memory usage: 45.2 MB
```

## Resources

### Vietnam Geographic Data

- [Vietnam Administrative Units](https://gadm.org/download_country_v3.html)
- [Province Coordinates](https://simplemaps.com/data/vn-cities)

### Weather Patterns

- [Vietnam Climate Overview](https://en.wikipedia.org/wiki/Climate_of_Vietnam)
- [Monsoon Patterns](https://www.worldweatheronline.com/vietnam-weather.aspx)

### NumPy References

- [Structured Arrays](https://numpy.org/doc/stable/user/basics.rec.html)
- [Random Data Generation](https://numpy.org/doc/stable/reference/random/index.html)
- [Statistical Functions](https://numpy.org/doc/stable/reference/routines.statistics.html)

## Support

- **Office Hours**: Tuesdays/Thursdays 2-4 PM
- **Discussion Forum**: Available 24/7
- **Code Review**: Optional peer review sessions

**Good luck! 🚀**
