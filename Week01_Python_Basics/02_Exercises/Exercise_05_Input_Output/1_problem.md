# Week 1 - Exercise 5: Input and Output

**Tương tác với người dùng qua input/output**

## 🎯 Mục tiêu

- Sử dụng `input()` để nhận dữ liệu từ người dùng
- Chuyển đổi kiểu dữ liệu (string to number)
- Xử lý và hiển thị kết quả

---

## 📋 Đề bài

Tạo chương trình tính diện tích hình chữ nhật:

1. Hỏi người dùng nhập **chiều dài** (length)
2. Hỏi người dùng nhập **chiều rộng** (width)
3. Tính **diện tích** = length × width
4. Tính **chu vi** = 2 × (length + width)
5. In ra kết quả theo format đã cho

---

## 💻 Yêu cầu

1. Sử dụng `input()` để nhận dữ liệu từ người dùng
2. Chuyển đổi string thành số thực (float)
3. Tính toán diện tích và chu vi
4. Hiển thị kết quả với 2 chữ số thập phân

---

## 💡 Hints

- Nhận input: `length = input("Enter length: ")`
- Chuyển sang float: `length = float(length)`
- Hoặc gộp: `length = float(input("Enter length: "))`
- Diện tích: `area = length * width`
- Chu vi: `perimeter = 2 * (length + width)`
- Format 2 chữ số thập phân: `{area:.2f}`

## 🎯 Expected Output (ví dụ)

```
Enter the length of rectangle: 5.5
Enter the width of rectangle: 3.2
Rectangle dimensions: 5.50 x 3.20
Area: 17.60 square units
Perimeter: 17.40 units
```

## 🔍 Self-Check

- [ ] Chương trình có hỏi input 2 lần không?
- [ ] Có chuyển đổi string sang float không?
- [ ] Công thức tính diện tích và chu vi có đúng không?
- [ ] Kết quả có hiển thị 2 chữ số thập phân không?
- [ ] Có test với số thập phân không?
