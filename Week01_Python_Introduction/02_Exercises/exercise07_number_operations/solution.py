# Exercise 07: Number Operations - Solution

# =============================================================================
# EXERCISE 07: NUMBER OPERATIONS
# =============================================================================

print("=" * 60)
print("    EXERCISE 07: NUMBER OPERATIONS")
print("=" * 60)

# =============================================================================
# PHẦN 1: PHÉP TOÁN CƠ BẢN
# =============================================================================

print("\n=== PHÉP TOÁN CƠ BẢN ===")

# 1. Tạo biến a và b
a = 15
b = 4
print(f"a = {a}, b = {b}")

# 2. Tổng
sum_result = a + b
print(f"Tổng: {a} + {b} = {sum_result}")

# 3. Hiệu
diff_result = a - b
print(f"Hiệu: {a} - {b} = {diff_result}")

# 4. Tích
product_result = a * b
print(f"Tích: {a} * {b} = {product_result}")

# 5. Thương (chia thực)
division_result = a / b
print(f"Thương: {a} / {b} = {division_result}")

# 6. Chia lấy phần nguyên
floor_div_result = a // b
print(f"Chia nguyên: {a} // {b} = {floor_div_result}")

# 7. Phần dư
modulo_result = a % b
print(f"Phần dư: {a} % {b} = {modulo_result}")

# 8. Lũy thừa
power_result = a ** b
print(f"Lũy thừa: {a} ** {b} = {power_result}")

# =============================================================================
# PHẦN 2: THỨ TỰ ƯU TIÊN PHÉP TOÁN
# =============================================================================

print("\n=== THỨ TỰ ƯU TIÊN ===")

# 9. Không dùng ngoặc (nhân trước, cộng sau)
expr1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {expr1}")

# 10. Có ngoặc (cộng trước, nhân sau)
expr2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {expr2}")

# 11. Phép toán hỗn hợp
expr3 = 10 - 6 / 2 + 1
print(f"10 - 6 / 2 + 1 = {expr3}")

# 12. Lũy thừa liên tiếp (từ phải qua trái)
expr4 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {expr4}")  # 2**(3**2) = 2**9 = 512

# Giải thích chi tiết
print("\nGiải thích:")
print(f"  3 ** 2 = {3 ** 2}")
print(f"  2 ** 9 = {2 ** 9}")

# =============================================================================
# PHẦN 3: LÀM VIỆC VỚI SỐ THỰC
# =============================================================================

print("\n=== SỐ THỰC ===")

# 13-14. Tính diện tích hình tròn
pi = 3.14159
radius = 5
print(f"Pi = {pi}, bán kính = {radius}")

# 14. Diện tích = π * r²
area = pi * radius ** 2
print(f"Diện tích = π * r² = {pi} * {radius}² = {area}")

# 15. Chu vi = 2 * π * r
circumference = 2 * pi * radius
print(f"Chu vi = 2 * π * r = 2 * {pi} * {radius} = {circumference}")

# 16. Làm tròn diện tích
area_rounded = round(area, 2)
print(f"Diện tích làm tròn = {area_rounded}")

# =============================================================================
# PHẦN 4: HÀM TOÁN HỌC BUILT-IN
# =============================================================================

print("\n=== HÀM TOÁN HỌC ===")

# 17. Giá trị tuyệt đối
abs_value = abs(-25)
print(f"abs(-25) = {abs_value}")

# 18. Giá trị lớn nhất
numbers = [10, 5, 8, 20, 3]
max_value = max(numbers)
print(f"max({numbers}) = {max_value}")

# 19. Giá trị nhỏ nhất
min_value = min(numbers)
print(f"min({numbers}) = {min_value}")

# 20. Tổng của list
sum_list = [1, 2, 3, 4, 5]
sum_value = sum(sum_list)
print(f"sum({sum_list}) = {sum_value}")

# 21. Làm tròn
round1 = round(3.7)
round2 = round(3.2)
print(f"round(3.7) = {round1}, round(3.2) = {round2}")

# Thêm ví dụ làm tròn với số chữ số thập phân
round3 = round(3.14159, 2)
print(f"round(3.14159, 2) = {round3}")

# =============================================================================
# PHẦN 5: SỐ HỌC VỚI MODULE MATH
# =============================================================================

print("\n=== MODULE MATH ===")

# 22. Import module math
import math

# 23. Căn bậc 2
sqrt_result = math.sqrt(16)
print(f"sqrt(16) = {sqrt_result}")

# 24. Làm tròn lên
ceil_result = math.ceil(3.2)
print(f"ceil(3.2) = {ceil_result}")

# 25. Làm tròn xuống
floor_result = math.floor(3.8)
print(f"floor(3.8) = {floor_result}")

# 26. Sin của π/2 (90 độ)
sin_result = math.sin(math.pi/2)
print(f"sin(π/2) = {sin_result}")

# Thêm một số hàm math khác
print(f"\nCác hằng số toán học:")
print(f"π (pi) = {math.pi}")
print(f"e = {math.e}")

print(f"\nCác hàm toán học khác:")
print(f"cos(0) = {math.cos(0)}")
print(f"tan(π/4) = {math.tan(math.pi/4)}")
print(f"log(e) = {math.log(math.e)}")
print(f"log10(100) = {math.log10(100)}")

# =============================================================================
# PHẦN 6: ỨNG DỤNG THỰC TẾ
# =============================================================================

print("\n=== ỨNG DỤNG THỰC TẾ ===")

# 27. Tính BMI
weight = 70  # kg
height = 1.75  # m
bmi = weight / (height ** 2)
print(f"BMI = {weight} / ({height})² = {bmi:.2f}")

# Phân loại BMI
if bmi < 18.5:
    bmi_category = "Thiếu cân"
elif bmi < 25:
    bmi_category = "Bình thường"
elif bmi < 30:
    bmi_category = "Thừa cân"
else:
    bmi_category = "Béo phì"
print(f"Phân loại: {bmi_category}")

# 28. Chuyển đổi nhiệt độ: C -> F
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Bonus: F -> C
fahrenheit_input = 77
celsius_converted = (fahrenheit_input - 32) * 5/9
print(f"{fahrenheit_input}°F = {celsius_converted:.1f}°C")

# 29. Tính lãi kép
principal = 1_000_000  # VND
rate = 0.05  # 5% per year
time = 3  # years
compound_amount = principal * (1 + rate) ** time
interest_earned = compound_amount - principal

print(f"Gốc: {principal:,} VND")
print(f"Lãi suất: {rate*100}%/năm")
print(f"Thời gian: {time} năm")
print(f"Số tiền sau {time} năm: {compound_amount:,.0f} VND")
print(f"Lãi thu được: {interest_earned:,.0f} VND")

# 30. Khoảng cách 2 điểm (công thức Euclidean)
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Khoảng cách từ ({x1},{y1}) đến ({x2},{y2}) = {distance}")

# =============================================================================
# BONUS: CÁC PHÉP TOÁN NÂNG CAO
# =============================================================================

print("\n=== BONUS: PHÉP TOÁN NÂNG CAO ===")

# Compound assignment operators
x = 10
print(f"x ban đầu = {x}")

x += 5
print(f"x += 5 → x = {x}")

x *= 2
print(f"x *= 2 → x = {x}")

x //= 3
print(f"x //= 3 → x = {x}")

# Divmod function
quotient, remainder = divmod(17, 5)
print(f"divmod(17, 5) = ({quotient}, {remainder})")
print(f"17 ÷ 5 = {quotient} dư {remainder}")

# Power với modulo
power_mod = pow(2, 10, 1000)  # 2^10 % 1000
print(f"pow(2, 10, 1000) = 2^10 % 1000 = {power_mod}")

# Số phức
complex_num = 3 + 4j
print(f"Số phức: {complex_num}")
print(f"Độ lớn: {abs(complex_num)}")
print(f"Phần thực: {complex_num.real}")
print(f"Phần ảo: {complex_num.imag}")

print("\n" + "=" * 60)
print("         HOÀN THÀNH NUMBER OPERATIONS!")
print("=" * 60)
