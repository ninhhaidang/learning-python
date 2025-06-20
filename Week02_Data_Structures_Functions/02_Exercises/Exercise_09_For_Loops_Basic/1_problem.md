# Week 2 - Exercise 9: Basic For Loops

**Vòng lặp For cơ bản**

## 🎯 Mục tiêu

- Sử dụng for loops với range()
- Lặp qua lists, strings
- Sử dụng enumerate() và zip()
- Tính toán với loops

---

## 📋 Đề bài

Phân tích dữ liệu bán hàng của cửa hàng:

### Yêu cầu:

1. **Lặp qua danh sách** sản phẩm và giá
2. **Tính tổng doanh thu** và số lượng sản phẩm
3. **Tìm sản phẩm** đắt nhất và rẻ nhất
4. **Sử dụng enumerate()** để đánh số thứ tự

---

## 💻 Yêu cầu cụ thể

```python
# Dữ liệu sản phẩm
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
prices = [15000000, 250000, 800000, 5000000, 1200000]

# 1. In danh sách sản phẩm với giá
# 2. Tính tổng doanh thu
# 3. Tìm sản phẩm đắt nhất
# 4. Đếm sản phẩm có giá > 1 triệu
# 5. Tạo bảng thống kê
```

---

## 🎯 Expected Output

```
=== Store Sales Analysis ===

Product List:
1. Laptop: 15,000,000 VND
2. Mouse: 250,000 VND
3. Keyboard: 800,000 VND
4. Monitor: 5,000,000 VND
5. Headphones: 1,200,000 VND

Sales Statistics:
Total Products: 5
Total Revenue: 22,250,000 VND
Average Price: 4,450,000 VND

Most Expensive: Laptop (15,000,000 VND)
Cheapest: Mouse (250,000 VND)

Products over 1 million VND: 3
- Laptop: 15,000,000 VND
- Monitor: 5,000,000 VND
- Headphones: 1,200,000 VND

Price Categories:
Under 500K: 1 products
500K - 1M: 1 products
1M - 5M: 1 products
Over 5M: 2 products
```

---

## 💡 Hints

- `for i in range(len(list)):` để lặp với index
- `for item in list:` để lặp qua elements
- `enumerate(list)` cho index và value
- `zip(list1, list2)` để lặp qua 2 lists cùng lúc
