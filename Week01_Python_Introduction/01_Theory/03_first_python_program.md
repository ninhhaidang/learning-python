# 🚀 Chương trình Python đầu tiên của bạn

## 📖 Mục lục

1. [Chương trình Hello World](#1-chương-trình-hello-world)
2. [Chạy code Python](#2-chạy-code-python)
3. [Hiểu kết quả đầu ra](#3-hiểu-kết-quả-đầu-ra)
4. [Chế độ tương tác vs Script](#4-chế-độ-tương-tác-vs-script)
5. [Chương trình thực tế đầu tiên](#5-chương-trình-thực-tế-đầu-tiên)

---

## 1. Chương trình Hello World

### 🎯 Truyền thống "Hello World"

Mọi lập trình viên đều bắt đầu với "Hello World" - đây là truyền thống trong ngành IT để:

- Xác minh thiết lập môi trường
- Hiểu cú pháp cơ bản
- Trải nghiệm chương trình thành công đầu tiên
- Xây dựng sự tự tin

### 📝 Hello World cổ điển

Tạo file `hello_world.py`:

```python
# Chương trình Python đầu tiên của tôi
print("Hello, World!")
```

**Phân tích code:**

- `#` : Comment (ghi chú) - không ảnh hưởng chương trình
- `print()` : Hàm có sẵn để xuất dữ liệu ra màn hình
- `"Hello, World!"` : Chuỗi ký tự (string literal)

### 🌟 Hello World nâng cao

```python
# Chương trình Hello World nâng cao
# Tác giả: [Tên của bạn]
# Ngày: [Ngày hôm nay]

print("Hello, World!")
print("Chào mừng đến với lập trình Python!")
print("Đây là chương trình Python đầu tiên của tôi.")

# Hãy thêm chút cá tính
print("🐍 Python thật tuyệt vời!")
print("Tôi rất háo hức học lập trình!")
```

---

## 2. Chạy code Python

### 💻 Phương pháp 1: Command Line/Terminal

#### Windows:

```cmd
# Di chuyển đến vị trí file
cd C:\path\to\your\file

# Chạy chương trình
python hello_world.py
```

#### macOS/Linux:

```bash
# Di chuyển đến vị trí file
cd /path/to/your/file

# Chạy chương trình
python3 hello_world.py
# hoặc
python hello_world.py
```

### 🔧 Phương pháp 2: VS Code

1. Mở `hello_world.py` trong VS Code
2. Nhấp nút "Run Python File" (▶️) ở góc trên bên phải
3. Hoặc nhấn `Ctrl+F5` (Windows) / `Cmd+F5` (Mac)
4. Kết quả xuất hiện trong panel terminal

### 📓 Phương pháp 3: Jupyter Notebook

```python
# Trong một cell Jupyter
print("Hello, World!")
# Nhấn Shift+Enter để chạy
```

### 🐍 Phương pháp 4: Chế độ tương tác Python

```bash
# Start Python interpreter
python

# In Python prompt:
>>> print(\"Hello, World!\")
Hello, World!
>>> exit()
```

---

## 3. Understanding the Output

### 📺 What You Should See

```
Hello, World!
Welcome to Python Programming!
This is my first Python program.
🐍 Python is awesome!
I'm excited to learn programming!
```

### 🔍 How `print()` Works

```python
# Different ways to use print()
print(\"Simple text\")                    # Basic string
print('Single quotes work too')          # Single vs double quotes
print(\"Text with\", \"multiple\", \"parts\")     # Multiple arguments
print()                                  # Empty line
print(\"Line 1\\nLine 2\")                 # New line character
```

**Output:**

```
Simple text
Single quotes work too
Text with multiple parts

Line 1
Line 2
```

### 📋 Print Function Parameters

```python
# Separator parameter
print(\"A\", \"B\", \"C\", sep=\"-\")           # Output: A-B-C
print(\"A\", \"B\", \"C\", sep=\" | \")         # Output: A | B | C

# End parameter
print(\"Hello\", end=\" \")
print(\"World\")                          # Output: Hello World (same line)

# Multiple parameters
print(\"Name\", \"Age\", \"City\", sep=\", \", end=\".\\n\")
# Output: Name, Age, City.
```

---

## 4. Interactive vs Script Mode

### 🎮 Interactive Mode (REPL)

**REPL** = Read-Eval-Print Loop

```python
# Start interactive mode
python

# Try these commands:
>>> 2 + 3
5
>>> name = \"Alice\"
>>> print(f\"Hello, {name}!\")
Hello, Alice!
>>> help(print)  # Get help on print function
```

**Advantages:**

- ✅ Immediate feedback
- ✅ Good for testing small code snippets
- ✅ Explore functions and modules
- ✅ Quick calculations

**Disadvantages:**

- ❌ Code doesn't persist
- ❌ Hard to edit long programs
- ❌ No version control

### 📜 Script Mode

Save code in `.py` files and run them.

**Advantages:**

- ✅ Code persists
- ✅ Can write complex programs
- ✅ Version control friendly
- ✅ Shareable and reusable

**Disadvantages:**

- ❌ Need to run entire file to see results
- ❌ Slower development cycle

### 🎯 When to Use Each?

| Task                   | Interactive | Script |
| ---------------------- | ----------- | ------ |
| Quick calculation      | ✅          | ❌     |
| Testing syntax         | ✅          | ❌     |
| Learning new functions | ✅          | ❌     |
| Writing programs       | ❌          | ✅     |
| Saving work            | ❌          | ✅     |
| Complex logic          | ❌          | ✅     |

---

## 5. Your First Real Program

### 🎯 Personal Introduction Program

Tạo file `introduction.py`:

```python
\"\"\"
Personal Introduction Program
My first real Python program that does something useful!
\"\"\"

# Program header
print(\"=\"*50)
print(\"     PERSONAL INTRODUCTION PROGRAM     \")
print(\"=\"*50)

# Personal information
name = \"[Your Name Here]\"
age = 25  # Replace with your age
city = \"[Your City]\"
hobby = \"[Your Hobby]\"

# Introduction message
print(f\"Hello! My name is {name}.\")
print(f\"I am {age} years old and I live in {city}.\")
print(f\"My favorite hobby is {hobby}.\")
print(\"I'm excited to learn Python programming!\")

# Fun facts
print(\"\\n\" + \"-\"*30)
print(\"FUN FACTS:\")
print(\"-\"*30)
print(f\"• In 10 years, I'll be {age + 10} years old\")
print(f\"• I've been alive for approximately {age * 365} days\")
print(f\"• My name has {len(name)} characters\")

# Closing
print(\"\\n\" + \"=\"*50)
print(\"Thanks for running my first Python program!\")
print(\"🐍 Let's continue learning together!\")
print(\"=\"*50)
```

### 🎨 Customization Challenges

1. **Personalize it**: Replace placeholder values with your real information
2. **Add more facts**: Calculate months lived, hours in a year, etc.
3. **Use emojis**: Make it more visually appealing
4. **Add colors**: Research how to add colored output (advanced)

### 📊 Expected Output

```
==================================================
     PERSONAL INTRODUCTION PROGRAM
==================================================
Hello! My name is Alice Johnson.
I am 25 years old and I live in San Francisco.
My favorite hobby is photography.
I'm excited to learn Python programming!

------------------------------
FUN FACTS:
------------------------------
• In 10 years, I'll be 35 years old
• I've been alive for approximately 9125 days
• My name has 12 characters

==================================================
Thanks for running my first Python program!
🐍 Let's continue learning together!
==================================================
```

---

## 6. Common Beginner Mistakes

### ❌ Mistake 1: Quotes Mismatch

```python
# Wrong
print(\"Hello World')  # SyntaxError

# Correct
print(\"Hello World\")  # or print('Hello World')
```

### ❌ Mistake 2: Missing Parentheses

```python
# Wrong (Python 2 syntax)
print \"Hello World\"  # SyntaxError in Python 3

# Correct
print(\"Hello World\")
```

### ❌ Mistake 3: Indentation Errors

```python
# Wrong
print(\"Hello\")
 print(\"World\")  # IndentationError

# Correct
print(\"Hello\")
print(\"World\")
```

### ❌ Mistake 4: Case Sensitivity

```python
# Wrong
Print(\"Hello\")  # NameError: 'Print' is not defined

# Correct
print(\"Hello\")  # lowercase 'p'
```

---

## 🧪 Practice Exercises

### Exercise 1: Personal Card

Create a program that prints your business card:

```
╔══════════════════════════════╗
║        [YOUR NAME]           ║
║    Python Developer          ║
║                              ║
║  📧 your.email@example.com   ║
║  📱 +1 (555) 123-4567        ║
║  🏠 Your City, Country       ║
╚══════════════════════════════╝
```

### Exercise 2: ASCII Art

Create a program that draws something with text:

```python
print(\"    /\\_/\\  \")
print(\"   ( o.o ) \")
print(\"    > ^ <  \")
print(\"  My first ASCII cat!\")
```

### Exercise 3: Calculation Display

```python
num1 = 15
num2 = 7
print(f\"{num1} + {num2} = {num1 + num2}\")
print(f\"{num1} - {num2} = {num1 - num2}\")
print(f\"{num1} * {num2} = {num1 * num2}\")
print(f\"{num1} / {num2} = {num1 / num2}\")
```

---

## 📋 Checklist

After completing this section, you should be able to:

- [ ] Create a new Python file (.py)
- [ ] Write a basic print statement
- [ ] Run Python code in multiple ways
- [ ] Understand the difference between interactive and script mode
- [ ] Use variables in print statements
- [ ] Format output with f-strings
- [ ] Add comments to your code
- [ ] Debug common syntax errors

---

## 🎯 Key Takeaways

1. **Start Simple**: Every expert was once a beginner
2. **Practice Regularly**: Run code frequently to build muscle memory
3. **Experiment**: Try modifying examples to see what happens
4. **Read Error Messages**: They're helpful, not scary
5. **Have Fun**: Programming should be enjoyable!

---

**Next**: Continue to `04_python_syntax_basics.md` to learn more about Python syntax rules.
