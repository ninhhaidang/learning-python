# Week 1 - Exercise 4: String Basics

**Làm việc với chuỗi ký tự cơ bản**

## 🎯 Mục tiêu

- Tạo và gán giá trị cho string
- Kết hợp strings
- Lấy độ dài của string
- In string với format

---

## 📋 Đề bài

Tạo chương trình làm việc với thông tin người dùng:

1. Tạo biến `first_name` = "John"
2. Tạo biến `last_name` = "Doe"
3. Tạo biến `full_name` bằng cách kết hợp first_name và last_name (có khoảng trắng ở giữa)
4. Đếm số ký tự trong full_name
5. In ra thông tin theo format đã cho

---

## 💻 Yêu cầu

1. Khai báo 2 biến string: first_name và last_name
2. Tạo full_name bằng cách kết hợp (concatenation)
3. Tính độ dài của full_name
4. In ra thông tin theo format mẫu

---

## 💡 Hints

- Kết hợp string: `full_name = first_name + " " + last_name`
- Hoặc dùng f-string: `full_name = f"{first_name} {last_name}"`
- Độ dài string: `len(full_name)`
- In kết quả: `print(f"Full name: {full_name}")`

## 🎯 Expected Output

```
First name: John
Last name: Doe
Full name: John Doe
Name length: 8 characters
```

## 🔍 Self-Check

- [ ] Có khai báo đúng 2 biến string không?
- [ ] Full name có khoảng trắng giữa first và last không?
- [ ] Độ dài có đúng không? (John Doe = 8 ký tự)
- [ ] Format output có đúng không?
