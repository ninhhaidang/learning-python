# =====================================
# Exercise 02: Pandas DataFrame - Week 4
# =====================================
# 
# Hướng dẫn:
# 1. Đọc đề bài trong file 1_problem.md
# 2. Viết code vào file này
# 3. Chạy và test chương trình của bạn
# 4. So sánh với đáp án trong 3_solution.py
#
# Bài tập: Phân tích dữ liệu ảnh vệ tinh, khí tượng và môi trường

import pandas as pd
import numpy as np

def exercise_1_satellite_analysis():
    """Bài 1: Phân tích dữ liệu ảnh vệ tinh Landsat"""
    print("Bài 1: Phân tích dữ liệu ảnh vệ tinh Landsat")
    print("-" * 50)
    
    # Dữ liệu pixel từ ảnh Landsat
    data = {
        'pixel_id': range(1, 21),
        'blue': [145, 180, 167, 156, 189, 134, 198, 123, 167, 145, 
                 178, 156, 134, 189, 167, 145, 178, 156, 134, 189],
        'green': [189, 234, 223, 198, 245, 167, 256, 156, 223, 189,
                  234, 198, 167, 245, 223, 189, 234, 198, 167, 245],
        'red': [134, 167, 156, 145, 178, 123, 189, 112, 156, 134,
                167, 145, 123, 178, 156, 134, 167, 145, 123, 178],
        'nir': [567, 890, 823, 634, 912, 456, 934, 389, 823, 567,
                890, 634, 456, 912, 823, 567, 890, 634, 456, 912],
        'latitude': [21.0285, 21.0290, 21.0295, 21.0300, 21.0305, 21.0310, 21.0315, 21.0320, 21.0325, 21.0330,
                    21.0335, 21.0340, 21.0345, 21.0350, 21.0355, 21.0360, 21.0365, 21.0370, 21.0375, 21.0380],
        'longitude': [105.8542, 105.8547, 105.8552, 105.8557, 105.8562, 105.8567, 105.8572, 105.8577, 105.8582, 105.8587,
                     105.8592, 105.8597, 105.8602, 105.8607, 105.8612, 105.8617, 105.8622, 105.8627, 105.8632, 105.8637]
    }
    
    # TODO: Tạo DataFrame từ dữ liệu trên
    df = None
    
    # TODO: Thêm cột Location (lat, lon)
    
    # TODO: Tính NDVI = (NIR - Red) / (NIR + Red)
    
    # TODO: Tạo cột phân loại Land Cover dựa trên NDVI
    # Water (<0), Bare Soil (0-0.2), Vegetation (0.2-0.8), Dense Vegetation (>0.8)
    
    # TODO: Thống kê số lượng pixel theo từng loại Land Cover
    
    # TODO: Tìm pixel có NDVI cao nhất và thấp nhất
    
    print("Complete Exercise 1!")


def exercise_2_weather_analysis():
    """Bài 2: Phân tích dữ liệu khí tượng theo vùng"""
    print("\nBài 2: Phân tích dữ liệu khí tượng theo vùng")
    print("-" * 50)
    
    # Dữ liệu khí tượng
    weather_data = {
        'station_name': ['Hà Nội', 'TP.HCM', 'Đà Nẵng', 'Hải Phòng', 'Cần Thơ', 
                        'Huế', 'Nha Trang', 'Đà Lạt', 'Vinh', 'Buôn Ma Thuột',
                        'Quy Nhon', 'Rạch Giá', 'Cà Mau', 'Sa Pa', 'Điện Biên'],
        'region': ['Bắc Bộ', 'Nam Bộ', 'Trung Bộ', 'Bắc Bộ', 'Nam Bộ',
                   'Trung Bộ', 'Trung Bộ', 'Tây Nguyên', 'Trung Bộ', 'Tây Nguyên',
                   'Trung Bộ', 'Nam Bộ', 'Nam Bộ', 'Bắc Bộ', 'Bắc Bộ'],
        'avg_temp': [23.6, 27.4, 25.8, 23.1, 27.0, 24.5, 26.2, 18.9, 24.2, 21.8,
                     26.4, 27.1, 26.8, 15.4, 21.5],
        'humidity': [79, 78, 81, 82, 83, 84, 76, 85, 85, 82, 77, 84, 86, 87, 81],
        'rainfall': [1678, 1949, 2505, 1943, 1635, 2815, 1361, 1804, 1956, 2391,
                     1878, 2034, 2153, 2539, 1764]
    }
    
    # TODO: Tạo DataFrame từ dữ liệu weather_data
    
    # TODO: Thêm cột phân loại khí hậu dựa trên nhiệt độ
    # Lạnh (<20°C), Mát (20-25°C), Ấm (25-30°C), Nóng (>30°C)
    
    # TODO: Tính trung bình nhiệt độ, độ ẩm, lượng mưa theo từng vùng
    
    # TODO: Tìm trạm có nhiệt độ cao nhất và thấp nhất
    
    # TODO: Lọc các trạm có lượng mưa trên 2000mm
    
    # TODO: Sắp xếp theo độ ẩm giảm dần
    
    print("Complete Exercise 2!")


def exercise_3_air_quality_analysis():
    """Bài 3: Quản lý dữ liệu điểm quan trắc môi trường"""
    print("\nBài 3: Quản lý dữ liệu điểm quan trắc môi trường")
    print("-" * 50)
    
    # TODO: Tạo dữ liệu mẫu cho 12 điểm quan trắc
    # Gồm: ID, tên địa điểm, quận/huyện, PM2.5, PM10, NO2, SO2, CO
    
    # TODO: Thêm cột đánh giá chất lượng không khí theo PM2.5
    # Tốt (<12), Trung bình (12-35), Kém (35-55), Rất kém (>55)
    
    # TODO: Tính trung bình các chỉ số ô nhiễm theo quận/huyện
    
    # TODO: Tìm điểm có chất lượng không khí tốt nhất và tệ nhất
    
    # TODO: Đếm số điểm quan trắc theo từng mức chất lượng
    
    # TODO: Lọc các điểm có PM10 vượt ngưỡng WHO (>20 μg/m³)
    
    print("Complete Exercise 3!")


def main():
    """Hàm main - điểm bắt đầu chương trình"""
    print("Exercise 02: Pandas DataFrame")
    print("=" * 50)
    
    # Chạy các bài tập
    exercise_1_satellite_analysis()
    exercise_2_weather_analysis()
    exercise_3_air_quality_analysis()
    
    print("\n" + "=" * 50)
    print("Hoàn thành tất cả bài tập!")
    print("Hãy kiểm tra kết quả và so sánh với solution.")


if __name__ == "__main__":
    main()
