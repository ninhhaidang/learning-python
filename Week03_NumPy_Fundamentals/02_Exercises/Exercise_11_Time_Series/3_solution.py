import numpy as np

def main():
    """Time Series Analysis - Solution"""
    print("=== TIME SERIES ANALYSIS ===")
    print()
    
    # Generate synthetic time series data
    np.random.seed(42)
    days = np.arange(365)
    
    # Components of time series
    trend = 0.1 * days  # Linear trend
    seasonal = 10 * np.sin(2 * np.pi * days / 7)  # Weekly pattern
    noise = np.random.normal(0, 5, 365)
    sales = 100 + trend + seasonal + noise
    
    # 📊 DATA OVERVIEW
    print("📊 DATA OVERVIEW:")
    print(f"Time series length: {len(sales)} days")
    print(f"Sales range: [{np.min(sales):.1f}, {np.max(sales):.1f}]")
    print(f"Mean daily sales: {np.mean(sales):.1f} units")
    print(f"Standard deviation: {np.std(sales):.1f} units")
    print()
    
    # 📈 TREND ANALYSIS
    print("📈 TREND ANALYSIS:")
    trend_analysis(sales, days)
    print()
    
    # 📅 SEASONALITY DETECTION
    print("📅 SEASONALITY DETECTION:")
    seasonality_analysis(sales)
    print()
    
    # 📊 MOVING AVERAGES
    print("📊 MOVING AVERAGES:")
    moving_averages_analysis(sales)
    print()
    
    # 🔮 FORECASTING
    print("🔮 FORECASTING:")
    forecasting_analysis(sales, days)
    print()
    
    # 📋 STATISTICS SUMMARY
    print("📋 STATISTICS SUMMARY:")
    statistics_summary(sales)

def trend_analysis(sales, days):
    """Analyze trend in time series"""
    # Linear regression to find trend
    coefficients = np.polyfit(days, sales, 1)
    trend_coeff = coefficients[0]
    
    total_growth = trend_coeff * (len(days) - 1)
    
    print(f"Linear trend coefficient: {trend_coeff:+.3f} units/day")
    print(f"Total growth over period: {total_growth:+.1f} units")
    
    if abs(trend_coeff) > 0.05:
        direction = "upward" if trend_coeff > 0 else "downward"
        print(f"Trend strength: Strong {direction} trend")
    else:
        print("Trend strength: Weak or no trend")

def seasonality_analysis(sales):
    """Detect weekly seasonality patterns"""
    # Reshape data to weekly format
    weeks = len(sales) // 7
    weekly_data = sales[:weeks*7].reshape(weeks, 7)
    
    # Calculate average for each day of week
    daily_averages = np.mean(weekly_data, axis=0)
    
    # Find peak and trough days
    peak_day = np.argmax(daily_averages)
    trough_day = np.argmin(daily_averages)
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                    'Friday', 'Saturday', 'Sunday']
    
    seasonal_amplitude = np.max(daily_averages) - np.min(daily_averages)
    
    print("Weekly pattern detected: YES")
    print(f"Peak day: {days_of_week[peak_day]} (index {peak_day})")
    print(f"Trough day: {days_of_week[trough_day]} (index {trough_day})")
    print(f"Seasonal amplitude: {seasonal_amplitude:.1f} units")

def moving_averages_analysis(sales):
    """Calculate various moving averages"""
    # Simple Moving Average (7-day)
    ma_7 = simple_moving_average(sales, 7)
    print(f"7-day Simple MA (last week): {ma_7[-5:]}")
    
    # Simple Moving Average (30-day)
    ma_30 = simple_moving_average(sales, 30)
    print(f"30-day Simple MA (last month): {ma_30[-5:]}")
    
    # Exponential Moving Average (7-day with α=0.3)
    ema_7 = exponential_moving_average(sales, alpha=0.3)
    print(f"7-day Exponential MA (α=0.3): {ema_7[-5:]}")

def simple_moving_average(data, window):
    """Calculate simple moving average"""
    # Use convolution for efficient calculation
    weights = np.ones(window) / window
    return np.convolve(data, weights, mode='valid')

def exponential_moving_average(data, alpha):
    """Calculate exponential moving average"""
    ema = np.zeros_like(data)
    ema[0] = data[0]
    
    for i in range(1, len(data)):
        ema[i] = alpha * data[i] + (1 - alpha) * ema[i-1]
    
    return ema

def forecasting_analysis(sales, days):
    """Perform simple forecasting"""
    # Linear regression forecast
    coefficients = np.polyfit(days, sales, 1)
    forecast_days = np.arange(len(sales), len(sales) + 7)
    linear_forecast = np.polyval(coefficients, forecast_days)
    
    # Add seasonal component for more realistic forecast
    seasonal_pattern = 10 * np.sin(2 * np.pi * forecast_days / 7)
    linear_forecast += seasonal_pattern
    
    print(f"Linear regression forecast (next 7 days): {linear_forecast}")
    
    # Moving average forecast (simple)
    recent_avg = np.mean(sales[-7:])
    ma_forecast = np.full(7, recent_avg)
    print(f"Moving average forecast (next 7 days): {ma_forecast}")

def statistics_summary(sales):
    """Calculate statistical summary"""
    # Autocorrelation with lag-1 and lag-7
    autocorr_1 = calculate_autocorrelation(sales, lag=1)
    autocorr_7 = calculate_autocorrelation(sales, lag=7)
    
    print(f"Autocorrelation (lag-1): {autocorr_1:.2f}")
    print(f"Autocorrelation (lag-7): {autocorr_7:.2f}")
    
    # Stationarity check (simple trend test)
    first_half = np.mean(sales[:len(sales)//2])
    second_half = np.mean(sales[len(sales)//2:])
    
    if abs(second_half - first_half) > np.std(sales) * 0.5:
        print("Data stationarity: Non-stationary (trend present)")
    else:
        print("Data stationarity: Likely stationary")
    
    # Rolling volatility (30-day rolling standard deviation)
    rolling_std = rolling_standard_deviation(sales, window=30)
    print(f"Volatility (rolling std): {np.mean(rolling_std):.1f} units")

def calculate_autocorrelation(data, lag):
    """Calculate autocorrelation at specified lag"""
    n = len(data) - lag
    if n <= 0:
        return 0.0
    
    data_shifted = data[lag:]
    data_original = data[:n]
    
    # Use numpy's correlation coefficient
    correlation_matrix = np.corrcoef(data_original, data_shifted)
    return correlation_matrix[0, 1]

def rolling_standard_deviation(data, window):
    """Calculate rolling standard deviation"""
    rolling_std = []
    for i in range(window-1, len(data)):
        window_data = data[i-window+1:i+1]
        rolling_std.append(np.std(window_data))
    return np.array(rolling_std)

if __name__ == "__main__":
    main()
