# Project 3: Economic Data Dashboard Backend 📊

## Mục tiêu Project

Xây dựng backend system cho dashboard kinh tế Việt Nam sử dụng NumPy, xử lý và phân tích dữ liệu kinh tế của 63 tỉnh thành qua nhiều năm.

## Yêu cầu Kỹ thuật

### Phase 1: Economic Data Simulation (25 điểm)

**File: `data_simulator.py`**

1. **Province Economic Profile**

   - 63 tỉnh thành với thông tin cơ bản
   - GDP, population, area, economic zones
   - Industry sectors: agriculture, industry, services
   - Geographic and demographic factors

2. **Multi-year Economic Indicators**

   - 5 years of monthly data (2019-2023)
   - 15 economic indicators per province
   - Realistic seasonal patterns và growth trends
   - Regional economic characteristics

3. **Data Quality và Consistency**
   - Handle missing data patterns
   - Ensure logical relationships between indicators
   - Apply realistic constraints và correlations

### Phase 2: Financial Calculations (25 điểm)

**File: `calculator.py`**

1. **Growth Metrics**

   - Year-over-year growth rates
   - Compound Annual Growth Rate (CAGR)
   - Quarter-over-quarter changes
   - Moving averages (3, 6, 12 months)

2. **Economic Ratios**

   - GDP per capita calculations
   - Economic density (GDP/area)
   - Sector contribution percentages
   - Investment-to-GDP ratios

3. **Statistical Measures**
   - Volatility calculations (standard deviation)
   - Correlation analysis between indicators
   - Trend analysis (linear regression)
   - Seasonality decomposition

### Phase 3: Comparative Analysis (30 điểm)

**File: `analyzer.py`**

1. **Ranking Systems**

   - Province rankings by various indicators
   - Composite economic index calculation
   - Percentile rankings và distributions
   - Performance tier classifications

2. **Regional Comparisons**

   - Economic regions performance (8 regions)
   - Cross-regional economic flows simulation
   - Regional specialization analysis
   - Economic convergence/divergence analysis

3. **Time Series Analysis**
   - Trend identification và forecasting
   - Cyclical pattern detection
   - Economic shock impact analysis
   - Recovery pattern analysis

### Phase 4: Dashboard Data Preparation (20 điểm)

**File: `dashboard_backend.py`**

1. **Data Aggregation**

   - Multi-level aggregations (national, regional, provincial)
   - Time-based rollups (monthly, quarterly, yearly)
   - Dynamic filtering và grouping
   - Real-time calculation simulation

2. **API-Ready Data Formats**

   - JSON exports for web dashboards
   - CSV exports for spreadsheet analysis
   - Structured formats for charts
   - Metadata và data dictionary generation

3. **Performance Optimization**
   - Efficient data structures for fast queries
   - Caching mechanisms simulation
   - Memory usage optimization
   - Batch processing capabilities

## Deliverables

### Required Files

```
Project3_Economic_Dashboard/
├── src/
│   ├── data_simulator.py      # Economic data generation
│   ├── calculator.py          # Financial calculations
│   ├── analyzer.py            # Comparative analysis
│   ├── dashboard_backend.py   # Dashboard data preparation
│   └── main.py               # Main application
├── data/
│   ├── provinces_economic.csv # Province basic information
│   ├── indicators_raw.npy     # Raw economic indicators
│   ├── indicators_processed.npz # Processed calculations
│   └── metadata.json         # Data dictionary
├── outputs/
│   ├── dashboard_data.json   # Dashboard-ready data
│   ├── rankings.csv          # Province rankings
│   ├── trends.csv            # Trend analysis results
│   ├── regional_summary.csv  # Regional statistics
│   └── forecast.csv          # Simple forecasts
├── README.md                 # Project documentation
└── demo_dashboard.py         # Interactive demo
```

### Sample Code Structure

**main.py:**

```python
import numpy as np
from src.data_simulator import EconomicDataSimulator
from src.calculator import EconomicCalculator
from src.analyzer import EconomicAnalyzer
from src.dashboard_backend import DashboardBackend

def main():
    print("=== VIETNAM ECONOMIC DASHBOARD BACKEND ===")

    # 1. Generate economic data
    simulator = EconomicDataSimulator()
    economic_data = simulator.generate_comprehensive_data()

    # 2. Perform financial calculations
    calculator = EconomicCalculator(economic_data)
    calculated_metrics = calculator.compute_all_metrics()

    # 3. Comparative analysis
    analyzer = EconomicAnalyzer(economic_data, calculated_metrics)
    analysis_results = analyzer.perform_comprehensive_analysis()

    # 4. Prepare dashboard data
    backend = DashboardBackend()
    dashboard_data = backend.prepare_dashboard_data(
        economic_data, calculated_metrics, analysis_results
    )

    # 5. Generate exports
    backend.export_all_formats(dashboard_data)

    print("Dashboard backend ready! Check outputs/ for data files.")

if __name__ == "__main__":
    main()
```

## Grading Rubric

### Technical Implementation (60%)

- **Data Simulation (15%)**: Realistic economic data với proper relationships
- **Financial Calculations (20%)**: Accurate economic metrics and ratios
- **Analysis Logic (15%)**: Sound comparative analysis algorithms
- **Data Preparation (10%)**: Efficient dashboard-ready data structures

### Functionality (25%)

- **Core Features (15%)**: All required calculations working
- **Advanced Features (10%)**: Creative analysis methods, optimization

### Code Quality (15%)

- **Documentation (8%)**: Clear README, well-documented functions
- **Performance (7%)**: Efficient NumPy usage, memory optimization

## Technical Specifications

### Economic Indicators

```python
# 15 key economic indicators
INDICATORS = [
    'gdp_billion_vnd',          # Gross Domestic Product
    'gdp_per_capita_million',   # GDP per capita
    'industrial_output',        # Industrial production index
    'agricultural_output',      # Agricultural production index
    'services_revenue',         # Services sector revenue
    'exports_million_usd',      # Export value
    'imports_million_usd',      # Import value
    'fdi_million_usd',          # Foreign Direct Investment
    'retail_sales',             # Retail sales index
    'cpi',                      # Consumer Price Index
    'unemployment_rate',        # Unemployment percentage
    'population_thousands',     # Population count
    'urban_population_pct',     # Urbanization rate
    'investment_billion_vnd',   # Total investment
    'budget_revenue_billion'    # Provincial budget revenue
]

# Data structure: [provinces, months, indicators]
data_shape = (63, 60, 15)  # 63 provinces, 60 months (5 years), 15 indicators
```

### Regional Classifications

```python
# Vietnam's 8 economic regions
ECONOMIC_REGIONS = {
    'Northwest': ['Lai Châu', 'Điện Biên', 'Sơn La', 'Hòa Bình'],
    'Northeast': ['Hà Giang', 'Cao Bằng', 'Lạng Sơn', 'Quảng Ninh', 'Bắc Giang', 'Phú Thọ', 'Thái Nguyên', 'Tuyên Quang', 'Bắc Kạn'],
    'Red_River_Delta': ['Hà Nội', 'Hải Phòng', 'Vĩnh Phúc', 'Bắc Ninh', 'Hải Dương', 'Hưng Yên', 'Thái Bình', 'Nam Định', 'Ninh Bình'],
    'North_Central': ['Thanh Hóa', 'Nghệ An', 'Hà Tĩnh', 'Quảng Bình', 'Quảng Trị', 'Thừa Thiên Huế'],
    'South_Central_Coast': ['Đà Nẵng', 'Quảng Nam', 'Quảng Ngãi', 'Bình Định', 'Phú Yên', 'Khánh Hòa', 'Ninh Thuận', 'Bình Thuận'],
    'Central_Highlands': ['Kon Tum', 'Gia Lai', 'Đắk Lắk', 'Đắk Nông', 'Lâm Đồng'],
    'Southeast': ['Hồ Chí Minh', 'Bà Rịa-Vũng Tàu', 'Bình Dương', 'Bình Phước', 'Đồng Nai', 'Tây Ninh'],
    'Mekong_Delta': ['An Giang', 'Bạc Liêu', 'Bến Tre', 'Cà Mau', 'Cần Thơ', 'Đồng Tháp', 'Hậu Giang', 'Kiên Giang', 'Long An', 'Sóc Trăng', 'Tiền Giang', 'Trà Vinh', 'Vĩnh Long']
}
```

### Sample Calculations

```python
def calculate_growth_rate(current, previous):
    """Calculate percentage growth rate"""
    return ((current - previous) / previous) * 100

def calculate_cagr(end_value, start_value, periods):
    """Calculate Compound Annual Growth Rate"""
    return ((end_value / start_value) ** (1/periods) - 1) * 100

def calculate_moving_average(data, window=3):
    """Calculate moving average"""
    return np.convolve(data, np.ones(window)/window, mode='valid')

def calculate_volatility(data):
    """Calculate volatility as standard deviation of returns"""
    returns = np.diff(data) / data[:-1]
    return np.std(returns) * 100
```

## Sample Output

```
=== VIETNAM ECONOMIC DASHBOARD BACKEND ===
Data Period: 2019-2023 (60 months)
Provinces: 63 | Indicators: 15

NATIONAL ECONOMIC SUMMARY:
Total GDP: 8,891.3 trillion VND (2023)
GDP Growth Rate: 5.8% (2023 vs 2022)
Average GDP per capita: 89.7 million VND
National unemployment: 2.3%

TOP 5 ECONOMIC PROVINCES (by GDP):
1. Hồ Chí Minh: 1,254.8 trillion VND
2. Hà Nội: 867.4 trillion VND
3. Bình Dương: 512.3 trillion VND
4. Đồng Nai: 387.9 trillion VND
5. Bà Rịa-Vũng Tàu: 298.7 trillion VND

REGIONAL PERFORMANCE:
Southeast: 34.2% of national GDP
Red River Delta: 28.7% of national GDP
South Central Coast: 12.4% of national GDP
Mekong Delta: 11.8% of national GDP

FASTEST GROWING PROVINCES (5-year CAGR):
1. Bắc Ninh: 12.3% CAGR
2. Bình Dương: 11.7% CAGR
3. Quảng Ninh: 10.9% CAGR
4. Vĩnh Phúc: 10.4% CAGR
5. Hải Phòng: 9.8% CAGR

ECONOMIC INDICATORS TRENDS:
Industrial Output: +7.2% average annual growth
Agricultural Output: +2.8% average annual growth
Services Revenue: +6.9% average annual growth
FDI Inflows: +4.3% average annual growth

VOLATILITY ANALYSIS:
Most Stable: Hà Nội (CV: 0.12)
Most Volatile: Cà Mau (CV: 0.34)
National Average CV: 0.19

DASHBOARD EXPORTS GENERATED:
✓ dashboard_data.json (2.3 MB)
✓ rankings.csv (245 KB)
✓ trends.csv (1.8 MB)
✓ regional_summary.csv (89 KB)
✓ forecast.csv (356 KB)

Processing Performance:
- Data generation: 0.45 seconds
- Calculations: 0.78 seconds
- Analysis: 1.23 seconds
- Export preparation: 0.34 seconds
- Total processing: 2.80 seconds
```

## Resources

### Vietnam Economic Data

- [General Statistics Office of Vietnam](https://www.gso.gov.vn/)
- [State Bank of Vietnam](https://www.sbv.gov.vn/)
- [Foreign Investment Agency](https://fia.mpi.gov.vn/)

### Economic Analysis Methods

- [Economic Growth Analysis](https://www.investopedia.com/terms/e/economicgrowth.asp)
- [Regional Economic Analysis](https://www.bea.gov/resources/methodologies/regional-handbook)
- [Time Series Econometrics](https://www.econometrics-with-r.org/ts.html)

### NumPy for Financial Data

- [NumPy Financial Functions](https://numpy.org/numpy-financial/)
- [Array Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [Linear Algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)

## Support

- **Economic Data**: Historical datasets provided in course materials
- **Calculation Methods**: Reference formulas và implementation guides
- **Dashboard Integration**: Sample frontend templates available

**Build the future of economic analysis! 📈💼**
