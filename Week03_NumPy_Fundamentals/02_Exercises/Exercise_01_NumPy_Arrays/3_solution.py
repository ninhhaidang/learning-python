"""
Exercise 01 Solutions: NumPy Arrays
Week 03 - NumPy Fundamentals

Đáp án chi tiết cho các bài tập về NumPy Arrays cơ bản
"""

import numpy as np

print("=" * 60)
print("EXERCISE 01 SOLUTIONS: NumPy Arrays")
print("=" * 60)

# =============================================================================
# Bài 1: Tạo và Phân tích Dữ liệu Nhiệt độ
# =============================================================================
print("\n" + "="*50)
print("BÀI 1: PHÂN TÍCH DỮ LIỆU NHIỆT ĐỘ")
print("="*50)

# Set seed để có kết quả reproducible
np.random.seed(42)

# 1. Tạo dữ liệu nhiệt độ
temperatures = np.random.uniform(18, 35, 30)
print(f"Dữ liệu nhiệt độ 30 ngày:")
print(f"{temperatures.round(1)}")

# 2. Tìm ngày có nhiệt độ cao nhất và thấp nhất
max_temp_day = np.argmax(temperatures)
min_temp_day = np.argmin(temperatures)
max_temp = temperatures[max_temp_day]
min_temp = temperatures[min_temp_day]

print(f"\nNhiệt độ cao nhất: {max_temp:.1f}°C (ngày {max_temp_day + 1})")
print(f"Nhiệt độ thấp nhất: {min_temp:.1f}°C (ngày {min_temp_day + 1})")

# 3. Tính nhiệt độ trung bình và độ lệch chuẩn
mean_temp = np.mean(temperatures)
std_temp = np.std(temperatures)
print(f"\nNhiệt độ trung bình: {mean_temp:.1f}°C")
print(f"Độ lệch chuẩn: {std_temp:.1f}°C")

# 4. Đếm số ngày có nhiệt độ trên 30°C
hot_days_count = np.sum(temperatures > 30)
print(f"\nSố ngày nóng (>30°C): {hot_days_count} ngày")

# 5. Tạo boolean mask cho ngày nóng và ngày mát
hot_mask = temperatures > 30
cool_mask = temperatures < 22

print(f"\nMask ngày nóng (>30°C):")
print(f"{hot_mask}")
print(f"Số ngày nóng: {np.sum(hot_mask)}")

print(f"\nMask ngày mát (<22°C):")
print(f"{cool_mask}")
print(f"Số ngày mát: {np.sum(cool_mask)}")

# Bonus: Thống kê chi tiết
print(f"\nTHỐNG KÊ CHI TIẾT:")
print(f"Nhiệt độ median: {np.median(temperatures):.1f}°C")
print(f"Nhiệt độ min: {np.min(temperatures):.1f}°C")
print(f"Nhiệt độ max: {np.max(temperatures):.1f}°C")
print(f"Khoảng nhiệt độ: {np.ptp(temperatures):.1f}°C")  # peak-to-peak

# =============================================================================
# Bài 2: Ma trận Điểm Thi
# =============================================================================
print("\n" + "="*50)
print("BÀI 2: MA TRẬN ĐIỂM THI")
print("="*50)

# Reset seed
np.random.seed(42)

# 1. Tạo ma trận điểm
scores = np.random.randint(0, 101, (20, 5))
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']

print(f"Ma trận điểm (20 học sinh x 5 môn):")
print(scores)

# 2. Tính điểm trung bình của mỗi học sinh
student_averages = np.mean(scores, axis=1)
print(f"\nĐiểm TB mỗi học sinh:")
for i, avg in enumerate(student_averages):
    print(f"Học sinh #{i+1:2d}: {avg:.1f}")

# 3. Tính điểm trung bình của mỗi môn học
subject_averages = np.mean(scores, axis=0)
print(f"\nĐiểm TB mỗi môn:")
for subject, avg in zip(subjects, subject_averages):
    print(f"{subject:10s}: {avg:.1f}")

# 4. Tìm học sinh có điểm trung bình cao nhất
best_student_idx = np.argmax(student_averages)
best_average = student_averages[best_student_idx]
print(f"\nHọc sinh xuất sắc nhất: Học sinh #{best_student_idx+1} (TB: {best_average:.1f})")

# 5. Tìm môn học có điểm trung bình thấp nhất
hardest_subject_idx = np.argmin(subject_averages)
hardest_subject = subjects[hardest_subject_idx]
hardest_average = subject_averages[hardest_subject_idx]
print(f"Môn khó nhất: {hardest_subject} (TB: {hardest_average:.1f})")

# 6. Đếm số học sinh đạt điểm trung bình >= 80
excellent_students = np.sum(student_averages >= 80)
print(f"\nSố học sinh giỏi (TB >= 80): {excellent_students}/20")

# Bonus: Phân tích chi tiết
print(f"\nPHÂN TÍCH CHI TIẾT:")
print(f"Điểm cao nhất toàn trường: {np.max(scores)}")
print(f"Điểm thấp nhất toàn trường: {np.min(scores)}")

# Tìm học sinh và môn của điểm cao nhất
max_score_position = np.unravel_index(np.argmax(scores), scores.shape)
print(f"Điểm cao nhất: Học sinh #{max_score_position[0]+1}, môn {subjects[max_score_position[1]]}: {scores[max_score_position]}")

# Phân loại học sinh
excellent_mask = student_averages >= 85
good_mask = (student_averages >= 70) & (student_averages < 85)
average_mask = (student_averages >= 50) & (student_averages < 70)
poor_mask = student_averages < 50

print(f"\nPHÂN LOẠI HỌC SINH:")
print(f"Xuất sắc (>=85): {np.sum(excellent_mask)} học sinh")
print(f"Giỏi (70-84): {np.sum(good_mask)} học sinh")
print(f"Trung bình (50-69): {np.sum(average_mask)} học sinh")
print(f"Yếu (<50): {np.sum(poor_mask)} học sinh")

# =============================================================================
# Bài 3: Xử lý Dữ liệu Hình ảnh Đơn giản
# =============================================================================
print("\n" + "="*50)
print("BÀI 3: XỬ LÝ HÌNH ẢNH ĐỔN GIẢN")
print("="*50)

# Reset seed
np.random.seed(42)

# 1. Tạo ma trận đại diện cho ảnh grayscale
image = np.random.randint(0, 256, (10, 10))
print(f"Ảnh gốc (10x10):")
print(image)

# 2. Áp dụng threshold
threshold = 128
binary_image = np.where(image > threshold, 255, 0)
print(f"\nẢnh sau threshold (>{threshold}):")
print(binary_image)

# 3. Tính histogram đơn giản
bins = [0, 64, 128, 192, 256]
bin_labels = ['0-63', '64-127', '128-191', '192-255']

print(f"\nHistogram:")
for i in range(len(bins)-1):
    count = np.sum((image >= bins[i]) & (image < bins[i+1]))
    print(f"{bin_labels[i]}: {count} pixels")

# 4. Tìm vùng sáng nhất (max 3x3 region)
max_avg = 0
max_position = (0, 0)

for i in range(image.shape[0] - 2):
    for j in range(image.shape[1] - 2):
        region = image[i:i+3, j:j+3]
        avg = np.mean(region)
        if avg > max_avg:
            max_avg = avg
            max_position = (i, j)

print(f"\nVùng sáng nhất (3x3) tại vị trí {max_position}: trung bình {max_avg:.1f}")
brightest_region = image[max_position[0]:max_position[0]+3, 
                        max_position[1]:max_position[1]+3]
print("Vùng sáng nhất:")
print(brightest_region)

# 5. Flip ảnh theo chiều ngang và dọc
flipped_horizontal = np.flip(image, axis=1)  # hoặc image[:, ::-1]
flipped_vertical = np.flip(image, axis=0)    # hoặc image[::-1, :]

print(f"\nẢnh flip ngang:")
print(flipped_horizontal)

print(f"\nẢnh flip dọc:")
print(flipped_vertical)

# Bonus: Các thống kê ảnh
print(f"\nTHỐNG KÊ ẢNH:")
print(f"Độ sáng trung bình: {np.mean(image):.1f}")
print(f"Độ tương phản (std): {np.std(image):.1f}")
print(f"Pixel sáng nhất: {np.max(image)}")
print(f"Pixel tối nhất: {np.min(image)}")
print(f"Số pixel sáng (>128): {np.sum(image > 128)}")
print(f"Số pixel tối (<=128): {np.sum(image <= 128)}")

print("\n" + "="*60)
print("HOÀN THÀNH EXERCISE 01!")
print("="*60)
