# Hướng dẫn: Variables & Assignments

## Lý thuyết cần biết

### 1. Biến trong Python

- **Biến** là tên được gán cho một vùng nhớ lưu trữ dữ liệu
- Python không cần khai báo kiểu dữ liệu trước
- Kiểu dữ liệu được xác định tự động khi gán giá trị

### 2. Quy tắc đặt tên biến

```python
# ✅ Đúng
student_name = "Nguyen Van A"    # Sử dụng underscore
age2 = 20                       # Có thể có số (không đầu)
_private = "internal"           # Bắt đầu bằng underscore
myVariable = "camelCase"        # CamelCase (ít dùng trong Python)

# ❌ Sai
2age = 20           # Không được bắt đầu bằng số
class = "A"         # Không được dùng từ khóa
student-name = "A"  # Không được dùng dấu gạch ngang
```

### 3. Các cách gán giá trị

#### Gán cơ bản

```python
name = "Python"
age = 25
height = 170.5
is_active = True
```

#### Gán nhiều biến cùng lúc

```python
# Gán khác nhau
x, y, z = 1, 2, 3

# Gán cùng giá trị
a = b = c = 10
```

#### Hoán đổi giá trị

```python
# Cách cũ (nhiều ngôn ngữ khác)
temp = a
a = b
b = temp

# Cách Python (elegant)
a, b = b, a
```

### 4. Kiểm tra thông tin biến

```python
name = "Python"
print(type(name))     # <class 'str'>
print(id(name))       # Địa chỉ bộ nhớ
```

## Các bước thực hiện

### Bước 1: Khai báo biến cơ bản

```python
# Thông tin cá nhân
student_name = "Nguyen Van A"  # Thay bằng tên của bạn
age = 20                       # Thay bằng tuổi của bạn
height = 175                   # Thay bằng chiều cao của bạn
is_student = True
```

### Bước 2: Tính toán từ biến có sẵn

```python
# Tính năm sinh
birth_year = 2024 - age

# Chuyển đổi đơn vị
height_in_meters = height / 100

# Kết hợp chuỗi
full_info = student_name + " - " + str(age) + " tuổi"
# Hoặc dùng f-string (modern):
full_info = f"{student_name} - {age} tuổi"
```

### Bước 3: Gán nhiều biến

```python
# Cách 1: Gán khác nhau
x, y, z = 10, 20, 30

# Cách 2: Gán cùng giá trị
a = b = c = 100

# Hoán đổi
num1, num2 = 5, 10
print(f"Trước: num1 = {num1}, num2 = {num2}")
num1, num2 = num2, num1  # Hoán đổi
print(f"Sau: num1 = {num1}, num2 = {num2}")
```

### Bước 4: In kết quả đẹp

```python
print("=== THÔNG TIN CÁ NHÂN ===")
print(f"Tên: {student_name}")
print(f"Tuổi: {age} năm")
print(f"Chiều cao: {height} cm ({height_in_meters} m)")
print(f"Năm sinh: {birth_year}")
print(f"Là sinh viên: {is_student}")
print(f"Thông tin đầy đủ: {full_info}")
```

## Lưu ý quan trọng

### 1. Naming Convention

- Python khuyến khích dùng **snake_case** cho tên biến
- Tên biến nên có ý nghĩa, dễ hiểu
- Tránh dùng tên quá ngắn (x, y) trừ khi là biến tạm

### 2. Kiểu dữ liệu động

```python
x = 10       # x là int
x = "Hello"  # Bây giờ x là string (OK trong Python)
```

### 3. Memory Management

- Python tự động quản lý bộ nhớ
- Các biến cùng giá trị có thể dùng chung bộ nhớ (cho số nhỏ)

## Tips & Tricks

### 1. Debug với type() và id()

```python
name = "Python"
print(f"Giá trị: {name}")
print(f"Kiểu: {type(name)}")
print(f"ID: {id(name)}")
```

### 2. Gán có điều kiện

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

### 3. Unpacking

```python
data = [1, 2, 3, 4, 5]
first, second, *rest = data
# first = 1, second = 2, rest = [3, 4, 5]
```
