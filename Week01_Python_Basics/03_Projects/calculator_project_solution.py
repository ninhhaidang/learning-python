"""
Week 1 - Project Solution: Python Calculator
ĐÁP ÁN THAM KHẢO cho dự án Calculator

⚠️  LƯU Ý: Đây là đáp án tham khảo, hãy cố gắng tự làm trước khi xem!

Đáp án này minh họa:
- Cách tổ chức code thành functions
- Input validation và error handling
- Menu-driven programming
- Sử dụng global variables và constants
- String formatting và user interface
- Exception handling

Chức năng được implement:
1. Phép toán cơ bản (+, -, *, /, %, **)
2. Chuyển đổi đơn vị (nhiệt độ, độ dài, tiền tệ)
3. Tính toán hình học (diện tích, chu vi)
4. Lịch sử tính toán
5. Menu điều hướng

Author: Python Learning Course
Version: 1.0 - Solution Reference
"""

import math

# =============================================================================
# GLOBAL VARIABLES
# =============================================================================

# Lưu lịch sử tính toán
calculation_history = []

# Exchange rates (simplified)
EXCHANGE_RATES = {
    'USD_TO_VND': 24000,
    'EUR_TO_VND': 26000,
    'JPY_TO_VND': 160
}

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def clear_screen():
    """Clear console screen (cross-platform)"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def add_to_history(calculation, result):
    """Add calculation to history"""
    history_entry = f"{calculation} = {result}"
    calculation_history.append(history_entry)
    
    # Keep only last 10 calculations
    if len(calculation_history) > 10:
        calculation_history.pop(0)

def display_header():
    """Display calculator header"""
    print("=" * 60)
    print("🧮 PYTHON CALCULATOR - WEEK 1 PROJECT")
    print("=" * 60)

def display_menu():
    """Display main menu"""
    print("\n📋 MENU CHÍNH:")
    print("1. Phép toán cơ bản")
    print("2. Chuyển đổi nhiệt độ")
    print("3. Chuyển đổi độ dài")
    print("4. Chuyển đổi tiền tệ")
    print("5. Tính toán hình học")
    print("6. Xem lịch sử")
    print("7. Xóa lịch sử")
    print("0. Thoát")
    print("-" * 40)

def get_number_input(prompt):
    """Get and validate number input"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập một số hợp lệ!")

def get_integer_input(prompt):
    """Get and validate integer input"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

def format_result(result):
    """Format calculation result"""
    if isinstance(result, float) and result.is_integer():
        return int(result)
    elif isinstance(result, float):
        return round(result, 6)
    return result

# =============================================================================
# BASIC ARITHMETIC FUNCTIONS
# =============================================================================

def basic_arithmetic():
    """Perform basic arithmetic operations"""
    print("\n➕ PHÉP TOÁN CỞ BẢN")
    print("-" * 30)
    
    # Get first number
    num1 = get_number_input("Nhập số thứ nhất: ")
    
    # Get operator
    print("\nCác phép toán có sẵn:")
    print("+ : Cộng")
    print("- : Trừ")
    print("* : Nhân")
    print("/ : Chia")
    print("% : Chia lấy dư")
    print("**: Lũy thừa")
    
    operator = input("\nNhập phép toán: ").strip()
    
    # Get second number
    num2 = get_number_input("Nhập số thứ hai: ")
    
    # Perform calculation
    calculation = f"{num1} {operator} {num2}"
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("❌ Lỗi: Không thể chia cho 0!")
            return
        result = num1 / num2
    elif operator == "%":
        if num2 == 0:
            print("❌ Lỗi: Không thể chia cho 0!")
            return
        result = num1 % num2
    elif operator == "**":
        try:
            result = num1 ** num2
        except OverflowError:
            print("❌ Lỗi: Kết quả quá lớn!")
            return
    else:
        print("❌ Lỗi: Phép toán không hợp lệ!")
        return
    
    # Display result
    formatted_result = format_result(result)
    print(f"\n✅ Kết quả: {calculation} = {formatted_result}")
    
    # Add to history
    add_to_history(calculation, formatted_result)

# =============================================================================
# TEMPERATURE CONVERSION
# =============================================================================

def temperature_conversion():
    """Convert between temperature units"""
    print("\n🌡️  CHUYỂN ĐỔI NHIỆT ĐỘ")
    print("-" * 30)
    
    print("1. Celsius sang Fahrenheit")
    print("2. Fahrenheit sang Celsius")
    print("3. Celsius sang Kelvin")
    print("4. Kelvin sang Celsius")
    
    choice = get_integer_input("\nChọn loại chuyển đổi: ")
    
    if choice == 1:
        celsius = get_number_input("Nhập nhiệt độ Celsius: ")
        fahrenheit = (celsius * 9/5) + 32
        result = f"{celsius}°C = {fahrenheit}°F"
        print(f"✅ {result}")
        add_to_history("Temperature conversion", result)
        
    elif choice == 2:
        fahrenheit = get_number_input("Nhập nhiệt độ Fahrenheit: ")
        celsius = (fahrenheit - 32) * 5/9
        result = f"{fahrenheit}°F = {celsius:.2f}°C"
        print(f"✅ {result}")
        add_to_history("Temperature conversion", result)
        
    elif choice == 3:
        celsius = get_number_input("Nhập nhiệt độ Celsius: ")
        kelvin = celsius + 273.15
        result = f"{celsius}°C = {kelvin}K"
        print(f"✅ {result}")
        add_to_history("Temperature conversion", result)
        
    elif choice == 4:
        kelvin = get_number_input("Nhập nhiệt độ Kelvin: ")
        if kelvin < 0:
            print("❌ Lỗi: Kelvin không thể âm!")
            return
        celsius = kelvin - 273.15
        result = f"{kelvin}K = {celsius:.2f}°C"
        print(f"✅ {result}")
        add_to_history("Temperature conversion", result)
        
    else:
        print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# LENGTH CONVERSION
# =============================================================================

def length_conversion():
    """Convert between length units"""
    print("\n📏 CHUYỂN ĐỔI ĐỘ DÀI")
    print("-" * 30)
    
    print("1. Meter sang Kilometer")
    print("2. Kilometer sang Meter")
    print("3. Meter sang Centimeter")
    print("4. Centimeter sang Meter")
    print("5. Meter sang Feet")
    print("6. Feet sang Meter")
    
    choice = get_integer_input("\nChọn loại chuyển đổi: ")
    
    if choice == 1:
        meters = get_number_input("Nhập số meter: ")
        km = meters / 1000
        result = f"{meters}m = {km}km"
        print(f"✅ {result}")
        add_to_history("Length conversion", result)
        
    elif choice == 2:
        km = get_number_input("Nhập số kilometer: ")
        meters = km * 1000
        result = f"{km}km = {meters}m"
        print(f"✅ {result}")
        add_to_history("Length conversion", result)
        
    elif choice == 3:
        meters = get_number_input("Nhập số meter: ")
        cm = meters * 100
        result = f"{meters}m = {cm}cm"
        print(f"✅ {result}")
        add_to_history("Length conversion", result)
        
    elif choice == 4:
        cm = get_number_input("Nhập số centimeter: ")
        meters = cm / 100
        result = f"{cm}cm = {meters}m"
        print(f"✅ {result}")
        add_to_history("Length conversion", result)
        
    elif choice == 5:
        meters = get_number_input("Nhập số meter: ")
        feet = meters * 3.28084
        result = f"{meters}m = {feet:.2f}ft"
        print(f"✅ {result}")
        add_to_history("Length conversion", result)
        
    elif choice == 6:
        feet = get_number_input("Nhập số feet: ")
        meters = feet / 3.28084
        result = f"{feet}ft = {meters:.2f}m"
        print(f"✅ {result}")
        add_to_history("Length conversion", result)
        
    else:
        print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# CURRENCY CONVERSION
# =============================================================================

def currency_conversion():
    """Convert between currencies"""
    print("\n💰 CHUYỂN ĐỔI TIỀN TỆ")
    print("-" * 30)
    
    print("1. USD sang VND")
    print("2. VND sang USD")
    print("3. EUR sang VND")
    print("4. VND sang EUR")
    
    choice = get_integer_input("\nChọn loại chuyển đổi: ")
    
    if choice == 1:
        usd = get_number_input("Nhập số USD: ")
        vnd = usd * EXCHANGE_RATES['USD_TO_VND']
        result = f"${usd} = {vnd:,.0f} VND"
        print(f"✅ {result}")
        add_to_history("Currency conversion", result)
        
    elif choice == 2:
        vnd = get_number_input("Nhập số VND: ")
        usd = vnd / EXCHANGE_RATES['USD_TO_VND']
        result = f"{vnd:,.0f} VND = ${usd:.2f}"
        print(f"✅ {result}")
        add_to_history("Currency conversion", result)
        
    elif choice == 3:
        eur = get_number_input("Nhập số EUR: ")
        vnd = eur * EXCHANGE_RATES['EUR_TO_VND']
        result = f"€{eur} = {vnd:,.0f} VND"
        print(f"✅ {result}")
        add_to_history("Currency conversion", result)
        
    elif choice == 4:
        vnd = get_number_input("Nhập số VND: ")
        eur = vnd / EXCHANGE_RATES['EUR_TO_VND']
        result = f"{vnd:,.0f} VND = €{eur:.2f}"
        print(f"✅ {result}")
        add_to_history("Currency conversion", result)
        
    else:
        print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# GEOMETRY CALCULATIONS
# =============================================================================

def geometry_calculations():
    """Perform geometry calculations"""
    print("\n📐 TÍNH TOÁN HÌNH HỌC")
    print("-" * 30)
    
    print("1. Hình tròn (chu vi và diện tích)")
    print("2. Hình chữ nhật (chu vi và diện tích)")
    print("3. Hình tam giác (diện tích)")
    print("4. Hình vuông (chu vi và diện tích)")
    
    choice = get_integer_input("\nChọn hình: ")
    
    if choice == 1:
        radius = get_number_input("Nhập bán kính: ")
        if radius < 0:
            print("❌ Lỗi: Bán kính không thể âm!")
            return
        
        circumference = 2 * math.pi * radius
        area = math.pi * radius ** 2
        
        print(f"✅ Hình tròn bán kính {radius}:")
        print(f"   Chu vi: {circumference:.2f}")
        print(f"   Diện tích: {area:.2f}")
        
        result = f"Circle r={radius}: C={circumference:.2f}, A={area:.2f}"
        add_to_history("Geometry", result)
        
    elif choice == 2:
        length = get_number_input("Nhập chiều dài: ")
        width = get_number_input("Nhập chiều rộng: ")
        
        if length < 0 or width < 0:
            print("❌ Lỗi: Kích thước không thể âm!")
            return
        
        perimeter = 2 * (length + width)
        area = length * width
        
        print(f"✅ Hình chữ nhật {length}x{width}:")
        print(f"   Chu vi: {perimeter}")
        print(f"   Diện tích: {area}")
        
        result = f"Rectangle {length}x{width}: P={perimeter}, A={area}"
        add_to_history("Geometry", result)
        
    elif choice == 3:
        base = get_number_input("Nhập đáy: ")
        height = get_number_input("Nhập chiều cao: ")
        
        if base < 0 or height < 0:
            print("❌ Lỗi: Kích thước không thể âm!")
            return
        
        area = 0.5 * base * height
        
        print(f"✅ Hình tam giác đáy {base}, cao {height}:")
        print(f"   Diện tích: {area}")
        
        result = f"Triangle base={base}, height={height}: A={area}"
        add_to_history("Geometry", result)
        
    elif choice == 4:
        side = get_number_input("Nhập cạnh: ")
        
        if side < 0:
            print("❌ Lỗi: Cạnh không thể âm!")
            return
        
        perimeter = 4 * side
        area = side ** 2
        
        print(f"✅ Hình vuông cạnh {side}:")
        print(f"   Chu vi: {perimeter}")
        print(f"   Diện tích: {area}")
        
        result = f"Square side={side}: P={perimeter}, A={area}"
        add_to_history("Geometry", result)
        
    else:
        print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# HISTORY FUNCTIONS
# =============================================================================

def display_history():
    """Display calculation history"""
    print("\n📜 LỊCH SỬ TÍNH TOÁN")
    print("-" * 40)
    
    if not calculation_history:
        print("Chưa có tính toán nào được lưu.")
    else:
        for i, entry in enumerate(calculation_history, 1):
            print(f"{i:2d}. {entry}")
    
    print("-" * 40)

def clear_history():
    """Clear calculation history"""
    global calculation_history
    calculation_history.clear()
    print("✅ Đã xóa lịch sử tính toán!")

# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    """Main calculator program"""
    print("🎉 Chào mừng đến với Python Calculator!")
    print("Calculator này được xây dựng với kiến thức Week 1")
    
    while True:
        display_header()
        display_menu()
        
        try:
            choice = get_integer_input("Chọn chức năng (0-7): ")
            
            if choice == 0:
                print("\n👋 Cảm ơn bạn đã sử dụng Python Calculator!")
                print("Hẹn gặp lại! 🚀")
                break
                
            elif choice == 1:
                basic_arithmetic()
                
            elif choice == 2:
                temperature_conversion()
                
            elif choice == 3:
                length_conversion()
                
            elif choice == 4:
                currency_conversion()
                
            elif choice == 5:
                geometry_calculations()
                
            elif choice == 6:
                display_history()
                
            elif choice == 7:
                clear_history()
                
            else:
                print("❌ Lựa chọn không hợp lệ! Vui lòng chọn từ 0-7.")
            
            # Pause để user xem kết quả
            input("\nNhấn Enter để tiếp tục...")
            
        except KeyboardInterrupt:
            print("\n\n👋 Chương trình bị dừng bởi người dùng. Tạm biệt!")
            break
        except Exception as e:
            print(f"❌ Có lỗi xảy ra: {e}")
            input("Nhấn Enter để tiếp tục...")

# =============================================================================
# RUN PROGRAM
# =============================================================================

if __name__ == "__main__":
    main()
