import numpy as np

def main():
    """Phân tích ma trận điểm thi của lớp học"""
    print("=== PHÂN TÍCH MA TRẬN ĐIỂM THI ===")
    print()
    
    # Tạo dữ liệu điểm thi
    np.random.seed(42)
    scores = np.random.randint(0, 101, (20, 5))
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
    
    print("Ma trận điểm (20 học sinh x 5 môn):")
    print(scores)
    print()
    
    # Thống kê theo học sinh (axis=1)
    student_averages = np.mean(scores, axis=1)
    print("📊 THỐNG KÊ THEO HỌC SINH:")
    for i, avg in enumerate(student_averages, 1):
        print(f"Học sinh #{i}: {avg:.1f} điểm")
    print()
    
    # Thống kê theo môn học (axis=0)
    subject_averages = np.mean(scores, axis=0)
    print("📚 THỐNG KÊ THEO MÔN HỌC:")
    for subject, avg in zip(subjects, subject_averages):
        print(f"{subject}: {avg:.1f} điểm")
    print()
    
    # Tìm học sinh xuất sắc nhất
    best_student_idx = np.argmax(student_averages)
    best_student_avg = student_averages[best_student_idx]
    
    # Tìm môn khó nhất và dễ nhất
    hardest_subject_idx = np.argmin(subject_averages)
    easiest_subject_idx = np.argmax(subject_averages)
    
    print("🏆 THÔNG TIN NỔI BẬT:")
    print(f"- Học sinh xuất sắc nhất: Học sinh #{best_student_idx + 1} (TB: {best_student_avg:.1f} điểm)")
    print(f"- Môn khó nhất: {subjects[hardest_subject_idx]} (TB: {subject_averages[hardest_subject_idx]:.1f} điểm)")
    print(f"- Môn dễ nhất: {subjects[easiest_subject_idx]} (TB: {subject_averages[easiest_subject_idx]:.1f} điểm)")
    print()
    
    # Phân loại học sinh giỏi
    excellent_students_mask = student_averages >= 80
    excellent_count = np.sum(excellent_students_mask)
    excellent_rate = excellent_count / len(student_averages) * 100
    
    print("📈 PHÂN LOẠI HỌC SINH:")
    print(f"- Số học sinh giỏi (TB >= 80): {excellent_count}/{len(student_averages)} học sinh")
    print(f"- Tỷ lệ đạt: {excellent_rate:.1f}%")
    print()
    
    # Thống kê bổ sung
    print("📊 THỐNG KÊ BỔ SUNG:")
    print(f"- Điểm cao nhất toàn lớp: {np.max(scores)} điểm")
    print(f"- Điểm thấp nhất toàn lớp: {np.min(scores)} điểm")
    print(f"- Điểm trung bình toàn lớp: {np.mean(scores):.1f} điểm")

if __name__ == "__main__":
    main()
