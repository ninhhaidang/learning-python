#!/usr/bin/env python3
"""
Project 2: Air Quality Monitoring System for Vietnamese Cities
Week 4: Pandas Data Analysis

Author: Learning Python Course
Date: June 19, 2025
Description: Real-time air quality monitoring and analysis system for major Vietnamese cities
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import sqlite3
import json
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class AirQualityMonitor:
    """
    Comprehensive air quality monitoring system for Vietnamese cities
    Integrates multiple data sources and provides real-time analysis
    """
    
    def __init__(self, cities=None):
        """Initialize the air quality monitoring system"""
        self.cities = cities or ['Hà Nội', 'TP.HCM', 'Đà Nẵng', 'Hải Phòng', 'Cần Thơ']
        self.sensor_data = None
        self.weather_data = None
        self.traffic_data = None
        self.aqi_data = None
        self.alerts = []
        self.thresholds = {
            'PM2.5': {'good': 12, 'moderate': 35, 'unhealthy_sensitive': 55, 'unhealthy': 150},
            'PM10': {'good': 20, 'moderate': 50, 'unhealthy_sensitive': 80, 'unhealthy': 200},
            'NO2': {'good': 40, 'moderate': 80, 'unhealthy_sensitive': 180, 'unhealthy': 280},
            'SO2': {'good': 20, 'moderate': 80, 'unhealthy_sensitive': 365, 'unhealthy': 800},
            'CO': {'good': 4.4, 'moderate': 9.4, 'unhealthy_sensitive': 12.4, 'unhealthy': 15.4},
            'O3': {'good': 100, 'moderate': 160, 'unhealthy_sensitive': 215, 'unhealthy': 265}
        }
        
        print(f"Air Quality Monitor initialized for {len(self.cities)} cities")
        print("Monitoring: PM2.5, PM10, NO2, SO2, CO, O3")
    
    def generate_sample_data(self, days=30):
        """
        Generate realistic air quality sensor data for demonstration
        In real implementation, this would connect to actual sensors/APIs
        """
        print(f"Generating {days} days of air quality data...")
        
        # Create hourly timestamps
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        timestamps = pd.date_range(start_date, end_date, freq='H')
        
        # Initialize data storage
        all_data = []
        
        for city in self.cities:
            # Base pollution levels vary by city
            base_levels = {
                'Hà Nội': {'PM2.5': 45, 'PM10': 85, 'NO2': 65, 'SO2': 25, 'CO': 2.5, 'O3': 120},
                'TP.HCM': {'PM2.5': 40, 'PM10': 80, 'NO2': 70, 'SO2': 30, 'CO': 3.0, 'O3': 110},
                'Đà Nẵng': {'PM2.5': 30, 'PM10': 60, 'NO2': 45, 'SO2': 20, 'CO': 2.0, 'O3': 95},
                'Hải Phòng': {'PM2.5': 35, 'PM10': 70, 'NO2': 55, 'SO2': 35, 'CO': 2.8, 'O3': 105},
                'Cần Thơ': {'PM2.5': 28, 'PM10': 55, 'NO2': 40, 'SO2': 18, 'CO': 1.8, 'O3': 90}
            }
            
            city_base = base_levels.get(city, base_levels['Đà Nẵng'])
            
            for timestamp in timestamps:
                # Add time-based patterns
                hour = timestamp.hour
                day_of_week = timestamp.weekday()
                
                # Rush hour effects (7-9 AM, 5-7 PM)
                rush_hour_multiplier = 1.0
                if hour in [7, 8, 17, 18]:
                    rush_hour_multiplier = 1.4
                elif hour in [6, 9, 16, 19]:
                    rush_hour_multiplier = 1.2
                
                # Weekend effects (lower traffic pollution)
                weekend_multiplier = 0.8 if day_of_week >= 5 else 1.0
                
                # Seasonal effects (higher pollution in winter)
                month = timestamp.month
                seasonal_multiplier = 1.3 if month in [12, 1, 2] else 1.0
                
                # Random variations
                random_factor = np.random.normal(1.0, 0.2)
                
                # Calculate final multiplier
                total_multiplier = rush_hour_multiplier * weekend_multiplier * seasonal_multiplier * random_factor
                
                # Generate sensor readings
                record = {
                    'timestamp': timestamp,
                    'city': city,
                    'station_id': f"{city.replace(' ', '').replace('.', '')}_Station_{np.random.randint(1, 4)}",
                    'PM2.5': max(0, city_base['PM2.5'] * total_multiplier + np.random.normal(0, 5)),
                    'PM10': max(0, city_base['PM10'] * total_multiplier + np.random.normal(0, 8)),
                    'NO2': max(0, city_base['NO2'] * total_multiplier + np.random.normal(0, 10)),
                    'SO2': max(0, city_base['SO2'] * total_multiplier + np.random.normal(0, 5)),
                    'CO': max(0, city_base['CO'] * total_multiplier + np.random.normal(0, 0.5)),
                    'O3': max(0, city_base['O3'] * total_multiplier + np.random.normal(0, 15)),
                    'temperature': 25 + 5 * np.sin(2 * np.pi * (timestamp.hour + timestamp.day) / 24) + np.random.normal(0, 2),
                    'humidity': 70 + 15 * np.sin(2 * np.pi * timestamp.hour / 24) + np.random.normal(0, 5),
                    'wind_speed': max(0, 3 + 2 * np.random.exponential(1)),
                    'pressure': 1013 + np.random.normal(0, 10)
                }
                
                all_data.append(record)
        
        # Create DataFrame
        self.sensor_data = pd.DataFrame(all_data)
        self.sensor_data['timestamp'] = pd.to_datetime(self.sensor_data['timestamp'])
        self.sensor_data.set_index('timestamp', inplace=True)
        
        print(f"Generated {len(self.sensor_data)} sensor readings")
        return self.sensor_data
    
    def calculate_aqi(self, pollutant, concentration):
        """
        Calculate Air Quality Index (AQI) for a given pollutant concentration
        Using Vietnamese AQI standards
        """
        thresholds = self.thresholds.get(pollutant, {})
        
        if concentration <= thresholds.get('good', 0):
            return min(50, (concentration / thresholds['good']) * 50)
        elif concentration <= thresholds.get('moderate', 0):
            return 50 + ((concentration - thresholds['good']) / 
                        (thresholds['moderate'] - thresholds['good'])) * 50
        elif concentration <= thresholds.get('unhealthy_sensitive', 0):
            return 100 + ((concentration - thresholds['moderate']) / 
                         (thresholds['unhealthy_sensitive'] - thresholds['moderate'])) * 50
        elif concentration <= thresholds.get('unhealthy', 0):
            return 150 + ((concentration - thresholds['unhealthy_sensitive']) / 
                         (thresholds['unhealthy'] - thresholds['unhealthy_sensitive'])) * 50
        else:
            return min(300, 200 + ((concentration - thresholds['unhealthy']) / 
                                  thresholds['unhealthy']) * 100)
    
    def process_aqi_data(self):
        """Calculate AQI for all pollutants and determine overall AQI"""
        if self.sensor_data is None:
            print("No sensor data available. Generate sample data first.")
            return
        
        print("Calculating AQI for all pollutants...")
        
        # Calculate individual AQI values
        pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
        
        for pollutant in pollutants:
            self.sensor_data[f'AQI_{pollutant}'] = self.sensor_data[pollutant].apply(
                lambda x: self.calculate_aqi(pollutant, x)
            )
        
        # Overall AQI is the maximum of individual AQIs
        aqi_columns = [f'AQI_{p}' for p in pollutants]
        self.sensor_data['AQI_Overall'] = self.sensor_data[aqi_columns].max(axis=1)
        
        # Determine AQI categories
        def get_aqi_category(aqi):
            if aqi <= 50:
                return 'Good'
            elif aqi <= 100:
                return 'Moderate'
            elif aqi <= 150:
                return 'Unhealthy for Sensitive Groups'
            elif aqi <= 200:
                return 'Unhealthy'
            elif aqi <= 300:
                return 'Very Unhealthy'
            else:
                return 'Hazardous'
        
        self.sensor_data['AQI_Category'] = self.sensor_data['AQI_Overall'].apply(get_aqi_category)
        
        # Create summary AQI data
        self.aqi_data = self.sensor_data[['city', 'station_id'] + aqi_columns + 
                                        ['AQI_Overall', 'AQI_Category']].copy()
        
        print("AQI calculation completed")
        return self.aqi_data
    
    def detect_pollution_events(self, threshold_multiplier=1.5):
        """Detect pollution events and anomalies"""
        if self.aqi_data is None:
            self.process_aqi_data()
        
        print("Detecting pollution events and anomalies...")
        
        events = []
        
        for city in self.cities:
            city_data = self.sensor_data[self.sensor_data['city'] == city].copy()
            
            # Calculate rolling statistics
            window = '24H'  # 24-hour window
            city_data['PM2.5_rolling_mean'] = city_data['PM2.5'].rolling(window).mean()
            city_data['PM2.5_rolling_std'] = city_data['PM2.5'].rolling(window).std()
            
            # Detect spikes (values significantly above rolling average)
            threshold = city_data['PM2.5_rolling_mean'] + (threshold_multiplier * city_data['PM2.5_rolling_std'])
            spike_events = city_data[city_data['PM2.5'] > threshold]
            
            for idx, event in spike_events.iterrows():
                events.append({
                    'timestamp': idx,
                    'city': city,
                    'event_type': 'PM2.5_Spike',
                    'severity': 'High' if event['PM2.5'] > threshold[idx] * 1.5 else 'Medium',
                    'pm25_value': event['PM2.5'],
                    'threshold': threshold[idx],
                    'aqi': event['AQI_Overall']
                })
        
        self.pollution_events = pd.DataFrame(events)
        
        if len(events) > 0:
            print(f"Detected {len(events)} pollution events")
            return self.pollution_events
        else:
            print("No significant pollution events detected")
            return pd.DataFrame()
    
    def generate_alerts(self, aqi_threshold=100):
        """Generate alerts for unhealthy air quality conditions"""
        if self.aqi_data is None:
            self.process_aqi_data()
        
        current_time = self.sensor_data.index.max()
        recent_data = self.sensor_data[self.sensor_data.index >= current_time - timedelta(hours=1)]
        
        alerts = []
        
        for city in self.cities:
            city_recent = recent_data[recent_data['city'] == city]
            if len(city_recent) > 0:
                latest_aqi = city_recent['AQI_Overall'].iloc[-1]
                latest_category = city_recent['AQI_Category'].iloc[-1]
                
                if latest_aqi > aqi_threshold:
                    alert = {
                        'timestamp': current_time,
                        'city': city,
                        'alert_type': 'High_AQI',
                        'current_aqi': latest_aqi,
                        'category': latest_category,
                        'recommendation': self._get_health_recommendation(latest_category)
                    }
                    alerts.append(alert)
        
        self.alerts = alerts
        
        if alerts:
            print(f"\n🚨 {len(alerts)} ACTIVE ALERTS:")
            for alert in alerts:
                print(f"  {alert['city']}: AQI {alert['current_aqi']:.0f} ({alert['category']})")
        
        return alerts
    
    def _get_health_recommendation(self, category):
        """Get health recommendations based on AQI category"""
        recommendations = {
            'Good': 'Air quality is satisfactory. Normal outdoor activities.',
            'Moderate': 'Air quality is acceptable. Sensitive individuals should consider limiting prolonged outdoor exertion.',
            'Unhealthy for Sensitive Groups': 'Sensitive groups should reduce outdoor activities.',
            'Unhealthy': 'Everyone should reduce outdoor activities. Wear masks when outside.',
            'Very Unhealthy': 'Avoid outdoor activities. Stay indoors with air purification.',
            'Hazardous': 'Emergency conditions. Everyone should avoid outdoor activities.'
        }
        return recommendations.get(category, 'Monitor air quality closely.')
    
    def create_hourly_summary(self):
        """Create hourly air quality summary statistics"""
        if self.sensor_data is None:
            print("No data available")
            return
        
        print("Creating hourly air quality summary...")
        
        # Group by city and hour
        hourly_summary = self.sensor_data.groupby(['city', self.sensor_data.index.hour]).agg({
            'PM2.5': ['mean', 'std', 'min', 'max'],
            'PM10': ['mean', 'std', 'min', 'max'],
            'NO2': ['mean', 'std', 'min', 'max'],
            'AQI_Overall': ['mean', 'std', 'min', 'max'],
            'temperature': 'mean',
            'humidity': 'mean',
            'wind_speed': 'mean'
        }).round(2)
        
        # Flatten column names
        hourly_summary.columns = ['_'.join(col).strip() for col in hourly_summary.columns]
        hourly_summary.reset_index(inplace=True)
        hourly_summary.rename(columns={'timestamp': 'hour'}, inplace=True)
        
        self.hourly_summary = hourly_summary
        
        print("Hourly summary created")
        return hourly_summary
    
    def create_daily_report(self, date=None):
        """Create daily air quality report for all cities"""
        if self.sensor_data is None:
            print("No data available")
            return
        
        if date is None:
            date = self.sensor_data.index.max().date()
        
        print(f"Creating daily report for {date}")
        
        # Filter data for the specified date
        daily_data = self.sensor_data[self.sensor_data.index.date == date]
        
        if len(daily_data) == 0:
            print(f"No data available for {date}")
            return
        
        # Calculate daily statistics
        daily_stats = daily_data.groupby('city').agg({
            'PM2.5': ['mean', 'max', 'min'],
            'PM10': ['mean', 'max', 'min'],
            'NO2': ['mean', 'max', 'min'],
            'SO2': ['mean', 'max', 'min'],
            'CO': ['mean', 'max', 'min'],
            'O3': ['mean', 'max', 'min'],
            'AQI_Overall': ['mean', 'max', 'min'],
            'temperature': ['mean', 'max', 'min'],
            'humidity': ['mean', 'max', 'min'],
            'wind_speed': 'mean'
        }).round(2)
        
        # Flatten column names
        daily_stats.columns = ['_'.join(col).strip() for col in daily_stats.columns]
        
        # Add AQI categories
        for city in daily_stats.index:
            city_max_aqi = daily_stats.loc[city, 'AQI_Overall_max']
            daily_stats.loc[city, 'worst_category'] = self.sensor_data[
                (self.sensor_data['city'] == city) & 
                (self.sensor_data.index.date == date)
            ]['AQI_Category'].mode()[0]
        
        print(f"\n📊 DAILY AIR QUALITY REPORT - {date}")
        print("=" * 60)
        
        for city in daily_stats.index:
            stats = daily_stats.loc[city]
            print(f"\n{city}:")
            print(f"  AQI: {stats['AQI_Overall_mean']:.0f} (avg), {stats['AQI_Overall_max']:.0f} (max)")
            print(f"  Category: {stats['worst_category']}")
            print(f"  PM2.5: {stats['PM2.5_mean']:.1f} μg/m³ (avg)")
            print(f"  Temperature: {stats['temperature_mean']:.1f}°C")
        
        self.daily_report = daily_stats
        return daily_stats
    
    def visualize_trends(self, days=7):
        """Create visualization of air quality trends"""
        if self.sensor_data is None:
            print("No data available")
            return
        
        # Get recent data
        end_date = self.sensor_data.index.max()
        start_date = end_date - timedelta(days=days)
        recent_data = self.sensor_data[self.sensor_data.index >= start_date]
        
        # Create subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle(f'Air Quality Trends - Last {days} Days', fontsize=16, fontweight='bold')
        
        # Plot 1: PM2.5 trends by city
        for city in self.cities:
            city_data = recent_data[recent_data['city'] == city]
            daily_avg = city_data['PM2.5'].resample('D').mean()
            axes[0, 0].plot(daily_avg.index, daily_avg.values, marker='o', label=city)
        
        axes[0, 0].set_title('PM2.5 Daily Average Trends')
        axes[0, 0].set_ylabel('PM2.5 (μg/m³)')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # Plot 2: AQI distribution by city
        aqi_by_city = [recent_data[recent_data['city'] == city]['AQI_Overall'] for city in self.cities]
        axes[0, 1].boxplot(aqi_by_city, labels=self.cities)
        axes[0, 1].set_title('AQI Distribution by City')
        axes[0, 1].set_ylabel('AQI')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Plot 3: Hourly pollution patterns
        hourly_avg = recent_data.groupby(recent_data.index.hour)['PM2.5'].mean()
        axes[1, 0].bar(hourly_avg.index, hourly_avg.values, alpha=0.7, color='orange')
        axes[1, 0].set_title('Average PM2.5 by Hour of Day')
        axes[1, 0].set_xlabel('Hour')
        axes[1, 0].set_ylabel('PM2.5 (μg/m³)')
        
        # Plot 4: AQI category distribution
        category_counts = recent_data['AQI_Category'].value_counts()
        colors = ['green', 'yellow', 'orange', 'red', 'purple', 'maroon']
        axes[1, 1].pie(category_counts.values, labels=category_counts.index, 
                      autopct='%1.1f%%', colors=colors[:len(category_counts)])
        axes[1, 1].set_title('AQI Category Distribution')
        
        plt.tight_layout()
        plt.show()
        
        return fig
    
    def export_data(self, export_format='csv', filename=None):
        """Export processed data to various formats"""
        if self.sensor_data is None:
            print("No data to export")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if export_format.lower() == 'csv':
            if filename is None:
                filename = f'air_quality_data_{timestamp}.csv'
            self.sensor_data.to_csv(filename)
            print(f"Data exported to {filename}")
            
        elif export_format.lower() == 'excel':
            if filename is None:
                filename = f'air_quality_report_{timestamp}.xlsx'
            
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # Main data
                self.sensor_data.to_excel(writer, sheet_name='Sensor_Data')
                
                # Daily summary
                if hasattr(self, 'daily_report'):
                    self.daily_report.to_excel(writer, sheet_name='Daily_Summary')
                
                # Hourly patterns
                if hasattr(self, 'hourly_summary'):
                    self.hourly_summary.to_excel(writer, sheet_name='Hourly_Patterns', index=False)
                
                # Pollution events
                if hasattr(self, 'pollution_events') and len(self.pollution_events) > 0:
                    self.pollution_events.to_excel(writer, sheet_name='Pollution_Events', index=False)
            
            print(f"Report exported to {filename}")
            
        elif export_format.lower() == 'json':
            if filename is None:
                filename = f'air_quality_data_{timestamp}.json'
            
            # Convert to JSON-serializable format
            export_data = {
                'metadata': {
                    'export_time': timestamp,
                    'cities': self.cities,
                    'data_period': {
                        'start': self.sensor_data.index.min().isoformat(),
                        'end': self.sensor_data.index.max().isoformat()
                    }
                },
                'sensor_data': self.sensor_data.reset_index().to_dict('records'),
                'alerts': self.alerts if self.alerts else []
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"Data exported to {filename}")
        
        return filename

def main():
    """Main demonstration function"""
    print("🌍 AIR QUALITY MONITORING SYSTEM FOR VIETNAM")
    print("=" * 60)
    
    # Initialize monitor
    monitor = AirQualityMonitor()
    
    # Generate sample data (30 days)
    print("\n1. Generating sample data...")
    monitor.generate_sample_data(days=30)
    
    # Process AQI data
    print("\n2. Processing AQI calculations...")
    monitor.process_aqi_data()
    
    # Generate current alerts
    print("\n3. Checking for current alerts...")
    alerts = monitor.generate_alerts(aqi_threshold=100)
    
    # Detect pollution events
    print("\n4. Detecting pollution events...")
    events = monitor.detect_pollution_events()
    
    # Create daily report
    print("\n5. Generating daily report...")
    daily_report = monitor.create_daily_report()
    
    # Create hourly summary
    print("\n6. Creating hourly patterns...")
    hourly_summary = monitor.create_hourly_summary()
    
    # Visualize trends
    print("\n7. Creating visualizations...")
    try:
        monitor.visualize_trends(days=7)
    except Exception as e:
        print(f"Visualization error: {e}")
    
    # Export data
    print("\n8. Exporting results...")
    monitor.export_data('excel', 'vietnam_air_quality_report.xlsx')
    monitor.export_data('json', 'vietnam_air_quality_data.json')
    
    print("\n✅ Air Quality Monitoring Analysis Complete!")
    print(f"📊 Processed {len(monitor.sensor_data)} sensor readings")
    print(f"🚨 Found {len(alerts)} active alerts")
    if hasattr(monitor, 'pollution_events'):
        print(f"⚠️ Detected {len(monitor.pollution_events)} pollution events")
    
    return monitor

if __name__ == "__main__":
    # Run the monitoring system
    monitor = main()
    
    # Additional analysis examples
    print("\n" + "="*60)
    print("ADDITIONAL ANALYSIS EXAMPLES:")
    
    # Example: Find worst air quality periods
    if monitor.sensor_data is not None:
        worst_aqi = monitor.sensor_data.nlargest(5, 'AQI_Overall')[['city', 'AQI_Overall', 'AQI_Category', 'PM2.5']]
        print("\n🔴 Top 5 Worst Air Quality Periods:")
        for idx, row in worst_aqi.iterrows():
            print(f"  {idx.strftime('%Y-%m-%d %H:%M')} - {row['city']}: AQI {row['AQI_Overall']:.0f} ({row['AQI_Category']})")
    
    # Example: City rankings
    if hasattr(monitor, 'daily_report'):
        city_rankings = monitor.daily_report['AQI_Overall_mean'].sort_values()
        print("\n🏆 City Air Quality Rankings (Best to Worst):")
        for i, (city, aqi) in enumerate(city_rankings.items(), 1):
            print(f"  {i}. {city}: {aqi:.1f} AQI")
    
    print("\n🎯 Monitoring system ready for real-time operations!")
