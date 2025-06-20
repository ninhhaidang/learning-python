# Week 2 - Exercise 7: Functions with Parameters

**Functions với parameters và default values**

## 🎯 Mục tiêu

- Hiểu về function parameters và arguments
- Sử dụng default parameters
- Làm việc với multiple parameters
- Tính toán thống kê từ danh sách số

---

## 📋 Đề bài

Tạo hệ thống tính toán điểm số học sinh:

### Yêu cầu:

1. **Function calculate_average()** tính điểm trung bình
2. **Function find_grade()** xác định xếp loại (A, B, C, D, F)
3. **Function analyze_scores()** phân tích tổng quát
4. **Sử dụng default parameters** cho một số function

---

## 💻 Yêu cầu cụ thể

```python
# 1. Function tính điểm trung bình
def calculate_average(scores):
    # return điểm trung bình của list scores

# 2. Function xếp loại (với default scale)
def find_grade(score, scale="standard"):
    # scale="standard": A(90+), B(80-89), C(70-79), D(60-69), F(<60)
    # scale="strict": A(95+), B(85-94), C(75-84), D(65-74), F(<65)

# 3. Function phân tích chi tiết
def analyze_scores(scores, student_name="Student"):
    # Tính average, grade, min, max

# 4. Test với dữ liệu cụ thể
```

---

## 🎯 Expected Output

```
=== Score Analysis System ===

Test scores: [85, 92, 78, 96, 88]

Average score: 87.8
Grade (standard scale): B
Grade (strict scale): B

Detailed Analysis for John:
Student: John
Scores: [85, 92, 78, 96, 88]
Average: 87.8
Grade: B
Highest: 96
Lowest: 78
Range: 18 points

Anonymous Analysis:
Student: Student
Average: 87.8
Grade: B
```

---

## 💡 Hints

- Default parameters: `def function(param1, param2="default")`
- Multiple parameters được phân tách bằng dấu phẩy
- `min()` và `max()` functions cho tìm giá trị nhỏ nhất/lớn nhất
- Có thể gọi function khác bên trong function
