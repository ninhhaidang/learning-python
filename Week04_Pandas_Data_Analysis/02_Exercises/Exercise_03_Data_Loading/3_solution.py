"""
Exercise 03: Data Loading and I/O Operations - Solution
Week 4: Pandas Data Analysis
"""

import pandas as pd
import numpy as np
import json
import sqlite3
from io import StringIO
import os

def exercise_1_csv_processing():
    """Bài 1: Xử lý dữ liệu khí tượng từ file CSV - SOLUTION"""
    print("Bài 1: Xử lý dữ liệu khí tượng từ file CSV - SOLUTION")
    print("-" * 60)
    
    # Dữ liệu CSV mẫu
    csv_content = """Station;Date;Temperature(°C);Humidity(%);Rainfall(mm);Wind_Speed(m/s);Notes
Hà Nội;2024-01-15;18.5;82;0.0;3.2;Normal
TP.HCM;2024-01-15;27.8;76;5.2;2.1;
Đà Nẵng;2024-01-15;22.4;85;12.8;4.5;Windy
Hải Phòng;2024-01-15;N/A;79;0.0;2.8;Sensor error
Cần Thơ;2024-01-15;28.1;NULL;3.4;1.9;Humidity sensor down
Huế;2024-01-15;20.9;88;-999;3.7;Invalid rainfall data
Nha Trang;2024-01-15;25.6;74;0.0;5.2;Normal
Đà Lạt;2024-01-15;16.2;92;8.5;1.5;
Vinh;2024-01-15;19.8;83;2.1;3.0;Normal
Sa Pa;2024-01-15;12.4;95;15.2;2.3;Foggy"""
    
    # Đọc CSV với parameters phù hợp
    df = pd.read_csv(StringIO(csv_content), 
                     delimiter=';', 
                     na_values=['N/A', 'NULL', -999])
    
    print("1. Raw data:")
    print(df.head())
    print(f"\nShape: {df.shape}")
    
    # Xử lý missing values
    original_missing = df.isnull().sum()
    print(f"\n2. Missing values before cleaning:")
    print(original_missing[original_missing > 0])
    
    # Fill missing temperature với mean
    df['Temperature(°C)'].fillna(df['Temperature(°C)'].mean(), inplace=True)
    
    # Fill missing humidity với median
    df['Humidity(%)'].fillna(df['Humidity(%)'].median(), inplace=True)
    
    # Chuyển đổi kiểu dữ liệu
    df['Date'] = pd.to_datetime(df['Date'])
    df['Temperature(°C)'] = pd.to_numeric(df['Temperature(°C)'], errors='coerce')
    df['Humidity(%)'] = pd.to_numeric(df['Humidity(%)'], errors='coerce')
    df['Rainfall(mm)'] = pd.to_numeric(df['Rainfall(mm)'], errors='coerce')
    
    print(f"\n3. Data types after conversion:")
    print(df.dtypes)
    
    # Tạo báo cáo chất lượng dữ liệu
    total_records = len(df)
    missing_after = df.isnull().sum()
    complete_records = len(df.dropna())
    
    quality_report = f"""
Data Quality Report:
==================
Total records: {total_records}
Missing temperature: {original_missing['Temperature(°C)']} ({original_missing['Temperature(°C)']/total_records*100:.1f}%)
Missing humidity: {original_missing['Humidity(%)']} ({original_missing['Humidity(%)']/total_records*100:.1f}%)
Invalid rainfall: {original_missing['Rainfall(mm)']} ({original_missing['Rainfall(mm)']/total_records*100:.1f}%)
Complete records after cleaning: {complete_records} ({complete_records/total_records*100:.1f}%)
"""
    
    print(quality_report)
    
    # Lưu dữ liệu đã xử lý
    output_file = "weather_cleaned.csv"
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to: {output_file}")
    
    return df


def exercise_2_excel_processing():
    """Bài 2: Kết hợp dữ liệu từ nhiều sheet Excel - SOLUTION"""
    print("\nBài 2: Kết hợp dữ liệu từ nhiều sheet Excel - SOLUTION")
    print("-" * 60)
    
    # Simulate Excel data từ multiple sheets
    pm25_data = {
        'Station_ID': ['HN001', 'HCM001', 'DN001', 'HP001', 'CT001'],
        'Date': ['2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15'],
        'PM25_Value': [35.2, 42.8, 28.9, 33.4, 38.7],
        'Status': ['Valid', 'Valid', 'Valid', 'Valid', 'Valid']
    }
    
    pm10_data = {
        'Station_ID': ['HN001', 'HCM001', 'DN001', 'HP001', 'CT001'],
        'Date': ['2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15'],
        'PM10_Value': [58.4, 67.2, 44.6, 52.1, 59.8],
        'Status': ['Valid', 'Valid', 'Valid', 'Valid', 'Valid']
    }
    
    no2_data = {
        'Station_ID': ['HN001', 'HCM001', 'DN001', 'HP001', 'CT001'],
        'Date': ['2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15'],
        'NO2_Value': [28.5, 35.7, 21.8, 27.3, 30.2],
        'Status': ['Valid', 'Valid', 'Valid', 'Valid', 'Valid']
    }
    
    # Tạo DataFrame từ từng sheet
    pm25_df = pd.DataFrame(pm25_data)
    pm10_df = pd.DataFrame(pm10_data)
    no2_df = pd.DataFrame(no2_data)
    
    print("1. Individual DataFrames:")
    print("PM2.5 Data:")
    print(pm25_df)
    print("\nPM10 Data:")
    print(pm10_df)
    print("\nNO2 Data:")
    print(no2_df)
    
    # Kết hợp dữ liệu từ 3 DataFrame
    combined_df = pm25_df.merge(pm10_df, on=['Station_ID', 'Date'], suffixes=('_pm25', '_pm10'))
    combined_df = combined_df.merge(no2_df, on=['Station_ID', 'Date'])
    
    # Xử lý duplicate records (nếu có)
    combined_df = combined_df.drop_duplicates()
    
    print(f"\n2. Combined DataFrame:")
    print(combined_df)
    
    # Tính correlation matrix
    pollutant_cols = ['PM25_Value', 'PM10_Value', 'NO2_Value']
    correlation_matrix = combined_df[pollutant_cols].corr()
    
    print(f"\n3. Correlation Matrix:")
    print(correlation_matrix)
    
    # Export kết quả ra Excel với multiple sheets
    output_file = "air_quality_analysis.xlsx"
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        combined_df.to_excel(writer, sheet_name='Combined', index=False)
        correlation_matrix.to_excel(writer, sheet_name='Correlation')
        
        # Summary statistics
        summary_stats = combined_df[pollutant_cols].describe()
        summary_stats.to_excel(writer, sheet_name='Summary')
    
    print(f"Results exported to: {output_file}")
    print("Sheets: Combined, Correlation, Summary")
    
    return combined_df


def exercise_3_json_processing():
    """Bài 3: Xử lý dữ liệu JSON từ API response - SOLUTION"""
    print("\nBài 3: Xử lý dữ liệu JSON từ API response - SOLUTION")
    print("-" * 60)
    
    # JSON data mẫu (weather API response)
    json_data = {
        "locations": [
            {
                "id": "VN_HN_001",
                "name": "Hà Nội",
                "coordinates": {"lat": 21.0285, "lon": 105.8542},
                "observations": [
                    {
                        "timestamp": "2024-01-15T08:00:00Z",
                        "weather": {
                            "temperature": 18.5,
                            "humidity": 82,
                            "pressure": 1013.2,
                            "wind": {"speed": 3.2, "direction": 45}
                        },
                        "air_quality": {
                            "pm25": 35.2,
                            "pm10": 58.4,
                            "no2": 28.5,
                            "aqi": 89
                        }
                    },
                    {
                        "timestamp": "2024-01-15T12:00:00Z",
                        "weather": {
                            "temperature": 22.1,
                            "humidity": 75,
                            "pressure": 1012.8,
                            "wind": {"speed": 2.8, "direction": 50}
                        },
                        "air_quality": {
                            "pm25": 38.7,
                            "pm10": 62.1,
                            "no2": 31.2,
                            "aqi": 95
                        }
                    }
                ]
            },
            {
                "id": "VN_HCM_001",
                "name": "TP.HCM",
                "coordinates": {"lat": 10.8231, "lon": 106.6297},
                "observations": [
                    {
                        "timestamp": "2024-01-15T08:00:00Z",
                        "weather": {
                            "temperature": 27.8,
                            "humidity": 76,
                            "pressure": 1011.5,
                            "wind": {"speed": 2.1, "direction": 120}
                        },
                        "air_quality": {
                            "pm25": 42.8,
                            "pm10": 67.2,
                            "no2": 35.7,
                            "aqi": 105
                        }
                    }
                ]
            }
        ]
    }
    
    print("1. Original JSON structure:")
    print(f"Locations: {len(json_data['locations'])}")
    for loc in json_data['locations']:
        print(f"  {loc['name']}: {len(loc['observations'])} observations")
    
    # Parse JSON và normalize nested structure
    df_normalized = pd.json_normalize(
        json_data['locations'],
        record_path=['observations'],
        meta=['id', 'name', ['coordinates', 'lat'], ['coordinates', 'lon']],
        meta_prefix='location_'
    )
    
    print(f"\n2. Normalized DataFrame:")
    print(df_normalized.head())
    print(f"Shape: {df_normalized.shape}")
    
    # Xử lý timestamp
    df_normalized['timestamp'] = pd.to_datetime(df_normalized['timestamp'])
    df_normalized['hour'] = df_normalized['timestamp'].dt.hour
    df_normalized['date'] = df_normalized['timestamp'].dt.date
    
    # Tách dữ liệu weather và air_quality
    weather_cols = ['location_id', 'location_name', 'timestamp', 'weather.temperature', 
                   'weather.humidity', 'weather.pressure', 'weather.wind.speed', 'weather.wind.direction']
    weather_df = df_normalized[weather_cols].copy()
    weather_df.columns = ['station_id', 'station_name', 'timestamp', 'temperature', 
                         'humidity', 'pressure', 'wind_speed', 'wind_direction']
    
    air_quality_cols = ['location_id', 'location_name', 'timestamp', 'air_quality.pm25',
                       'air_quality.pm10', 'air_quality.no2', 'air_quality.aqi']
    air_quality_df = df_normalized[air_quality_cols].copy()
    air_quality_df.columns = ['station_id', 'station_name', 'timestamp', 'pm25', 'pm10', 'no2', 'aqi']
    
    print(f"\n3. Weather DataFrame:")
    print(weather_df)
    
    print(f"\n4. Air Quality DataFrame:")
    print(air_quality_df)
    
    # Aggregate dữ liệu theo time period (hourly averages)
    hourly_weather = weather_df.groupby(['station_id', df_normalized['timestamp'].dt.hour]).agg({
        'temperature': 'mean',
        'humidity': 'mean',
        'pressure': 'mean',
        'wind_speed': 'mean'
    }).round(1)
    
    print(f"\n5. Hourly weather averages:")
    print(hourly_weather)
    
    # Save processed data to multiple formats
    weather_df.to_csv("weather_data.csv", index=False)
    air_quality_df.to_json("air_quality_data.json", orient='records', date_format='iso')
    
    # Combined data to parquet (if possible)
    try:
        combined_json = df_normalized.drop(['weather.wind.speed', 'weather.wind.direction'], axis=1, errors='ignore')
        combined_json.to_parquet("combined_data.parquet", index=False)
        print("Data saved to: weather_data.csv, air_quality_data.json, combined_data.parquet")
    except:
        print("Data saved to: weather_data.csv, air_quality_data.json")
    
    return df_normalized


def exercise_4_database_operations():
    """Bài 4: Tạo và quản lý database connection - SOLUTION"""
    print("\nBài 4: Tạo và quản lý database connection - SOLUTION")
    print("-" * 60)
    
    # Tạo SQLite database
    db_name = "weather_database.db"
    conn = sqlite3.connect(db_name)
    
    try:
        # Tạo tables
        conn.execute('''
        CREATE TABLE IF NOT EXISTS weather_stations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_code TEXT UNIQUE,
            name TEXT,
            latitude REAL,
            longitude REAL,
            elevation REAL,
            region TEXT
        )
        ''')
        
        conn.execute('''
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_id INTEGER,
            observation_date DATE,
            temperature REAL,
            humidity REAL,
            rainfall REAL,
            wind_speed REAL,
            FOREIGN KEY (station_id) REFERENCES weather_stations (id)
        )
        ''')
        
        print("1. Database tables created successfully")
        
        # Tạo sample data
        stations_data = {
            'station_code': ['HN001', 'HCM001', 'DN001', 'HP001'],
            'name': ['Hà Nội', 'TP.HCM', 'Đà Nẵng', 'Hải Phòng'],
            'latitude': [21.0285, 10.8231, 16.0544, 20.8449],
            'longitude': [105.8542, 106.6297, 108.2022, 106.6881],
            'elevation': [16, 5, 10, 3],
            'region': ['Bắc Bộ', 'Nam Bộ', 'Trung Bộ', 'Bắc Bộ']
        }
        
        observations_data = {
            'station_id': [1, 1, 2, 2, 3, 3, 4, 4],
            'observation_date': ['2024-01-15', '2024-01-16', '2024-01-15', '2024-01-16',
                                '2024-01-15', '2024-01-16', '2024-01-15', '2024-01-16'],
            'temperature': [18.5, 19.2, 27.8, 28.1, 22.4, 23.1, 20.1, 19.8],
            'humidity': [82, 80, 76, 78, 85, 83, 84, 86],
            'rainfall': [0.0, 2.1, 5.2, 3.8, 12.8, 8.5, 0.0, 1.2],
            'wind_speed': [3.2, 2.8, 2.1, 2.5, 4.5, 3.9, 2.8, 3.1]
        }
        
        # Import DataFrames vào database
        stations_df = pd.DataFrame(stations_data)
        observations_df = pd.DataFrame(observations_data)
        
        stations_df.to_sql('weather_stations', conn, if_exists='replace', index=False)
        observations_df.to_sql('observations', conn, if_exists='append', index=False)
        
        print("2. Sample data imported successfully")
        
        # Thực hiện SQL queries để phân tích
        print("\n3. Analysis Queries:")
        
        # Trung bình nhiệt độ theo vùng
        query1 = """
        SELECT ws.region, AVG(o.temperature) as avg_temp, COUNT(*) as num_observations
        FROM weather_stations ws
        JOIN observations o ON ws.id = o.station_id
        GROUP BY ws.region
        ORDER BY avg_temp DESC
        """
        
        region_temps = pd.read_sql_query(query1, conn)
        print("\nAverage temperature by region:")
        print(region_temps)
        
        # Trạm có lượng mưa cao nhất
        query2 = """
        SELECT ws.name, ws.region, AVG(o.rainfall) as avg_rainfall
        FROM weather_stations ws
        JOIN observations o ON ws.id = o.station_id
        GROUP BY ws.id, ws.name, ws.region
        ORDER BY avg_rainfall DESC
        LIMIT 3
        """
        
        top_rainfall = pd.read_sql_query(query2, conn)
        print("\nTop 3 stations with highest rainfall:")
        print(top_rainfall)
        
        # Observations trong khoảng thời gian
        query3 = """
        SELECT ws.name, o.observation_date, o.temperature, o.humidity, o.rainfall
        FROM weather_stations ws
        JOIN observations o ON ws.id = o.station_id
        WHERE o.observation_date BETWEEN '2024-01-15' AND '2024-01-16'
        ORDER BY ws.name, o.observation_date
        """
        
        time_range_data = pd.read_sql_query(query3, conn)
        print(f"\nObservations in date range:")
        print(time_range_data)
        
        # Export query results
        region_temps.to_csv("region_temperature_analysis.csv", index=False)
        top_rainfall.to_csv("top_rainfall_stations.csv", index=False)
        time_range_data.to_csv("observations_timerange.csv", index=False)
        
        print("\n4. Query results exported to CSV files")
        
        # Tạo backup database
        backup_query = "SELECT * FROM weather_stations"
        stations_backup = pd.read_sql_query(backup_query, conn)
        stations_backup.to_csv("stations_backup.csv", index=False)
        
        backup_query2 = "SELECT * FROM observations"
        observations_backup = pd.read_sql_query(backup_query2, conn)
        observations_backup.to_csv("observations_backup.csv", index=False)
        
        print("5. Database backup created: stations_backup.csv, observations_backup.csv")
        
        return time_range_data
        
    finally:
        conn.close()
        print(f"Database connection closed: {db_name}")


def main():
    """Hàm main - chạy tất cả solutions"""
    print("Exercise 03: Data Loading and I/O Operations - SOLUTIONS")
    print("=" * 70)
    
    # Chạy tất cả bài tập solutions
    try:
        df1 = exercise_1_csv_processing()
        df2 = exercise_2_excel_processing()
        df3 = exercise_3_json_processing()
        df4 = exercise_4_database_operations()
        
        print("\n" + "=" * 70)
        print("SUMMARY:")
        print(f"- Bài 1: Processed {len(df1)} weather records from CSV")
        print(f"- Bài 2: Combined {len(df2)} air quality measurements from Excel")
        print(f"- Bài 3: Normalized {len(df3)} observations from JSON API")
        print(f"- Bài 4: Queried {len(df4)} records from SQLite database")
        print("\nAll data loading exercises completed successfully!")
        print("Check generated files for outputs.")
        
    except Exception as e:
        print(f"Error during execution: {str(e)}")
        raise


if __name__ == "__main__":
    main()
