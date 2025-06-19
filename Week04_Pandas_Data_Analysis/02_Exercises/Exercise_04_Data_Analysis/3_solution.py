"""
Exercise 04: Data Analysis - Solution
Week 4: Pandas Data Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

def exercise_1_climate_trend_analysis():
    """Bài 1: Phân tích xu hướng biến đổi khí hậu Việt Nam - SOLUTION"""
    print("Bài 1: Phân tích xu hướng biến đổi khí hậu Việt Nam - SOLUTION")
    print("-" * 70)
    
    # Tạo dữ liệu khí hậu từ 1990-2023
    years = list(range(1990, 2024))
    np.random.seed(42)  # For reproducible results
    
    # Base temperatures with warming trend
    base_temp = 26.0
    warming_trend = 0.03  # 0.03°C per year
    
    regions_data = {}
    regions = ['Bắc Bộ', 'Trung Bộ', 'Nam Bộ', 'Tây Nguyên', 'Đồng bằng sông Cửu Long']
    
    for i, region in enumerate(regions):
        regional_adjustment = i * 0.5 - 1.0  # Regional temperature differences
        temperatures = []
        rainfall = []
        
        for year in years:
            # Temperature with warming trend + random variation
            temp = (base_temp + regional_adjustment + 
                   warming_trend * (year - 1990) + 
                   np.random.normal(0, 0.8))
            temperatures.append(temp)
            
            # Rainfall with some correlation to temperature (inverse)
            base_rainfall = 1500 + regional_adjustment * 200
            rain = base_rainfall - (temp - base_temp) * 50 + np.random.normal(0, 200)
            rainfall.append(max(0, rain))
        
        regions_data[region] = {
            'temperature': temperatures,
            'rainfall': rainfall
        }
    
    # Create DataFrame
    data_records = []
    for region in regions:
        for i, year in enumerate(years):
            data_records.append({
                'year': year,
                'region': region,
                'temperature': regions_data[region]['temperature'][i],
                'rainfall': regions_data[region]['rainfall'][i]
            })
    
    climate_df = pd.DataFrame(data_records)
    print(f"Tạo DataFrame khí hậu: {len(climate_df)} records, {len(years)} năm, {len(regions)} vùng")
    
    # 1. Phân tích xu hướng nhiệt độ trung bình
    annual_temp = climate_df.groupby('year')['temperature'].mean()
    
    # Linear regression for trend
    slope, intercept, r_value, p_value, std_err = stats.linregress(years, annual_temp)
    trend_line = [slope * year + intercept for year in years]
    
    print(f"\n1. Xu hướng nhiệt độ trung bình (1990-2023):")
    print(f"   Nhiệt độ TB 1990: {annual_temp.iloc[0]:.2f}°C")
    print(f"   Nhiệt độ TB 2023: {annual_temp.iloc[-1]:.2f}°C")
    print(f"   Xu hướng: +{slope:.3f}°C/năm")
    print(f"   Tổng tăng: +{slope * len(years):.2f}°C trong {len(years)} năm")
    print(f"   R² = {r_value**2:.3f}, p-value = {p_value:.3e}")
    
    # 2. Moving averages
    ma_5 = annual_temp.rolling(window=5).mean()
    ma_10 = annual_temp.rolling(window=10).mean()
    
    print(f"\n2. Moving averages:")
    print(f"   MA(5) 2019-2023: {ma_5.iloc[-5:].mean():.2f}°C")
    print(f"   MA(10) 2014-2023: {ma_10.iloc[-10:].mean():.2f}°C")
    
    # 3. Extreme years
    hottest_year = annual_temp.idxmax()
    coldest_year = annual_temp.idxmin()
    
    print(f"\n3. Các năm cực trị:")
    print(f"   Năm nóng nhất: {hottest_year} ({annual_temp[hottest_year]:.2f}°C)")
    print(f"   Năm lạnh nhất: {coldest_year} ({annual_temp[coldest_year]:.2f}°C)")
    
    # 4. Regional comparison
    regional_trends = {}
    print(f"\n4. So sánh xu hướng theo vùng:")
    
    for region in regions:
        region_data = climate_df[climate_df['region'] == region]
        region_temps = region_data.groupby('year')['temperature'].mean()
        region_slope, _, region_r, region_p, _ = stats.linregress(years, region_temps)
        regional_trends[region] = {
            'slope': region_slope,
            'r_squared': region_r**2,
            'avg_temp': region_temps.mean()
        }
        print(f"   {region}: +{region_slope:.3f}°C/năm (R²={region_r**2:.3f})")
    
    # 5. Temperature-rainfall correlation
    temp_rain_corr = climate_df.groupby('year').agg({
        'temperature': 'mean',
        'rainfall': 'mean'
    }).corr().iloc[0, 1]
    
    print(f"\n5. Tương quan nhiệt độ - lượng mưa:")
    print(f"   Correlation coefficient: {temp_rain_corr:.3f}")
    
    # 6. Anomaly detection
    temp_mean = annual_temp.mean()
    temp_std = annual_temp.std()
    anomalies = annual_temp[(annual_temp > temp_mean + 2*temp_std) | 
                           (annual_temp < temp_mean - 2*temp_std)]
    
    print(f"\n6. Phát hiện bất thường (>2σ):")
    if len(anomalies) > 0:
        for year, temp in anomalies.items():
            deviation = (temp - temp_mean) / temp_std
            print(f"   {year}: {temp:.2f}°C (Z-score: {deviation:+.2f})")
    else:
        print("   Không phát hiện bất thường nhiệt độ")
    
    return climate_df, annual_temp, regional_trends

def exercise_2_air_pollution_time_series():
    """Bài 2: Phân tích chuỗi thời gian ô nhiễm không khí - SOLUTION"""
    print("\nBài 2: Phân tích chuỗi thời gian ô nhiễm không khí - SOLUTION")
    print("-" * 70)
    
    # Tạo dữ liệu hourly cho 3 tháng
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 3, 31)
    timestamps = pd.date_range(start_date, end_date, freq='H')
    
    np.random.seed(123)
    
    # Generate realistic pollution data with patterns
    pollution_data = []
    
    for ts in timestamps:
        hour = ts.hour
        day_of_week = ts.weekday()
        month = ts.month
        
        # Base pollution levels
        base_pm25 = 35
        base_pm10 = 60
        base_no2 = 45
        
        # Time patterns
        # Rush hour effects
        if hour in [7, 8, 17, 18, 19]:
            traffic_multiplier = 1.6
        elif hour in [6, 9, 16, 20]:
            traffic_multiplier = 1.3
        elif hour in [22, 23, 0, 1, 2, 3, 4, 5]:
            traffic_multiplier = 0.7
        else:
            traffic_multiplier = 1.0
        
        # Weekend effects
        weekend_multiplier = 0.8 if day_of_week >= 5 else 1.0
        
        # Seasonal effects
        seasonal_multiplier = 1.3 if month in [1, 2] else 1.0
        
        # Weather effects (simplified)
        weather_factor = np.random.uniform(0.7, 1.4)
        
        total_multiplier = traffic_multiplier * weekend_multiplier * seasonal_multiplier * weather_factor
        
        pm25 = max(5, base_pm25 * total_multiplier + np.random.normal(0, 8))
        pm10 = max(10, base_pm10 * total_multiplier + np.random.normal(0, 12))
        no2 = max(5, base_no2 * total_multiplier + np.random.normal(0, 10))
        
        pollution_data.append({
            'timestamp': ts,
            'PM2.5': pm25,
            'PM10': pm10,
            'NO2': no2
        })
    
    pollution_df = pd.DataFrame(pollution_data)
    pollution_df.set_index('timestamp', inplace=True)
    
    print(f"Tạo time series ô nhiễm: {len(pollution_df)} hours từ {start_date.date()} đến {end_date.date()}")
    
    # 1. Hourly patterns
    hourly_patterns = pollution_df.groupby(pollution_df.index.hour).mean()
    
    print(f"\n1. Patterns theo giờ trong ngày:")
    peak_hour_pm25 = hourly_patterns['PM2.5'].idxmax()
    low_hour_pm25 = hourly_patterns['PM2.5'].idxmin()
    print(f"   PM2.5 cao nhất: {peak_hour_pm25}h ({hourly_patterns.loc[peak_hour_pm25, 'PM2.5']:.1f} μg/m³)")
    print(f"   PM2.5 thấp nhất: {low_hour_pm25}h ({hourly_patterns.loc[low_hour_pm25, 'PM2.5']:.1f} μg/m³)")
    
    # 2. Rolling statistics
    rolling_24h = pollution_df.rolling(window=24).agg(['mean', 'std'])
    rolling_24h.columns = ['_'.join(col).strip() for col in rolling_24h.columns]
    
    latest_24h_avg = rolling_24h['PM2.5_mean'].iloc[-1]
    latest_24h_std = rolling_24h['PM2.5_std'].iloc[-1]
    
    print(f"\n2. Rolling statistics (24h window):")
    print(f"   PM2.5 TB 24h cuối: {latest_24h_avg:.1f} ± {latest_24h_std:.1f} μg/m³")
    
    # 3. Peak pollution periods
    pm25_95th = pollution_df['PM2.5'].quantile(0.95)
    peak_periods = pollution_df[pollution_df['PM2.5'] > pm25_95th]
    
    print(f"\n3. Thời điểm ô nhiễm nặng (top 5%):")
    print(f"   Ngưỡng: {pm25_95th:.1f} μg/m³")
    print(f"   Số giờ vượt ngưỡng: {len(peak_periods)} ({len(peak_periods)/len(pollution_df)*100:.1f}%)")
    
    if len(peak_periods) > 0:
        peak_hours = peak_periods.groupby(peak_periods.index.hour).size()
        print(f"   Giờ thường xuyên ô nhiễm nặng: {peak_hours.idxmax()}h ({peak_hours.max()} lần)")
    
    # 4. Weekend vs weekday comparison
    pollution_df['is_weekend'] = pollution_df.index.weekday >= 5
    weekday_avg = pollution_df[~pollution_df['is_weekend']]['PM2.5'].mean()
    weekend_avg = pollution_df[pollution_df['is_weekend']]['PM2.5'].mean()
    
    print(f"\n4. So sánh tuần vs cuối tuần:")
    print(f"   PM2.5 TB ngày thường: {weekday_avg:.1f} μg/m³")
    print(f"   PM2.5 TB cuối tuần: {weekend_avg:.1f} μg/m³")
    print(f"   Chênh lệch: {((weekday_avg - weekend_avg)/weekend_avg)*100:+.1f}%")
    
    # 5. Seasonal decomposition (simplified)
    daily_avg = pollution_df.resample('D').mean()
    
    # Linear trend
    days = np.arange(len(daily_avg))
    trend_slope, trend_intercept, _, _, _ = stats.linregress(days, daily_avg['PM2.5'])
    trend_component = trend_slope * days + trend_intercept
    
    # Residual after removing trend
    detrended = daily_avg['PM2.5'] - trend_component
    
    print(f"\n5. Decomposition đơn giản:")
    print(f"   Xu hướng: {trend_slope:.3f} μg/m³/ngày")
    print(f"   Biến động sau khi loại bỏ xu hướng: {detrended.std():.1f} μg/m³")
    
    return pollution_df, hourly_patterns

def exercise_3_ndvi_vegetation_analysis():
    """Bài 3: Phân tích NDVI và thảm thực vật - SOLUTION"""
    print("\nBài 3: Phân tích NDVI và thảm thực vật - SOLUTION")
    print("-" * 70)
    
    # Create monthly NDVI data for different land cover types
    months = pd.date_range('2020-01', '2023-12', freq='MS')
    
    land_cover_types = [
        'Dense Forest', 'Sparse Forest', 'Agricultural Land', 
        'Grassland', 'Urban Area', 'Water Body', 'Bare Land'
    ]
    
    # Base NDVI values for each land cover type
    base_ndvi = {
        'Dense Forest': 0.75,
        'Sparse Forest': 0.55,
        'Agricultural Land': 0.45,
        'Grassland': 0.35,
        'Urban Area': 0.15,
        'Water Body': -0.05,
        'Bare Land': 0.05
    }
    
    np.random.seed(456)
    ndvi_data = []
    
    for month in months:
        month_num = month.month
        year = month.year
        
        # Seasonal pattern (Vietnam has 2 main seasons)
        if month_num in [5, 6, 7, 8, 9, 10]:  # Rainy season
            seasonal_boost = 0.15
        else:  # Dry season
            seasonal_boost = -0.05
        
        # Long-term trend (slight degradation for some types)
        years_passed = year - 2020
        degradation_trend = -0.01 * years_passed
        
        for land_type in land_cover_types:
            base = base_ndvi[land_type]
            
            # Seasonal effects vary by land type
            if land_type in ['Dense Forest', 'Sparse Forest']:
                seasonal_effect = seasonal_boost * 0.7  # Forests less affected
            elif land_type in ['Agricultural Land', 'Grassland']:
                seasonal_effect = seasonal_boost * 1.2  # Agriculture more affected
            else:
                seasonal_effect = seasonal_boost * 0.3
            
            # Degradation effects
            if land_type in ['Dense Forest', 'Sparse Forest']:
                degradation = degradation_trend * 2  # Deforestation
            elif land_type == 'Agricultural Land':
                degradation = degradation_trend * 0.5  # Some sustainability practices
            else:
                degradation = degradation_trend
            
            # Random variation
            noise = np.random.normal(0, 0.05)
            
            # Calculate final NDVI
            final_ndvi = base + seasonal_effect + degradation + noise
            final_ndvi = np.clip(final_ndvi, -1, 1)  # NDVI range constraint
            
            ndvi_data.append({
                'date': month,
                'land_cover': land_type,
                'ndvi': final_ndvi,
                'area_hectares': np.random.randint(1000, 50000)  # Random area
            })
    
    ndvi_df = pd.DataFrame(ndvi_data)
    ndvi_df.set_index('date', inplace=True)
    
    print(f"Tạo NDVI dataset: {len(ndvi_df)} records, {len(months)} tháng, {len(land_cover_types)} loại đất")
    
    # 1. Monthly NDVI averages by land cover
    monthly_averages = ndvi_df.groupby(['land_cover', ndvi_df.index]).agg({
        'ndvi': 'mean',
        'area_hectares': 'sum'
    })
    
    print(f"\n1. NDVI trung bình theo loại đất:")
    overall_averages = ndvi_df.groupby('land_cover')['ndvi'].mean().sort_values(ascending=False)
    for land_type, avg_ndvi in overall_averages.items():
        print(f"   {land_type}: {avg_ndvi:.3f}")
    
    # 2. Seasonal patterns
    ndvi_df['month'] = ndvi_df.index.month
    seasonal_patterns = ndvi_df.groupby(['land_cover', 'month'])['ndvi'].mean()
    
    print(f"\n2. Biến động theo mùa (NDVI cao nhất vs thấp nhất):")
    for land_type in land_cover_types:
        land_seasonal = seasonal_patterns[land_type]
        max_month = land_seasonal.idxmax()
        min_month = land_seasonal.idxmin()
        seasonal_range = land_seasonal.max() - land_seasonal.min()
        print(f"   {land_type}: Tháng {max_month} ({land_seasonal.max():.3f}) - Tháng {min_month} ({land_seasonal.min():.3f}) = {seasonal_range:.3f}")
    
    # 3. Deforestation detection
    forest_data = ndvi_df[ndvi_df['land_cover'].isin(['Dense Forest', 'Sparse Forest'])]
    forest_yearly = forest_data.groupby([forest_data.index.year, 'land_cover'])['ndvi'].mean()
    
    print(f"\n3. Phát hiện suy thoái rừng:")
    for forest_type in ['Dense Forest', 'Sparse Forest']:
        if forest_type in forest_yearly.index.get_level_values(1):
            forest_trend = forest_yearly[:, forest_type]
            years = forest_trend.index
            slope, _, r_value, p_value, _ = stats.linregress(years, forest_trend.values)
            
            print(f"   {forest_type}:")
            print(f"     Xu hướng: {slope:.4f} NDVI/năm")
            print(f"     R² = {r_value**2:.3f}, p = {p_value:.3f}")
            
            if slope < -0.005 and p_value < 0.05:
                loss_rate = abs(slope) * 100  # Convert to percentage
                print(f"     ⚠️ Suy thoái đáng kể: {loss_rate:.2f}%/năm")
    
    # 4. Protected vs non-protected areas comparison
    # Simulate protected area status
    ndvi_df['is_protected'] = np.random.choice([True, False], size=len(ndvi_df), p=[0.3, 0.7])
    
    protection_comparison = ndvi_df.groupby(['land_cover', 'is_protected'])['ndvi'].mean()
    
    print(f"\n4. So sánh khu vực được bảo vệ vs không được bảo vệ:")
    for land_type in land_cover_types:
        if land_type in protection_comparison.index.get_level_values(0):
            try:
                protected = protection_comparison[land_type, True]
                unprotected = protection_comparison[land_type, False]
                difference = protected - unprotected
                print(f"   {land_type}: Được BV {protected:.3f} vs Không BV {unprotected:.3f} (Δ{difference:+.3f})")
            except KeyError:
                continue
    
    # 5. Vegetation recovery analysis
    # Simulate some disturbance events and recovery
    recovery_events = []
    for land_type in ['Dense Forest', 'Agricultural Land']:
        land_data = ndvi_df[ndvi_df['land_cover'] == land_type].copy()
        land_data = land_data.sort_index()
        
        # Find significant drops (simulated disturbances)
        land_data['ndvi_diff'] = land_data['ndvi'].diff()
        disturbances = land_data[land_data['ndvi_diff'] < -0.1]
        
        for dist_date, _ in disturbances.iterrows():
            # Check recovery in next 12 months
            recovery_period = land_data[land_data.index > dist_date][:12]
            if len(recovery_period) >= 6:
                initial_ndvi = land_data.loc[dist_date, 'ndvi']
                recovery_ndvi = recovery_period['ndvi'].max()
                recovery_rate = (recovery_ndvi - initial_ndvi) / len(recovery_period)
                
                recovery_events.append({
                    'land_cover': land_type,
                    'disturbance_date': dist_date,
                    'initial_ndvi': initial_ndvi,
                    'recovery_ndvi': recovery_ndvi,
                    'recovery_rate': recovery_rate
                })
    
    if recovery_events:
        print(f"\n5. Phân tích phục hồi thảm thực vật:")
        recovery_df = pd.DataFrame(recovery_events)
        avg_recovery = recovery_df.groupby('land_cover')['recovery_rate'].mean()
        
        for land_type, rate in avg_recovery.items():
            print(f"   {land_type}: Tốc độ phục hồi TB {rate:.4f} NDVI/tháng")
    
    # 6. Vegetation health index
    # Create composite index
    health_weights = {
        'Dense Forest': 1.0,
        'Sparse Forest': 0.8,
        'Agricultural Land': 0.6,
        'Grassland': 0.5,
        'Urban Area': 0.2,
        'Water Body': 0.1,
        'Bare Land': 0.1
    }
    
    ndvi_df['weighted_ndvi'] = ndvi_df.apply(
        lambda row: row['ndvi'] * health_weights[row['land_cover']], axis=1
    )
    
    monthly_health = ndvi_df.groupby(ndvi_df.index).agg({
        'weighted_ndvi': 'mean',
        'area_hectares': 'sum'
    })
    
    # Health trend
    months_numeric = np.arange(len(monthly_health))
    health_slope, _, health_r, health_p, _ = stats.linregress(months_numeric, monthly_health['weighted_ndvi'])
    
    print(f"\n6. Chỉ số sức khỏe thảm thực vật:")
    print(f"   Chỉ số TB: {monthly_health['weighted_ndvi'].mean():.3f}")
    print(f"   Xu hướng: {health_slope:.4f}/tháng")
    print(f"   R² = {health_r**2:.3f}, p = {health_p:.3f}")
    
    if health_slope < 0 and health_p < 0.05:
        print(f"   ⚠️ Suy giảm đáng kể sức khỏe thảm thực vật")
    elif health_slope > 0 and health_p < 0.05:
        print(f"   ✅ Cải thiện sức khỏe thảm thực vật")
    
    return ndvi_df, monthly_health

def exercise_4_socioeconomic_correlation():
    """Bài 4: Phân tích tương quan kinh tế xã hội - SOLUTION"""
    print("\nBài 4: Phân tích tương quan dữ liệu kinh tế xã hội - SOLUTION")
    print("-" * 70)
    
    # Vietnamese provinces data
    provinces = [
        'Hà Nội', 'TP.HCM', 'Hải Phòng', 'Đà Nẵng', 'Cần Thơ',
        'Hải Dương', 'Hưng Yên', 'Bắc Ninh', 'Quảng Ninh', 'Thanh Hóa',
        'Nghệ An', 'Thừa Thiên Huế', 'Quảng Nam', 'Bình Dương', 'Đồng Nai'
    ]
    
    np.random.seed(789)
    
    # Generate realistic socio-economic data
    socio_data = []
    for province in provinces:
        # Major cities have higher values
        if province in ['Hà Nội', 'TP.HCM']:
            gdp_multiplier = 2.5
            urbanization_base = 0.85
            education_base = 0.92
        elif province in ['Hải Phòng', 'Đà Nẵng', 'Cần Thơ']:
            gdp_multiplier = 1.8
            urbanization_base = 0.75
            education_base = 0.88
        else:
            gdp_multiplier = 1.0
            urbanization_base = 0.45
            education_base = 0.82
        
        # GDP per capita (million VND)
        gdp_per_capita = 45 * gdp_multiplier + np.random.normal(0, 5)
        
        # Population (thousands)
        if province in ['Hà Nội', 'TP.HCM']:
            population = np.random.randint(6000, 10000)
        elif province in ['Hải Phòng', 'Đà Nẵng', 'Cần Thơ']:
            population = np.random.randint(1200, 2500)
        else:
            population = np.random.randint(800, 2000)
        
        # Urbanization rate
        urbanization = urbanization_base + np.random.normal(0, 0.05)
        urbanization = np.clip(urbanization, 0, 1)
        
        # Education rate (high school completion)
        education = education_base + np.random.normal(0, 0.03)
        education = np.clip(education, 0, 1)
        
        # Healthcare index (0-100)
        healthcare = 60 + gdp_multiplier * 10 + np.random.normal(0, 5)
        healthcare = np.clip(healthcare, 0, 100)
        
        # Environmental quality index (inversely related to urbanization/GDP)
        environmental = 70 - (gdp_per_capita - 45) * 0.3 - urbanization * 15 + np.random.normal(0, 8)
        environmental = np.clip(environmental, 0, 100)
        
        # Industry share in GDP
        industry_share = 0.35 + (gdp_multiplier - 1) * 0.1 + np.random.normal(0, 0.05)
        industry_share = np.clip(industry_share, 0, 1)
        
        socio_data.append({
            'province': province,
            'gdp_per_capita': gdp_per_capita,
            'population_thousands': population,
            'urbanization_rate': urbanization,
            'education_rate': education,
            'healthcare_index': healthcare,
            'environmental_quality': environmental,
            'industry_share': industry_share
        })
    
    socio_df = pd.DataFrame(socio_data)
    print(f"Tạo dữ liệu kinh tế xã hội cho {len(provinces)} tỉnh thành")
    
    # 1. Basic statistics
    print(f"\n1. Thống kê mô tả:")
    numeric_cols = ['gdp_per_capita', 'population_thousands', 'urbanization_rate', 
                   'education_rate', 'healthcare_index', 'environmental_quality']
    
    for col in numeric_cols:
        mean_val = socio_df[col].mean()
        std_val = socio_df[col].std()
        print(f"   {col}: {mean_val:.2f} ± {std_val:.2f}")
    
    # 2. Correlation analysis
    correlation_matrix = socio_df[numeric_cols].corr()
    
    print(f"\n2. Ma trận tương quan (top correlations):")
    # Find strongest correlations
    correlations = []
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            var1 = correlation_matrix.columns[i]
            var2 = correlation_matrix.columns[j]
            corr_val = correlation_matrix.iloc[i, j]
            correlations.append((var1, var2, abs(corr_val), corr_val))
    
    # Sort by absolute correlation
    correlations.sort(key=lambda x: x[2], reverse=True)
    
    for var1, var2, abs_corr, corr in correlations[:5]:
        direction = "positive" if corr > 0 else "negative"
        print(f"   {var1} - {var2}: {corr:.3f} ({direction})")
    
    # 3. Economic development classification
    # Create development index
    socio_df['development_index'] = (
        (socio_df['gdp_per_capita'] - socio_df['gdp_per_capita'].min()) / 
        (socio_df['gdp_per_capita'].max() - socio_df['gdp_per_capita'].min()) * 0.4 +
        socio_df['urbanization_rate'] * 0.3 +
        socio_df['education_rate'] * 0.2 +
        (socio_df['healthcare_index'] / 100) * 0.1
    )
    
    # Classify development levels
    dev_quantiles = socio_df['development_index'].quantile([0.33, 0.67])
    
    def classify_development(index):
        if index <= dev_quantiles.iloc[0]:
            return 'Developing'
        elif index <= dev_quantiles.iloc[1]:
            return 'Moderate'
        else:
            return 'Advanced'
    
    socio_df['development_level'] = socio_df['development_index'].apply(classify_development)
    
    print(f"\n3. Phân loại mức độ phát triển:")
    dev_counts = socio_df['development_level'].value_counts()
    for level, count in dev_counts.items():
        avg_gdp = socio_df[socio_df['development_level'] == level]['gdp_per_capita'].mean()
        provinces_list = socio_df[socio_df['development_level'] == level]['province'].tolist()
        print(f"   {level}: {count} tỉnh (GDP TB: {avg_gdp:.1f} tr VNĐ)")
        print(f"     {', '.join(provinces_list)}")
    
    # 4. Environmental vs Economic trade-off
    eco_env_corr = socio_df['gdp_per_capita'].corr(socio_df['environmental_quality'])
    print(f"\n4. Trade-off Kinh tế - Môi trường:")
    print(f"   Tương quan GDP - Chất lượng môi trường: {eco_env_corr:.3f}")
    
    # Find outliers (good/bad performers)
    socio_df['eco_env_ratio'] = socio_df['environmental_quality'] / socio_df['gdp_per_capita']
    
    best_balance = socio_df.nlargest(3, 'eco_env_ratio')[['province', 'gdp_per_capita', 'environmental_quality']]
    worst_balance = socio_df.nsmallest(3, 'eco_env_ratio')[['province', 'gdp_per_capita', 'environmental_quality']]
    
    print(f"   Cân bằng tốt nhất (Môi trường/GDP cao):")
    for _, row in best_balance.iterrows():
        print(f"     {row['province']}: GDP {row['gdp_per_capita']:.1f}, Môi trường {row['environmental_quality']:.1f}")
    
    print(f"   Cần cải thiện (Môi trường/GDP thấp):")
    for _, row in worst_balance.iterrows():
        print(f"     {row['province']}: GDP {row['gdp_per_capita']:.1f}, Môi trường {row['environmental_quality']:.1f}")
    
    # 5. Regression analysis
    from scipy.stats import pearsonr
    
    # Healthcare vs GDP
    healthcare_gdp_corr, healthcare_p = pearsonr(socio_df['healthcare_index'], socio_df['gdp_per_capita'])
    
    # Education vs GDP  
    education_gdp_corr, education_p = pearsonr(socio_df['education_rate'], socio_df['gdp_per_capita'])
    
    print(f"\n5. Phân tích hồi quy:")
    print(f"   Healthcare - GDP: r={healthcare_gdp_corr:.3f}, p={healthcare_p:.3f}")
    print(f"   Education - GDP: r={education_gdp_corr:.3f}, p={education_p:.3f}")
    
    # Multiple regression (simplified)
    # Predict GDP from other factors
    predictors = ['urbanization_rate', 'education_rate', 'healthcare_index', 'industry_share']
    X = socio_df[predictors]
    y = socio_df['gdp_per_capita']
    
    # Calculate R-squared manually (simplified)
    correlation_with_gdp = X.corrwith(y)
    avg_correlation = correlation_with_gdp.abs().mean()
    
    print(f"\n6. Dự đoán GDP từ các yếu tố:")
    print(f"   Tương quan TB với GDP: {avg_correlation:.3f}")
    print(f"   Yếu tố quan trọng nhất: {correlation_with_gdp.abs().idxmax()} ({correlation_with_gdp.abs().max():.3f})")
    
    # Policy recommendations
    print(f"\n7. Khuyến nghị chính sách:")
    
    # For developing provinces
    developing = socio_df[socio_df['development_level'] == 'Developing']
    if len(developing) > 0:
        low_education = developing[developing['education_rate'] < developing['education_rate'].quantile(0.5)]
        if len(low_education) > 0:
            print(f"   Tỉnh cần đầu tư giáo dục: {', '.join(low_education['province'].tolist())}")
    
    # For advanced provinces
    advanced = socio_df[socio_df['development_level'] == 'Advanced']
    if len(advanced) > 0:
        low_env = advanced[advanced['environmental_quality'] < advanced['environmental_quality'].median()]
        if len(low_env) > 0:
            print(f"   Tỉnh phát triển cần bảo vệ môi trường: {', '.join(low_env['province'].tolist())}")
    
    return socio_df, correlation_matrix

def main():
    """Hàm main với đáp án mẫu"""
    print("Exercise 04: Data Analysis - COMPLETE SOLUTION")
    print("=" * 70)
    
    # Run all exercises
    climate_df, annual_temp, regional_trends = exercise_1_climate_trend_analysis()
    pollution_df, hourly_patterns = exercise_2_air_pollution_time_series()
    ndvi_df, monthly_health = exercise_3_ndvi_vegetation_analysis()
    socio_df, correlation_matrix = exercise_4_socioeconomic_correlation()
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 TỔNG KẾT PHÂN TÍCH DỮ LIỆU NÂNG CAO")
    print("=" * 70)
    
    print(f"✅ Bài 1 - Khí hậu: {len(climate_df)} records, xu hướng +{annual_temp.pct_change().mean()*100:.2f}%/năm")
    print(f"✅ Bài 2 - Ô nhiễm: {len(pollution_df)} hours, patterns theo giờ và ngày")
    print(f"✅ Bài 3 - NDVI: {len(ndvi_df)} observations, {len(ndvi_df['land_cover'].unique())} loại đất")
    print(f"✅ Bài 4 - Kinh tế XH: {len(socio_df)} tỉnh thành, phân tích tương quan đa chiều")
    
    print("\n🎯 Kỹ năng đã thành thạo:")
    print("   - Time series analysis và trend detection")
    print("   - Statistical testing và correlation analysis")
    print("   - Anomaly detection và change point analysis")
    print("   - Multi-dimensional data analysis")
    print("   - Environmental data interpretation")
    print("   - Policy insight generation")
    
    return {
        'climate': climate_df,
        'pollution': pollution_df,
        'ndvi': ndvi_df,
        'socioeconomic': socio_df
    }

if __name__ == "__main__":
    results = main()
