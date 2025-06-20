import numpy as np

def main():
    """Phân tích dữ liệu nhiệt độ 30 ngày"""
    print("=== PHÂN TÍCH DỮ LIỆU NHIỆT ĐỘ ===")
    print()
    
    # Tạo dữ liệu nhiệt độ ngẫu nhiên từ 18-35°C
    np.random.seed(42)  # Để có kết quả reproducible
    temperatures = np.random.uniform(18, 35, 30)
    
    print("Dữ liệu nhiệt độ 30 ngày (°C):")
    print(np.round(temperatures, 1))
    print()
    
    # Thống kê cơ bản
    max_temp = np.max(temperatures)
    min_temp = np.min(temperatures)
    max_day = np.argmax(temperatures) + 1  # +1 vì ngày đếm từ 1
    min_day = np.argmin(temperatures) + 1
    mean_temp = np.mean(temperatures)
    std_temp = np.std(temperatures)
    
    print("📊 THỐNG KÊ TỔNG QUAN:")
    print(f"- Nhiệt độ cao nhất: {max_temp:.1f}°C (ngày {max_day})")
    print(f"- Nhiệt độ thấp nhất: {min_temp:.1f}°C (ngày {min_day})")
    print(f"- Nhiệt độ trung bình: {mean_temp:.1f}°C")
    print(f"- Độ lệch chuẩn: {std_temp:.1f}°C")
    print()
    
    # Phân loại ngày theo nhiệt độ
    hot_days_mask = temperatures > 30
    cool_days_mask = temperatures < 22
    normal_days_mask = (temperatures >= 22) & (temperatures <= 30)
    
    hot_days_count = np.sum(hot_days_mask)
    cool_days_count = np.sum(cool_days_mask)
    normal_days_count = np.sum(normal_days_mask)
    
    print("🌡️  PHÂN LOẠI NGÀY:")
    print(f"- Số ngày nóng (>30°C): {hot_days_count} ngày")
    print(f"- Số ngày mát (<22°C): {cool_days_count} ngày")
    print(f"- Số ngày bình thường: {normal_days_count} ngày")
    print()
    
    # Boolean masks
    print("🔍 BOOLEAN MASKS:")
    print("Ngày nóng (>30°C):", hot_days_mask[:10], "...")
    print("Ngày mát (<22°C):", cool_days_mask[:10], "...")
    print()
    
    # Thống kê bổ sung
    print("📈 THỐNG KÊ BỔ SUNG:")
    print(f"- Tỷ lệ ngày nóng: {hot_days_count/30*100:.1f}%")
    print(f"- Tỷ lệ ngày mát: {cool_days_count/30*100:.1f}%")
    print(f"- Khoảng biến thiên: {max_temp - min_temp:.1f}°C")

if __name__ == "__main__":
    main()
