# Student Management System - Week 2 Project

## Mục tiêu dự án

Xây dựng một hệ thống quản lý sinh viên hoàn chỉnh sử dụng các data structures đã học: Lists, Tuples, Dictionaries, Sets và Functions.

## Yêu cầu chức năng

### 1. **Student Database Management**

- Lưu trữ thông tin sinh viên: ID, Name, Age, Email, Phone
- Quản lý điểm số theo môn học
- Theo dõi enrollment status

### 2. **Grade Management**

- Nhập điểm cho nhiều môn học
- Tính GPA tự động
- Phân loại học lực (Excellent, Good, Average, Poor)
- Tìm sinh viên cần hỗ trợ

### 3. **Data Analysis & Reporting**

- Thống kê theo lớp/khóa
- Top performers analysis
- Subject performance analysis
- Attendance tracking

### 4. **Search & Filter**

- Tìm kiếm sinh viên theo multiple criteria
- Filter theo GPA, age, status
- Sort theo different fields

---

## **Cấu trúc dữ liệu đề xuất**

```python
# Student record structure
student = {
    "id": "SV001",
    "name": "Nguyen Van A",
    "age": 20,
    "email": "nva@email.com",
    "phone": "0123456789",
    "class": "CS2024A",
    "grades": {
        "Math": [8.5, 7.0, 9.0],
        "Physics": [7.5, 8.0, 8.5],
        "Programming": [9.0, 9.5, 8.5]
    },
    "attendance": {
        "Math": 0.95,
        "Physics": 0.88,
        "Programming": 0.92
    },
    "status": "Active"  # Active, Inactive, Graduated
}

# Database structure
database = {
    "students": [],      # List of student dictionaries
    "subjects": set(),   # Set of all subjects
    "classes": set(),    # Set of all classes
    "statistics": {}     # Computed statistics
}
```

---

## **Chức năng cần implement**

### **Part 1: Core Functions (60%)**

#### 1.1 Student Management

```python
def add_student(database, student_info):
    """
    Thêm sinh viên mới vào database
    Args:
        database (dict): Database chính
        student_info (dict): Thông tin sinh viên
    Returns:
        bool: True if successful, False otherwise
    """
    pass

def remove_student(database, student_id):
    """Xóa sinh viên khỏi database"""
    pass

def update_student(database, student_id, updated_info):
    """Cập nhật thông tin sinh viên"""
    pass

def find_student(database, student_id):
    """Tìm sinh viên theo ID"""
    pass
```

#### 1.2 Grade Management

```python
def add_grade(database, student_id, subject, grade):
    """Thêm điểm cho sinh viên"""
    pass

def calculate_gpa(grades_dict):
    """Tính GPA từ dictionary điểm"""
    pass

def get_student_gpa(database, student_id):
    """Lấy GPA của sinh viên"""
    pass

def classify_performance(gpa):
    """Phân loại học lực theo GPA"""
    # Excellent: >= 3.6
    # Good: 3.0 - 3.59
    # Average: 2.5 - 2.99
    # Poor: < 2.5
    pass
```

### **Part 2: Advanced Features (30%)**

#### 2.1 Search & Filter

```python
def search_students(database, **criteria):
    """
    Tìm kiếm sinh viên theo multiple criteria
    Examples:
        search_students(db, name="Nguyen", min_gpa=3.0)
        search_students(db, class="CS2024A", status="Active")
    """
    pass

def filter_by_performance(database, performance_level):
    """Filter sinh viên theo học lực"""
    pass

def sort_students(database, sort_by="name", reverse=False):
    """Sắp xếp sinh viên theo field"""
    pass
```

#### 2.2 Analytics

```python
def class_statistics(database, class_name):
    """Thống kê của một lớp"""
    pass

def subject_analysis(database, subject):
    """Phân tích performance theo môn học"""
    pass

def top_performers(database, n=10):
    """Top N sinh viên xuất sắc nhất"""
    pass

def students_at_risk(database, gpa_threshold=2.0):
    """Sinh viên có nguy cơ bị đuổi"""
    pass
```

### **Part 3: Bonus Features (10%)**

#### 3.1 Data Import/Export

```python
def import_from_csv(database, file_path):
    """Import dữ liệu từ CSV"""
    pass

def export_to_csv(database, file_path):
    """Export dữ liệu ra CSV"""
    pass
```

#### 3.2 Reporting

```python
def generate_report(database, report_type="summary"):
    """Tạo báo cáo tổng hợp"""
    pass

def grade_distribution(database, subject=None):
    """Phân bố điểm số"""
    pass
```

---

## **Sample Data để test**

```python
# Sample students data
sample_students = [
    {
        "id": "SV001",
        "name": "Nguyen Van An",
        "age": 20,
        "email": "nva@email.com",
        "phone": "0123456789",
        "class": "CS2024A",
        "grades": {
            "Math": [8.5, 7.0, 9.0],
            "Physics": [7.5, 8.0, 8.5],
            "Programming": [9.0, 9.5, 8.5]
        },
        "status": "Active"
    },
    {
        "id": "SV002",
        "name": "Tran Thi Binh",
        "age": 19,
        "email": "ttb@email.com",
        "phone": "0987654321",
        "class": "CS2024A",
        "grades": {
            "Math": [6.5, 7.5, 8.0],
            "Physics": [8.0, 8.5, 9.0],
            "Programming": [7.0, 8.0, 9.0]
        },
        "status": "Active"
    },
    {
        "id": "SV003",
        "name": "Le Van Cuong",
        "age": 21,
        "email": "lvc@email.com",
        "phone": "0345678901",
        "class": "CS2024B",
        "grades": {
            "Math": [9.0, 9.5, 9.0],
            "Physics": [8.5, 9.0, 9.5],
            "Programming": [9.5, 9.0, 9.5]
        },
        "status": "Active"
    }
]
```

---

## **Test Cases**

### Test 1: Basic Operations

```python
def test_basic_operations():
    # Initialize database
    db = {"students": [], "subjects": set(), "classes": set()}

    # Test add student
    student1 = sample_students[0]
    assert add_student(db, student1) == True
    assert len(db["students"]) == 1

    # Test find student
    found = find_student(db, "SV001")
    assert found["name"] == "Nguyen Van An"

    # Test calculate GPA
    gpa = get_student_gpa(db, "SV001")
    expected_gpa = (8.17 + 8.0 + 9.0) / 3  # Average of subject averages
    assert abs(gpa - expected_gpa) < 0.1
```

### Test 2: Search & Filter

```python
def test_search_filter():
    db = initialize_database_with_sample_data()

    # Test search by class
    cs2024a_students = search_students(db, class="CS2024A")
    assert len(cs2024a_students) == 2

    # Test filter by performance
    excellent_students = filter_by_performance(db, "Excellent")
    assert len(excellent_students) >= 1
```

### Test 3: Analytics

```python
def test_analytics():
    db = initialize_database_with_sample_data()

    # Test class statistics
    stats = class_statistics(db, "CS2024A")
    assert "average_gpa" in stats
    assert "student_count" in stats

    # Test top performers
    top3 = top_performers(db, 3)
    assert len(top3) <= 3
    assert top3[0]["gpa"] >= top3[1]["gpa"]  # Sorted by GPA
```

---

## **Expected Output Examples**

### 1. Student List Display

```
=== STUDENT MANAGEMENT SYSTEM ===

ID: SV001 | Name: Nguyen Van An | Class: CS2024A | GPA: 8.39 | Status: Active
ID: SV002 | Name: Tran Thi Binh | Class: CS2024A | GPA: 7.72 | Status: Active
ID: SV003 | Name: Le Van Cuong | Class: CS2024B | GPA: 9.17 | Status: Active
```

### 2. Class Statistics

```
=== CLASS STATISTICS: CS2024A ===
Total Students: 2
Average GPA: 8.06
Top Student: Nguyen Van An (8.39)
Subject Performance:
  - Math: 7.38 average
  - Physics: 8.13 average
  - Programming: 8.50 average
```

### 3. Performance Analysis

```
=== PERFORMANCE DISTRIBUTION ===
Excellent (GPA >= 3.6): 3 students (100%)
Good (GPA 3.0-3.59): 0 students (0%)
Average (GPA 2.5-2.99): 0 students (0%)
Poor (GPA < 2.5): 0 students (0%)

Students at Risk: None
```

---

## **Hướng dẫn thực hiện**

### Phase 1: Setup & Core (2-3 hours)

1. Tạo database structure
2. Implement basic CRUD operations
3. Grade management functions
4. Test với sample data

### Phase 2: Advanced Features (2-3 hours)

1. Search & filter functions
2. Analytics & statistics
3. Performance classification
4. Comprehensive testing

### Phase 3: Polish & Bonus (1-2 hours)

1. Error handling
2. Input validation
3. Bonus features
4. Code optimization

---

## **Tiêu chí đánh giá**

- ✅ **Cơ bản (60%)**: Hoàn thành Part 1
- ✅ **Khá (75%)**: Hoàn thành Part 1-2
- ✅ **Giỏi (85%)**: Hoàn thành Part 1-2 + Testing
- ✅ **Xuất sắc (95%)**: Hoàn thành tất cả + Bonus

## **Lưu ý quan trọng**

1. **Code Quality**: Clean, readable, well-commented
2. **Error Handling**: Handle edge cases gracefully
3. **Efficiency**: Consider performance for large datasets
4. **Testing**: Verify functions work correctly
5. **Documentation**: Clear docstrings for functions

---

**Good luck with your project! 🚀**
