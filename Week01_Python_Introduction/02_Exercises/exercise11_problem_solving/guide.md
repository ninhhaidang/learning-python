# Hướng dẫn Exercise 11: Problem Solving Challenge

## Tổng quan

Bài tập này tập trung vào việc phát triển kỹ năng giải quyết vấn đề thông qua các thử thách thực tế. Bạn sẽ học cách phân tích vấn đề, thiết kế thuật toán và implement giải pháp hoàn chỉnh.

## Chuẩn bị

Trước khi bắt đầu, hãy đảm bảo bạn đã nắm vững:

- Cách sử dụng input(), print()
- Phép toán cơ bản và operator
- String manipulation
- Conditional statements (if/elif/else)
- Vòng lặp (for, while)
- Type conversion

## Chi tiết từng Challenge

### Challenge 1: Máy tính tiền tip

**Phân tích vấn đề:**

- Input: số tiền hóa đơn, % tip, số người
- Process: tính tip total, tip per person, total per person
- Output: kết quả được format đẹp

**Hướng dẫn step by step:**

```python
# Step 1: Nhận input từ user
bill_amount = float(input("Nhập số tiền hóa đơn: "))
tip_percentage = float(input("Nhập % tip: "))
num_people = int(input("Số người chia bill: "))

# Step 2: Tính toán
tip_total = bill_amount * (tip_percentage / 100)
tip_per_person = tip_total / num_people
total_per_person = (bill_amount + tip_total) / num_people

# Step 3: Format và hiển thị
print(f"Tip total: {tip_total:,.0f} VND")
print(f"Tip mỗi người: {tip_per_person:,.0f} VND")
print(f"Tổng mỗi người: {total_per_person:,.0f} VND")
```

**Kiến thức quan trọng:**

- String formatting với f-strings
- Number formatting với `:,.0f`
- Input validation (kiểm tra số âm)

### Challenge 2: Kiểm tra mật khẩu mạnh

**Phân tích vấn đề:**

- Cần kiểm tra multiple conditions
- Mỗi condition cho điểm riêng
- Feedback dựa trên tổng điểm

**Hướng dẫn approach:**

```python
password = input("Nhập mật khẩu: ")
score = 0
feedback = []

# Kiểm tra độ dài
if len(password) >= 8:
    score += 1
    feedback.append("✓ Độ dài >= 8 ký tự")
else:
    feedback.append("✗ Cần ít nhất 8 ký tự")

# Kiểm tra chữ hoa
if any(c.isupper() for c in password):
    score += 1
    feedback.append("✓ Có chữ hoa")

# Tương tự cho các điều kiện khác...
```

**Kiến thức quan trọng:**

- Built-in methods: `isupper()`, `islower()`, `isdigit()`
- Generator expressions với `any()`
- List comprehension để tạo feedback

### Challenge 3: Chuyển đổi đơn vị

**Phân tích vấn đề:**

- Tạo menu với multiple options
- Switch-case logic (dùng if/elif)
- Bidirectional conversion

**Hướng dẫn structure:**

```python
def display_menu():
    print("1. Celsius ↔ Fahrenheit")
    print("2. Kilogram ↔ Pound")
    print("3. Kilometer ↔ Mile")

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Main logic
choice = int(input("Chọn chuyển đổi: "))
if choice == 1:
    # Temperature conversion logic
    pass
```

**Kiến thức quan trọng:**

- Function definition và parameters
- Menu-driven programming
- Mathematical formulas implementation

### Challenge 4: Phân tích số điện thoại

**Phân tích vấn đề:**

- Input có thể có nhiều format khác nhau
- Cần normalize trước khi xử lý
- Pattern matching để xác định vùng

**Hướng dẫn approach:**

```python
def normalize_phone(phone):
    # Remove all non-digit characters
    return ''.join(c for c in phone if c.isdigit())

def identify_region(phone):
    # Vietnamese phone number patterns
    if phone.startswith('024'):
        return "Hà Nội"
    elif phone.startswith('028'):
        return "TP.HCM"
    # Add more patterns...

def format_phone(phone):
    if len(phone) == 10:
        return f"({phone[:3]}) {phone[3:7]}-{phone[7:]}"
```

**Kiến thức quan trọng:**

- String slicing và indexing
- List comprehension với conditions
- Pattern matching với `startswith()`

### Challenge 5: Rock-Paper-Scissors Game

**Phân tích vấn đề:**

- Random choice cho máy
- Game logic để xác định winner
- Score tracking qua multiple rounds

**Hướng dẫn structure:**

```python
import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

# Game loop
for round_num in range(3):
    user_choice = input("Chọn (rock/paper/scissors): ").lower()
    computer_choice = random.choice(choices)

    winner = determine_winner(user_choice, computer_choice)
    # Update scores and display results
```

**Kiến thức quan trọng:**

- `random` module và `random.choice()`
- Complex conditional logic
- Loop với round counting

## Tips để thành công

### 1. Problem Decomposition

- Chia bài toán lớn thành các phần nhỏ
- Giải quyết từng phần một cách độc lập
- Combine các solution lại với nhau

### 2. Input Validation

```python
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Vui lòng nhập số dương!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
```

### 3. Error Handling

- Sử dụng try/except cho input validation
- Kiểm tra edge cases (số âm, chuỗi rỗng, etc.)
- Provide helpful error messages

### 4. Code Organization

```python
# Good structure
def main():
    print("=== CALCULATOR TIP ===")
    calculate_tip()

    print("\n=== KIỂM TRA MẬT KHẨU ===")
    check_password_strength()

    # Call other challenges...

if __name__ == "__main__":
    main()
```

## Common Mistakes và Cách tránh

### 1. Format Number không đúng

```python
# Wrong
print("Số tiền:", amount)

# Right
print(f"Số tiền: {amount:,.0f} VND")
```

### 2. Logic Error trong Game

```python
# Make sure to handle all cases
def determine_winner(user, computer):
    # Don't forget the tie case!
    if user == computer:
        return "tie"
    # ... rest of logic
```

### 3. Input Validation thiếu

```python
# Always validate user input
while True:
    try:
        choice = int(input("Chọn (1-3): "))
        if 1 <= choice <= 3:
            break
        else:
            print("Chọn từ 1-3!")
    except ValueError:
        print("Vui lòng nhập số!")
```

## Testing và Debug

### Test Cases để thử

1. **Tip Calculator:** Test với số âm, 0 người, tip 0%
2. **Password:** Test empty string, very short, missing criteria
3. **Unit Converter:** Test số âm, 0, số rất lớn
4. **Phone:** Test format khác nhau, số không hợp lệ
5. **Game:** Test invalid choices, play multiple rounds

### Debug Techniques

```python
# Add debug prints
print(f"Debug: bill={bill}, tip%={tip_pct}, people={num_people}")

# Test individual functions
if __name__ == "__main__":
    # Test functions individually before integration
    test_password = "Test123!"
    result = check_password_strength(test_password)
    print(f"Test result: {result}")
```

## Mở rộng (Optional)

### Advanced Features có thể thêm:

1. **Tip Calculator:** Lưu history các bill, split unevenly
2. **Password:** Generate strong password suggestions
3. **Converter:** Add more units, currency conversion
4. **Phone:** International format, carrier detection
5. **Game:** Best of N rounds, difficulty levels

### Code Quality Improvements:

- Add docstrings cho functions
- Implement proper error classes
- Add logging thay vì print statements
- Create config file cho settings

Hãy thực hành từng challenge một cách cẩn thận và test kỹ lưỡng trước khi chuyển sang challenge tiếp theo!
