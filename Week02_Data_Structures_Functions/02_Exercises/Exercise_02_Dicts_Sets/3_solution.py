"""
Exercise 02: Dictionaries and Sets - Solutions
Bài giải mẫu cho các bài tập về Dictionary và Sets
"""

def exercise_1_student_management():
    """Bài 1: Quản lý thông tin sinh viên"""
    print("=== BÀI 1: QUẢN LÝ THÔNG TIN SINH VIÊN ===\n")
    
    # 1. Tạo dictionary chứa thông tin sinh viên
    students = {
        "SV001": {"name": "Nguyễn Văn A", "age": 20, "score": 8.5},
        "SV002": {"name": "Trần Thị B", "age": 19, "score": 7.2},
        "SV003": {"name": "Lê Văn C", "age": 21, "score": 9.1}
    }
    
    # 2. In ra thông tin tất cả sinh viên
    print("=== THÔNG TIN TẤT CẢ SINH VIÊN ===")
    for student_id, info in students.items():
        print(f"{student_id}: {info['name']} - Tuổi: {info['age']} - Điểm: {info['score']}")
    print()
    
    # 3. Tìm sinh viên có điểm cao nhất
    best_student = max(students.items(), key=lambda x: x[1]['score'])
    print("=== SINH VIÊN CÓ ĐIỂM CAO NHẤT ===")
    print(f"{best_student[0]}: {best_student[1]['name']} - Điểm: {best_student[1]['score']}")
    print()
    
    # 4. Thêm sinh viên mới
    students["SV004"] = {"name": "Phạm Thị D", "age": 20, "score": 8.8}
    print("=== SAU KHI THÊM SINH VIÊN MỚI ===")
    print("Đã thêm SV004: Phạm Thị D")
    print()
    
    # 5. Cập nhật điểm sinh viên
    students["SV002"]["score"] = 8.0
    print("=== SAU KHI CẬP NHẬT ĐIỂM ===")
    print("Đã cập nhật điểm SV002 thành 8.0")
    print()
    
    # 6. Xóa sinh viên có điểm thấp nhất
    worst_student = min(students.items(), key=lambda x: x[1]['score'])
    removed_student = students.pop(worst_student[0])
    print("=== SAU KHI XÓA SINH VIÊN ĐIỂM THẤP NHẤT ===")
    print(f"Đã xóa {worst_student[0]}: {removed_student['name']}")
    print()

def exercise_2_sales_analysis():
    """Bài 2: Phân tích dữ liệu bán hàng"""
    print("=== BÀI 2: PHÂN TÍCH DỮ LIỆU BÁN HÀNG ===\n")
    
    sales_data = {
        "Tháng 1": 45000000,
        "Tháng 2": 52000000,
        "Tháng 3": 48000000,
        "Tháng 4": 61000000,
        "Tháng 5": 58000000,
        "Tháng 6": 67000000,
        "Tháng 7": 72000000,
        "Tháng 8": 69000000,
        "Tháng 9": 55000000,
        "Tháng 10": 63000000,
        "Tháng 11": 71000000,
        "Tháng 12": 75000000
    }
    
    print("=== PHÂN TÍCH DOANH THU NĂM 2024 ===")
    
    # Tính tổng doanh thu
    total_revenue = sum(sales_data.values())
    print(f"Tổng doanh thu cả năm: {total_revenue:,} VNĐ")
    
    # Tính doanh thu trung bình
    avg_revenue = total_revenue / len(sales_data)
    print(f"Doanh thu trung bình/tháng: {avg_revenue:,.0f} VNĐ")
    print()
    
    # Tìm tháng có doanh thu cao nhất và thấp nhất
    best_month = max(sales_data.items(), key=lambda x: x[1])
    worst_month = min(sales_data.items(), key=lambda x: x[1])
    print(f"Tháng có doanh thu cao nhất: {best_month[0]} ({best_month[1]:,} VNĐ)")
    print(f"Tháng có doanh thu thấp nhất: {worst_month[0]} ({worst_month[1]:,} VNĐ)")
    print()
    
    # Liệt kê các tháng có doanh thu trên 50 triệu
    print("Các tháng có doanh thu trên 50 triệu:")
    for month, revenue in sales_data.items():
        if revenue > 50000000:
            print(f"- {month}: {revenue:,} VNĐ")
    print()

def exercise_3_sets_operations():
    """Bài 3: Thao tác với Sets"""
    print("=== BÀI 3: THAO TÁC VỚI SETS ===\n")
    
    class_a = {"An", "Bình", "Chi", "Dũng", "Em", "Giang"}
    class_b = {"Bình", "Chi", "Hoa", "Khoa", "Linh", "An"}
    class_c = {"Chi", "Dũng", "Hoa", "Nam", "Oanh", "Bình"}
    
    print("=== THÔNG TIN CÁC LỚP ===")
    print(f"Lớp A: {class_a}")
    print(f"Lớp B: {class_b}")
    print(f"Lớp C: {class_c}")
    print()
    
    print("=== PHÂN TÍCH TẬP HỢP ===")
    
    # Học sinh có ở cả 3 lớp
    all_three = class_a & class_b & class_c
    print(f"Học sinh có ở cả 3 lớp: {all_three}")
    
    # Học sinh chỉ có ở lớp A
    only_a = class_a - class_b - class_c
    print(f"Học sinh chỉ có ở lớp A: {only_a}")
    
    # Tổng số học sinh khác nhau
    all_students = class_a | class_b | class_c
    print(f"Tổng số học sinh khác nhau: {len(all_students)}")
    
    # Học sinh ở A hoặc B nhưng không ở C
    a_or_b_not_c = (class_a | class_b) - class_c
    print(f"Học sinh ở A hoặc B nhưng không ở C: {a_or_b_not_c}")
    print()

def exercise_4_word_frequency():
    """Bài 4: Đếm tần suất từ khóa"""
    print("=== BÀI 4: ĐẾM TẦN SUẤT TỪ KHÓA ===\n")
    
    text = """Python là ngôn ngữ lập trình mạnh mẽ. Python dễ học và dễ sử dụng. 
    Với Python, bạn có thể phát triển ứng dụng web, mobile, AI và machine learning."""
    
    # Xử lý văn bản
    import re
    # Loại bỏ ký tự đặc biệt và chuyển về chữ thường
    words = re.findall(r'\b[a-zA-ZÀ-ỹ]+\b', text.lower())
    
    # Đếm tần suất
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    print("=== PHÂN TÍCH TẦN SUẤT TỪ KHÓA ===")
    print(f"Tổng số từ: {len(words)}")
    print(f"Số từ khác nhau: {len(word_count)}")
    print()
    
    # Top 5 từ xuất hiện nhiều nhất
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 từ xuất hiện nhiều nhất:")
    for i, (word, count) in enumerate(sorted_words[:5], 1):
        print(f"{i}. {word}: {count} lần")
    print()
    
    # Các từ chỉ xuất hiện 1 lần
    once_words = [word for word, count in word_count.items() if count == 1]
    print("Các từ chỉ xuất hiện 1 lần:")
    print(", ".join(sorted(once_words)))
    print()

def main():
    """Hàm main chạy tất cả bài tập"""
    print("GIẢI BÀI TẬP DICTIONARIES VÀ SETS")
    print("=" * 50)
    
    exercise_1_student_management()
    print("-" * 50)
    
    exercise_2_sales_analysis()
    print("-" * 50)
    
    exercise_3_sets_operations()
    print("-" * 50)
    
    exercise_4_word_frequency()

if __name__ == "__main__":
    main()
