# Project 3: Economic Dashboard Backend - Starter Code

"""
Vietnam Economic Dashboard Backend System
Week 3 - NumPy Fundamentals Project

Hướng dẫn:
1. Đọc kỹ yêu cầu trong Project3_Economic_Dashboard.md
2. Hoàn thiện các hàm TODO trong file này
3. Test với dữ liệu nhỏ trước khi scale up
4. Chạy main() để xem kết quả dashboard backend

Structure:
- EconomicDataSimulator: Tạo dữ liệu kinh tế synthetic
- EconomicCalculator: Tính toán các chỉ số tài chính
- EconomicAnalyzer: Phân tích so sánh và xu hướng
- DashboardBackend: Chuẩn bị dữ liệu cho dashboard
"""

import numpy as np
import json
from datetime import datetime, timedelta

class EconomicDataSimulator:
    """Simulate comprehensive economic data for Vietnam provinces"""
    
    def __init__(self):
        self.provinces = self._load_province_data()
        self.indicators = self._define_indicators()
        self.regions = self._define_regions()
        self.years = 5  # 2019-2023
        self.months_per_year = 12
        self.total_months = self.years * self.months_per_year
        
    def _load_province_data(self):
        """Load basic province information"""
        # TODO: Create comprehensive province database
        provinces = [
            ('Hà Nội', 'Red_River_Delta', 3500000, 3358.6, True),
            ('Hồ Chí Minh', 'Southeast', 9100000, 2095.0, True),
            ('Đà Nẵng', 'South_Central_Coast', 1200000, 1285.4, True),
            # TODO: Add all 63 provinces with realistic data
        ]
        
        dtype = [('name', 'U30'), ('region', 'U20'), ('population', 'i4'), 
                ('area_km2', 'f4'), ('is_major_city', '?')]
        
        return np.array(provinces[:3], dtype=dtype)  # Starter with 3 provinces
    
    def _define_indicators(self):
        """Define 15 key economic indicators"""
        return [
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
    
    def _define_regions(self):
        """Define Vietnam's 8 economic regions"""
        # TODO: Complete regional classification
        return {
            'Red_River_Delta': ['Hà Nội'],
            'Southeast': ['Hồ Chí Minh'],
            'South_Central_Coast': ['Đà Nẵng'],
            # TODO: Add all regions
        }
    
    def generate_comprehensive_data(self):
        """Generate complete economic dataset"""
        num_provinces = len(self.provinces)
        num_indicators = len(self.indicators)
        
        # Create main data array: [provinces, months, indicators]
        economic_data = np.zeros((num_provinces, self.total_months, num_indicators))
        
        for i, province in enumerate(self.provinces):
            economic_data[i] = self._generate_province_economics(province)
            
        # Create metadata
        metadata = self._create_metadata()
        
        return economic_data, metadata
    
    def _generate_province_economics(self, province):
        """Generate economic time series for one province"""
        # TODO: Implement realistic economic data generation
        
        province_data = np.zeros((self.total_months, len(self.indicators)))
        
        # Base economic characteristics by province type
        if province['is_major_city']:
            gdp_base = 100.0  # Major cities start higher
            growth_rate = 0.06  # 6% annual growth
        else:
            gdp_base = 20.0
            growth_rate = 0.04  # 4% annual growth
            
        # Generate each indicator time series
        for month in range(self.total_months):
            year_progress = month / 12.0
            
            # GDP (with seasonal patterns and growth)
            seasonal_factor = 1 + 0.1 * np.sin(2 * np.pi * month / 12)
            growth_factor = (1 + growth_rate) ** year_progress
            noise = np.random.normal(0.95, 0.05)
            gdp = gdp_base * growth_factor * seasonal_factor * noise
            
            # GDP per capita
            gdp_per_capita = gdp * 1000 / (province['population'] / 1000000)
            
            # TODO: Generate other indicators with realistic relationships
            # Industrial output (correlated with GDP)
            industrial = 100 * growth_factor * seasonal_factor * np.random.normal(0.98, 0.08)
            
            # Agricultural output (less volatile, seasonal)
            agri_seasonal = 1 + 0.3 * np.sin(2 * np.pi * (month - 3) / 12)  # Peak in harvest season
            agricultural = 100 * (1 + growth_rate * 0.5) ** year_progress * agri_seasonal * np.random.normal(0.99, 0.04)
            
            # Services (steady growth)
            services = 100 * (1 + growth_rate * 1.2) ** year_progress * np.random.normal(1.0, 0.06)
            
            # Trade (volatile)
            exports = np.random.uniform(50, 200) if province['is_major_city'] else np.random.uniform(5, 50)
            imports = exports * np.random.uniform(0.8, 1.5)
            
            # FDI (lumpy, mostly to major cities)
            fdi = np.random.exponential(100) if province['is_major_city'] else np.random.exponential(10)
            
            # Other indicators
            retail_sales = industrial * 0.8 * np.random.normal(1.0, 0.05)
            cpi = 100 + year_progress * 3 + np.random.normal(0, 0.5)  # 3% annual inflation
            unemployment = np.random.uniform(1.5, 4.0)
            population = province['population'] / 1000  # Convert to thousands
            urban_pct = min(95, 40 + year_progress * 2 + np.random.normal(0, 1))
            investment = gdp * 0.3 * np.random.normal(1.0, 0.1)
            budget_revenue = gdp * 0.15 * np.random.normal(1.0, 0.08)
            
            # Store all indicators
            province_data[month] = [
                gdp, gdp_per_capita, industrial, agricultural, services,
                exports, imports, fdi, retail_sales, cpi,
                unemployment, population, urban_pct, investment, budget_revenue
            ]
            
        return province_data
    
    def _create_metadata(self):
        """Create comprehensive metadata"""
        return {
            'provinces': [p['name'] for p in self.provinces],
            'indicators': self.indicators,
            'regions': self.regions,
            'time_period': f'{2019}-{2023}',
            'total_months': self.total_months,
            'generation_date': datetime.now().isoformat(),
            'data_shape': [len(self.provinces), self.total_months, len(self.indicators)]
        }


class EconomicCalculator:
    """Calculate financial metrics and economic ratios"""
    
    def __init__(self, economic_data, metadata):
        self.data, self.metadata = economic_data
        self.indicators = self.metadata['indicators']
        
    def compute_all_metrics(self):
        """Compute comprehensive economic metrics"""
        metrics = {}
        
        # TODO: Implement all metric calculations
        metrics['growth_rates'] = self._calculate_growth_rates()
        metrics['moving_averages'] = self._calculate_moving_averages()
        metrics['volatility'] = self._calculate_volatility()
        metrics['correlations'] = self._calculate_correlations()
        metrics['ratios'] = self._calculate_economic_ratios()
        
        return metrics
    
    def _calculate_growth_rates(self):
        """Calculate various growth rate metrics"""
        # TODO: Implement growth rate calculations
        # - Month-over-month
        # - Year-over-year
        # - CAGR (Compound Annual Growth Rate)
        
        growth_rates = {}
        
        # Year-over-year growth for GDP (indicator 0)
        gdp_data = self.data[:, :, 0]  # [provinces, months]
        
        # Calculate YoY growth (current month vs same month last year)
        yoy_growth = np.zeros_like(gdp_data)
        for month in range(12, gdp_data.shape[1]):  # Start from month 12
            current = gdp_data[:, month]
            previous_year = gdp_data[:, month - 12]
            yoy_growth[:, month] = ((current - previous_year) / previous_year) * 100
            
        growth_rates['gdp_yoy'] = yoy_growth
        
        # TODO: Calculate growth for other indicators
        
        return growth_rates
    
    def _calculate_moving_averages(self):
        """Calculate moving averages for smoothing"""
        # TODO: Implement moving averages
        # - 3-month, 6-month, 12-month MA
        
        moving_averages = {}
        
        # 3-month moving average for all indicators
        ma_3m = np.zeros_like(self.data)
        for i in range(2, self.data.shape[1]):  # Start from month 3
            ma_3m[:, i, :] = np.mean(self.data[:, i-2:i+1, :], axis=1)
            
        moving_averages['ma_3m'] = ma_3m
        
        return moving_averages
    
    def _calculate_volatility(self):
        """Calculate volatility measures"""
        # TODO: Implement volatility calculations
        volatility = {}
        
        # Standard deviation of monthly changes
        monthly_changes = np.diff(self.data, axis=1)
        vol_monthly = np.std(monthly_changes, axis=1)  # [provinces, indicators]
        
        volatility['monthly_std'] = vol_monthly
        
        return volatility
    
    def _calculate_correlations(self):
        """Calculate correlations between indicators"""
        # TODO: Implement correlation analysis
        correlations = {}
        
        # Correlation matrix for each province
        num_provinces = self.data.shape[0]
        num_indicators = self.data.shape[2]
        
        correlation_matrices = np.zeros((num_provinces, num_indicators, num_indicators))
        
        for province in range(num_provinces):
            province_data = self.data[province, :, :]  # [months, indicators]
            correlation_matrices[province] = np.corrcoef(province_data.T)
            
        correlations['indicator_correlations'] = correlation_matrices
        
        return correlations
    
    def _calculate_economic_ratios(self):
        """Calculate important economic ratios"""
        # TODO: Implement economic ratio calculations
        ratios = {}
        
        # Investment-to-GDP ratio
        gdp = self.data[:, :, 0]  # GDP
        investment = self.data[:, :, 13]  # Investment
        investment_gdp_ratio = (investment / gdp) * 100
        
        ratios['investment_gdp_ratio'] = investment_gdp_ratio
        
        # TODO: Calculate other ratios
        # - Trade balance (exports - imports)
        # - Economic density (GDP/area)
        # - Productivity measures
        
        return ratios


class EconomicAnalyzer:
    """Perform comparative analysis and ranking"""
    
    def __init__(self, economic_data, calculated_metrics):
        self.data, self.metadata = economic_data
        self.metrics = calculated_metrics
        
    def perform_comprehensive_analysis(self):
        """Perform all analysis tasks"""
        analysis = {}
        
        # TODO: Implement comprehensive analysis
        analysis['rankings'] = self._calculate_rankings()
        analysis['regional_analysis'] = self._regional_analysis()
        analysis['time_trends'] = self._analyze_time_trends()
        analysis['performance_tiers'] = self._classify_performance_tiers()
        
        return analysis
    
    def _calculate_rankings(self):
        """Calculate province rankings by various metrics"""
        # TODO: Implement ranking calculations
        rankings = {}
        
        # GDP ranking (latest month)
        latest_gdp = self.data[:, -1, 0]  # Latest month GDP
        gdp_ranking = np.argsort(latest_gdp)[::-1]  # Descending order
        
        rankings['gdp_ranking'] = gdp_ranking
        
        # TODO: Calculate rankings for other indicators
        
        return rankings
    
    def _regional_analysis(self):
        """Analyze performance by economic regions"""
        # TODO: Implement regional analysis
        regional = {}
        
        # TODO: Group provinces by region and calculate aggregates
        
        return regional
    
    def _analyze_time_trends(self):
        """Analyze trends over time"""
        # TODO: Implement trend analysis
        trends = {}
        
        # Linear trend fitting for GDP
        months = np.arange(self.data.shape[1])
        gdp_trends = np.zeros(self.data.shape[0])
        
        for province in range(self.data.shape[0]):
            gdp_series = self.data[province, :, 0]
            # Simple linear regression: slope
            trend_slope = np.polyfit(months, gdp_series, 1)[0]
            gdp_trends[province] = trend_slope
            
        trends['gdp_trends'] = gdp_trends
        
        return trends
    
    def _classify_performance_tiers(self):
        """Classify provinces into performance tiers"""
        # TODO: Implement tier classification
        tiers = {}
        
        # Based on GDP per capita
        gdp_per_capita = self.data[:, -1, 1]  # Latest month
        
        # Simple percentile-based classification
        tier_1_threshold = np.percentile(gdp_per_capita, 80)
        tier_2_threshold = np.percentile(gdp_per_capita, 60)
        tier_3_threshold = np.percentile(gdp_per_capita, 40)
        
        province_tiers = np.zeros(len(gdp_per_capita), dtype=int)
        province_tiers[gdp_per_capita >= tier_1_threshold] = 1
        province_tiers[(gdp_per_capita >= tier_2_threshold) & (gdp_per_capita < tier_1_threshold)] = 2
        province_tiers[(gdp_per_capita >= tier_3_threshold) & (gdp_per_capita < tier_2_threshold)] = 3
        province_tiers[gdp_per_capita < tier_3_threshold] = 4
        
        tiers['performance_tiers'] = province_tiers
        
        return tiers


class DashboardBackend:
    """Prepare data for dashboard consumption"""
    
    def __init__(self):
        self.export_formats = ['json', 'csv']
        
    def prepare_dashboard_data(self, economic_data, metrics, analysis):
        """Prepare comprehensive dashboard data"""
        # TODO: Implement dashboard data preparation
        
        dashboard_data = {}
        
        # National summary
        dashboard_data['national_summary'] = self._create_national_summary(economic_data, metrics)
        
        # Province profiles
        dashboard_data['province_profiles'] = self._create_province_profiles(economic_data, analysis)
        
        # Regional comparisons
        dashboard_data['regional_data'] = self._create_regional_data(economic_data, analysis)
        
        # Time series data for charts
        dashboard_data['time_series'] = self._create_time_series_data(economic_data, metrics)
        
        # Rankings and performance
        dashboard_data['rankings'] = self._create_ranking_data(analysis)
        
        return dashboard_data
    
    def _create_national_summary(self, economic_data, metrics):
        """Create national level summary statistics"""
        # TODO: Implement national summary
        data, metadata = economic_data
        
        # National aggregates (sum across provinces)
        national_totals = np.sum(data, axis=0)  # [months, indicators]
        latest_month = national_totals[-1, :]
        
        summary = {
            'total_gdp': float(latest_month[0]),
            'avg_gdp_per_capita': float(np.mean(data[:, -1, 1])),
            'national_unemployment': float(np.mean(data[:, -1, 10])),
            'total_population': float(np.sum(data[:, -1, 11])),
            # TODO: Add more summary statistics
        }
        
        return summary
    
    def _create_province_profiles(self, economic_data, analysis):
        """Create individual province profiles"""
        # TODO: Implement province profiles
        return {}
    
    def _create_regional_data(self, economic_data, analysis):
        """Create regional comparison data"""
        # TODO: Implement regional data
        return {}
    
    def _create_time_series_data(self, economic_data, metrics):
        """Create time series data for charts"""
        # TODO: Implement time series preparation
        return {}
    
    def _create_ranking_data(self, analysis):
        """Create ranking tables"""
        # TODO: Implement ranking data
        return {}
    
    def export_all_formats(self, dashboard_data):
        """Export data in multiple formats"""
        # TODO: Implement file exports
        
        print("\\nExporting dashboard data...")
        print("TODO: Implement JSON export to outputs/dashboard_data.json")
        print("TODO: Implement CSV exports to outputs/")
        print("TODO: Implement metadata export")
        
        return True


def main():
    """Main function - economic dashboard backend pipeline"""
    print("=" * 60)
    print("VIETNAM ECONOMIC DASHBOARD BACKEND")
    print("=" * 60)
    
    # 1. Generate economic data
    print("\\n1. Generating comprehensive economic data...")
    simulator = EconomicDataSimulator()
    economic_data = simulator.generate_comprehensive_data()
    data, metadata = economic_data
    print(f"Generated data shape: {data.shape}")
    print(f"Provinces: {len(metadata['provinces'])}")
    print(f"Indicators: {len(metadata['indicators'])}")
    print(f"Time period: {metadata['time_period']}")
    
    # 2. Calculate financial metrics
    print("\\n2. Computing financial metrics...")
    calculator = EconomicCalculator(economic_data, metadata)
    calculated_metrics = calculator.compute_all_metrics()
    print("Financial calculations complete.")
    
    # 3. Perform comparative analysis
    print("\\n3. Performing comparative analysis...")
    analyzer = EconomicAnalyzer(economic_data, calculated_metrics)
    analysis_results = analyzer.perform_comprehensive_analysis()
    print("Analysis complete.")
    
    # 4. Prepare dashboard data
    print("\\n4. Preparing dashboard backend data...")
    backend = DashboardBackend()
    dashboard_data = backend.prepare_dashboard_data(
        economic_data, calculated_metrics, analysis_results
    )
    print("Dashboard data prepared.")
    
    # 5. Export all formats
    print("\\n5. Exporting data files...")
    success = backend.export_all_formats(dashboard_data)
    
    if success:
        print("\\n" + "=" * 60)
        print("DASHBOARD BACKEND READY!")
        print("=" * 60)
        print("✓ Economic data generated")
        print("✓ Financial metrics calculated")
        print("✓ Comparative analysis complete")
        print("✓ Dashboard data prepared")
        print("✓ Export files ready")
        print("\\nCheck outputs/ folder for dashboard data files.")


if __name__ == "__main__":
    main()
