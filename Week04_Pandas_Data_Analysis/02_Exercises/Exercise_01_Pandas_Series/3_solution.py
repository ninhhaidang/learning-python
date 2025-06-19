"""
Exercise 01: Pandas Series - Solution
Week 4: Pandas Data Analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def exercise_1_temperature_analysis():
    """Bài 1: Phân tích nhiệt độ theo thời gian - SOLUTION"""
    print("Bài 1: Phân tích nhiệt độ theo thời gian - SOLUTION")
    print("-" * 60)
    
    # Tạo dữ liệu nhiệt độ hàng ngày cho Hà Nội (30 ngày)
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    temperatures = [
        18.5, 19.2, 17.8, 20.1, 22.3, 16.7, 15.2, 14.8, 18.9, 21.4,
        23.1, 24.5, 22.8, 20.6, 19.3, 17.9, 16.4, 18.7, 20.9, 22.2,
        25.1, 26.3, 24.7, 23.5, 21.8, 19.6, 17.3, 18.1, 20.4, 22.7
    ]
    
    temp_series = pd.Series(temperatures, index=dates, name='Temperature(°C)')
    print(f"Created temperature series with {len(temp_series)} daily readings")
    print(f"Date range: {temp_series.index.min().date()} to {temp_series.index.max().date()}")
    
    # 1. Thống kê cơ bản
    print("\n1. Thống kê cơ bản:")
    print(f"   Nhiệt độ trung bình: {temp_series.mean():.2f}°C")
    print(f"   Nhiệt độ cao nhất: {temp_series.max():.2f}°C vào {temp_series.idxmax().date()}")
    print(f"   Nhiệt độ thấp nhất: {temp_series.min():.2f}°C vào {temp_series.idxmin().date()}")
    print(f"   Độ lệch chuẩn: {temp_series.std():.2f}°C")
    
    # 2. Xu hướng nhiệt độ (Moving average)
    moving_avg_3 = temp_series.rolling(window=3).mean()
    moving_avg_7 = temp_series.rolling(window=7).mean()
    
    print("\n2. Xu hướng nhiệt độ (Moving averages):")
    print(f"   MA(3) cuối cùng: {moving_avg_3.iloc[-1]:.2f}°C")
    print(f"   MA(7) cuối cùng: {moving_avg_7.iloc[-1]:.2f}°C")
    
    # 3. Lọc ngày lạnh (< 18°C) và ngày nóng (> 23°C)
    cold_days = temp_series[temp_series < 18]
    hot_days = temp_series[temp_series > 23]
    
    print(f"\n3. Phân loại ngày:")
    print(f"   Ngày lạnh (< 18°C): {len(cold_days)} ngày")
    print(f"   Ngày nóng (> 23°C): {len(hot_days)} ngày")
    print(f"   Ngày ôn hòa: {len(temp_series) - len(cold_days) - len(hot_days)} ngày")
    
    # 4. Tính độ thay đổi nhiệt độ hàng ngày
    temp_change = temp_series.diff()
    print(f"\n4. Độ thay đổi nhiệt độ:")
    print(f"   Thay đổi trung bình: {temp_change.mean():.2f}°C/ngày")
    print(f"   Thay đổi lớn nhất: {temp_change.max():.2f}°C vào {temp_change.idxmax().date()}")
    print(f"   Giảm mạnh nhất: {temp_change.min():.2f}°C vào {temp_change.idxmin().date()}")
    
    return temp_series

def exercise_2_student_scores():
    """Bài 2: Phân tích điểm thi học sinh - SOLUTION"""
    print("\nBài 2: Phân tích điểm thi học sinh - SOLUTION")
    print("-" * 60)
    
    # Dữ liệu điểm thi của 25 học sinh
    student_ids = [f'SV{i:03d}' for i in range(1, 26)]
    scores = [
        8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 8.2, 9.3, 7.8, 8.6,
        6.9, 8.1, 7.9, 8.8, 9.0, 7.4, 8.3, 7.6, 8.7, 9.2,
        7.1, 8.4, 7.7, 8.0, 9.4
    ]
    
    scores_series = pd.Series(scores, index=student_ids, name='Math_Score')
    print(f"Tạo Series điểm thi cho {len(scores_series)} học sinh")
    
    # 1. Thống kê mô tả
    print("\n1. Thống kê mô tả:")
    print(scores_series.describe())
    
    # 2. Phân loại học lực
    def classify_grade(score):
        if score >= 9.0:
            return 'Xuất sắc'
        elif score >= 8.0:
            return 'Giỏi'
        elif score >= 6.5:
            return 'Khá'
        elif score >= 5.0:
            return 'Trung bình'
        else:
            return 'Yếu'
    
    grades = scores_series.apply(classify_grade)
    grade_counts = grades.value_counts()
    
    print("\n2. Phân bố học lực:")
    for grade, count in grade_counts.items():
        percentage = (count / len(scores_series)) * 100
        print(f"   {grade}: {count} học sinh ({percentage:.1f}%)")
    
    # 3. Top và bottom performers
    top_5 = scores_series.nlargest(5)
    bottom_5 = scores_series.nsmallest(5)
    
    print("\n3. Top 5 học sinh:")
    for student, score in top_5.items():
        print(f"   {student}: {score}")
    
    print("\n4. Bottom 5 học sinh:")
    for student, score in bottom_5.items():
        print(f"   {student}: {score}")
    
    # 5. Lọc học sinh đạt điểm giỏi
    excellent_students = scores_series[scores_series >= 8.0]
    print(f"\n5. Học sinh đạt điểm giỏi trở lên: {len(excellent_students)} học sinh")
    
    return scores_series, grades

def exercise_3_stock_analysis():
    """Bài 3: Phân tích giá cổ phiếu VIC - SOLUTION"""
    print("\nBài 3: Phân tích giá cổ phiếu VIC - SOLUTION")
    print("-" * 60)
    
    # Tạo dữ liệu giá cổ phiếu VIC (20 ngày giao dịch)
    dates = pd.date_range('2024-01-02', periods=20, freq='B')  # Business days only
    prices = [
        95000, 96500, 94800, 97200, 98100, 96800, 99200, 101500, 100300, 102800,
        104200, 103600, 105800, 107300, 106100, 108900, 110200, 109500, 112300, 114600
    ]
    
    stock_series = pd.Series(prices, index=dates, name='VIC_Price(VND)')
    print(f"Tạo Series giá cổ phiếu VIC cho {len(stock_series)} phiên giao dịch")
    
    # 1. Thống kê cơ bản
    print("\n1. Thống kê giá cổ phiếu:")
    print(f"   Giá trung bình: {stock_series.mean():,.0f} VNĐ")
    print(f"   Giá cao nhất: {stock_series.max():,.0f} VNĐ vào {stock_series.idxmax().date()}")
    print(f"   Giá thấp nhất: {stock_series.min():,.0f} VNĐ vào {stock_series.idxmin().date()}")
    
    # 2. Tính tỷ suất sinh lời hàng ngày
    daily_returns = stock_series.pct_change() * 100
    print(f"\n2. Tỷ suất sinh lời:")
    print(f"   Sinh lời trung bình: {daily_returns.mean():.2f}%/ngày")
    print(f"   Độ lệch chuẩn: {daily_returns.std():.2f}%")
    print(f"   Ngày tăng mạnh nhất: {daily_returns.max():.2f}% vào {daily_returns.idxmax().date()}")
    print(f"   Ngày giảm mạnh nhất: {daily_returns.min():.2f}% vào {daily_returns.idxmin().date()}")
    
    # 3. Moving averages
    ma5 = stock_series.rolling(window=5).mean()
    ma10 = stock_series.rolling(window=10).mean()
    
    current_price = stock_series.iloc[-1]
    current_ma5 = ma5.iloc[-1]
    current_ma10 = ma10.iloc[-1]
    
    print(f"\n3. Phân tích kỹ thuật:")
    print(f"   Giá hiện tại: {current_price:,.0f} VNĐ")
    print(f"   MA5: {current_ma5:,.0f} VNĐ")
    print(f"   MA10: {current_ma10:,.0f} VNĐ")
    
    # Tín hiệu giao dịch
    if current_price > current_ma5 > current_ma10:
        signal = "Tín hiệu MUA mạnh"
    elif current_price > current_ma5:
        signal = "Tín hiệu MUA"
    elif current_price < current_ma5 < current_ma10:
        signal = "Tín hiệu BÁN mạnh"
    else:
        signal = "Tín hiệu BÁN"
    
    print(f"   Tín hiệu: {signal}")
    
    # 4. Phân tích xu hướng
    total_return = ((stock_series.iloc[-1] / stock_series.iloc[0]) - 1) * 100
    print(f"\n4. Hiệu suất tổng thể:")
    print(f"   Tăng trưởng: {total_return:.2f}% trong {len(stock_series)} phiên")
    print(f"   Lợi nhuận trên 100 triệu VNĐ: {total_return * 1000000:,.0f} VNĐ")
    
    # 5. Ngày có khối lượng giao dịch cao (giả lập)
    volume_multiplier = np.abs(daily_returns) + np.random.normal(1, 0.2, len(stock_series))
    high_volume_days = stock_series[volume_multiplier > volume_multiplier.quantile(0.8)]
    
    print(f"\n5. Ngày giao dịch sôi động (top 20%):")
    for date, price in high_volume_days.items():
        return_rate = daily_returns.loc[date]
        print(f"   {date.date()}: {price:,.0f} VNĐ ({return_rate:+.2f}%)")
    
    return stock_series, daily_returns

def main():
    """Hàm main với đáp án mẫu"""
    print("Exercise 01: Pandas Series - COMPLETE SOLUTION")
    print("=" * 60)
    
    # Chạy từng bài tập
    temp_data = exercise_1_temperature_analysis()
    scores_data, grades_data = exercise_2_student_scores()
    stock_data, returns_data = exercise_3_stock_analysis()
    
    # Tổng kết
    print("\n" + "=" * 60)
    print("📊 TỔNG KẾT PHÂN TÍCH SERIES")
    print("=" * 60)
    
    print(f"✅ Bài 1 - Nhiệt độ: {len(temp_data)} ngày, từ {temp_data.min():.1f}°C đến {temp_data.max():.1f}°C")
    print(f"✅ Bài 2 - Điểm thi: {len(scores_data)} học sinh, điểm TB: {scores_data.mean():.2f}")
    print(f"✅ Bài 3 - Cổ phiếu: {len(stock_data)} phiên, tăng {((stock_data.iloc[-1]/stock_data.iloc[0])-1)*100:.1f}%")
    
    print("\n🎯 Đã thành thạo:")
    print("   - Tạo và thao tác với pandas Series")
    print("   - Indexing với datetime và string index")
    print("   - Statistical operations và aggregations")
    print("   - Time series analysis cơ bản")
    print("   - Data filtering và boolean indexing")
    print("   - Rolling windows và moving averages")
    
    return {
        'temperature': temp_data,
        'scores': scores_data,
        'grades': grades_data,
        'stock': stock_data,
        'returns': returns_data
    }

if __name__ == "__main__":
    results = main()
