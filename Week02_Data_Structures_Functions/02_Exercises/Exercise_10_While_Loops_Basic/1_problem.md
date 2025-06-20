# Week 2 - Exercise 10: Basic While Loops

**Vòng lặp While cơ bản**

## 🎯 Mục tiêu

- Sử dụng while loops với điều kiện
- Hiểu về loop control (break, continue)
- Tạo interactive programs
- Xử lý user input validation

---

## 📋 Đề bài

Tạo hệ thống đoán số đơn giản:

### Yêu cầu:

1. **Generate random number** từ 1-100
2. **User đoán số** và nhận phản hồi (quá cao/thấp)
3. **Đếm số lần đoán**
4. **Tùy chọn chơi lại** sau khi kết thúc

---

## 💻 Yêu cầu cụ thể

```python
import random

# 1. Generate số bí mật
# 2. While loop để user đoán
# 3. Kiểm tra input hợp lệ
# 4. Đưa ra gợi ý (cao/thấp/đúng)
# 5. Đếm số lần đoán
# 6. Hỏi chơi lại
```

---

## 🎯 Expected Output

```
=== Number Guessing Game ===

I'm thinking of a number between 1 and 100!

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Too high! Try again.

Enter your guess: 31
Too low! Try again.

Enter your guess: 34
Congratulations! You guessed it in 5 attempts!

Game Statistics:
- Secret number: 34
- Your guesses: 5
- Guesses per attempt: [50, 25, 37, 31, 34]

Do you want to play again? (y/n): n
Thanks for playing! Goodbye!
```

---

## 💡 Hints

- `import random` và `random.randint(1, 100)`
- `while True:` cho vòng lặp vô hạn
- `break` để thoát khỏi loop
- `continue` để bỏ qua iteration hiện tại
- `try/except` để xử lý input không hợp lệ
