# =====================================
# Exercise 04: Data Analysis - Week 4
# =====================================
# 
# Hướng dẫn:
# 1. Đọc đề bài trong file 1_problem.md
# 2. Viết code vào file này
# 3. Chạy và test chương trình của bạn
# 4. So sánh với đáp án trong 3_solution.py
#
# Bài tập: Advanced Data Analysis với Pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def exercise_1_climate_trend_analysis():
    """Bài 1: Phân tích xu hướng biến đổi khí hậu"""
    print("Bài 1: Phân tích xu hướng biến đổi khí hậu")
    print("-" * 50)
    
    # Tạo dữ liệu time series mẫu
    years = range(1990, 2024)
    regions = ['Bắc Bộ', 'Trung Bộ', 'Nam Bộ', 'Tây Nguyên']
    
    # TODO: Tạo DataFrame với climate data
    # Gồm: year, region, avg_temperature, total_rainfall, extreme_events
    
    # TODO: Phân tích xu hướng nhiệt độ trung bình theo năm (1990-2023)
    
    # TODO: Tính moving average 5 năm và 10 năm
    
    # TODO: Xác định các năm có nhiệt độ extreme (cao nhất, thấp nhất)
    
    # TODO: So sánh xu hướng giữa các vùng miền
    
    # TODO: Tính correlation giữa nhiệt độ và lượng mưa
    
    # TODO: Detect anomaly patterns trong dữ liệu
    
    print("Complete Exercise 1!")


def exercise_2_air_quality_time_series():
    """Bài 2: Phân tích chất lượng không khí theo thời gian"""
    print("\nBài 2: Phân tích chất lượng không khí theo thời gian")
    print("-" * 50)
    
    # TODO: Tạo time series với dữ liệu hourly PM2.5, PM10, NO2
    # Date range: 6 tháng, hourly data
    
    # TODO: Phân tích patterns theo giờ trong ngày và ngày trong tuần
    
    # TODO: Tính rolling statistics (mean, std, percentiles)
    
    # TODO: Identify peak pollution periods
    
    # TODO: Compare weekday vs weekend patterns
    
    # TODO: Seasonal decomposition của time series
    
    print("Complete Exercise 2!")


def exercise_3_ndvi_analysis():
    """Bài 3: Phân tích dữ liệu NDVI từ ảnh vệ tinh"""
    print("\nBài 3: Phân tích dữ liệu NDVI từ ảnh vệ tinh")
    print("-" * 50)
    
    # TODO: Tạo monthly NDVI data cho các loại land cover
    # Land covers: Forest, Cropland, Urban, Water, Grassland
    # Protected status: Protected, Non-protected
    
    # TODO: Tính NDVI trung bình theo tháng cho từng loại land cover
    
    # TODO: Phân tích seasonal patterns của vegetation
    
    # TODO: Detect deforestation events (NDVI drops significantly)
    
    # TODO: Compare NDVI trends between protected và non-protected areas
    
    # TODO: Calculate vegetation recovery rate after disturbances
    
    # TODO: Create vegetation health index
    
    print("Complete Exercise 3!")


def exercise_4_socio_economic_analysis():
    """Bài 4: Phân tích kinh tế-xã hội từ dữ liệu không gian"""
    print("\nBài 4: Phân tích kinh tế-xã hội từ dữ liệu không gian")
    print("-" * 50)
    
    # TODO: Tạo socio-economic data cho 15 tỉnh thành
    # Gồm: province, gdp_per_capita, population, urban_rate, pm25_avg, forest_cover, water_quality_index
    
    # TODO: Phân tích correlation giữa GDP, dân số và ô nhiễm
    
    # TODO: Clustering các tỉnh thành theo đặc điểm kinh tế-môi trường
    
    # TODO: Tính Environmental Kuznets Curve
    
    # TODO: Predict pollution levels based on economic indicators
    
    # TODO: Identify outliers và investigate causes
    
    # TODO: Create composite sustainability index
    
    print("Complete Exercise 4!")


def main():
    """Hàm main - điểm bắt đầu chương trình"""
    print("Exercise 04: Data Analysis with Pandas")
    print("=" * 60)
    
    # Chạy các bài tập
    exercise_1_climate_trend_analysis()
    exercise_2_air_quality_time_series()
    exercise_3_ndvi_analysis()
    exercise_4_socio_economic_analysis()
    
    print("\n" + "=" * 60)
    print("Hoàn thành tất cả bài tập!")
    print("Hãy kiểm tra kết quả và so sánh với solution.")


if __name__ == "__main__":
    main()
