# Tuần 4: Pandas Data Analysis

## 🎯 Mục Tiêu Tuần 4

- Thành thạo Pandas Series và DataFrame cho phân tích dữ liệu địa lý và viễn thám
- Xử lý dữ liệu từ nhiều nguồn: CSV, Excel, JSON, Database
- Thực hiện data cleaning, transformation và aggregation
- Phân tích time series và spatial data patterns
- Áp dụng statistical analysis cho environmental data
- Tạo báo cáo và dashboard từ dữ liệu thực tế

## 📚 Nội Dung Học

### 1. Pandas Series Fundamentals

- Series creation, indexing, operations
- Time series với datetime index
- Statistical operations và aggregations
- Data filtering và boolean indexing

### 2. DataFrame Operations

- DataFrame creation từ multiple data sources
- Column/row selection, filtering, sorting
- Multi-level indexing và groupby operations
- Data transformation và feature engineering

### 3. Data I/O và Integration

- CSV/Excel reading với error handling
- JSON parsing và normalization
- Database connectivity (SQLite)
- Multi-source data integration

### 4. Advanced Data Analysis

- Time series analysis và trend detection
- Statistical testing và correlation analysis
- Anomaly detection và change point analysis
- Environmental data visualization

## 📁 Cấu Trúc Files

```
Week04_Pandas_Data_Analysis/
├── 01_Theory/
│   ├── 01_pandas_series_basics.md
│   ├── 02_pandas_dataframe_basics.md
│   ├── 03_data_io_operations.md
│   └── 04_data_cleaning_manipulation.md
├── 02_Exercises/
│   ├── Exercise_01_Pandas_Series/
│   │   ├── 1_problem.md
│   │   ├── 2_practice.py
│   │   └── 3_solution.py
│   ├── Exercise_02_Pandas_DataFrame/
│   │   ├── 1_problem.md
│   │   ├── 2_practice.py
│   │   └── 3_solution.py
│   ├── Exercise_03_Data_Loading/
│   │   ├── 1_problem.md
│   │   ├── 2_practice.py
│   │   └── 3_solution.py
│   ├── Exercise_04_Data_Analysis/
│   │   ├── 1_problem.md
│   │   ├── 2_practice.py
│   │   └── 3_solution.py
│   └── README.md
├── 03_Projects/
│   ├── Project1_Climate_Analysis.md
│   ├── Project1_Climate_Analysis.py
│   ├── Project2_Air_Quality_Monitor.md
│   ├── Project2_Air_Quality_Monitor.py
│   ├── Project3_NDVI_LandUse.md
│   ├── Project3_NDVI_LandUse.py
│   └── README.md
└── Week04_Overview.md
```

## 📋 Chi Tiết Bài Tập

### Exercise 01: Pandas Series

- **Temperature analysis**: Time series temperature data
- **Student scores**: Educational data statistics
- **Stock prices**: Financial data analysis
- **Focus**: Series indexing, operations, statistical functions

### Exercise 02: Pandas DataFrame

- **Satellite imagery**: NDVI calculation từ Landsat data
- **Weather stations**: Multi-regional climate analysis
- **Air quality**: Environmental monitoring data
- **Focus**: DataFrame operations, grouping, filtering

### Exercise 03: Data Loading

- **CSV processing**: Weather data với missing values
- **Excel integration**: Multi-sheet air quality data
- **JSON parsing**: API weather response handling
- **Database ops**: SQLite weather database management
- **Focus**: Multi-format data integration, quality control

### Exercise 04: Data Analysis

- **Climate trends**: Long-term temperature/rainfall analysis
- **Air quality time series**: Pollution pattern detection
- **NDVI analysis**: Vegetation change monitoring
- **Socio-economic**: Environmental-economic correlations
- **Focus**: Advanced analytics, statistical testing, insights

## 🚀 Projects Thực Tế

### Project 1: Vietnam Climate Change Analysis

- **Scope**: Long-term climate trend analysis (1990-2023)
- **Data**: Temperature, rainfall, extreme events
- **Techniques**: Time series, statistical testing, anomaly detection
- **Output**: Scientific climate change report

### Project 2: Urban Air Quality Monitoring

- **Scope**: Real-time air quality monitoring system
- **Data**: PM2.5, PM10, NO2, weather, traffic
- **Techniques**: Multi-source integration, alerting, dashboard
- **Output**: Automated monitoring và reporting system

### Project 3: Forest Change Detection

- **Scope**: NDVI-based deforestation monitoring
- **Data**: Satellite NDVI time series, land cover
- **Techniques**: Change detection, trend analysis, spatial analysis
- **Output**: Environmental monitoring và conservation reports

## ⏰ Lịch Học Gợi Ý (2 tuần)

### Tuần 1: Foundations

- **Ngày 1-2:** Theory 01-02 + Exercise 01 (Series basics)
- **Ngày 3-4:** Theory 03 + Exercise 02 (DataFrame operations)
- **Ngày 5-6:** Theory 04 + Exercise 03 (Data loading)
- **Ngày 7:** Exercise 04 (Advanced analysis) + Review

### Tuần 2: Projects

- **Ngày 8-10:** Project 1 (Climate Analysis)
- **Ngày 11-12:** Project 2 (Air Quality Monitor)
- **Ngày 13-14:** Project 3 (NDVI Analysis) + Integration

## 🎯 Learning Outcomes

Sau tuần 4, sinh viên sẽ có thể:

- [ ] Thành thạo pandas cho environmental data analysis
- [ ] Xử lý và integrate dữ liệu từ multiple sources
- [ ] Thực hiện time series analysis cho climate data
- [ ] Detect patterns và anomalies trong environmental data
- [ ] Tạo automated reports và monitoring systems
- [ ] Apply statistical methods cho scientific analysis
- [ ] Develop real-world environmental applications

## 🔧 Technical Requirements

### Libraries cần thiết:

```python
pandas >= 1.3.0
numpy >= 1.20.0
matplotlib >= 3.3.0
seaborn >= 0.11.0
scipy >= 1.7.0
```

### Optional advanced libraries:

```python
plotly          # Interactive visualizations
sqlite3         # Database operations
requests        # API data access
scikit-learn    # Machine learning
statsmodels     # Advanced statistics
```

## 🌟 Đánh Giá

- **Exercises**: 40% (4 bài × 10% each)
- **Projects**: 60% (3 projects × 20% each)
- **Bonus**: Advanced features, real-world integration, code quality

## 📚 Tài Liệu Tham Khảo

- Pandas official documentation
- "Python for Data Analysis" by Wes McKinney
- Environmental data analysis best practices
- Time series analysis methods
- Remote sensing data processing
