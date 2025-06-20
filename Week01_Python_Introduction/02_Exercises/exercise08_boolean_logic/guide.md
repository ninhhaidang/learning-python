# Hướng dẫn: Boolean Logic

## Lý thuyết cần biết

### 1. Giá trị Boolean

Boolean là kiểu dữ liệu logic chỉ có 2 giá trị:

- `True`: Đúng (1)
- `False`: Sai (0)

```python
is_student = True
is_graduated = False
print(type(is_student))  # <class 'bool'>
```

### 2. Phép toán so sánh

Các phép so sánh trả về giá trị Boolean:

```python
# So sánh bằng
5 == 5          # True
5 == 3          # False

# So sánh khác
5 != 3          # True
5 != 5          # False

# So sánh lớn nhỏ
10 > 5          # True
10 < 5          # False
10 >= 10        # True
10 <= 5         # False
```

### 3. Phép toán logic

#### AND (và)

Chỉ True khi **cả hai** đều True:

```python
True and True    # True
True and False   # False
False and True   # False
False and False  # False
```

#### OR (hoặc)

True khi **ít nhất một** là True:

```python
True or True     # True
True or False    # True
False or True    # True
False or False   # False
```

#### NOT (phủ định)

Đảo ngược giá trị:

```python
not True         # False
not False        # True
```

### 4. Truthiness và Falsiness

#### Falsy values (được coi là False)

```python
bool(False)      # False
bool(0)          # False
bool(0.0)        # False
bool("")         # False (chuỗi rỗng)
bool([])         # False (list rỗng)
bool({})         # False (dict rỗng)
bool(set())      # False (set rỗng)
bool(None)       # False
```

#### Truthy values (được coi là True)

```python
bool(True)       # True
bool(1)          # True
bool(-1)         # True
bool("hello")    # True
bool([1, 2])     # True
bool({"a": 1})   # True
```

### 5. Short-circuit evaluation

Python đánh giá logic theo nguyên tắc "đoản mạch":

```python
# AND: Nếu phần đầu False, không kiểm tra phần sau
False and print("Không in")  # Không in gì

# OR: Nếu phần đầu True, không kiểm tra phần sau
True or print("Không in")    # Không in gì
```

## Các bước thực hiện

### Bước 1: Tạo biến Boolean

```python
is_python_fun = True
is_difficult = False

print(f"Python có vui không? {is_python_fun}")
print(f"Python có khó không? {is_difficult}")
print(f"Kiểu dữ liệu: {type(is_python_fun)}")
```

### Bước 2: Thực hiện so sánh

```python
age1 = 20
age2 = 25

print(f"age1 == age2: {age1 == age2}")
print(f"age1 != age2: {age1 != age2}")
print(f"age1 < age2: {age1 < age2}")
print(f"age1 > age2: {age1 > age2}")
print(f"age1 <= age2: {age1 <= age2}")
print(f"age1 >= age2: {age1 >= age2}")
```

### Bước 3: Phép toán logic

```python
# AND
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")

# OR
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

# NOT
print(f"not True = {not True}")
print(f"not False = {not False}")
```

### Bước 4: Logic phức tạp

```python
age = 20

# Kiểm tra tuổi làm việc
working_age = (age >= 18) and (age <= 65)
print(f"Tuổi làm việc: {working_age}")

# Kết hợp nhiều điều kiện
good_to_learn = is_python_fun and not is_difficult
print(f"Tốt để học: {good_to_learn}")
```

### Bước 5: Test truthiness

```python
# Test các giá trị
test_values = [1, 0, "", "hello", [], [1, 2], None]

for value in test_values:
    print(f"bool({repr(value)}) = {bool(value)}")
```

## Lưu ý quan trọng

### 1. So sánh vs Gán

```python
# So sánh (comparison)
x == 5      # Kiểm tra x có bằng 5 không

# Gán (assignment)
x = 5       # Gán giá trị 5 cho x
```

### 2. So sánh chuỗi

```python
"abc" < "def"        # True (so sánh lexicographic)
"Apple" < "apple"    # True (chữ hoa < chữ thường)
```

### 3. So sánh kiểu khác nhau

```python
# Cẩn thận khi so sánh kiểu khác nhau
"10" < 20           # Error! Không thể so sánh str và int
```

### 4. Chaining comparisons

```python
# Python cho phép nối so sánh
x = 15
10 < x < 20         # True (tương đương: 10 < x and x < 20)
```

## Tips & Tricks

### 1. Sử dụng boolean để kiểm soát flow

```python
debug_mode = True

if debug_mode:
    print("Debug: Processing data...")
```

### 2. Boolean arithmetic

```python
# True = 1, False = 0
True + True         # 2
True * 5            # 5
False + 10          # 10
```

### 3. Default values với or

```python
name = "" or "Unknown"      # "Unknown"
count = 0 or 1              # 1
```

### 4. Validation với and

```python
def is_valid_age(age):
    return isinstance(age, int) and 0 <= age <= 150
```

### 5. Toggle boolean

```python
flag = True
flag = not flag     # False
```
