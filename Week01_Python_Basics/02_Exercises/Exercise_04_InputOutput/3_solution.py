"""
Week 1 - Solution 4: Input/Output Operations
Đáp án chi tiết cho bài tập về input/output và xử lý dữ liệu người dùng

Author: Python Learning Course
Version: 1.0
"""

import random
import datetime

# =============================================================================
# SOLUTION 1: BASIC INPUT/OUTPUT
# =============================================================================

print("=" * 50)
print("SOLUTION 1: BASIC INPUT/OUTPUT")
print("=" * 50)

def personal_info_demo():
    """Demo chương trình nhập thông tin cá nhân"""
    print("CHƯƠNG TRÌNH NHẬP THÔNG TIN CÁ NHÂN")
    print("-" * 40)
    
    # Nhập thông tin
    name = input("Nhập tên của bạn: ")
    birth_year = int(input("Nhập năm sinh: "))
    current_year = 2024
    age = current_year - birth_year
    
    # In kết quả
    print(f"\nXin chào {name}!")
    print(f"Bạn {age} tuổi (tính đến năm {current_year})")
    
    # Phân loại độ tuổi
    if age < 13:
        age_group = "trẻ em"
    elif age < 20:
        age_group = "thanh thiếu niên"
    elif age < 60:
        age_group = "người lớn"
    else:
        age_group = "người cao tuổi"
    
    print(f"Bạn thuộc nhóm {age_group}")

# Uncomment để chạy demo:
# personal_info_demo()

def calculator_demo():
    """Demo calculator đơn giản"""
    print("\nCALCULATOR ĐƠN GIẢN")
    print("-" * 40)
    
    try:
        num1 = float(input("Nhập số thứ nhất: "))
        operator = input("Nhập phép toán (+, -, *, /): ")
        num2 = float(input("Nhập số thứ hai: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Lỗi: Không thể chia cho 0!")
                return
        else:
            print("Phép toán không hợp lệ!")
            return
        
        print(f"\nKết quả: {num1} {operator} {num2} = {result}")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ!")

# Uncomment để chạy demo:
# calculator_demo()

# =============================================================================
# SOLUTION 2: STRING INPUT PROCESSING
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 2: STRING INPUT PROCESSING")
print("=" * 50)

def name_processor_demo():
    """Demo xử lý tên người dùng"""
    print("XỬ LÝ TÊN NGƯỜI DÙNG")
    print("-" * 40)
    
    full_name = input("Nhập họ tên đầy đủ: ").strip()
    
    # Chuẩn hóa tên
    normalized_name = ' '.join(full_name.split()).title()
    
    # Tách các phần của tên
    name_parts = normalized_name.split()
    
    if len(name_parts) >= 2:
        first_name = name_parts[-1]
        last_name = name_parts[0]
        middle_names = ' '.join(name_parts[1:-1]) if len(name_parts) > 2 else ""
        
        print(f"\nTên chuẩn hóa: {normalized_name}")
        print(f"Họ: {last_name}")
        if middle_names:
            print(f"Tên đệm: {middle_names}")
        print(f"Tên: {first_name}")
        
        # Tạo email và username
        email_parts = [part.lower() for part in name_parts]
        email = '.'.join(email_parts) + "@email.com"
        username = ''.join(email_parts)
        initials = ''.join([part[0].upper() for part in name_parts])
        
        print(f"\nEmail đề xuất: {email}")
        print(f"Username đề xuất: {username}")
        print(f"Chữ cái đầu: {initials}")
    
    else:
        print("Vui lòng nhập ít nhất họ và tên!")

# Uncomment để chạy demo:
# name_processor_demo()

def password_validator_demo():
    """Demo kiểm tra mật khẩu"""
    print("\nKIỂM TRA ĐỘ MẠNH MẬT KHẨU")
    print("-" * 40)
    
    password = input("Nhập mật khẩu: ")
    
    # Kiểm tra các tiêu chí
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    print(f"\nKiểm tra mật khẩu: '{password}'")
    print(f"✓ Ít nhất 8 ký tự: {'✓' if length_ok else '✗'}")
    print(f"✓ Có chữ hoa: {'✓' if has_upper else '✗'}")
    print(f"✓ Có chữ thường: {'✓' if has_lower else '✗'}")
    print(f"✓ Có số: {'✓' if has_digit else '✗'}")
    print(f"✓ Có ký tự đặc biệt: {'✓' if has_special else '✗'}")
    
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    if score == 5:
        strength = "Rất mạnh"
    elif score >= 4:
        strength = "Mạnh"
    elif score >= 3:
        strength = "Trung bình"
    elif score >= 2:
        strength = "Yếu"
    else:
        strength = "Rất yếu"
    
    print(f"\nĐộ mạnh: {strength} ({score}/5)")

# Uncomment để chạy demo:
# password_validator_demo()

# =============================================================================
# SOLUTION 3: NUMERIC INPUT VALIDATION
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 3: NUMERIC INPUT VALIDATION")
print("=" * 50)

def safe_input_int(prompt, min_val=None, max_val=None):
    """Nhập số nguyên an toàn với validation"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Giá trị phải >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Giá trị phải <= {max_val}")
                continue
            return value
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")

def safe_input_float(prompt, min_val=None, max_val=None):
    """Nhập số thực an toàn với validation"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Giá trị phải >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Giá trị phải <= {max_val}")
                continue
            return value
        except ValueError:
            print("Vui lòng nhập số thực hợp lệ!")

def bmi_calculator_demo():
    """Demo tính BMI với input validation"""
    print("TÍNH CHỈ SỐ BMI")
    print("-" * 40)
    
    weight = safe_input_float("Nhập cân nặng (kg): ", min_val=1, max_val=1000)
    height = safe_input_float("Nhập chiều cao (m): ", min_val=0.5, max_val=3.0)
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Thiếu cân"
        advice = "Nên tăng cân"
    elif bmi < 25:
        category = "Bình thường"
        advice = "Duy trì cân nặng hiện tại"
    elif bmi < 30:
        category = "Thừa cân"
        advice = "Nên giảm cân"
    else:
        category = "Béo phì"
        advice = "Cần giảm cân nghiêm túc"
    
    print(f"\nKết quả:")
    print(f"Cân nặng: {weight} kg")
    print(f"Chiều cao: {height} m")
    print(f"BMI: {bmi:.2f}")
    print(f"Phân loại: {category}")
    print(f"Lời khuyên: {advice}")

# Uncomment để chạy demo:
# bmi_calculator_demo()

def grade_calculator_demo():
    """Demo tính điểm trung bình"""
    print("\nTÍNH ĐIỂM TRUNG BÌNH")
    print("-" * 40)
    
    num_subjects = safe_input_int("Nhập số môn học: ", min_val=1, max_val=20)
    
    total_score = 0
    scores = []
    
    for i in range(num_subjects):
        score = safe_input_float(f"Nhập điểm môn {i+1}: ", min_val=0, max_val=10)
        scores.append(score)
        total_score += score
    
    average = total_score / num_subjects
    
    # Xếp loại
    if average >= 9:
        rank = "Xuất sắc"
    elif average >= 8:
        rank = "Giỏi"
    elif average >= 6.5:
        rank = "Khá"
    elif average >= 5:
        rank = "Trung bình"
    else:
        rank = "Yếu"
    
    print(f"\nKết quả:")
    print(f"Các điểm: {scores}")
    print(f"Điểm cao nhất: {max(scores)}")
    print(f"Điểm thấp nhất: {min(scores)}")
    print(f"Điểm trung bình: {average:.2f}")
    print(f"Xếp loại: {rank}")

# Uncomment để chạy demo:
# grade_calculator_demo()

# =============================================================================
# SOLUTION 4: MENU-DRIVEN PROGRAMS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 4: MENU-DRIVEN PROGRAMS")
print("=" * 50)

def simple_atm_demo():
    """Demo ATM đơn giản"""
    print("HỆ THỐNG ATM ĐƠN GIẢN")
    print("=" * 40)
    
    balance = 1000000  # Số dư ban đầu
    pin = "1234"
    
    # Đăng nhập
    entered_pin = input("Nhập mã PIN: ")
    if entered_pin != pin:
        print("Mã PIN không đúng!")
        return
    
    print(f"Đăng nhập thành công!")
    
    while True:
        print("\n" + "-" * 40)
        print("1. Kiểm tra số dư")
        print("2. Rút tiền")
        print("3. Nạp tiền")
        print("4. Thoát")
        print("-" * 40)
        
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == "1":
            print(f"Số dư hiện tại: {balance:,} VND")
            
        elif choice == "2":
            try:
                amount = int(input("Nhập số tiền muốn rút: "))
                if amount <= 0:
                    print("Số tiền phải > 0!")
                elif amount > balance:
                    print("Số dư không đủ!")
                elif amount % 50000 != 0:
                    print("Số tiền phải là bội số của 50,000!")
                else:
                    balance -= amount
                    print(f"Rút thành công {amount:,} VND")
                    print(f"Số dư còn lại: {balance:,} VND")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
                
        elif choice == "3":
            try:
                amount = int(input("Nhập số tiền muốn nạp: "))
                if amount <= 0:
                    print("Số tiền phải > 0!")
                elif amount % 10000 != 0:
                    print("Số tiền phải là bội số của 10,000!")
                else:
                    balance += amount
                    print(f"Nạp thành công {amount:,} VND")
                    print(f"Số dư hiện tại: {balance:,} VND")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
                
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ!")
            break
            
        else:
            print("Lựa chọn không hợp lệ!")

# Uncomment để chạy demo:
# simple_atm_demo()

def quiz_game_demo():
    """Demo game quiz đơn giản"""
    print("\nGAME QUIZ TOÁN HỌC")
    print("=" * 40)
    
    score = 0
    total_questions = 5
    
    print(f"Trả lời {total_questions} câu hỏi toán học:")
    
    for i in range(total_questions):
        # Tạo câu hỏi ngẫu nhiên
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        operation = random.choice(["+", "-", "*"])
        
        if operation == "+":
            correct_answer = a + b
        elif operation == "-":
            correct_answer = a - b
        else:  # multiplication
            correct_answer = a * b
        
        print(f"\nCâu {i+1}: {a} {operation} {b} = ?")
        
        try:
            user_answer = int(input("Đáp án: "))
            if user_answer == correct_answer:
                print("Chính xác! +1 điểm")
                score += 1
            else:
                print(f"Sai rồi! Đáp án đúng là {correct_answer}")
        except ValueError:
            print(f"Đáp án không hợp lệ! Đáp án đúng là {correct_answer}")
    
    print(f"\nKết quả cuối cùng: {score}/{total_questions}")
    
    if score == total_questions:
        print("Xuất sắc! Bạn trả lời đúng tất cả!")
    elif score >= total_questions * 0.8:
        print("Tốt lắm!")
    elif score >= total_questions * 0.6:
        print("Khá!")
    else:
        print("Cần cố gắng thêm!")

# Uncomment để chạy demo:
# quiz_game_demo()

# =============================================================================
# SOLUTION 5: FILE-LIKE INPUT/OUTPUT
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTION 5: FILE-LIKE INPUT/OUTPUT")
print("=" * 50)

def contact_book_demo():
    """Demo sổ điện thoại đơn giản"""
    print("SỔ ĐIỆN THOẠI ĐƠN GIẢN")
    print("=" * 40)
    
    contacts = {}
    
    while True:
        print("\n" + "-" * 30)
        print("1. Thêm liên hệ")
        print("2. Tìm liên hệ")
        print("3. Hiển thị tất cả")
        print("4. Xóa liên hệ")
        print("5. Thoát")
        print("-" * 30)
        
        choice = input("Chọn chức năng (1-5): ")
        
        if choice == "1":
            name = input("Nhập tên: ").strip().title()
            if not name:
                print("Tên không được rỗng!")
                continue
                
            phone = input("Nhập số điện thoại: ").strip()
            if not phone.isdigit() or len(phone) not in [10, 11]:
                print("Số điện thoại không hợp lệ!")
                continue
                
            contacts[name] = phone
            print(f"Đã thêm {name}: {phone}")
            
        elif choice == "2":
            if not contacts:
                print("Sổ điện thoại trống!")
                continue
                
            search_name = input("Nhập tên cần tìm: ").strip().title()
            if search_name in contacts:
                print(f"{search_name}: {contacts[search_name]}")
            else:
                print("Không tìm thấy!")
                
        elif choice == "3":
            if not contacts:
                print("Sổ điện thoại trống!")
            else:
                print("Danh sách liên hệ:")
                for name, phone in sorted(contacts.items()):
                    print(f"  {name}: {phone}")
                    
        elif choice == "4":
            if not contacts:
                print("Sổ điện thoại trống!")
                continue
                
            name_to_delete = input("Nhập tên cần xóa: ").strip().title()
            if name_to_delete in contacts:
                del contacts[name_to_delete]
                print(f"Đã xóa {name_to_delete}")
            else:
                print("Không tìm thấy!")
                
        elif choice == "5":
            print("Tạm biệt!")
            break
            
        else:
            print("Lựa chọn không hợp lệ!")

# Uncomment để chạy demo:
# contact_book_demo()

def expense_tracker_demo():
    """Demo theo dõi chi tiêu"""
    print("\nTHEO DÕI CHI TIÊU")
    print("=" * 40)
    
    expenses = []
    categories = ["Ăn uống", "Đi lại", "Mua sắm", "Giải trí", "Khác"]
    
    while True:
        print("\n" + "-" * 30)
        print("1. Thêm chi tiêu")
        print("2. Xem chi tiêu")
        print("3. Thống kê theo loại")
        print("4. Tổng chi tiêu")
        print("5. Thoát")
        print("-" * 30)
        
        choice = input("Chọn chức năng (1-5): ")
        
        if choice == "1":
            print("Chọn loại chi tiêu:")
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat}")
            
            try:
                cat_choice = int(input("Chọn loại (1-5): "))
                if 1 <= cat_choice <= 5:
                    category = categories[cat_choice - 1]
                else:
                    print("Lựa chọn không hợp lệ!")
                    continue
            except ValueError:
                print("Vui lòng nhập số!")
                continue
            
            try:
                amount = float(input("Nhập số tiền: "))
                if amount <= 0:
                    print("Số tiền phải > 0!")
                    continue
            except ValueError:
                print("Số tiền không hợp lệ!")
                continue
            
            description = input("Mô tả (tùy chọn): ").strip()
            
            expense = {
                'category': category,
                'amount': amount,
                'description': description,
                'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            
            expenses.append(expense)
            print(f"Đã thêm chi tiêu: {category} - {amount:,} VND")
            
        elif choice == "2":
            if not expenses:
                print("Chưa có chi tiêu nào!")
            else:
                print("Danh sách chi tiêu:")
                for i, exp in enumerate(expenses, 1):
                    desc = f" - {exp['description']}" if exp['description'] else ""
                    print(f"  {i}. {exp['date']} | {exp['category']} | {exp['amount']:,} VND{desc}")
                    
        elif choice == "3":
            if not expenses:
                print("Chưa có chi tiêu nào!")
            else:
                category_totals = {}
                for exp in expenses:
                    cat = exp['category']
                    category_totals[cat] = category_totals.get(cat, 0) + exp['amount']
                
                print("Thống kê theo loại:")
                for cat, total in category_totals.items():
                    print(f"  {cat}: {total:,} VND")
                    
        elif choice == "4":
            if not expenses:
                print("Chưa có chi tiêu nào!")
            else:
                total = sum(exp['amount'] for exp in expenses)
                print(f"Tổng chi tiêu: {total:,} VND")
                print(f"Số lần chi tiêu: {len(expenses)}")
                print(f"Chi tiêu trung bình: {total/len(expenses):,.0f} VND")
                
        elif choice == "5":
            print("Tạm biệt!")
            break
            
        else:
            print("Lựa chọn không hợp lệ!")

# Uncomment để chạy demo:
# expense_tracker_demo()

# =============================================================================
# DEMO FUNCTIONS (FOR TESTING)
# =============================================================================

def run_all_demos():
    """Chạy tất cả các demo (dành cho testing)"""
    print("DEMO TẤT CẢ CHỨC NĂNG INPUT/OUTPUT")
    print("=" * 50)
    
    # Demo với dữ liệu mẫu thay vì input thật
    print("1. Personal Info Demo (với dữ liệu mẫu):")
    print("Tên: Nguyễn Văn Nam")
    print("Năm sinh: 1995")
    print("Tuổi: 29")
    print("Nhóm tuổi: người lớn")
    
    print("\n2. Calculator Demo (với dữ liệu mẫu):")
    print("15 + 7 = 22")
    print("20 - 8 = 12")
    print("6 * 9 = 54")
    print("100 / 4 = 25.0")
    
    print("\n3. BMI Calculator Demo (với dữ liệu mẫu):")
    weight, height = 70, 1.75
    bmi = weight / (height ** 2)
    print(f"Cân nặng: {weight} kg")
    print(f"Chiều cao: {height} m")
    print(f"BMI: {bmi:.2f}")
    print("Phân loại: Bình thường")
    
    print("\n4. Password Strength Demo:")
    passwords = ["weak", "Strong123", "VeryStrong123!"]
    for pwd in passwords:
        length_ok = len(pwd) >= 8
        has_upper = any(c.isupper() for c in pwd)
        has_lower = any(c.islower() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in pwd)
        score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
        
        if score >= 4:
            strength = "Mạnh"
        elif score >= 3:
            strength = "Trung bình"
        else:
            strength = "Yếu"
        
        print(f"  '{pwd}': {strength} ({score}/5)")

# Chạy demo với dữ liệu mẫu
run_all_demos()

print("\n" + "=" * 50)
print("HOÀN THÀNH SOLUTION 4!")
print("Để chạy các chương trình interactive, uncomment các demo function")
print("=" * 50)
