"""
Exercise 03: Functions - Solutions
Bài giải mẫu cho các bài tập về Functions
"""

import random
import string

def exercise_1_calculator():
    """Bài 1: Máy tính cơ bản với Functions"""
    print("=== BÀI 1: MÁY TÍNH CƠ BẢN ===\n")
    
    def add(x, y):
        """Cộng hai số"""
        return x + y
    
    def subtract(x, y):
        """Trừ hai số"""
        return x - y
    
    def multiply(x, y):
        """Nhân hai số"""
        return x * y
    
    def divide(x, y):
        """Chia hai số"""
        if y == 0:
            return "Lỗi: Không thể chia cho 0"
        return x / y
    
    def display_menu():
        """Hiển thị menu"""
        print("Chọn phép toán:")
        print("1. Cộng (+)")
        print("2. Trừ (-)")
        print("3. Nhân (*)")
        print("4. Chia (/)")
    
    def get_input():
        """Nhận input từ user"""
        try:
            choice = int(input("Lựa chọn: "))
            if choice not in [1, 2, 3, 4]:
                return None, None, None
            
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
            return choice, num1, num2
        except ValueError:
            return None, None, None
    
    def calculate(operator, x, y):
        """Thực hiện phép tính"""
        operations = {
            1: (add, '+'),
            2: (subtract, '-'),
            3: (multiply, '*'),
            4: (divide, '/')
        }
        
        if operator in operations:
            func, symbol = operations[operator]
            result = func(x, y)
            return f"{x} {symbol} {y} = {result}"
        return "Phép toán không hợp lệ"
    
    # Demo chương trình
    display_menu()
    choice, num1, num2 = 1, 15, 7  # Mô phỏng input
    print(f"Lựa chọn: {choice}")
    print(f"Nhập số thứ nhất: {num1}")
    print(f"Nhập số thứ hai: {num2}")
    print()
    
    result = calculate(choice, num1, num2)
    print(f"Kết quả: {result}")
    print()

def exercise_2_grade_management():
    """Bài 2: Hệ thống quản lý điểm số"""
    print("=== BÀI 2: HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===\n")
    
    def calculate_average(scores):
        """Tính điểm trung bình"""
        return sum(scores) / len(scores) if scores else 0
    
    def find_max_min(scores):
        """Tìm điểm cao nhất và thấp nhất"""
        if not scores:
            return None, None
        return max(scores), min(scores)
    
    def classify_grade(score):
        """Phân loại học lực"""
        if score >= 8.5:
            return "Giỏi"
        elif score >= 7.0:
            return "Khá"
        elif score >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"
    
    def count_by_grade(scores):
        """Đếm số học sinh theo từng loại"""
        grade_count = {"Giỏi": 0, "Khá": 0, "Trung bình": 0, "Yếu": 0}
        
        for score in scores:
            grade = classify_grade(score)
            grade_count[grade] += 1
        
        return grade_count
    
    def display_statistics(scores):
        """Hiển thị thống kê tổng hợp"""
        if not scores:
            print("Không có dữ liệu điểm số!")
            return
        
        print("=== THỐNG KÊ ĐIỂM SỐ LỚP HỌC ===")
        print(f"Danh sách điểm: {scores}")
        print(f"Số học sinh: {len(scores)}")
        print()
        
        avg = calculate_average(scores)
        max_score, min_score = find_max_min(scores)
        
        print(f"Điểm trung bình: {avg:.2f}")
        print(f"Điểm cao nhất: {max_score}")
        print(f"Điểm thấp nhất: {min_score}")
        print()
        
        grade_counts = count_by_grade(scores)
        total_students = len(scores)
        
        print("Phân loại học lực:")
        grade_criteria = {
            "Giỏi": "≥8.5",
            "Khá": "≥7.0", 
            "Trung bình": "≥5.0",
            "Yếu": "<5.0"
        }
        
        for grade, count in grade_counts.items():
            percentage = (count / total_students) * 100
            criteria = grade_criteria[grade]
            print(f"- {grade} ({criteria}): {count} học sinh ({percentage:.1f}%)")
    
    # Demo với dữ liệu mẫu
    scores = [8.5, 7.2, 9.1, 6.8, 5.5, 8.8, 7.9, 4.2, 9.5, 6.1]
    display_statistics(scores)
    print()

def exercise_3_string_processing():
    """Bài 3: Chuyển đổi và xử lý chuỗi"""
    print("=== BÀI 3: XỬ LÝ CHUỖI ===\n")
    
    def reverse_string(text):
        """Đảo ngược chuỗi"""
        return text[::-1]
    
    def count_words(text):
        """Đếm số từ trong chuỗi"""
        return len(text.split())
    
    def capitalize_words(text):
        """Viết hoa chữ cái đầu mỗi từ"""
        return text.title()
    
    def remove_duplicates(text):
        """Loại bỏ từ trùng lặp"""
        words = text.split()
        unique_words = []
        seen = set()
        
        for word in words:
            if word.lower() not in seen:
                unique_words.append(word)
                seen.add(word.lower())
        
        return " ".join(unique_words)
    
    def find_longest_word(text):
        """Tìm từ dài nhất"""
        words = text.split()
        longest = max(words, key=len) if words else ""
        return longest, len(longest)
    
    def count_character_frequency(text):
        """Đếm tần suất ký tự"""
        char_count = {}
        for char in text.lower():
            char_count[char] = char_count.get(char, 0) + 1
        
        # Sắp xếp theo tần suất giảm dần
        sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_chars
    
    # Demo với dữ liệu mẫu
    text = "python programming is fun and python is powerful"
    
    print("=== XỬ LÝ CHUỖI ===")
    print(f'Chuỗi gốc: "{text}"')
    print()
    
    reversed_text = reverse_string(text)
    print(f'Chuỗi đảo ngược: "{reversed_text}"')
    
    word_count = count_words(text)
    print(f"Số từ: {word_count}")
    
    capitalized = capitalize_words(text)
    print(f'Viết hoa chữ cái đầu: "{capitalized}"')
    
    no_duplicates = remove_duplicates(text)
    print(f'Loại bỏ từ trùng: "{no_duplicates}"')
    
    longest_word, length = find_longest_word(text)
    print(f'Từ dài nhất: "{longest_word}" ({length} ký tự)')
    print()
    
    char_freq = count_character_frequency(text)
    print("Tần suất ký tự (top 5):")
    for char, count in char_freq[:5]:
        char_display = f"'{char}'" if char != ' ' else "' '"
        print(f"- {char_display}: {count} lần")
    print()

def exercise_4_salary_system():
    """Bài 4: Hệ thống tính lương"""
    print("=== BÀI 4: HỆ THỐNG TÍNH LƯƠNG ===\n")
    
    def calculate_basic_salary(hours, hourly_rate):
        """Tính lương cơ bản"""
        basic_hours = min(hours, 40)
        return basic_hours * hourly_rate
    
    def calculate_overtime(hours, hourly_rate):
        """Tính lương làm thêm giờ"""
        if hours > 40:
            overtime_hours = hours - 40
            return overtime_hours * hourly_rate * 1.5
        return 0
    
    def calculate_bonus(basic_salary, performance_rate):
        """Tính thưởng theo hiệu suất"""
        return basic_salary * performance_rate
    
    def calculate_tax(total_income):
        """Tính thuế thu nhập"""
        tax_threshold = 11000000
        tax_rate = 0.10
        
        if total_income > tax_threshold:
            return (total_income - tax_threshold) * tax_rate
        return 0
    
    def calculate_net_salary(basic, overtime, bonus, tax):
        """Tính lương thực lãnh"""
        return basic + overtime + bonus - tax
    
    def generate_payslip(name, hours, hourly_rate, performance_rate):
        """Tạo phiếu lương"""
        basic_salary = calculate_basic_salary(hours, hourly_rate)
        overtime_salary = calculate_overtime(hours, hourly_rate)
        bonus = calculate_bonus(basic_salary, performance_rate)
        total_income = basic_salary + overtime_salary + bonus
        tax = calculate_tax(total_income)
        net_salary = calculate_net_salary(basic_salary, overtime_salary, bonus, tax)
        
        print("=== PHIẾU LƯƠNG THÁNG 3/2024 ===")
        print(f"Nhân viên: {name}")
        print()
        
        print("CHI TIẾT TÍNH LƯƠNG:")
        basic_hours = min(hours, 40)
        overtime_hours = max(0, hours - 40)
        print(f"- Giờ làm việc cơ bản: {basic_hours} giờ")
        print(f"- Giờ làm thêm: {overtime_hours} giờ")
        print(f"- Đơn giá giờ: {hourly_rate:,} VNĐ")
        print()
        
        print("THÀNH PHẦN LƯƠNG:")
        print(f"- Lương cơ bản: {basic_salary:,.0f} VNĐ")
        print(f"- Lương làm thêm: {overtime_salary:,.0f} VNĐ")
        print(f"- Thưởng hiệu suất ({performance_rate*100:.0f}%): {bonus:,.0f} VNĐ")
        print(f"- Tổng thu nhập: {total_income:,.0f} VNĐ")
        print()
        
        print("KHẤU TRỪ:")
        print(f"- Thuế thu nhập cá nhân: {tax:,.0f} VNĐ")
        print()
        
        print(f"LƯƠNG THỰC LÃNH: {net_salary:,.0f} VNĐ")
    
    # Demo với dữ liệu mẫu
    generate_payslip("Nguyễn Văn A", 45, 50000, 0.15)
    print()

def exercise_5_number_guessing_game():
    """Bài 5: Game đoán số"""
    print("=== BÀI 5: GAME ĐOÁN SỐ ===\n")
    
    def generate_random_number(min_num=1, max_num=100):
        """Tạo số ngẫu nhiên"""
        return random.randint(min_num, max_num)
    
    def check_guess(guess, target):
        """Kiểm tra và đưa ra gợi ý"""
        if guess == target:
            return "correct"
        elif guess > target:
            return "too_high"
        else:
            return "too_low"
    
    def display_result(attempts, target, won):
        """Hiển thị kết quả"""
        if won:
            print(f"Chúc mừng! Bạn đã đoán đúng số {target} sau {attempts} lần!")
        else:
            print(f"Bạn đã hết lượt đoán! Số tôi nghĩ là {target}")
    
    def show_statistics(games_played, games_won, total_attempts):
        """Hiển thị thống kê"""
        print("\nTHỐNG KÊ:")
        print(f"- Số lần chơi: {games_played}")
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            avg_attempts = total_attempts / games_played
            print(f"- Tỷ lệ thắng: {win_rate:.1f}%")
            print(f"- Số lần đoán trung bình: {avg_attempts:.1f}")
    
    # Demo game (mô phỏng)
    print("=== GAME ĐOÁN SỐ ===")
    print("Tôi đã nghĩ ra một số từ 1 đến 100.")
    print("Bạn có 7 lần đoán!")
    print()
    
    # Mô phỏng một game
    target = 43
    guesses = [50, 25, 37, 43]
    max_attempts = 7
    
    for i, guess in enumerate(guesses, 1):
        print(f"Lần đoán {i}: Nhập số: {guess}")
        
        result = check_guess(guess, target)
        if result == "correct":
            print(f"Chúc mừng! Bạn đã đoán đúng số {target} sau {i} lần!")
            break
        elif result == "too_high":
            print("Số bạn đoán lớn hơn số tôi nghĩ!")
        else:
            print("Số bạn đoán nhỏ hơn số tôi nghĩ!")
        print()
    
    show_statistics(1, 1, len(guesses))
    print()

def main():
    """Hàm main chạy tất cả bài tập"""
    print("GIẢI BÀI TẬP FUNCTIONS")
    print("=" * 50)
    
    exercise_1_calculator()
    print("-" * 50)
    
    exercise_2_grade_management()
    print("-" * 50)
    
    exercise_3_string_processing()
    print("-" * 50)
    
    exercise_4_salary_system()
    print("-" * 50)
    
    exercise_5_number_guessing_game()

if __name__ == "__main__":
    main()
