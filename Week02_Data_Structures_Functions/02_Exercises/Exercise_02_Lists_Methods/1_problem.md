# Week 2 - Exercise 2: List Methods

**Sử dụng các phương thức của List**

## 🎯 Mục tiêu

- Sử dụng các phương thức quan trọng của list
- Thao tác với list: count, index, insert, remove, sort
- Hiểu cách list methods hoạt động

---

## 📋 Đề bài

Quản lý danh sách trái cây trong cửa hàng:

### Yêu cầu:

1. **Tạo list fruits** với một số trái cây, có trái cây trùng lặp
2. **Đếm số lượng** của một loại trái cây cụ thể
3. **Tìm vị trí** của một trái cây
4. **Thêm trái cây** vào vị trí cụ thể
5. **Xóa trái cây** đầu tiên khỏi list
6. **Sắp xếp** list theo thứ tự alphabet

---

## 💻 Yêu cầu cụ thể

```python
# 1. Tạo list với trái cây trùng lặp
fruits = ["apple", "banana", "orange", "apple", "grape", "banana"]

# 2. Đếm số lượng "apple"
# 3. Tìm vị trí của "orange"
# 4. Thêm "kiwi" vào vị trí index 2
# 5. Xóa "apple" đầu tiên
# 6. Sắp xếp list theo alphabet
# 7. In kết quả từng bước
```

---

## 🎯 Expected Output

```
Original fruits: ['apple', 'banana', 'orange', 'apple', 'grape', 'banana']
Number of apples: 2
Position of orange: 2

After inserting kiwi at index 2:
['apple', 'banana', 'kiwi', 'orange', 'apple', 'grape', 'banana']

After removing first apple:
['banana', 'kiwi', 'orange', 'apple', 'grape', 'banana']

After sorting:
['apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
```

---

## 💡 Hints

- `list.count(item)` - đếm số lần xuất hiện
- `list.index(item)` - tìm vị trí đầu tiên
- `list.insert(index, item)` - chèn vào vị trí
- `list.remove(item)` - xóa lần xuất hiện đầu tiên
- `list.sort()` - sắp xếp tại chỗ
