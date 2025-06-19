# Exercise 1: Lists và Tuples

## Mục tiêu học tập

Sau khi hoàn thành bài tập này, bạn sẽ:

- Thành thạo làm việc với Lists và Tuples
- Hiểu cách sử dụng List comprehensions
- Biết cách xử lý dữ liệu cấu trúc
- Áp dụng trong xử lý dữ liệu thực tế

---

## **PHẦN 1: LISTS CỞ BẢN**

### Bài 1.1: Tạo và thao tác Lists

```python
# TODO 1.1.1: Tạo lists với các loại dữ liệu khác nhau
# Tạo một list chứa tên các thành phố Việt Nam
cities = []

# Tạo một list chứa nhiệt độ 7 ngày
temperatures = []

# Tạo một list chứa thông tin mixed (số, string, boolean)
mixed_data = []

# TODO 1.1.2: Truy cập và thay đổi elements
# In ra thành phố đầu tiên và cuối cùng
# Thay đổi nhiệt độ ngày thứ 3
# Thêm một thành phố mới vào cuối list
```

### Bài 1.2: List methods và operations

```python
# TODO 1.2.1: Sử dụng các List methods
fruits = ["apple", "banana", "orange", "apple", "grape"]

# Đếm số lần xuất hiện của "apple"
# Tìm vị trí của "banana"
# Thêm "kiwi" vào cuối list
# Thêm "mango" vào vị trí index 2
# Xóa "apple" đầu tiên
# Sắp xếp list theo alphabet

# TODO 1.2.2: List comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tạo list các số chẵn
evens = []

# Tạo list bình phương của các số lẻ
odd_squares = []

# Tạo list các từ viết hoa từ fruits
uppercase_fruits = []
```

---

## **PHẦN 2: TUPLES VÀ UNPACKING**

### Bài 2.1: Tạo và sử dụng Tuples

```python
# TODO 2.1.1: Tạo tuples cho coordinates
# Tạo tuple cho tọa độ Hà Nội (21.0285, 105.8542)
hanoi_coords = ()

# Tạo tuple cho thông tin sinh viên (tên, tuổi, điểm GPA)
student_info = ()

# Tạo tuple chứa màu RGB (255, 128, 0)
orange_color = ()

# TODO 2.1.2: Tuple unpacking
# Unpacking coordinates
lat, lon = hanoi_coords
# In ra: "Latitude: 21.0285, Longitude: 105.8542"

# Unpacking student info
name, age, gpa = student_info
# In ra thông tin sinh viên

# Unpacking với *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
# In ra first, middle, last
```

### Bài 2.2: Tuples trong practical applications

```python
# TODO 2.2.1: Swap variables sử dụng tuples
a = 10
b = 20
# Hoán đổi giá trị a và b bằng tuple

# TODO 2.2.2: Return multiple values từ function
def get_statistics(numbers):
    # Return tuple chứa (mean, median, mode)
    pass

# TODO 2.2.3: Enumerate và zip
cities = ["Hanoi", "Ho Chi Minh", "Da Nang"]
populations = [8000000, 9000000, 1200000]

# Sử dụng enumerate để in: "1. Hanoi", "2. Ho Chi Minh", etc.

# Sử dụng zip để kết hợp cities và populations
```

---

## **PHẦN 3: XỬ LÝ DỮ LIỆU THỰC TẾ**

### Bài 3.1: Temperature Data Analysis

```python
# Dữ liệu nhiệt độ 14 ngày (Celsius)
daily_temps = [
    22.5, 24.1, 23.8, 26.3, 25.7, 21.9, 27.2,
    24.8, 23.4, 25.6, 22.1, 26.8, 24.3, 25.9
]

# TODO 3.1.1: Thống kê cơ bản
# Tính nhiệt độ trung bình
average_temp = 0

# Tìm nhiệt độ cao nhất và thấp nhất
max_temp = 0
min_temp = 0

# Đếm số ngày có nhiệt độ > 25°C
hot_days = 0

# TODO 3.1.2: Data transformation
# Chuyển đổi tất cả nhiệt độ sang Fahrenheit
temps_fahrenheit = []

# Tạo list các ngày với nhiệt độ trong khoảng 23-26°C
comfortable_days = []

# TODO 3.1.3: Phân loại nhiệt độ
# Tạo list tuples (ngày, nhiệt độ, phân loại)
# Phân loại: "Lạnh" (<23), "Vừa" (23-26), "Nóng" (>26)
temp_analysis = []
```

### Bài 3.2: Student Grade Management

```python
# Dữ liệu điểm sinh viên: (tên, điểm toán, điểm lý, điểm hóa)
students = [
    ("Alice", 85, 92, 78),
    ("Bob", 92, 88, 94),
    ("Charlie", 76, 82, 80),
    ("Diana", 95, 98, 92),
    ("Eve", 88, 85, 89)
]

# TODO 3.2.1: Tính GPA cho mỗi sinh viên
# Thêm GPA vào tuple: (tên, toán, lý, hóa, GPA)
students_with_gpa = []

# TODO 3.2.2: Tìm sinh viên xuất sắc
# Sinh viên có GPA >= 90
excellent_students = []

# TODO 3.2.3: Phân tích theo môn học
# Tính điểm trung bình cho từng môn
math_scores = []
physics_scores = []
chemistry_scores = []

math_average = 0
physics_average = 0
chemistry_average = 0

# TODO 3.2.4: Ranking students
# Sắp xếp sinh viên theo GPA (cao nhất đầu tiên)
ranked_students = []
```

### Bài 3.3: Sales Data Processing

```python
# Dữ liệu bán hàng: (sản phẩm, số lượng, giá)
sales_data = [
    ("Laptop", 15, 25000000),
    ("Phone", 32, 15000000),
    ("Tablet", 8, 12000000),
    ("Watch", 25, 8000000),
    ("Headphones", 45, 3000000),
    ("Laptop", 10, 25000000),  # Same product, different sale
    ("Phone", 18, 15000000)
]

# TODO 3.3.1: Tính doanh thu cho mỗi record
# Thêm doanh thu vào tuple: (sản phẩm, số lượng, giá, doanh thu)
sales_with_revenue = []

# TODO 3.3.2: Tổng hợp theo sản phẩm
# Dictionary: {sản phẩm: [tổng số lượng, tổng doanh thu]}
product_summary = {}

# TODO 3.3.3: Top products
# List sản phẩm sắp xếp theo doanh thu (cao nhất đầu tiên)
top_products = []

# TODO 3.3.4: Analysis insights
# Sản phẩm bán chạy nhất (theo số lượng)
# Sản phẩm có doanh thu cao nhất
# Tổng doanh thu all products
```

---

## **PHẦN 4: ADVANCED CHALLENGES**

### Bài 4.1: Matrix Operations với Lists

```python
# Ma trận 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# TODO 4.1.1: Matrix traversal
# In tất cả elements theo hàng
# In tất cả elements theo cột
# In đường chéo chính (1, 5, 9)

# TODO 4.1.2: Matrix operations
# Tính tổng tất cả elements
total_sum = 0

# Tìm element lớn nhất và nhỏ nhất
max_element = 0
min_element = 0

# Transpose matrix (đổi hàng thành cột)
transposed = []

# TODO 4.1.3: Create new matrices
# Tạo matrix với tất cả elements * 2
doubled_matrix = []

# Tạo matrix chứa chỉ các số chẵn
even_matrix = []
```

### Bài 4.2: Data Cleaning Challenge

```python
# Messy data from different sources
messy_data = [
    "25", "30.5", "", "invalid", "28", None, "32.1",
    "27", "abc", "29.8", "31", "xyz", "26.5"
]

# TODO 4.2.1: Clean và convert data
# Loại bỏ invalid values và convert sang float
cleaned_numbers = []

# TODO 4.2.2: Data validation
# Tạo tuple cho mỗi value: (original, cleaned, is_valid)
validation_results = []

# TODO 4.2.3: Statistics on cleaned data
# Chỉ tính trên valid numbers
valid_count = 0
invalid_count = 0
average_of_valid = 0
```

### Bài 4.3: Nested Data Structures

```python
# Complex nested data
company_data = [
    ("TechCorp", [
        ("Alice", "Engineer", 85000),
        ("Bob", "Designer", 75000),
        ("Charlie", "Manager", 95000)
    ]),
    ("DataInc", [
        ("Diana", "Analyst", 70000),
        ("Eve", "Scientist", 90000),
        ("Frank", "Engineer", 88000)
    ])
]

# TODO 4.3.1: Extract information
# List tất cả employee names
all_employees = []

# List tất cả unique job titles
job_titles = []

# TODO 4.3.2: Salary analysis
# Tính average salary by company
company_salaries = {}

# Tìm highest paid employee overall
highest_paid = ()

# TODO 4.3.3: Restructure data
# Convert sang format: [(name, company, title, salary), ...]
flattened_data = []
```

---

## **BONUS CHALLENGES**

### Bonus 1: Pascal's Triangle

```python
# TODO: Tạo Pascal's triangle với n rows sử dụng lists
def generate_pascals_triangle(n):
    # Return list of lists representing Pascal's triangle
    pass
```

### Bonus 2: Data Aggregation

```python
# TODO: Group và aggregate complex data
weather_data = [
    ("Hanoi", "2024-01-01", 20.5, "Sunny"),
    ("Hanoi", "2024-01-02", 18.2, "Cloudy"),
    ("Ho Chi Minh", "2024-01-01", 28.5, "Sunny"),
    ("Ho Chi Minh", "2024-01-02", 30.1, "Rainy"),
    ("Da Nang", "2024-01-01", 25.3, "Sunny"),
    ("Da Nang", "2024-01-02", 26.8, "Cloudy")
]

# Group by city và tính average temperature
# Count weather conditions by city
```

### Bonus 3: Algorithm Implementation

```python
# TODO: Implement sorting algorithm using lists
def bubble_sort(numbers):
    # Sort list using bubble sort algorithm
    pass

def binary_search(sorted_list, target):
    # Find target in sorted list, return index or -1
    pass
```

---

## **Hướng dẫn nộp bài**

1. **File thực hành**: Làm bài trong file `2_practice.py`
2. **Test code**: Chạy từng phần và kiểm tra kết quả
3. **So sánh**: Tham khảo `3_solution.py` khi cần
4. **Thời gian**: 90-120 phút cho toàn bộ bài tập

## **Tiêu chí đánh giá**

- ✅ **Cơ bản (60%)**: Hoàn thành Phần 1-2
- ✅ **Khá (75%)**: Hoàn thành Phần 1-3
- ✅ **Giỏi (85%)**: Hoàn thành Phần 1-4
- ✅ **Xuất sắc (95%)**: Hoàn thành + Bonus challenges

## **Tips quan trọng**

1. **Đọc kỹ requirements** trước khi code
2. **Test với sample data** nhỏ trước
3. **Sử dụng print()** để debug
4. **Viết code rõ ràng** với meaningful variable names
5. **Handle edge cases** (empty lists, invalid data)

---

**Good luck! 🚀**
