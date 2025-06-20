# Week 2 - Exercise 1: Basic Lists

**Tạo và thao tác Lists cơ bản**

## 🎯 Mục tiêu

- Tạo lists với các kiểu dữ liệu khác nhau
- Truy cập và thay đổi elements trong list
- Sử dụng indexing và slicing cơ bản

---

## 📋 Đề bài

Tạo một chương trình quản lý danh sách thành phố và nhiệt độ:

### Yêu cầu:

1. **Tạo list cities** chứa 5 tên thành phố Việt Nam
2. **Tạo list temperatures** chứa nhiệt độ tương ứng của 5 thành phố (số thực)
3. **In thông tin** thành phố đầu tiên và cuối cùng
4. **Thay đổi** nhiệt độ của thành phố thứ 3
5. **Thêm** một thành phố mới và nhiệt độ của nó

---

## 💻 Yêu cầu cụ thể

```python
# 1. Tạo lists
cities = ["Hanoi", "Ho Chi Minh", "Da Nang", "Hue", "Can Tho"]
temperatures = [25.5, 28.0, 26.5, 24.0, 27.5]

# 2. In thông tin đầu và cuối
# 3. Thay đổi nhiệt độ thành phố thứ 3 thành 30.0
# 4. Thêm "Nha Trang" với nhiệt độ 29.0
# 5. In toàn bộ danh sách cuối cùng
```

---

## 🎯 Expected Output

```
First city: Hanoi (25.5°C)
Last city: Can Tho (27.5°C)

After updating Da Nang temperature:
Da Nang: 30.0°C

Final cities and temperatures:
Hanoi: 25.5°C
Ho Chi Minh: 28.0°C
Da Nang: 30.0°C
Hue: 24.0°C
Can Tho: 27.5°C
Nha Trang: 29.0°C
```

---

## 💡 Hints

- Sử dụng `list[0]` để truy cập element đầu tiên
- Sử dụng `list[-1]` để truy cập element cuối cùng
- Sử dụng `list[index] = new_value` để thay đổi
- Sử dụng `list.append()` để thêm element mới
