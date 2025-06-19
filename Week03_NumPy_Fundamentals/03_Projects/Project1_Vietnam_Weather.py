# Project 1: Vietnam Weather Analysis - Starter Code

"""
Vietnam Weather Analysis System
Week 3 - NumPy Fundamentals Project

Hướng dẫn:
1. Đọc kỹ yêu cầu trong Project1_Vietnam_Weather.md
2. Hoàn thiện các hàm TODO trong file này
3. Test từng module trước khi integrate
4. Chạy main() để xem kết quả tổng thể

Structure:
- WeatherDataGenerator: Tạo dữ liệu thời tiết synthetic
- WeatherAnalyzer: Phân tích thống kê
- GeographicAnalyzer: Phân tích theo vùng địa lý
- ReportGenerator: Tạo báo cáo
"""

import numpy as np
import json
from datetime import datetime, timedelta

class WeatherDataGenerator:
    """Generate synthetic weather data for Vietnam provinces"""
    
    def __init__(self):
        self.provinces = self._load_province_data()
        self.start_date = datetime(2022, 1, 1)
        self.end_date = datetime(2024, 1, 1)
        self.num_days = (self.end_date - self.start_date).days
        
    def _load_province_data(self):
        """Create province information with coordinates"""
        # TODO: Implement province data creation
        # Should return structured array with:
        # - province_name (string)
        # - region (string): 'North', 'Central', 'South'
        # - latitude (float)
        # - longitude (float)
        # - elevation (float)
        # - is_coastal (bool)
        
        # Sample data structure:
        provinces = [
            ('Hà Nội', 'North', 21.0285, 105.8542, 12.0, False),
            ('Hồ Chí Minh', 'South', 10.8231, 106.6297, 19.0, False),
            ('Đà Nẵng', 'Central', 16.0471, 108.2068, 10.0, True),
            # TODO: Add all 63 provinces
        ]
        
        dtype = [('name', 'U20'), ('region', 'U10'), ('lat', 'f4'), 
                ('lon', 'f4'), ('elevation', 'f4'), ('coastal', '?')]
        
        return np.array(provinces[:3], dtype=dtype)  # Starter with 3 provinces
    
    def generate_synthetic_data(self):
        """Generate weather data for all provinces and days"""
        num_provinces = len(self.provinces)
        
        # TODO: Create 4D array: [days, provinces, parameters]
        # Parameters: temperature, humidity, pressure, rainfall, wind_speed
        weather_data = np.zeros((self.num_days, num_provinces, 5))
        
        for i, province in enumerate(self.provinces):
            weather_data[:, i, :] = self._generate_province_weather(province)
            
        return weather_data
    
    def _generate_province_weather(self, province):
        """Generate weather for a specific province"""
        # TODO: Implement weather generation với:
        # - Seasonal patterns (monthly variations)
        # - Regional characteristics (North cooler, South warmer)
        # - Elevation effects (higher = cooler)
        # - Coastal effects (more humidity)
        # - Random variations
        
        # Sample implementation (replace with proper logic):
        base_temp = 25.0  # TODO: Calculate based on region, elevation
        seasonal_temp = np.sin(np.arange(self.num_days) * 2 * np.pi / 365) * 5
        random_temp = np.random.normal(0, 2, self.num_days)
        temperature = base_temp + seasonal_temp + random_temp
        
        # TODO: Generate other parameters
        humidity = np.random.uniform(60, 90, self.num_days)
        pressure = np.random.uniform(1005, 1025, self.num_days)
        rainfall = np.random.exponential(2, self.num_days)
        wind_speed = np.random.uniform(5, 25, self.num_days)
        
        return np.column_stack([temperature, humidity, pressure, rainfall, wind_speed])


class WeatherAnalyzer:
    """Analyze weather data statistically"""
    
    def __init__(self, weather_data, provinces):
        self.weather_data = weather_data
        self.provinces = provinces
        self.param_names = ['temperature', 'humidity', 'pressure', 'rainfall', 'wind_speed']
        
    def compute_statistics(self):
        """Compute comprehensive statistics"""
        stats = {}
        
        # TODO: Implement statistical analysis
        # - National averages
        # - Monthly trends
        # - Extreme value detection
        # - Percentile calculations
        
        # Sample structure:
        stats['national'] = self._national_statistics()
        stats['monthly'] = self._monthly_statistics()
        stats['extremes'] = self._detect_extremes()
        
        return stats
    
    def _national_statistics(self):
        """Calculate national level statistics"""
        # TODO: Implement
        # Return dict with mean, std, min, max for each parameter
        return {}
    
    def _monthly_statistics(self):
        """Calculate monthly aggregated statistics"""
        # TODO: Implement
        # Group by month, calculate averages
        return {}
    
    def _detect_extremes(self):
        """Detect extreme weather events"""
        # TODO: Implement
        # - Heatwaves (>35°C for 3+ consecutive days)
        # - Cold spells (<10°C for 2+ consecutive days)
        # - Heavy rainfall (>50mm/day)
        return {}


class GeographicAnalyzer:
    """Analyze weather patterns by geographic regions"""
    
    def __init__(self, weather_data, provinces):
        self.weather_data = weather_data
        self.provinces = provinces
        
    def regional_analysis(self):
        """Analyze by North/Central/South regions"""
        # TODO: Implement regional comparison
        # Group provinces by region, compare statistics
        return {}
    
    def elevation_analysis(self):
        """Analyze elevation impact on weather"""
        # TODO: Implement
        # Correlate elevation with temperature, humidity
        return {}
    
    def coastal_analysis(self):
        """Compare coastal vs inland weather patterns"""
        # TODO: Implement
        # Compare coastal vs inland provinces
        return {}


class ReportGenerator:
    """Generate comprehensive weather reports"""
    
    def __init__(self):
        pass
        
    def generate_all_reports(self, statistics, regional_stats):
        """Generate all report formats"""
        # TODO: Implement report generation
        # - Text summary report
        # - CSV data exports
        # - JSON data for dashboards
        
        self._generate_text_report(statistics, regional_stats)
        self._export_csv_data(statistics)
        self._export_json_summary(statistics)
    
    def _generate_text_report(self, statistics, regional_stats):
        """Generate human-readable text report"""
        # TODO: Implement
        pass
    
    def _export_csv_data(self, statistics):
        """Export statistics to CSV files"""
        # TODO: Implement
        pass
    
    def _export_json_summary(self, statistics):
        """Export summary to JSON for dashboards"""
        # TODO: Implement
        pass


def main():
    """Main function - entry point"""
    print("=" * 60)
    print("VIETNAM WEATHER ANALYSIS SYSTEM")
    print("=" * 60)
    
    # 1. Generate weather data
    print("\\n1. Generating synthetic weather data...")
    generator = WeatherDataGenerator()
    weather_data = generator.generate_synthetic_data()
    print(f"Generated data shape: {weather_data.shape}")
    print(f"Provinces: {len(generator.provinces)}")
    print(f"Days: {generator.num_days}")
    
    # 2. Statistical analysis
    print("\\n2. Performing statistical analysis...")
    analyzer = WeatherAnalyzer(weather_data, generator.provinces)
    statistics = analyzer.compute_statistics()
    print("Statistical analysis complete.")
    
    # 3. Geographic analysis
    print("\\n3. Performing geographic analysis...")
    geo_analyzer = GeographicAnalyzer(weather_data, generator.provinces)
    regional_stats = geo_analyzer.regional_analysis()
    print("Geographic analysis complete.")
    
    # 4. Generate reports
    print("\\n4. Generating reports...")
    reporter = ReportGenerator()
    reporter.generate_all_reports(statistics, regional_stats)
    print("Reports generated in outputs/ folder.")
    
    print("\\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    main()
