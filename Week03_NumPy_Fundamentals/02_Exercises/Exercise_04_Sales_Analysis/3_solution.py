import numpy as np

def main():
    """Phân tích dữ liệu bán hàng 4 quý"""
    print("=== PHÂN TÍCH DỮ LIỆU BÁN HÀNG ===")
    print()
    
    # Tạo dữ liệu doanh thu 4 quý x 3 tháng
    np.random.seed(42)
    revenue = np.random.uniform(50, 200, (4, 3))
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    
    # Hiển thị doanh thu theo quý
    print("Doanh thu theo quý (triệu VND):")
    print("      T1    T2    T3   Tổng")
    for i, quarter in enumerate(quarters):
        quarter_total = np.sum(revenue[i])
        print(f"{quarter}  [{revenue[i, 0]:5.1f} {revenue[i, 1]:5.1f} {revenue[i, 2]:5.1f}] {quarter_total:.1f}")
    print()
    
    # Tính tổng theo quý và tăng trưởng
    quarterly_totals = np.sum(revenue, axis=1)
    growth_rates = np.diff(quarterly_totals) / quarterly_totals[:-1] * 100
    
    print("📊 TỔNG KẾT THEO QUÝ:")
    print(f"Q1: {quarterly_totals[0]:.1f} triệu")
    for i in range(1, 4):
        print(f"Q{i+1}: {quarterly_totals[i]:.1f} triệu ({growth_rates[i-1]:+.1f}%)")
    print()
    
    # Tính tổng theo tháng
    monthly_totals = np.sum(revenue, axis=0)
    print("📊 TỔNG KẾT THEO THÁNG:")
    for i, total in enumerate(monthly_totals, 1):
        print(f"Tháng {i}: {total:.1f} triệu")
    print()
    
    # Tính thuế 10%
    revenue_after_tax = revenue * 0.9
    total_tax = np.sum(revenue) * 0.1
    
    print("💰 SAU THUẾ (10%):")
    print(f"Doanh thu sau thuế: {np.sum(revenue_after_tax):.1f} triệu")
    print(f"Thuế phải nộp: {total_tax:.1f} triệu")
    print()
    
    # So sánh với target
    target = 150
    meets_target = revenue >= target
    months_meet_target = np.sum(meets_target)
    total_months = revenue.size
    
    print(f"🎯 SO SÁNH TARGET ({target} triệu/tháng):")
    print(f"Số tháng đạt target: {months_meet_target}/{total_months} tháng")
    print(f"Tỷ lệ đạt: {months_meet_target/total_months*100:.1f}%")

if __name__ == "__main__":
    main()
