# Exercise 04: Variables & Assignments - Solution

# =============================================================================
# PHẦN 1: KHAI BÁO BIẾN CƠ BẢN
# =============================================================================

# 1. Thông tin cá nhân
student_name = "Nguyen Van A"    # Thay bằng tên thật của bạn
age = 20                         # Thay bằng tuổi thật của bạn  
height = 175                     # Thay bằng chiều cao thật (cm)
is_student = True

# =============================================================================
# PHẦN 2: GÁN GIÁ TRỊ TỪ BIẾN KHÁC
# =============================================================================

# 5. Tính năm sinh
birth_year = 2024 - age

# 6. Chuyển đổi chiều cao sang mét
height_in_meters = height / 100

# 7. Kết hợp thông tin thành chuỗi
full_info = f"{student_name} - {age} tuổi"

# =============================================================================
# PHẦN 3: GÁN NHIỀU BIẾN CÙNG LÚC
# =============================================================================

# 8. Gán nhiều biến khác giá trị trên một dòng
x, y, z = 10, 20, 30

# 9. Gán nhiều biến cùng giá trị
a = b = c = 100

# 10. Hoán đổi giá trị
num1, num2 = 5, 10
print(f"Trước hoán đổi: num1 = {num1}, num2 = {num2}")
# Hoán đổi bằng tuple unpacking (Python style)
num1, num2 = num2, num1

# =============================================================================
# PHẦN 4: IN KẾT QUẢ
# =============================================================================

print("=" * 50)
print("    EXERCISE 04: VARIABLES & ASSIGNMENTS")
print("=" * 50)

# 11. In thông tin cá nhân
print("\n=== THÔNG TIN CÁ NHÂN ===")
print(f"Tên: {student_name}")
print(f"Tuổi: {age} năm")
print(f"Chiều cao: {height} cm ({height_in_meters:.2f} m)")
print(f"Năm sinh: {birth_year}")
print(f"Là sinh viên: {is_student}")
print(f"Thông tin đầy đủ: {full_info}")

# In các biến số
print("\n=== CÁC BIẾN SỐ ===")
print(f"x = {x}, y = {y}, z = {z}")
print(f"a = {a}, b = {b}, c = {c}")

# In kết quả hoán đổi
print("\n=== HOÁN ĐỔI GIÁ TRỊ ===")
print(f"Sau hoán đổi: num1 = {num1}, num2 = {num2}")

# 12. In kiểu dữ liệu của các biến
print("\n=== THÔNG TIN KỸ THUẬT ===")
print("Kiểu dữ liệu:")
print(f"- student_name: {type(student_name)}")
print(f"- age: {type(age)}")
print(f"- height: {type(height)}")
print(f"- is_student: {type(is_student)}")
print(f"- birth_year: {type(birth_year)}")
print(f"- height_in_meters: {type(height_in_meters)}")
print(f"- full_info: {type(full_info)}")

# 13. In địa chỉ bộ nhớ (ID) của các biến số
print("\nĐịa chỉ bộ nhớ (ID):")
print(f"- age: {id(age)}")
print(f"- height: {id(height)}")
print(f"- x: {id(x)}")
print(f"- a: {id(a)}")
print(f"- b: {id(b)}")  # Chú ý: a, b, c có thể cùng ID vì cùng giá trị
print(f"- c: {id(c)}")

# =============================================================================
# BONUS: DEMO THÊM VỀ BIẾN
# =============================================================================

print("\n=== BONUS: THỬ NGHIỆM THÊM ===")

# Thay đổi kiểu dữ liệu của biến
demo_var = 10
print(f"demo_var = {demo_var}, type = {type(demo_var)}")

demo_var = "Hello"
print(f"demo_var = {demo_var}, type = {type(demo_var)}")

demo_var = [1, 2, 3]
print(f"demo_var = {demo_var}, type = {type(demo_var)}")

# Multiple assignment khác
name, *scores, final = "Alice", 85, 90, 88, 92
print(f"name = {name}")
print(f"scores = {scores}")
print(f"final = {final}")

print("\n" + "=" * 50)
print("             HOÀN THÀNH!")
print("=" * 50)