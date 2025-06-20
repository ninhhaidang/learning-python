# Hướng dẫn: Number Operations

## Lý thuyết cần biết

### 1. Các phép toán cơ bản trong Python

#### Toán tử số học

```python
a = 15
b = 4

# Cộng
result = a + b      # 19

# Trừ
result = a - b      # 11

# Nhân
result = a * b      # 60

# Chia (luôn trả về float)
result = a / b      # 3.75

# Chia lấy phần nguyên
result = a // b     # 3

# Chia lấy phần dư (modulo)
result = a % b      # 3

# Lũy thừa
result = a ** b     # 50625
```

### 2. Thứ tự ưu tiên phép toán (PEMDAS)

1. **P**arentheses (Ngoặc đơn): `()`
2. **E**xponents (Lũy thừa): `**`
3. **M**ultiplication/Division (Nhân/Chia): `*, /, //, %`
4. **A**ddition/Subtraction (Cộng/Trừ): `+, -`

```python
# Không có ngoặc
result = 2 + 3 * 4      # = 2 + 12 = 14

# Có ngoặc
result = (2 + 3) * 4    # = 5 * 4 = 20

# Lũy thừa từ phải qua trái
result = 2 ** 3 ** 2    # = 2 ** (3 ** 2) = 2 ** 9 = 512
```

### 3. Làm việc với số thực

#### Độ chính xác số thực

```python
# Phép chia luôn trả về float
result = 10 / 3         # 3.3333333333333335

# Làm tròn
rounded = round(10/3, 2)  # 3.33
```

#### Vấn đề với floating point

```python
# Có thể có sai số nhỏ
result = 0.1 + 0.2      # 0.30000000000000004 (không phải 0.3)

# Nên so sánh với độ chính xác
import math
def almost_equal(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance
```

### 4. Hàm toán học built-in

```python
# Giá trị tuyệt đối
abs(-25)                # 25
abs(3.14)               # 3.14

# Tìm min/max
max(1, 5, 3, 9, 2)      # 9
min([10, 5, 8, 20, 3])  # 3

# Tính tổng
sum([1, 2, 3, 4, 5])    # 15
sum(range(1, 6))        # 15

# Làm tròn
round(3.7)              # 4
round(3.14159, 2)       # 3.14

# Lũy thừa (cách khác)
pow(2, 3)               # 8 (giống 2 ** 3)
pow(2, 3, 5)            # 3 (2**3 % 5)
```

### 5. Module math

```python
import math

# Hằng số toán học
math.pi                 # 3.141592653589793
math.e                  # 2.718281828459045

# Căn bậc hai
math.sqrt(16)           # 4.0
math.sqrt(2)            # 1.4142135623730951

# Làm tròn
math.ceil(3.2)          # 4 (làm tròn lên)
math.floor(3.8)         # 3 (làm tròn xuống)

# Hàm lượng giác (đơn vị radian)
math.sin(math.pi/2)     # 1.0 (sin 90°)
math.cos(0)             # 1.0 (cos 0°)
math.tan(math.pi/4)     # 1.0 (tan 45°)

# Chuyển đổi độ/radian
math.radians(90)        # 1.5707963267948966 (90° to radian)
math.degrees(math.pi)   # 180.0 (π radian to degree)

# Logarit
math.log(math.e)        # 1.0 (log tự nhiên)
math.log10(100)         # 2.0 (log cơ số 10)
math.log(8, 2)          # 3.0 (log cơ số 2)
```

## Các bước thực hiện

### Bước 1: Phép toán cơ bản

```python
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Tổng: {a} + {b} = {a + b}")
print(f"Hiệu: {a} - {b} = {a - b}")
print(f"Tích: {a} * {b} = {a * b}")
print(f"Thương: {a} / {b} = {a / b}")
print(f"Chia nguyên: {a} // {b} = {a // b}")
print(f"Phần dư: {a} % {b} = {a % b}")
print(f"Lũy thừa: {a} ** {b} = {a ** b}")
```

### Bước 2: Thứ tự ưu tiên

```python
# So sánh với và không có ngoặc
expr1 = 2 + 3 * 4
expr2 = (2 + 3) * 4
print(f"2 + 3 * 4 = {expr1}")
print(f"(2 + 3) * 4 = {expr2}")

# Phép toán phức tạp
expr3 = 10 - 6 / 2 + 1
print(f"10 - 6 / 2 + 1 = {expr3}")

# Lũy thừa liên tiếp
expr4 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {expr4}")  # 2**(3**2) = 2**9 = 512
```

### Bước 3: Ứng dụng thực tế

```python
import math

# Tính diện tích hình tròn
pi = 3.14159
radius = 5
area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"Diện tích hình tròn: {area}")
print(f"Chu vi hình tròn: {circumference}")
print(f"Diện tích làm tròn: {round(area, 2)}")

# BMI calculator
weight = 70  # kg
height = 1.75  # m
bmi = weight / (height ** 2)
print(f"BMI = {bmi:.2f}")

# Chuyển đổi nhiệt độ
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

## Lưu ý quan trọng

### 1. Chia cho 0

```python
# Sẽ gây lỗi ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")
```

### 2. Overflow với số lớn

```python
# Python tự động xử lý số nguyên lớn
big_number = 2 ** 1000
print(f"2^1000 có {len(str(big_number))} chữ số")
```

### 3. Sử dụng modulo

```python
# Kiểm tra số chẵn/lẻ
number = 17
if number % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")

# Tìm chữ số cuối
last_digit = 12345 % 10  # 5
```

## Tips & Tricks

### 1. Compound assignment operators

```python
x = 10
x += 5      # x = x + 5 = 15
x -= 3      # x = x - 3 = 12
x *= 2      # x = x * 2 = 24
x /= 4      # x = x / 4 = 6.0
x //= 2     # x = x // 2 = 3.0
x %= 2      # x = x % 2 = 1.0
x **= 3     # x = x ** 3 = 1.0
```

### 2. Divmod function

```python
# Trả về cả thương và dư
quotient, remainder = divmod(17, 5)
print(f"17 ÷ 5 = {quotient} dư {remainder}")  # 17 ÷ 5 = 3 dư 2
```

### 3. Complex numbers

```python
# Python hỗ trợ số phức
z1 = 3 + 4j
z2 = 1 - 2j
result = z1 + z2        # (4+2j)
magnitude = abs(z1)     # 5.0
```

### 4. Infinity và NaN

```python
import math

# Vô cực
positive_inf = math.inf
negative_inf = -math.inf

# Not a Number
nan = math.nan

# Kiểm tra
math.isinf(positive_inf)    # True
math.isnan(nan)             # True
```
