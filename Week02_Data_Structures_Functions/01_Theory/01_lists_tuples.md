# Lists và Tuples trong Python

## Giới thiệu về Data Structures

Data structures (cấu trúc dữ liệu) là cách tổ chức và lưu trữ dữ liệu để có thể sử dụng hiệu quả. Python cung cấp nhiều built-in data structures mạnh mẽ.

## Lists (Danh sách)

### Khái niệm

List là một collection có thứ tự, có thể thay đổi (mutable) và cho phép duplicate values.

### Tạo Lists

```python
# List rỗng
empty_list = []
empty_list2 = list()

# List với dữ liệu
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]

# List lồng nhau
nested = [[1, 2], [3, 4], [5, 6]]

print(numbers)      # [1, 2, 3, 4, 5]
print(fruits)       # ['apple', 'banana', 'orange']
print(mixed)        # [1, 'hello', 3.14, True]
```

### Truy cập phần tử

```python
fruits = ["apple", "banana", "orange", "grape"]

# Indexing (chỉ số từ 0)
print(fruits[0])    # apple
print(fruits[1])    # banana
print(fruits[-1])   # grape (từ cuối)
print(fruits[-2])   # orange

# Slicing
print(fruits[1:3])  # ['banana', 'orange']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[2:])   # ['orange', 'grape']
print(fruits[::2])  # ['apple', 'orange'] (mỗi 2 phần tử)
```

### Thay đổi Lists

```python
fruits = ["apple", "banana", "orange"]

# Thay đổi phần tử
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'orange']

# Thêm phần tử
fruits.append("grape")          # Thêm vào cuối
print(fruits)  # ['apple', 'blueberry', 'orange', 'grape']

fruits.insert(1, "kiwi")        # Thêm vào vị trí cụ thể
print(fruits)  # ['apple', 'kiwi', 'blueberry', 'orange', 'grape']

# Mở rộng list
more_fruits = ["mango", "pineapple"]
fruits.extend(more_fruits)
print(fruits)  # ['apple', 'kiwi', 'blueberry', 'orange', 'grape', 'mango', 'pineapple']
```

### Xóa phần tử

```python
fruits = ["apple", "banana", "orange", "grape", "banana"]

# Xóa theo giá trị (lần xuất hiện đầu tiên)
fruits.remove("banana")
print(fruits)  # ['apple', 'orange', 'grape', 'banana']

# Xóa theo index
del fruits[1]
print(fruits)  # ['apple', 'grape', 'banana']

# Pop - xóa và trả về phần tử
last_fruit = fruits.pop()      # Xóa phần tử cuối
print(last_fruit)  # banana
print(fruits)      # ['apple', 'grape']

second_fruit = fruits.pop(1)   # Xóa phần tử tại index 1
print(second_fruit)  # grape
print(fruits)        # ['apple']

# Xóa tất cả
fruits.clear()
print(fruits)  # []
```

### Các phương thức hữu ích

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Đếm phần tử
print(numbers.count(1))     # 2

# Tìm vị trí
print(numbers.index(4))     # 2

# Sắp xếp
numbers.sort()              # Sắp xếp tại chỗ
print(numbers)              # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # Sắp xếp giảm dần
print(numbers)              # [9, 6, 5, 4, 3, 2, 1, 1]

# Đảo ngược
numbers.reverse()
print(numbers)              # [1, 1, 2, 3, 4, 5, 6, 9]

# Copy list
numbers_copy = numbers.copy()
numbers_copy2 = numbers[:]
numbers_copy3 = list(numbers)
```

### List Comprehension

```python
# Cách truyền thống
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Với điều kiện
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Với string
words = ["hello", "world", "python", "data"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON', 'DATA']
```

## Tuples (Bộ)

### Khái niệm

Tuple là một collection có thứ tự và không thể thay đổi (immutable). Cho phép duplicate values.

### Tạo Tuples

```python
# Tuple rỗng
empty_tuple = ()
empty_tuple2 = tuple()

# Tuple với dữ liệu
coordinates = (3, 4)
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14, True)

# Tuple với một phần tử (cần dấu phẩy)
single = (5,)  # Không có dấu phẩy thì không phải tuple
single2 = 5,

print(coordinates)  # (3, 4)
print(colors)       # ('red', 'green', 'blue')
print(type(single)) # <class 'tuple'>
```

### Truy cập Tuples

```python
colors = ("red", "green", "blue", "yellow")

# Indexing và slicing giống list
print(colors[0])    # red
print(colors[-1])   # yellow
print(colors[1:3])  # ('green', 'blue')

# Unpacking tuples
r, g, b, y = colors
print(r)  # red
print(g)  # green

# Unpacking với *
first, *middle, last = colors
print(first)   # red
print(middle)  # ['green', 'blue']
print(last)    # yellow
```

### Tuple methods

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# Đếm phần tử
print(numbers.count(2))  # 3

# Tìm vị trí
print(numbers.index(3))  # 2
```

### Ứng dụng Tuples

```python
# Coordinates
point = (10, 20)
x, y = point

# Swap variables
a = 5
b = 10
a, b = b, a  # Swap sử dụng tuple
print(a, b)  # 10 5

# Return multiple values từ function
def get_name_age():
    return "Alice", 25

name, age = get_name_age()
print(f"Name: {name}, Age: {age}")

# Dictionary items
student = {"name": "Bob", "age": 20, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
```

## So sánh Lists vs Tuples

| Đặc điểm    | Lists              | Tuples                |
| ----------- | ------------------ | --------------------- |
| Mutable     | ✅ Có thể thay đổi | ❌ Không thể thay đổi |
| Syntax      | `[1, 2, 3]`        | `(1, 2, 3)`           |
| Performance | Chậm hơn           | Nhanh hơn             |
| Memory      | Nhiều hơn          | Ít hơn                |
| Use case    | Dữ liệu thay đổi   | Dữ liệu cố định       |

## Ứng dụng trong Data Science

### Xử lý dữ liệu với Lists

```python
# Dataset mẫu
temperatures = [23.5, 25.1, 22.8, 26.3, 24.7, 21.9, 27.2]

# Tính toán cơ bản
avg_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)

print(f"Average: {avg_temp:.2f}°C")
print(f"Max: {max_temp}°C")
print(f"Min: {min_temp}°C")

# Filter data
hot_days = [temp for temp in temperatures if temp > 25]
print(f"Hot days: {hot_days}")

# Data transformation
temp_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]
print(f"Fahrenheit: {temp_fahrenheit}")
```

### Coordinates với Tuples

```python
# GPS coordinates
locations = [
    ("Hanoi", (21.0285, 105.8542)),
    ("Ho Chi Minh", (10.8231, 106.6297)),
    ("Da Nang", (16.0544, 108.2022))
]

# Xử lý coordinates
for city, (lat, lon) in locations:
    print(f"{city}: Latitude {lat}, Longitude {lon}")

# Tính khoảng cách (simplified)
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

hanoi_coords = (21.0285, 105.8542)
hcm_coords = (10.8231, 106.6297)
dist = distance(hanoi_coords, hcm_coords)
print(f"Distance: {dist:.2f}")
```

## Bài tập thực hành

### Bài 1: Quản lý danh sách sinh viên

```python
# Tạo list sinh viên với điểm số
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 96)
]

# TODO: Viết code để:
# 1. Tìm sinh viên có điểm cao nhất
# 2. Tính điểm trung bình
# 3. Lọc sinh viên có điểm >= 90
```

### Bài 2: Xử lý dữ liệu nhiệt độ

```python
# Dữ liệu nhiệt độ 7 ngày
daily_temps = [
    (1, 22.5), (2, 24.1), (3, 23.8),
    (4, 26.3), (5, 25.7), (6, 21.9), (7, 27.2)
]

# TODO: Viết code để:
# 1. Tìm ngày nóng nhất và lạnh nhất
# 2. Tính nhiệt độ trung bình
# 3. Đếm số ngày có nhiệt độ > 25°C
```

## Tóm tắt

- **Lists**: Mutable, dùng cho dữ liệu thay đổi, nhiều methods
- **Tuples**: Immutable, nhanh hơn, dùng cho dữ liệu cố định
- **List Comprehension**: Cách ngắn gọn để tạo lists
- **Unpacking**: Gán multiple values từ tuples/lists
- **Ứng dụng**: Xử lý datasets, coordinates, structured data

### Next Steps

- Học về Dictionaries và Sets
- Làm quen với nested data structures
- Thực hành với real datasets
