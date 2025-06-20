# 🚀 Week 1 - Projects: Dự Án Thực Hành

## 📁 Cấu trúc Projects

```
03_Project/
├── project1_calculator/      # Advanced Calculator
├── project2_profile/         # Personal Profile Generator
└── README.md                 # File này
```

---

## 🎯 Project 1: Advanced Calculator

### 📖 Mô tả

Xây dựng calculator nâng cao có thể thực hiện nhiều phép tính và có giao diện user-friendly.

### 🔧 Tính năng

1. **Basic Operations**: +, -, \*, /
2. **Advanced Operations**: Power (^), Square root, Percentage
3. **Scientific Functions**: Sin, Cos, Tan (bonus)
4. **Memory Functions**: Store và recall results
5. **Input Validation**: Handle invalid inputs
6. **User Menu**: Interactive menu system

### 📋 Requirements

- Chương trình chạy trong loop cho đến khi user chọn exit
- Menu rõ ràng, dễ sử dụng
- Handle errors gracefully
- Code được organize tốt với functions

### 🎯 Expected Features

```
====== ADVANCED CALCULATOR ======
1. Basic Calculator (+, -, *, /)
2. Scientific Calculator
3. Unit Converter
4. History
5. Exit

Choose option (1-5):
```

### 📁 Files cần tạo:

- `calculator.py`: Main program
- `functions.py`: Calculator functions
- `utils.py`: Utility functions

---

## 🎯 Project 2: Personal Profile Generator

### 📖 Mô tả

Tạo chương trình thu thập thông tin cá nhân và generate profile card đẹp mắt với nhiều format khác nhau.

### 🔧 Tính năng

1. **Data Collection**: Collect comprehensive personal info
2. **Validation**: Validate email, phone, age
3. **Multiple Formats**: Business card, CV summary, social media bio
4. **Export Options**: Save to text file
5. **Templates**: Multiple card templates
6. **Statistics**: Calculate some personal stats

### 📋 Information to Collect

- Personal: Name, age, birth date, location
- Contact: Email, phone, social media
- Professional: Job title, company, experience
- Interests: Hobbies, skills, goals
- Physical: Height, weight (optional)

### 🎯 Sample Output

```
╔══════════════════════════════════════╗
║           PROFILE CARD               ║
╠══════════════════════════════════════╣
║ Name: Nguyen Van A                   ║
║ Age: 25 | Location: Ho Chi Minh      ║
║ Job: Python Developer                ║
║ Email: nguyenvana@email.com          ║
║ Interests: Coding, Music, Travel     ║
╚══════════════════════════════════════╝
```

### 📁 Files cần tạo:

- `profile_generator.py`: Main program
- `validation.py`: Input validation functions
- `templates.py`: Card templates
- `data_storage.py`: Save/load functionality

---

## 📊 Grading Criteria

### Project 1: Advanced Calculator (50 points)

- **Functionality (20 pts)**: All required features work correctly
- **Code Quality (10 pts)**: Clean, readable, well-commented
- **Error Handling (10 pts)**: Proper input validation and error messages
- **User Experience (10 pts)**: Easy to use, clear instructions

### Project 2: Profile Generator (50 points)

- **Data Collection (15 pts)**: Comprehensive info gathering
- **Validation (10 pts)**: Proper input validation
- **Output Format (15 pts)**: Beautiful, well-formatted output
- **Code Organization (10 pts)**: Good structure and functions

### Bonus Points (Up to 20 points)

- **Extra Features**: Additional functionalities
- **Creative Design**: Innovative approaches
- **Documentation**: Detailed README files
- **Testing**: Test different scenarios

---

## 🏆 Challenge Features (Bonus)

### Calculator Enhancements:

- [ ] Graph plotting (simple ASCII)
- [ ] Equation solver
- [ ] Matrix calculations
- [ ] Base conversion (binary, hex, octal)
- [ ] Statistical functions

### Profile Generator Enhancements:

- [ ] QR code generation for contact info
- [ ] Multiple language support
- [ ] Photo ASCII art integration
- [ ] Social media link validation
- [ ] Export to different formats (JSON, CSV)

---

## 🔧 Development Guidelines

### 1. Planning Phase

- [ ] Sketch program flow
- [ ] List all required functions
- [ ] Design user interface (text-based)
- [ ] Plan error scenarios

### 2. Development Phase

- [ ] Start with basic functionality
- [ ] Add features incrementally
- [ ] Test each feature thoroughly
- [ ] Refactor and optimize

### 3. Testing Phase

- [ ] Test with valid inputs
- [ ] Test with invalid inputs
- [ ] Test edge cases
- [ ] User acceptance testing

### 4. Documentation Phase

- [ ] Add comments to code
- [ ] Create user manual
- [ ] Document known issues
- [ ] Write reflection

---

## 📝 Submission Requirements

### Files to Submit:

1. **Source Code**: All .py files
2. **Documentation**: README.md for each project
3. **Test Cases**: Sample inputs and outputs
4. **Reflection**: What you learned, challenges faced

### Submission Format:

```
Week01_Projects_[YourName]/
├── project1_calculator/
│   ├── calculator.py
│   ├── functions.py
│   ├── utils.py
│   └── README.md
├── project2_profile/
│   ├── profile_generator.py
│   ├── validation.py
│   ├── templates.py
│   └── README.md
└── reflection.md
```

---

## 🎯 Learning Outcomes

After completing these projects, you should be able to:

- [ ] Structure a larger Python program
- [ ] Use functions to organize code
- [ ] Handle user input and validation
- [ ] Implement error handling
- [ ] Create user-friendly interfaces
- [ ] Debug and test programs
- [ ] Document your code properly

---

## 🔗 Resources

### Python Documentation:

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Math Module](https://docs.python.org/3/library/math.html)

### Tutorials:

- [Real Python - Python Functions](https://realpython.com/defining-your-own-python-function/)
- [Python Error Handling](https://realpython.com/python-exceptions/)

---

**Timeline**: Complete both projects in 3-4 days, spend 1 day on documentation and testing.
