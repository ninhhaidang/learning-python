"""
Exercise 02: Pandas DataFrame - Solution
Week 4: Pandas Data Analysis
"""

import pandas as pd
import numpy as np

def exercise_1_satellite_analysis():
    """Bài 1: Phân tích dữ liệu ảnh vệ tinh Landsat - SOLUTION"""
    print("Bài 1: Phân tích dữ liệu ảnh vệ tinh Landsat - SOLUTION")
    print("-" * 60)
    
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
    
    # 1. Tạo DataFrame từ dữ liệu
    df = pd.DataFrame(data)
    print("1. DataFrame được tạo với shape:", df.shape)
    print(df.head())
    
    # 2. Thêm cột Location
    df['location'] = df.apply(lambda row: f"({row['latitude']:.4f}, {row['longitude']:.4f})", axis=1)
    print("\n2. Đã thêm cột Location")
    
    # 3. Tính NDVI
    df['ndvi'] = (df['nir'] - df['red']) / (df['nir'] + df['red'])
    print("\n3. Đã tính NDVI")
    print(f"NDVI trung bình: {df['ndvi'].mean():.3f}")
    print(f"NDVI min: {df['ndvi'].min():.3f}, max: {df['ndvi'].max():.3f}")
    
    # 4. Phân loại Land Cover
    def classify_land_cover(ndvi):
        if ndvi < 0:
            return 'Water'
        elif ndvi < 0.2:
            return 'Bare Soil'
        elif ndvi < 0.8:
            return 'Vegetation'
        else:
            return 'Dense Vegetation'
    
    df['land_cover'] = df['ndvi'].apply(classify_land_cover)
    print("\n4. Đã phân loại Land Cover")
    
    # 5. Thống kê số lượng pixel theo loại Land Cover
    land_cover_stats = df['land_cover'].value_counts()
    print("\n5. Thống kê Land Cover:")
    for cover_type, count in land_cover_stats.items():
        print(f"   {cover_type}: {count} pixels ({count/len(df)*100:.1f}%)")
    
    # 6. Tìm pixel có NDVI cao nhất và thấp nhất
    max_ndvi_idx = df['ndvi'].idxmax()
    min_ndvi_idx = df['ndvi'].idxmin()
    
    print(f"\n6. Pixel có NDVI cao nhất:")
    print(f"   Pixel ID: {df.loc[max_ndvi_idx, 'pixel_id']}")
    print(f"   NDVI: {df.loc[max_ndvi_idx, 'ndvi']:.3f}")
    print(f"   Location: {df.loc[max_ndvi_idx, 'location']}")
    print(f"   Land Cover: {df.loc[max_ndvi_idx, 'land_cover']}")
    
    print(f"\n   Pixel có NDVI thấp nhất:")
    print(f"   Pixel ID: {df.loc[min_ndvi_idx, 'pixel_id']}")
    print(f"   NDVI: {df.loc[min_ndvi_idx, 'ndvi']:.3f}")
    print(f"   Location: {df.loc[min_ndvi_idx, 'location']}")
    print(f"   Land Cover: {df.loc[min_ndvi_idx, 'land_cover']}")
    
    return df


def exercise_2_weather_analysis():
    """Bài 2: Phân tích dữ liệu khí tượng theo vùng - SOLUTION"""
    print("\n" + "="*60)
    print("Bài 2: Phân tích dữ liệu khí tượng theo vùng - SOLUTION")
    print("-" * 60)
    
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
    
    # 1. Tạo DataFrame
    df = pd.DataFrame(weather_data)
    print("1. DataFrame khí tượng:")
    print(df.head())
    
    # 2. Phân loại khí hậu
    def classify_climate(temp):
        if temp < 20:
            return 'Lạnh'
        elif temp < 25:
            return 'Mát'
        elif temp < 30:
            return 'Ấm'
        else:
            return 'Nóng'
    
    df['climate_type'] = df['avg_temp'].apply(classify_climate)
    print("\n2. Phân loại khí hậu:")
    climate_stats = df['climate_type'].value_counts()
    for climate, count in climate_stats.items():
        print(f"   {climate}: {count} trạm")
    
    # 3. Trung bình theo vùng
    region_stats = df.groupby('region').agg({
        'avg_temp': 'mean',
        'humidity': 'mean', 
        'rainfall': 'mean'
    }).round(1)
    
    print("\n3. Trung bình theo vùng:")
    print(region_stats)
    
    # 4. Trạm có nhiệt độ cao nhất và thấp nhất
    max_temp_station = df.loc[df['avg_temp'].idxmax()]
    min_temp_station = df.loc[df['avg_temp'].idxmin()]
    
    print(f"\n4. Nhiệt độ extreme:")
    print(f"   Cao nhất: {max_temp_station['station_name']} ({max_temp_station['avg_temp']}°C)")
    print(f"   Thấp nhất: {min_temp_station['station_name']} ({min_temp_station['avg_temp']}°C)")
    
    # 5. Lọc trạm có lượng mưa > 2000mm
    high_rainfall = df[df['rainfall'] > 2000]
    print(f"\n5. Trạm có lượng mưa > 2000mm ({len(high_rainfall)} trạm):")
    for _, station in high_rainfall.iterrows():
        print(f"   {station['station_name']}: {station['rainfall']}mm")
    
    # 6. Sắp xếp theo độ ẩm giảm dần
    df_sorted = df.sort_values('humidity', ascending=False)
    print(f"\n6. Top 5 trạm có độ ẩm cao nhất:")
    for i, (_, row) in enumerate(df_sorted.head().iterrows()):
        print(f"   {i+1}. {row['station_name']}: {row['humidity']}%")
    
    return df


def exercise_3_air_quality_analysis():
    """Bài 3: Quản lý dữ liệu điểm quan trắc môi trường - SOLUTION"""
    print("\n" + "="*60)
    print("Bài 3: Quản lý dữ liệu điểm quan trắc môi trường - SOLUTION")
    print("-" * 60)
    
    # 1. Tạo dữ liệu mẫu cho 12 điểm quan trắc
    air_quality_data = {
        'monitoring_id': [f'AQ{i:03d}' for i in range(1, 13)],
        'location_name': ['Hoàn Kiếm', 'Ba Đình', 'Đống Đa', 'Hai Bà Trưng', 
                         'Quận 1', 'Quận 3', 'Quận 7', 'Thủ Đức',
                         'Hải Châu', 'Sơn Trà', 'Cẩm Lệ', 'Ngũ Hành Sơn'],
        'district': ['Hoàn Kiếm', 'Ba Đình', 'Đống Đa', 'Hai Bà Trưng',
                    'Quận 1', 'Quận 3', 'Quận 7', 'Thủ Đức', 
                    'Hải Châu', 'Sơn Trà', 'Cẩm Lệ', 'Ngũ Hành Sơn'],
        'pm2_5': [45.2, 38.7, 52.3, 41.8, 67.2, 43.5, 29.8, 35.2, 
                  33.4, 28.9, 40.1, 31.7],
        'pm10': [68.5, 59.2, 78.9, 64.3, 89.7, 66.8, 45.2, 54.8,
                 52.1, 44.6, 61.7, 49.3],
        'no2': [34.8, 29.5, 41.2, 33.7, 52.3, 35.9, 22.4, 28.6,
                27.3, 21.8, 32.5, 25.9],
        'so2': [15.2, 12.8, 18.7, 14.3, 23.4, 16.1, 9.8, 13.5,
                12.9, 10.2, 15.8, 11.6],
        'co': [1.8, 1.5, 2.3, 1.9, 3.2, 2.1, 1.2, 1.7,
               1.6, 1.1, 1.9, 1.4]
    }
    
    df = pd.DataFrame(air_quality_data)
    print("1. DataFrame điểm quan trắc môi trường:")
    print(df.head())
    
    # 2. Đánh giá chất lượng không khí theo PM2.5
    def classify_air_quality(pm25):
        if pm25 < 12:
            return 'Tốt'
        elif pm25 < 35:
            return 'Trung bình'
        elif pm25 < 55:
            return 'Kém'
        else:
            return 'Rất kém'
    
    df['air_quality'] = df['pm2_5'].apply(classify_air_quality)
    print("\n2. Phân loại chất lượng không khí:")
    air_quality_stats = df['air_quality'].value_counts()
    for quality, count in air_quality_stats.items():
        print(f"   {quality}: {count} điểm")
    
    # 3. Trung bình theo quận/huyện (group by district)
    district_stats = df.groupby('district').agg({
        'pm2_5': 'mean',
        'pm10': 'mean',
        'no2': 'mean',
        'so2': 'mean',
        'co': 'mean'
    }).round(1)
    
    print("\n3. Trung bình các chỉ số theo quận/huyện:")
    print(district_stats.head())
    
    # 4. Điểm có chất lượng không khí tốt nhất và tệ nhất
    best_station = df.loc[df['pm2_5'].idxmin()]
    worst_station = df.loc[df['pm2_5'].idxmax()]
    
    print(f"\n4. Chất lượng không khí:")
    print(f"   Tốt nhất: {best_station['location_name']} (PM2.5: {best_station['pm2_5']} μg/m³)")
    print(f"   Tệ nhất: {worst_station['location_name']} (PM2.5: {worst_station['pm2_5']} μg/m³)")
    
    # 5. Đếm số điểm theo từng mức chất lượng
    print(f"\n5. Thống kê chất lượng không khí:")
    for quality, count in air_quality_stats.items():
        percentage = count / len(df) * 100
        print(f"   {quality}: {count} điểm ({percentage:.1f}%)")
    
    # 6. Lọc điểm có PM10 vượt ngưỡng WHO (>20 μg/m³)
    high_pm10 = df[df['pm10'] > 20]
    print(f"\n6. Điểm có PM10 vượt ngưỡng WHO (>20 μg/m³): {len(high_pm10)}/{len(df)} điểm")
    for _, station in high_pm10.iterrows():
        print(f"   {station['location_name']}: {station['pm10']} μg/m³")
    
    return df


def main():
    """Hàm main với đáp án hoàn chỉnh"""
    print("Exercise 02: Pandas DataFrame - COMPLETE SOLUTION")
    print("=" * 60)
    
    # Chạy tất cả các bài tập với solution
    df1 = exercise_1_satellite_analysis()
    df2 = exercise_2_weather_analysis() 
    df3 = exercise_3_air_quality_analysis()
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print(f"- Bài 1: Phân tích {len(df1)} pixel ảnh vệ tinh")
    print(f"- Bài 2: Phân tích {len(df2)} trạm khí tượng") 
    print(f"- Bài 3: Phân tích {len(df3)} điểm quan trắc môi trường")
    print("Tất cả bài tập đã hoàn thành!")


if __name__ == "__main__":
    main()
