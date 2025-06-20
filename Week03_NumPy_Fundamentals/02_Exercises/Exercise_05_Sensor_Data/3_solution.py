import numpy as np

def main():
    """Sensor Data Processing với NumPy"""
    print("=== SENSOR DATA PROCESSING ===")
    print()
    
    # Generate sensor data (5 sensors x 24 hours)
    np.random.seed(42)
    n_sensors = 5
    n_hours = 24
    
    # Create realistic sensor data with some missing values
    base_temps = np.random.uniform(20, 30, (n_sensors, n_hours))
    noise = np.random.normal(0, 2, (n_sensors, n_hours))
    sensor_data = base_temps + noise
    
    # Introduce some missing values (NaN)
    missing_indices = np.random.choice(n_sensors * n_hours, size=8, replace=False)
    flat_data = sensor_data.flatten()
    flat_data[missing_indices] = np.nan
    sensor_data = flat_data.reshape(n_sensors, n_hours)
    
    print("📊 DATASET OVERVIEW:")
    print(f"Sensors: {n_sensors}")
    print(f"Time periods: {n_hours} hours")
    print(f"Missing values: {np.sum(np.isnan(sensor_data))}/{sensor_data.size}")
    print()
    
    # Display sample data
    print("Sensor data sample (first 8 hours):")
    for i in range(n_sensors):
        row_sample = sensor_data[i, :8]
        print(f"Sensor_{i+1}: {np.round(row_sample, 1)}")
    print()
    
    # Handle missing values
    print("🔧 MISSING VALUES HANDLING:")
    # Method 1: Forward fill
    sensor_data_filled = sensor_data.copy()
    for i in range(n_sensors):
        for j in range(n_hours):
            if np.isnan(sensor_data_filled[i, j]) and j > 0:
                sensor_data_filled[i, j] = sensor_data_filled[i, j-1]
    
    missing_before = np.sum(np.isnan(sensor_data))
    missing_after = np.sum(np.isnan(sensor_data_filled))
    
    print(f"Missing values before: {missing_before}")
    print(f"Missing values after forward fill: {missing_after}")
    print()
    
    # Rolling statistics
    print("📈 ROLLING STATISTICS:")
    window_size = 3
    
    # Calculate 3-hour moving average for each sensor
    rolling_avg = np.full_like(sensor_data_filled, np.nan)
    for i in range(n_sensors):
        for j in range(window_size-1, n_hours):
            window = sensor_data_filled[i, j-window_size+1:j+1]
            if not np.any(np.isnan(window)):
                rolling_avg[i, j] = np.mean(window)
    
    print(f"3-hour moving average (last 8 hours):")
    for i in range(n_sensors):
        row_sample = rolling_avg[i, -8:]
        print(f"Sensor_{i+1}: {np.round(row_sample, 1)}")
    print()
    
    # Outlier detection
    print("⚠️  OUTLIER DETECTION:")
    # Define outliers as values > 2 standard deviations from mean
    for i in range(n_sensors):
        sensor_values = sensor_data_filled[i]
        valid_values = sensor_values[~np.isnan(sensor_values)]
        
        if len(valid_values) > 0:
            mean_val = np.mean(valid_values)
            std_val = np.std(valid_values)
            threshold = 2 * std_val
            
            outliers = np.abs(valid_values - mean_val) > threshold
            outlier_count = np.sum(outliers)
            
            print(f"Sensor_{i+1}: {outlier_count} outliers detected")
    print()
    
    # Sensor correlations
    print("🔗 SENSOR CORRELATIONS:")
    # Create correlation matrix (excluding NaN values)
    valid_data = []
    for i in range(n_sensors):
        sensor_values = sensor_data_filled[i]
        valid_values = sensor_values[~np.isnan(sensor_values)]
        if len(valid_values) == n_hours:  # Only use sensors with complete data
            valid_data.append(valid_values)
    
    if len(valid_data) >= 2:
        corr_matrix = np.corrcoef(valid_data)
        print("Correlation matrix:")
        print(np.round(corr_matrix, 2))
    else:
        print("Insufficient data for correlation analysis")
    print()
    
    # Summary statistics
    print("📊 SUMMARY STATISTICS:")
    overall_mean = np.nanmean(sensor_data_filled)
    overall_std = np.nanstd(sensor_data_filled)
    overall_min = np.nanmin(sensor_data_filled)
    overall_max = np.nanmax(sensor_data_filled)
    
    print(f"Overall mean temperature: {overall_mean:.1f}°C")
    print(f"Overall std deviation: {overall_std:.1f}°C")
    print(f"Temperature range: {overall_min:.1f}°C to {overall_max:.1f}°C")
    
    # Per-sensor statistics
    print()
    print("Per-sensor statistics:")
    for i in range(n_sensors):
        sensor_values = sensor_data_filled[i]
        valid_values = sensor_values[~np.isnan(sensor_values)]
        
        if len(valid_values) > 0:
            sensor_mean = np.mean(valid_values)
            sensor_std = np.std(valid_values)
            print(f"Sensor_{i+1}: Mean {sensor_mean:.1f}°C, Std {sensor_std:.1f}°C")

if __name__ == "__main__":
    main()
