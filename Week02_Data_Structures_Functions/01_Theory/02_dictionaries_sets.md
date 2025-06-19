# Dictionaries và Sets trong Python

## Dictionaries (Từ điển)

### Khái niệm

Dictionary là một collection không có thứ tự cố định, có thể thay đổi (mutable) và được index bằng keys. Không cho phép duplicate keys.

### Tạo Dictionaries

```python
# Dictionary rỗng
empty_dict = {}
empty_dict2 = dict()

# Dictionary với dữ liệu
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"]
}

# Sử dụng dict() constructor
coordinates = dict(x=10, y=20, z=5)

# Từ list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters = dict(pairs)

print(student)      # {'name': 'Alice', 'age': 20, 'grade': 'A', 'subjects': ['Math', 'Physics', 'Chemistry']}
print(coordinates)  # {'x': 10, 'y': 20, 'z': 5}
print(letters)      # {'a': 1, 'b': 2, 'c': 3}
```

### Truy cập Dictionary

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "gpa": 3.8
}

# Truy cập bằng key
print(student["name"])     # Alice
print(student["age"])      # 20

# Sử dụng get() method (an toàn hơn)
print(student.get("name"))      # Alice
print(student.get("height"))    # None
print(student.get("height", "Unknown"))  # Unknown

# Kiểm tra key có tồn tại
print("name" in student)        # True
print("height" in student)      # False
```

### Thay đổi Dictionary

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Thêm/sửa phần tử
student["age"] = 21           # Sửa
student["height"] = 165       # Thêm mới
student["subjects"] = ["Math", "Physics"]

print(student)
# {'name': 'Alice', 'age': 21, 'grade': 'A', 'height': 165, 'subjects': ['Math', 'Physics']}

# Update nhiều items
student.update({"gpa": 3.8, "year": 2})
student.update(email="alice@example.com")

print(student)
```

### Xóa khỏi Dictionary

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "gpa": 3.8,
    "email": "alice@example.com"
}

# Xóa theo key
del student["email"]
print(student)

# Pop - xóa và trả về value
grade = student.pop("grade")
print(f"Removed grade: {grade}")
print(student)

# Pop với default value
height = student.pop("height", "Not specified")
print(f"Height: {height}")

# Xóa item cuối cùng (Python 3.7+)
last_item = student.popitem()
print(f"Removed: {last_item}")

# Xóa tất cả
student.clear()
print(student)  # {}
```

### Dictionary Methods

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Lấy keys, values, items
print(student.keys())    # dict_keys(['name', 'age', 'grade'])
print(student.values())  # dict_values(['Alice', 20, 'A'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])

# Chuyển thành lists
keys_list = list(student.keys())
values_list = list(student.values())
items_list = list(student.items())

# Copy dictionary
student_copy = student.copy()
student_copy2 = dict(student)
```

### Lặp qua Dictionary

```python
student = {"name": "Alice", "age": 20, "grade": "A", "gpa": 3.8}

# Lặp qua keys
for key in student:
    print(f"{key}: {student[key]}")

# Lặp qua keys (explicit)
for key in student.keys():
    print(f"{key}: {student[key]}")

# Lặp qua values
for value in student.values():
    print(value)

# Lặp qua items (key-value pairs)
for key, value in student.items():
    print(f"{key}: {value}")
```

### Nested Dictionaries

```python
# Dictionary chứa dictionaries
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": {"math": 95, "physics": 87, "chemistry": 92}
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "grades": {"math": 88, "physics": 95, "chemistry": 85}
    }
}

# Truy cập nested data
print(students["student1"]["name"])                    # Alice
print(students["student1"]["grades"]["math"])          # 95

# Thêm data vào nested dictionary
students["student1"]["email"] = "alice@example.com"
students["student2"]["grades"]["biology"] = 90

# Lặp qua nested dictionary
for student_id, info in students.items():
    print(f"\n{student_id}:")
    print(f"  Name: {info['name']}")
    print(f"  Age: {info['age']}")
    print("  Grades:")
    for subject, grade in info['grades'].items():
        print(f"    {subject}: {grade}")
```

### Dictionary Comprehension

```python
# Tạo dictionary từ list
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Với điều kiện
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16}

# Từ string
text = "hello world"
char_count = {char: text.count(char) for char in set(text) if char != ' '}
print(char_count)  # {'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'd': 1, 'w': 1}

# Đảo ngược key-value
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}
```

## Sets (Tập hợp)

### Khái niệm

Set là một collection không có thứ tự, không thể thay đổi các phần tử (nhưng có thể thêm/xóa), và không cho phép duplicate values.

### Tạo Sets

```python
# Set rỗng (chú ý: {} tạo dictionary, không phải set)
empty_set = set()

# Set với dữ liệu
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# Từ list (tự động loại bỏ duplicates)
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)  # {1, 2, 3, 4, 5}

# Từ string
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}
```

### Thao tác với Sets

```python
fruits = {"apple", "banana", "orange"}

# Thêm phần tử
fruits.add("grape")
print(fruits)  # {'apple', 'banana', 'orange', 'grape'}

# Thêm nhiều phần tử
fruits.update(["kiwi", "mango"])
fruits.update("pear")  # Thêm từng ký tự
print(fruits)

# Xóa phần tử
fruits.remove("banana")     # KeyError nếu không tồn tại
fruits.discard("watermelon")  # Không lỗi nếu không tồn tại
print(fruits)

# Pop - xóa và trả về phần tử ngẫu nhiên
random_fruit = fruits.pop()
print(f"Removed: {random_fruit}")

# Xóa tất cả
fruits.clear()
```

### Set Operations (Các phép toán tập hợp)

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (Hợp) - tất cả phần tử
union1 = set1.union(set2)
union2 = set1 | set2
print(union1)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (Giao) - phần tử chung
intersection1 = set1.intersection(set2)
intersection2 = set1 & set2
print(intersection1)  # {4, 5}

# Difference (Hiệu) - phần tử trong set1 nhưng không trong set2
difference1 = set1.difference(set2)
difference2 = set1 - set2
print(difference1)  # {1, 2, 3}

# Symmetric Difference (Hiệu đối xứng) - phần tử không chung
sym_diff1 = set1.symmetric_difference(set2)
sym_diff2 = set1 ^ set2
print(sym_diff1)  # {1, 2, 3, 6, 7, 8}
```

### Set Relationships

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {6, 7, 8}

# Subset (Tập con)
print(set1.issubset(set2))    # True
print(set1 <= set2)           # True

# Superset (Tập cha)
print(set2.issuperset(set1))  # True
print(set2 >= set1)           # True

# Disjoint (Không giao nhau)
print(set1.isdisjoint(set3))  # True
```

### Set Comprehension

```python
# Tạo set từ comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x**2 for x in numbers if x % 2 == 0}
print(even_squares)  # {4, 16, 36, 64, 100}

# Loại bỏ duplicates từ string
text = "hello world"
unique_chars = {char for char in text if char.isalpha()}
print(unique_chars)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
```

## Ứng dụng trong Data Science

### Đếm tần suất với Dictionary

```python
# Phân tích text
text = "the quick brown fox jumps over the lazy dog"
words = text.split()

# Đếm từ
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

# Cách ngắn gọn với dict comprehension
from collections import Counter
word_count2 = Counter(words)
print(word_count2)  # Counter({'the': 2, 'quick': 1, 'brown': 1, ...})
```

### Grouping data với Dictionary

```python
# Nhóm sinh viên theo lớp
students = [
    {"name": "Alice", "class": "A", "score": 85},
    {"name": "Bob", "class": "B", "score": 92},
    {"name": "Charlie", "class": "A", "score": 78},
    {"name": "Diana", "class": "B", "score": 96},
    {"name": "Eve", "class": "A", "score": 88}
]

# Group by class
classes = {}
for student in students:
    class_name = student["class"]
    if class_name not in classes:
        classes[class_name] = []
    classes[class_name].append(student)

for class_name, class_students in classes.items():
    print(f"Class {class_name}:")
    for student in class_students:
        print(f"  {student['name']}: {student['score']}")
    print()
```

### Unique values với Sets

```python
# Dữ liệu có duplicate
data = [
    {"country": "Vietnam", "city": "Hanoi"},
    {"country": "Vietnam", "city": "Ho Chi Minh"},
    {"country": "USA", "city": "New York"},
    {"country": "USA", "city": "Los Angeles"},
    {"country": "Vietnam", "city": "Da Nang"}
]

# Lấy unique countries
countries = {item["country"] for item in data}
print(f"Countries: {countries}")  # {'Vietnam', 'USA'}

# Lấy unique cities
cities = {item["city"] for item in data}
print(f"Cities: {cities}")  # {'Hanoi', 'Ho Chi Minh', 'New York', 'Los Angeles', 'Da Nang'}

# Đếm số lượng unique values
print(f"Number of countries: {len(countries)}")
print(f"Number of cities: {len(cities)}")
```

### Data validation với Sets

```python
# Kiểm tra dữ liệu hợp lệ
valid_grades = {"A", "B", "C", "D", "F"}
student_grades = ["A", "B", "C", "X", "A", "D", "Y"]

# Tìm grades không hợp lệ
invalid_grades = set(student_grades) - valid_grades
print(f"Invalid grades: {invalid_grades}")  # {'X', 'Y'}

# Kiểm tra tất cả grades có hợp lệ không
all_valid = set(student_grades).issubset(valid_grades)
print(f"All grades valid: {all_valid}")  # False
```

## So sánh Data Structures

| Đặc điểm   | Lists     | Tuples     | Dictionaries     | Sets          |
| ---------- | --------- | ---------- | ---------------- | ------------- |
| Ordered    | ✅        | ✅         | ✅ (Python 3.7+) | ❌            |
| Mutable    | ✅        | ❌         | ✅               | ✅            |
| Duplicates | ✅        | ✅         | ❌ (keys)        | ❌            |
| Indexing   | ✅        | ✅         | By key           | ❌            |
| Use case   | Sequences | Fixed data | Key-value        | Unique values |

## Bài tập thực hành

### Bài 1: Student Management System

```python
# Tạo hệ thống quản lý sinh viên
students_db = {}

# TODO:
# 1. Thêm sinh viên với thông tin: name, age, grades (dict)
# 2. Tính GPA cho mỗi sinh viên
# 3. Tìm sinh viên có GPA cao nhất
# 4. Lọc sinh viên theo điều kiện
```

### Bài 2: Text Analysis

```python
text = """
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms and systems to extract knowledge and insights from
structured and unstructured data in various forms.
"""

# TODO:
# 1. Đếm tần suất từ
# 2. Tìm từ dài nhất/ngắn nhất
# 3. Lấy unique words
# 4. Phân tích character frequency
```

### Bài 3: Survey Data Processing

```python
survey_responses = [
    {"age": 25, "city": "Hanoi", "job": "Engineer", "satisfaction": 8},
    {"age": 30, "city": "Ho Chi Minh", "job": "Teacher", "satisfaction": 7},
    {"age": 25, "city": "Hanoi", "job": "Developer", "satisfaction": 9},
    {"age": 35, "city": "Da Nang", "job": "Engineer", "satisfaction": 6},
    {"age": 28, "city": "Ho Chi Minh", "job": "Designer", "satisfaction": 8}
]

# TODO:
# 1. Group by city
# 2. Tính average satisfaction by job
# 3. Tìm unique age groups
# 4. Top cities by number of responses
```

## Tóm tắt

### Dictionaries

- **Key-value pairs**: Lưu trữ dữ liệu có cấu trúc
- **Fast lookup**: Truy cập O(1) average case
- **Flexible**: Keys có thể là strings, numbers, tuples

### Sets

- **Unique values**: Tự động loại bỏ duplicates
- **Set operations**: Union, intersection, difference
- **Fast membership testing**: `in` operator O(1)

### Best Practices

- Sử dụng dictionaries cho key-value mappings
- Sử dụng sets cho unique collections
- Dictionary comprehension cho code ngắn gọn
- Sets cho filtering duplicates và set operations

### Next Steps

- Functions và scope
- Error handling
- File I/O với structured data
