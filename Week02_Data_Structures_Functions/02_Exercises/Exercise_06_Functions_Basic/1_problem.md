# Week 2 - Exercise 6: Basic Functions

**Định nghĩa và sử dụng Functions cơ bản**

## 🎯 Mục tiêu

- Học cách định nghĩa function với `def`
- Hiểu về parameters và return values
- Tạo functions đơn giản cho tính toán
- Sử dụng functions để tổ chức code

---

## 📋 Đề bài

Tạo máy tính cơ bản sử dụng functions:

### Yêu cầu:

1. **Tạo 4 functions** cho các phép toán cơ bản
2. **Function calculate()** để thực hiện phép toán
3. **Test** tất cả functions với số liệu cụ thể

---

## 💻 Yêu cầu cụ thể

```python
# 1. Tạo functions cho phép toán
def add(a, b):
    # return tổng của a và b

def subtract(a, b):
    # return hiệu của a và b

def multiply(a, b):
    # return tích của a và b

def divide(a, b):
    # return thương của a và b (chú ý chia cho 0)

# 2. Function tổng quát
def calculate(operation, num1, num2):
    # Gọi function tương ứng dựa trên operation
    # operation có thể là: "+", "-", "*", "/"

# 3. Test với các số cụ thể
```

---

## 🎯 Expected Output

```
=== Testing Basic Calculator Functions ===

Addition: 15 + 7 = 22
Subtraction: 15 - 7 = 8
Multiplication: 15 * 7 = 105
Division: 15 / 7 = 2.14

Testing calculate function:
calculate('+', 10, 5) = 15
calculate('-', 10, 5) = 5
calculate('*', 10, 5) = 50
calculate('/', 10, 5) = 2.0

Error handling:
Division by zero: Cannot divide by zero!
```

---

## 💡 Hints

- Function định nghĩa với `def function_name(parameters):`
- Sử dụng `return` để trả về kết quả
- Kiểm tra điều kiện chia cho 0 trước khi chia
- Function có thể gọi function khác
