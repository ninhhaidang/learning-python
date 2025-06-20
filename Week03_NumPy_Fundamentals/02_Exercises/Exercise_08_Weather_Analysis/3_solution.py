import numpy as np

def main():
    """Weather Data Analysis với NumPy"""
    print("=== WEATHER DATA ANALYSIS ===")
    print()
    
    # Generate weather data for 365 days
    np.random.seed(42)
    days = 365
    
    # Temperature with seasonal pattern
    day_of_year = np.arange(days)
    base_temp = 18 + 12 * np.sin(2 * np.pi * (day_of_year - 81) / 365)  # Peak in summer
    temp_noise = np.random.normal(0, 3, days)
    temperature = base_temp + temp_noise
    
    # Humidity (inverse correlation with temperature)
    humidity = 80 - 0.8 * (temperature - 18) + np.random.normal(0, 8, days)
    humidity = np.clip(humidity, 25, 95)
    
    # Rainfall (random with seasonal bias)
    rainfall_prob = 0.3 + 0.2 * np.sin(2 * np.pi * (day_of_year - 275) / 365)  # More in winter
    rainfall = np.where(np.random.random(days) < rainfall_prob,
                       np.random.exponential(8, days), 0)
    
    print("📊 DATASET OVERVIEW:")
    print(f"Period: {days} days (1 year)")
    print(f"Temperature range: {np.min(temperature):.1f}°C to {np.max(temperature):.1f}°C")
    print(f"Humidity range: {np.min(humidity):.0f}% to {np.max(humidity):.0f}%")
    print(f"Total rainfall: {np.sum(rainfall):.1f} mm")
    print()
    
    # Monthly statistics
    print("📅 MONTHLY STATISTICS:")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    for month in range(12):
        start_day = month * 30
        end_day = min((month + 1) * 30, days)
        
        month_temp = np.mean(temperature[start_day:end_day])
        month_humidity = np.mean(humidity[start_day:end_day])
        month_rain = np.sum(rainfall[start_day:end_day])
        
        print(f"Month {month+1:2d} ({months[month]}): Temp {month_temp:.1f}°C, "
              f"Humidity {month_humidity:.0f}%, Rain {month_rain:.1f}mm")
    print()
    
    # Temperature trends
    print("🌡️  TEMPERATURE TRENDS:")
    monthly_temps = [np.mean(temperature[i*30:(i+1)*30]) for i in range(12)]
    coldest_month = np.argmin(monthly_temps)
    warmest_month = np.argmax(monthly_temps)
    
    print(f"Coldest month: {months[coldest_month]} ({monthly_temps[coldest_month]:.1f}°C)")
    print(f"Warmest month: {months[warmest_month]} ({monthly_temps[warmest_month]:.1f}°C)")
    print(f"Annual average: {np.mean(temperature):.1f}°C")
    print(f"Temperature volatility: {np.std(temperature):.1f}°C std")
    print()
    
    # Rainfall patterns
    print("💧 RAINFALL PATTERNS:")
    monthly_rains = [np.sum(rainfall[i*30:(i+1)*30]) for i in range(12)]
    wettest_month = np.argmax(monthly_rains)
    driest_month = np.argmin(monthly_rains)
    rainy_days = np.sum(rainfall > 1)
    
    print(f"Wettest month: {months[wettest_month]} ({monthly_rains[wettest_month]:.1f}mm)")
    print(f"Driest month: {months[driest_month]} ({monthly_rains[driest_month]:.1f}mm)")
    print(f"Annual total: {np.sum(rainfall):.1f}mm")
    print(f"Rainy days (>1mm): {rainy_days} days")
    print()
    
    # Rolling averages
    print("📈 ROLLING AVERAGES:")
    rolling_7 = np.convolve(temperature, np.ones(7)/7, mode='valid')
    rolling_30 = np.convolve(temperature, np.ones(30)/30, mode='valid')
    
    print(f"7-day moving avg temp: [{rolling_7[0]:.1f}, {rolling_7[1]:.1f}, "
          f"{rolling_7[2]:.1f}, {rolling_7[3]:.1f}, ...]")
    print(f"30-day moving avg temp: [{rolling_30[0]:.1f}, {rolling_30[1]:.1f}, "
          f"{rolling_30[2]:.1f}, {rolling_30[3]:.1f}, ...]")
    print()
    
    # Extreme weather events
    print("⚠️  EXTREME WEATHER EVENTS:")
    heatwave_days = np.sum(temperature > 35)
    cold_days = np.sum(temperature < 0)
    heavy_rain_days = np.sum(rainfall > 50)
    
    # Drought periods (consecutive dry days)
    dry_days = rainfall < 1
    drought_periods = 0
    current_drought = 0
    for is_dry in dry_days:
        if is_dry:
            current_drought += 1
        else:
            if current_drought > 21:
                drought_periods += 1
            current_drought = 0
    
    print(f"Heatwave days (>35°C): {heatwave_days} days")
    print(f"Cold snaps (<0°C): {cold_days} days")
    print(f"Heavy rain days (>50mm): {heavy_rain_days} days")
    print(f"Drought periods (>21 consecutive dry days): {drought_periods} periods")
    print()
    
    # Weather correlations
    print("🔗 WEATHER CORRELATIONS:")
    corr_matrix = np.corrcoef([temperature, humidity, rainfall])
    
    print(f"Temp-Humidity correlation: {corr_matrix[0, 1]:.2f}")
    print(f"Temp-Rainfall correlation: {corr_matrix[0, 2]:.2f}")
    print(f"Humidity-Rainfall correlation: {corr_matrix[1, 2]:.2f}")

if __name__ == "__main__":
    main()
