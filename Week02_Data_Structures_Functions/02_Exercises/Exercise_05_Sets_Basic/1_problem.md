# Week 2 - Exercise 5: Basic Sets

**Tạo và sử dụng Sets cơ bản**

## 🎯 Mục tiêu

- Hiểu khái niệm set và tính chất unique
- Thực hiện các phép toán tập hợp (union, intersection, difference)
- Sử dụng sets để loại bỏ duplicate data
- Ứng dụng trong phân tích dữ liệu

---

## 📋 Đề bài

Phân tích dữ liệu học sinh tham gia các môn học:

### Yêu cầu:

1. **Tạo sets** chứa danh sách học sinh trong các môn khác nhau
2. **Tìm học sinh** học cả hai môn (intersection)
3. **Tìm học sinh** chỉ học một môn (difference)
4. **Tìm tất cả học sinh** (union)
5. **Loại bỏ duplicate** trong danh sách

---

## 💻 Yêu cầu cụ thể

```python
# 1. Tạo sets cho hai môn học
math_students = {"An", "Binh", "Chi", "Duc", "Em"}
english_students = {"Binh", "Chi", "Phong", "Giang", "Huong"}

# 2. Tìm học sinh học cả hai môn
# 3. Tìm học sinh chỉ học Math
# 4. Tìm học sinh chỉ học English
# 5. Tìm tất cả học sinh
# 6. Loại bỏ duplicate từ list
```

---

## 🎯 Expected Output

```
Math students: {'An', 'Binh', 'Chi', 'Duc', 'Em'}
English students: {'Binh', 'Chi', 'Phong', 'Giang', 'Huong'}

Students taking both subjects: {'Binh', 'Chi'}
Students taking only Math: {'An', 'Duc', 'Em'}
Students taking only English: {'Phong', 'Giang', 'Huong'}
All students: {'An', 'Binh', 'Chi', 'Duc', 'Em', 'Phong', 'Giang', 'Huong'}

Original list with duplicates: ['An', 'Binh', 'An', 'Chi', 'Binh', 'Duc']
After removing duplicates: {'An', 'Binh', 'Chi', 'Duc'}
```

---

## 💡 Hints

- Set được tạo với `{item1, item2}` hoặc `set([list])`
- Intersection: `set1 & set2` hoặc `set1.intersection(set2)`
- Union: `set1 | set2` hoặc `set1.union(set2)`
- Difference: `set1 - set2` hoặc `set1.difference(set2)`
- Sets tự động loại bỏ duplicates
