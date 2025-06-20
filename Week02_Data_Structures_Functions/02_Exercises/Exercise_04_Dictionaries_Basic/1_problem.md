# Week 2 - Exercise 4: Basic Dictionaries

**Tạo và sử dụng Dictionaries cơ bản**

## 🎯 Mục tiêu

- Tạo và truy cập dictionaries
- Thêm, sửa, xóa key-value pairs
- Sử dụng dictionary methods cơ bản
- Ứng dụng cho quản lý thông tin sinh viên

---

## 📋 Đề bài

Quản lý thông tin sinh viên trong lớp học:

### Yêu cầu:

1. **Tạo dictionary** chứa thông tin một sinh viên
2. **Truy cập và in** các thông tin
3. **Thêm thông tin** mới (điểm số)
4. **Cập nhật thông tin** hiện có (tuổi)
5. **Xóa một key** không cần thiết

---

## 💻 Yêu cầu cụ thể

```python
# 1. Tạo dictionary sinh viên
student = {
    "name": "Nguyen Van A",
    "age": 20,
    "major": "Computer Science",
    "university": "VNU"
}

# 2. In thông tin sinh viên
# 3. Thêm điểm số
# 4. Cập nhật tuổi
# 5. Xóa university
# 6. In thông tin cuối cùng
```

---

## 🎯 Expected Output

```
Student Information:
Name: Nguyen Van A
Age: 20
Major: Computer Science
University: VNU

After adding grade:
Name: Nguyen Van A
Age: 20
Major: Computer Science
University: VNU
Grade: 8.5

After updating age to 21:
Name: Nguyen Van A
Age: 21
Major: Computer Science
University: VNU
Grade: 8.5

After removing university:
Name: Nguyen Van A
Age: 21
Major: Computer Science
Grade: 8.5

Dictionary keys: dict_keys(['name', 'age', 'major', 'grade'])
Dictionary values: dict_values(['Nguyen Van A', 21, 'Computer Science', 8.5])
```

---

## 💡 Hints

- Dictionary được tạo với `{key: value}`
- Truy cập: `dict[key]` hoặc `dict.get(key)`
- Thêm/sửa: `dict[key] = value`
- Xóa: `del dict[key]` hoặc `dict.pop(key)`
- Methods: `.keys()`, `.values()`, `.items()`
