"""
Week 2 - Exercise 1: Lists và Tuples - SOLUTION
Đáp án chi tiết cho bài tập về Lists và Tuples

Author: AI Assistant
Date: Week 2 - Data Structures & Functions
"""

print("=" * 60)
print("EXERCISE 1: LISTS VÀ TUPLES - SOLUTION")
print("=" * 60)

# =============================================================================
# PHẦN 1: LISTS CỞ BẢN
# =============================================================================

print("\n" + "=" * 50)
print("PHẦN 1: LISTS CỞ BẢN")
print("=" * 50)

# Bài 1.1: Tạo và thao tác Lists
print("\n--- Bài 1.1: Tạo và thao tác Lists ---")

# TODO 1.1.1: Tạo lists với các loại dữ liệu khác nhau
cities = ["Hanoi", "Ho Chi Minh", "Da Nang", "Can Tho", "Hue"]
temperatures = [22.5, 24.1, 23.8, 26.3, 25.7, 21.9, 27.2]
mixed_data = [42, "Python", True, 3.14, "Data Science", False]

print(f"Cities: {cities}")
print(f"Temperatures: {temperatures}")
print(f"Mixed data: {mixed_data}")

# TODO 1.1.2: Truy cập và thay đổi elements
print(f"\\nFirst city: {cities[0]}")
print(f"Last city: {cities[-1]}")

# Thay đổi nhiệt độ ngày thứ 3 (index 2)
temperatures[2] = 24.5
print(f"Updated temperatures: {temperatures}")

# Thêm thành phố mới
cities.append("Nha Trang")
print(f"Cities after adding: {cities}")

# Bài 1.2: List methods và operations
print("\\n--- Bài 1.2: List methods và operations ---")

fruits = ["apple", "banana", "orange", "apple", "grape"]
print(f"Original fruits: {fruits}")

# Đếm số lần xuất hiện của "apple"
apple_count = fruits.count("apple")
print(f"Apple count: {apple_count}")

# Tìm vị trí của "banana"
banana_index = fruits.index("banana")
print(f"Banana index: {banana_index}")

# Thêm "kiwi" vào cuối list
fruits.append("kiwi")
print(f"After adding kiwi: {fruits}")

# Thêm "mango" vào vị trí index 2
fruits.insert(2, "mango")
print(f"After inserting mango: {fruits}")

# Xóa "apple" đầu tiên
fruits.remove("apple")
print(f"After removing first apple: {fruits}")

# Sắp xếp list theo alphabet
fruits.sort()
print(f"Sorted fruits: {fruits}")

# List comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tạo list các số chẵn
evens = [num for num in numbers if num % 2 == 0]
print(f"\\nEven numbers: {evens}")

# Tạo list bình phương của các số lẻ
odd_squares = [num**2 for num in numbers if num % 2 == 1]
print(f"Odd squares: {odd_squares}")

# Tạo list các từ viết hoa từ fruits
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(f"Uppercase fruits: {uppercase_fruits}")

# =============================================================================
# PHẦN 2: TUPLES VÀ UNPACKING
# =============================================================================

print("\\n" + "=" * 50)
print("PHẦN 2: TUPLES VÀ UNPACKING")
print("=" * 50)

# Bài 2.1: Tạo và sử dụng Tuples
print("\\n--- Bài 2.1: Tạo và sử dụng Tuples ---")

# Tạo tuples
hanoi_coords = (21.0285, 105.8542)
student_info = ("Alice", 20, 3.8)
orange_color = (255, 128, 0)

print(f"Hanoi coordinates: {hanoi_coords}")
print(f"Student info: {student_info}")
print(f"Orange color RGB: {orange_color}")

# Tuple unpacking
lat, lon = hanoi_coords
print(f"\\nLatitude: {lat}, Longitude: {lon}")

name, age, gpa = student_info
print(f"Student: {name}, Age: {age}, GPA: {gpa}")

# Unpacking với *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"\\nFirst: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")

# Bài 2.2: Tuples trong practical applications
print("\\n--- Bài 2.2: Practical applications ---")

# Swap variables
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Function returning multiple values
def get_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    median = sorted_nums[n//2] if n % 2 == 1 else (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    from collections import Counter
    mode = Counter(numbers).most_common(1)[0][0]
    return mean, median, mode

test_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
mean, median, mode = get_statistics(test_numbers)
print(f"\\nStatistics for {test_numbers}:")
print(f"Mean: {mean:.2f}, Median: {median}, Mode: {mode}")

# Enumerate và zip
cities = ["Hanoi", "Ho Chi Minh", "Da Nang"]
populations = [8000000, 9000000, 1200000]

print("\\nCities with numbers:")
for i, city in enumerate(cities, 1):
    print(f"{i}. {city}")

print("\\nCities with populations:")
for city, pop in zip(cities, populations):
    print(f"{city}: {pop:,} people")

# =============================================================================
# PHẦN 3: XỬ LÝ DỮ LIỆU THỰC TẾ
# =============================================================================

print("\\n" + "=" * 50)
print("PHẦN 3: XỬ LÝ DỮ LIỆU THỰC TẾ")
print("=" * 50)

# Bài 3.1: Temperature Data Analysis
print("\\n--- Bài 3.1: Temperature Analysis ---")

daily_temps = [
    22.5, 24.1, 23.8, 26.3, 25.7, 21.9, 27.2,
    24.8, 23.4, 25.6, 22.1, 26.8, 24.3, 25.9
]

# Thống kê cơ bản
average_temp = sum(daily_temps) / len(daily_temps)
max_temp = max(daily_temps)
min_temp = min(daily_temps)
hot_days = len([temp for temp in daily_temps if temp > 25])

print(f"Temperature Statistics:")
print(f"  Average: {average_temp:.2f}°C")
print(f"  Maximum: {max_temp}°C")
print(f"  Minimum: {min_temp}°C")
print(f"  Hot days (>25°C): {hot_days}")

# Data transformation
temps_fahrenheit = [(temp * 9/5) + 32 for temp in daily_temps]
comfortable_days = [i+1 for i, temp in enumerate(daily_temps) if 23 <= temp <= 26]

print(f"\\nFirst 5 temps in Fahrenheit: {temps_fahrenheit[:5]}")
print(f"Comfortable days (23-26°C): {comfortable_days}")

# Phân loại nhiệt độ
temp_analysis = []
for i, temp in enumerate(daily_temps):
    day = i + 1
    if temp < 23:
        category = "Lạnh"
    elif temp <= 26:
        category = "Vừa"
    else:
        category = "Nóng"
    temp_analysis.append((day, temp, category))

print("\\nTemperature Classification:")
for day, temp, category in temp_analysis[:5]:  # Show first 5
    print(f"  Day {day}: {temp}°C - {category}")

# Bài 3.2: Student Grade Management
print("\\n--- Bài 3.2: Student Grades ---")

students = [
    ("Alice", 85, 92, 78),
    ("Bob", 92, 88, 94),
    ("Charlie", 76, 82, 80),
    ("Diana", 95, 98, 92),
    ("Eve", 88, 85, 89)
]

# Tính GPA cho mỗi sinh viên
students_with_gpa = []
for name, math, physics, chemistry in students:
    gpa = (math + physics + chemistry) / 3
    students_with_gpa.append((name, math, physics, chemistry, round(gpa, 2)))

print("Students with GPA:")
for student in students_with_gpa:
    name, math, physics, chemistry, gpa = student
    print(f"  {name}: Math={math}, Physics={physics}, Chemistry={chemistry}, GPA={gpa}")

# Tìm sinh viên xuất sắc (GPA >= 90)
excellent_students = [student for student in students_with_gpa if student[4] >= 90]
print(f"\\nExcellent students (GPA >= 90): {len(excellent_students)}")
for student in excellent_students:
    print(f"  {student[0]}: GPA {student[4]}")

# Phân tích theo môn học
math_scores = [student[1] for student in students]
physics_scores = [student[2] for student in students]
chemistry_scores = [student[3] for student in students]

math_average = sum(math_scores) / len(math_scores)
physics_average = sum(physics_scores) / len(physics_scores)
chemistry_average = sum(chemistry_scores) / len(chemistry_scores)

print(f"\\nSubject Averages:")
print(f"  Math: {math_average:.2f}")
print(f"  Physics: {physics_average:.2f}")
print(f"  Chemistry: {chemistry_average:.2f}")

# Ranking students
ranked_students = sorted(students_with_gpa, key=lambda x: x[4], reverse=True)
print(f"\\nStudent Rankings:")
for i, student in enumerate(ranked_students, 1):
    print(f"  {i}. {student[0]}: GPA {student[4]}")

# =============================================================================
# PHẦN 4: ADVANCED CHALLENGES
# =============================================================================

print("\\n" + "=" * 50)
print("PHẦN 4: ADVANCED CHALLENGES")
print("=" * 50)

# Bài 4.1: Matrix Operations
print("\\n--- Bài 4.1: Matrix Operations ---")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix traversal
print("Matrix elements by row:")
for row in matrix:
    print(f"  {row}")

print("\\nMatrix elements by column:")
for j in range(len(matrix[0])):
    column = [matrix[i][j] for i in range(len(matrix))]
    print(f"  Column {j+1}: {column}")

print("\\nMain diagonal:")
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(f"  {diagonal}")

# Matrix operations
total_sum = sum(sum(row) for row in matrix)
all_elements = [element for row in matrix for element in row]
max_element = max(all_elements)
min_element = min(all_elements)

print(f"\\nMatrix Statistics:")
print(f"  Total sum: {total_sum}")
print(f"  Max element: {max_element}")
print(f"  Min element: {min_element}")

# Transpose matrix
transposed = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(f"\\nTransposed matrix:")
for row in transposed:
    print(f"  {row}")

# Create new matrices
doubled_matrix = [[element * 2 for element in row] for row in matrix]
even_matrix = [[element for element in row if element % 2 == 0] for row in matrix]

print(f"\\nDoubled matrix:")
for row in doubled_matrix:
    print(f"  {row}")

print(f"\\nEven elements by row:")
for i, row in enumerate(even_matrix):
    print(f"  Row {i+1}: {row}")

print("\\n" + "=" * 60)
print("EXERCISE 1 COMPLETED SUCCESSFULLY!")
print("=" * 60)
