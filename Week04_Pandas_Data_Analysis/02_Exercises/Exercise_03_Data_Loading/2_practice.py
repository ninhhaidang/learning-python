# =====================================
# Exercise 03: Data Loading - Week 4
# =====================================
# 
# Hướng dẫn:
# 1. Đọc đề bài trong file 1_problem.md
# 2. Viết code vào file này
# 3. Chạy và test chương trình của bạn
# 4. So sánh với đáp án trong 3_solution.py
#
# Bài tập: Xử lý dữ liệu từ CSV, Excel, JSON và Database

import pandas as pd
import numpy as np
import json
import sqlite3
from io import StringIO

def exercise_1_csv_processing():
    """Bài 1: Xử lý dữ liệu khí tượng từ file CSV"""
    print("Bài 1: Xử lý dữ liệu khí tượng từ file CSV")
    print("-" * 50)
    
    # Dữ liệu CSV mẫu (simulate file content)
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
    
    # TODO: Đọc CSV với parameters phù hợp (delimiter, na_values)
    # Hint: Sử dụng StringIO để simulate file reading
    
    # TODO: Xử lý missing values và dữ liệu không hợp lệ
    # - Thay thế N/A, NULL, -999 bằng NaN
    # - Fill missing temperature với mean
    # - Fill missing humidity với median
    
    # TODO: Chuyển đổi kiểu dữ liệu
    # - Date thành datetime
    # - Các cột số thành numeric
    
    # TODO: Tạo báo cáo chất lượng dữ liệu
    # - Tổng số records
    # - Số missing values mỗi cột
    # - Phần trăm complete records
    
    # TODO: Lưu dữ liệu đã xử lý ra file CSV mới
    
    print("Complete Exercise 1!")


def exercise_2_excel_processing():
    """Bài 2: Kết hợp dữ liệu từ nhiều sheet Excel"""
    print("\nBài 2: Kết hợp dữ liệu từ nhiều sheet Excel")
    print("-" * 50)
    
    # Simulate Excel data from multiple sheets
    # Sheet PM25 data
    pm25_data = {
        'Station_ID': ['HN001', 'HCM001', 'DN001', 'HP001', 'CT001'],
        'Date': ['2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15'],
        'PM25_Value': [35.2, 42.8, 28.9, 33.4, 38.7],
        'Status': ['Valid', 'Valid', 'Valid', 'Valid', 'Valid']
    }
    
    # Sheet PM10 data  
    pm10_data = {
        'Station_ID': ['HN001', 'HCM001', 'DN001', 'HP001', 'CT001'],
        'Date': ['2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15'],
        'PM10_Value': [58.4, 67.2, 44.6, 52.1, 59.8],
        'Status': ['Valid', 'Valid', 'Valid', 'Valid', 'Valid']
    }
    
    # Sheet NO2 data
    no2_data = {
        'Station_ID': ['HN001', 'HCM001', 'DN001', 'HP001', 'CT001'], 
        'Date': ['2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15', '2024-01-15'],
        'NO2_Value': [28.5, 35.7, 21.8, 27.3, 30.2],
        'Status': ['Valid', 'Valid', 'Valid', 'Valid', 'Valid']
    }
    
    # TODO: Tạo DataFrame từ từng sheet data
    
    # TODO: Kết hợp dữ liệu từ 3 DataFrame thành 1
    # Hint: Sử dụng merge() hoặc join()
    
    # TODO: Xử lý duplicate records nếu có
    
    # TODO: Tính correlation matrix giữa PM25, PM10, NO2
    
    # TODO: Export kết quả ra file Excel với multiple sheets
    # - Sheet 'Combined': dữ liệu kết hợp
    # - Sheet 'Correlation': correlation matrix
    # - Sheet 'Summary': thống kê tóm tắt
    
    print("Complete Exercise 2!")


def exercise_3_json_processing():
    """Bài 3: Xử lý dữ liệu JSON từ API response"""
    print("\nBài 3: Xử lý dữ liệu JSON từ API response")
    print("-" * 50)
    
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
    
    # TODO: Parse JSON data và normalize nested structure
    # Hint: Sử dụng pd.json_normalize()
    
    # TODO: Xử lý timestamp (convert to datetime, handle timezone)
    
    # TODO: Tách dữ liệu weather và air_quality thành separate DataFrames
    
    # TODO: Lọc và aggregate dữ liệu theo time period
    
    # TODO: Save processed data sang multiple formats
    # - CSV: weather data
    # - JSON: air quality data
    # - Parquet: combined data (if possible)
    
    print("Complete Exercise 3!")


def exercise_4_database_operations():
    """Bài 4: Tạo và quản lý database connection"""
    print("\nBài 4: Tạo và quản lý database connection")
    print("-" * 50)
    
    # TODO: Tạo SQLite database và tables
    # Schema: weather_stations, observations
    
    # TODO: Tạo sample data
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
    
    # TODO: Import DataFrames vào database
    
    # TODO: Thực hiện SQL queries để phân tích
    # - Trung bình nhiệt độ theo vùng
    # - Trạm có lượng mưa cao nhất
    # - Observations trong khoảng thời gian
    
    # TODO: Export query results thành các file khác nhau
    
    # TODO: Tạo backup database (export to CSV)
    
    print("Complete Exercise 4!")


def main():
    """Hàm main - điểm bắt đầu chương trình"""
    print("Exercise 03: Data Loading and I/O Operations")
    print("=" * 60)
    
    # Chạy các bài tập
    exercise_1_csv_processing()
    exercise_2_excel_processing() 
    exercise_3_json_processing()
    exercise_4_database_operations()
    
    print("\n" + "=" * 60)
    print("Hoàn thành tất cả bài tập!")
    print("Hãy kiểm tra kết quả và so sánh với solution.")


if __name__ == "__main__":
    main()
