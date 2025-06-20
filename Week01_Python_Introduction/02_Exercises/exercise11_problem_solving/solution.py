"""
Exercise 11: Problem Solving Challenge - Complete Solution

This file demonstrates advanced problem-solving skills using Python fundamentals.
Each challenge focuses on real-world problems that require logical thinking.

Key concepts demonstrated:
- Problem decomposition
- Input validation
- String manipulation
- Mathematical calculations
- Conditional logic
- Error handling
"""

import random
import string

def challenge1_tip_calculator():
    """Challenge 1: Máy tính tiền tip"""
    print("=== CALCULATOR TIP ===")
    
    try:
        # Nhận input từ user
        bill_amount = float(input("Số tiền hóa đơn (VND): "))
        tip_percentage = float(input("Tỷ lệ tip (%): "))
        num_people = int(input("Số người chia bill: "))
        
        if num_people <= 0:
            print("Số người phải lớn hơn 0!")
            return
        
        # Tính toán
        tip_total = bill_amount * (tip_percentage / 100)
        tip_per_person = tip_total / num_people
        total_per_person = (bill_amount + tip_total) / num_people
        
        # Hiển thị kết quả
        print(f"\nSố tiền hóa đơn: {bill_amount:,.0f} VND")
        print(f"Tỷ lệ tip: {tip_percentage}%")
        print(f"Số người: {num_people}")
        print()
        print(f"Tip total: {tip_total:,.0f} VND")
        print(f"Tip mỗi người: {tip_per_person:,.0f} VND")
        print(f"Tổng mỗi người: {total_per_person:,.0f} VND")
        
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

def challenge2_password_checker():
    """Challenge 2: Kiểm tra mật khẩu mạnh"""
    print("=== KIỂM TRA MẬT KHẨU ===")
    
    password = input("Nhập mật khẩu cần kiểm tra: ")
    
    # Các tiêu chí kiểm tra
    criteria = {
        'length': len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digit': any(c.isdigit() for c in password),
        'special': any(c in string.punctuation for c in password)
    }
    
    score = sum(criteria.values())
    
    print(f"\nMật khẩu: \"{password}\"")
    
    # Hiển thị kết quả từng tiêu chí
    if criteria['length']:
        print("✓ Độ dài >= 8 ký tự")
    else:
        print("✗ Độ dài < 8 ký tự")
        
    if criteria['uppercase']:
        print("✓ Có chữ hoa")
    else:
        print("✗ Thiếu chữ hoa")
        
    if criteria['lowercase']:
        print("✓ Có chữ thường")
    else:
        print("✗ Thiếu chữ thường")
        
    if criteria['digit']:
        print("✓ Có số")
    else:
        print("✗ Thiếu số")
        
    if criteria['special']:
        print("✓ Có ký tự đặc biệt")
    else:
        print("✗ Thiếu ký tự đặc biệt")
    
    # Đánh giá tổng thể
    if score == 5:
        strength = "RẤT MẠNH!"
    elif score == 4:
        strength = "MẠNH"
    elif score == 3:
        strength = "TRUNG BÌNH"
    elif score == 2:
        strength = "YẾU"
    else:
        strength = "RẤT YẾU"
    
    print(f"\nĐiểm: {score}/5 - MẬT KHẨU {strength}")

def challenge3_unit_converter():
    """Challenge 3: Chuyển đổi đơn vị"""
    print("=== CHUYỂN ĐỔI ĐƠN VỊ ===")
    print("1. Celsius ↔ Fahrenheit")
    print("2. Kilogram ↔ Pound")
    print("3. Kilometer ↔ Mile")
    
    try:
        choice = input("Chọn (1-3): ")
        
        if choice == "1":
            # Temperature conversion
            temp_type = input("Chuyển từ (C)elsius hay (F)ahrenheit? ").upper()
            
            if temp_type == "C":
                celsius = float(input("Nhập độ C: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}°C = {fahrenheit:.1f}°F")
            elif temp_type == "F":
                fahrenheit = float(input("Nhập độ F: "))
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}°F = {celsius:.1f}°C")
            else:
                print("Lựa chọn không hợp lệ!")
                
        elif choice == "2":
            # Weight conversion
            weight_type = input("Chuyển từ (K)g hay (P)ound? ").upper()
            
            if weight_type == "K":
                kg = float(input("Nhập kg: "))
                pound = kg * 2.20462
                print(f"{kg} kg = {pound:.2f} pound")
            elif weight_type == "P":
                pound = float(input("Nhập pound: "))
                kg = pound / 2.20462
                print(f"{pound} pound = {kg:.2f} kg")
            else:
                print("Lựa chọn không hợp lệ!")
                
        elif choice == "3":
            # Distance conversion
            dist_type = input("Chuyển từ (K)m hay (M)ile? ").upper()
            
            if dist_type == "K":
                km = float(input("Nhập km: "))
                mile = km * 0.621371
                print(f"{km} km = {mile:.2f} mile")
            elif dist_type == "M":
                mile = float(input("Nhập mile: "))
                km = mile / 0.621371
                print(f"{mile} mile = {km:.2f} km")
            else:
                print("Lựa chọn không hợp lệ!")
        else:
            print("Lựa chọn không hợp lệ!")
            
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

def challenge4_phone_analyzer():
    """Challenge 4: Phân tích số điện thoại"""
    print("=== PHÂN TÍCH SỐ ĐIỆN THOẠI ===")
    
    phone_input = input("Nhập số điện thoại: ")
    
    # Loại bỏ các ký tự không phải số
    phone_clean = ''.join(c for c in phone_input if c.isdigit())
    
    print(f"Input: \"{phone_input}\"")
    print(f"Chuẩn hóa: \"{phone_clean}\"")
    
    # Kiểm tra tính hợp lệ (số VN thường 10-11 số)
    if len(phone_clean) == 10 or len(phone_clean) == 11:
        valid = True
        
        # Xác định vùng miền (đơn giản hóa)
        if phone_clean.startswith(('024', '028')):
            area = "Hà Nội/HCM"
        elif phone_clean.startswith(('09', '08', '07', '05', '03')):
            area = "Di động"
        else:
            area = "Không xác định"
        
        # Format đẹp
        if len(phone_clean) == 10:
            formatted = f"({phone_clean[:3]}) {phone_clean[3:6]}-{phone_clean[6:]}"
        else:
            formatted = f"({phone_clean[:3]}) {phone_clean[3:7]}-{phone_clean[7:]}"
            
    else:
        valid = False
        area = "Không hợp lệ"
        formatted = phone_clean
    
    print(f"Vùng: {area}")
    print(f"Hợp lệ: {'✓' if valid else '✗'}")
    print(f"Format: {formatted}")

def challenge5_rock_paper_scissors():
    """Challenge 5: Game rock-paper-scissors"""
    print("=== ROCK-PAPER-SCISSORS ===")
    
    choices = ['rock', 'paper', 'scissors']
    choice_display = {'rock': 'Rock', 'paper': 'Paper', 'scissors': 'Scissors'}
    
    player_score = 0
    computer_score = 0
    round_num = 1
    
    while True:
        print(f"\nRound {round_num}")
        print("Chọn: (r)ock, (p)aper, (s)cissors, hoặc (q)uit")
        
        player_input = input("Lựa chọn của bạn: ").lower()
        
        if player_input == 'q':
            break
        
        # Chuyển đổi input
        if player_input == 'r':
            player_choice = 'rock'
        elif player_input == 'p':
            player_choice = 'paper'
        elif player_input == 's':
            player_choice = 'scissors'
        else:
            print("Lựa chọn không hợp lệ!")
            continue
        
        # Máy chọn random
        computer_choice = random.choice(choices)
        
        # Xác định người thắng
        if player_choice == computer_choice:
            result = "Hòa!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            result = "Bạn thắng!"
            player_score += 1
        else:
            result = "Máy thắng!"
            computer_score += 1
        
        print(f"Round {round_num}: Bạn ({choice_display[player_choice]}) vs Máy ({choice_display[computer_choice]}) → {result}")
        
        round_num += 1
    
    # Hiển thị thống kê cuối game
    print(f"\nKẾT QUẢ: Bạn {player_score} - {computer_score} Máy")
    
    if player_score > computer_score:
        print("Bạn là NHẤT!")
    elif player_score < computer_score:
        print("Máy thắng!")
    else:
        print("Hòa!")

def main_menu():
    """Menu chính cho tất cả challenges"""
    while True:
        print("\n" + "="*50)
        print("=== PROBLEM SOLVING CHALLENGES ===")
        print("1. Máy tính tiền tip")
        print("2. Kiểm tra mật khẩu mạnh")
        print("3. Chuyển đổi đơn vị")
        print("4. Phân tích số điện thoại")
        print("5. Game Rock-Paper-Scissors")
        print("6. Thoát")
        
        choice = input("\nChọn challenge (1-6): ")
        
        if choice == "1":
            challenge1_tip_calculator()
        elif choice == "2":
            challenge2_password_checker()
        elif choice == "3":
            challenge3_unit_converter()
        elif choice == "4":
            challenge4_phone_analyzer()
        elif choice == "5":
            challenge5_rock_paper_scissors()
        elif choice == "6":
            print("Cảm ơn bạn đã tham gia Problem Solving Challenges!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để tiếp tục...")

# Chạy chương trình chính
if __name__ == "__main__":
    main_menu()
