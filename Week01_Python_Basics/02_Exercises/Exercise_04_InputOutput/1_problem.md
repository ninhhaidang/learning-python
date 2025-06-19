# Week 1 - Exercise 4: Input/Output & Integration

**Bài tập tích hợp toàn bộ kiến thức Week 1 với user interaction**

## 🎯 Mục tiêu

- Thực hành user input và validation
- Xử lý errors và edge cases
- Tích hợp tất cả concepts đã học
- Xây dựng interactive programs
- Format output professional

---

## Exercise 1: Interactive Data Collector

### TODO 1.1: Personal Information Collector

Viết chương trình thu thập và validate thông tin cá nhân:

```python
def collect_personal_info():
    """Interactive personal information collector with validation"""

    print("=== PERSONAL INFORMATION COLLECTOR ===\n")

    # Collect name
    while True:
        name = input("Enter your full name: ").strip()
        if len(name) >= 2 and name.replace(" ", "").isalpha():
            name = name.title()  # Proper case
            break
        else:
            print("❌ Please enter a valid name (letters only, min 2 characters)")

    # Collect age
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 <= age <= 120:
                break
            else:
                print("❌ Please enter an age between 0 and 120")
        except ValueError:
            print("❌ Please enter a valid number")

    # Collect height
    while True:
        try:
            height = float(input("Enter your height in meters (e.g., 1.75): "))
            if 0.5 <= height <= 3.0:
                break
            else:
                print("❌ Please enter a realistic height between 0.5 and 3.0 meters")
        except ValueError:
            print("❌ Please enter a valid decimal number")

    # Collect email
    while True:
        email = input("Enter your email: ").strip().lower()
        if "@" in email and "." in email.split("@")[1] and len(email) >= 5:
            break
        else:
            print("❌ Please enter a valid email address")

    # Display summary
    print(f"\n✅ INFORMATION SUMMARY")
    print(f"{'='*40}")
    print(f"Name: {name}")
    print(f"Age: {age} years old")
    print(f"Height: {height:.2f} meters")
    print(f"Email: {email}")

    # Calculate additional info
    age_group = classify_age(age)
    bmi_height_check = "Normal height" if 1.5 <= height <= 2.0 else "Unusual height"

    print(f"\n📊 ANALYSIS")
    print(f"Age group: {age_group}")
    print(f"Height status: {bmi_height_check}")

    return {
        'name': name,
        'age': age,
        'height': height,
        'email': email
    }

def classify_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

# Uncomment to run:
# collect_personal_info()
```

---

## Exercise 2: Interactive Calculator Suite

### TODO 2.1: Menu-driven Calculator

```python
def interactive_calculator():
    """Interactive calculator with multiple functions"""

    while True:
        print("\n🧮 PYTHON CALCULATOR")
        print("=" * 30)
        print("1. Basic arithmetic")
        print("2. Temperature conversion")
        print("3. BMI calculator")
        print("4. Loan calculator")
        print("5. Exit")
        print("-" * 30)

        try:
            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                basic_arithmetic()
            elif choice == 2:
                temperature_converter()
            elif choice == 3:
                bmi_calculator()
            elif choice == 4:
                loan_calculator()
            elif choice == 5:
                print("👋 Thank you for using Python Calculator!")
                break
            else:
                print("❌ Please choose a number between 1-5")

        except ValueError:
            print("❌ Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\n👋 Calculator interrupted. Goodbye!")
            break

        input("\nPress Enter to continue...")

def basic_arithmetic():
    """Basic arithmetic with error handling"""
    print("\n➕ BASIC ARITHMETIC")
    print("-" * 20)

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, %, **): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("❌ Error: Cannot divide by zero!")
                return
            result = num1 / num2
        elif operator == "%":
            if num2 == 0:
                print("❌ Error: Cannot divide by zero!")
                return
            result = num1 % num2
        elif operator == "**":
            try:
                result = num1 ** num2
            except OverflowError:
                print("❌ Error: Result too large!")
                return
        else:
            print("❌ Error: Invalid operator!")
            return

        print(f"✅ Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("❌ Error: Please enter valid numbers!")

def temperature_converter():
    """Interactive temperature converter"""
    print("\n🌡️ TEMPERATURE CONVERTER")
    print("-" * 25)

    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    try:
        choice = int(input("Choose conversion (1-3): "))
        temp = float(input("Enter temperature: "))

        if choice == 1:
            result = (temp * 9/5) + 32
            print(f"✅ {temp}°C = {result:.2f}°F")
        elif choice == 2:
            result = (temp - 32) * 5/9
            print(f"✅ {temp}°F = {result:.2f}°C")
        elif choice == 3:
            if temp < -273.15:
                print("❌ Error: Temperature below absolute zero!")
                return
            result = temp + 273.15
            print(f"✅ {temp}°C = {result:.2f}K")
        else:
            print("❌ Invalid choice!")

    except ValueError:
        print("❌ Please enter valid numbers!")

def bmi_calculator():
    """Interactive BMI calculator"""
    print("\n⚖️ BMI CALCULATOR")
    print("-" * 17)

    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        if weight <= 0 or height <= 0:
            print("❌ Weight and height must be positive!")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"✅ Your BMI: {bmi:.1f}")
        print(f"Category: {category}")

    except ValueError:
        print("❌ Please enter valid numbers!")

def loan_calculator():
    """Simple loan payment calculator"""
    print("\n💰 LOAN CALCULATOR")
    print("-" * 18)

    try:
        principal = float(input("Enter loan amount ($): "))
        rate = float(input("Enter annual interest rate (%): ")) / 100
        years = int(input("Enter loan term (years): "))

        if principal <= 0 or rate < 0 or years <= 0:
            print("❌ Please enter positive values!")
            return

        monthly_rate = rate / 12
        months = years * 12

        if rate == 0:
            monthly_payment = principal / months
        else:
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / \
                            ((1 + monthly_rate)**months - 1)

        total_payment = monthly_payment * months
        total_interest = total_payment - principal

        print(f"✅ LOAN SUMMARY:")
        print(f"Loan amount: ${principal:,.2f}")
        print(f"Interest rate: {rate*100:.2f}% per year")
        print(f"Loan term: {years} years")
        print(f"Monthly payment: ${monthly_payment:,.2f}")
        print(f"Total payment: ${total_payment:,.2f}")
        print(f"Total interest: ${total_interest:,.2f}")

    except ValueError:
        print("❌ Please enter valid numbers!")

# Uncomment to run:
# interactive_calculator()
```

---

## Exercise 3: Data Processing System

### TODO 3.1: Student Grade Manager

```python
def student_grade_manager():
    """Interactive student grade management system"""

    students = {}  # Dictionary to store student data

    while True:
        print("\n📚 STUDENT GRADE MANAGER")
        print("=" * 30)
        print("1. Add student")
        print("2. View student")
        print("3. View all students")
        print("4. Calculate statistics")
        print("5. Exit")
        print("-" * 30)

        try:
            choice = int(input("Choose option (1-5): "))

            if choice == 1:
                add_student(students)
            elif choice == 2:
                view_student(students)
            elif choice == 3:
                view_all_students(students)
            elif choice == 4:
                calculate_statistics(students)
            elif choice == 5:
                print("👋 Goodbye!")
                break
            else:
                print("❌ Please choose 1-5")

        except ValueError:
            print("❌ Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break

def add_student(students):
    """Add a new student with grades"""
    print("\n➕ ADD STUDENT")
    print("-" * 15)

    # Get student name
    while True:
        name = input("Enter student name: ").strip().title()
        if len(name) >= 2 and name.replace(" ", "").isalpha():
            break
        print("❌ Please enter a valid name")

    if name in students:
        print(f"❌ Student {name} already exists!")
        return

    # Get grades
    grades = {}
    subjects = ["Math", "English", "Science", "History"]

    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter {subject} grade (0-100): "))
                if 0 <= grade <= 100:
                    grades[subject] = grade
                    break
                else:
                    print("❌ Grade must be between 0 and 100")
            except ValueError:
                print("❌ Please enter a valid number")

    students[name] = grades
    print(f"✅ Student {name} added successfully!")

def view_student(students):
    """View individual student details"""
    if not students:
        print("❌ No students in database!")
        return

    print("\n👤 VIEW STUDENT")
    print("-" * 15)

    name = input("Enter student name: ").strip().title()

    if name not in students:
        print(f"❌ Student {name} not found!")
        return

    grades = students[name]
    average = sum(grades.values()) / len(grades)

    print(f"\n📊 STUDENT REPORT: {name}")
    print("=" * 30)

    for subject, grade in grades.items():
        print(f"{subject:10}: {grade:5.1f}")

    print("-" * 20)
    print(f"{'Average':10}: {average:5.1f}")

    # Determine letter grade
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"{'Grade':10}: {letter_grade:>5}")

def view_all_students(students):
    """View all students summary"""
    if not students:
        print("❌ No students in database!")
        return

    print(f"\n📋 ALL STUDENTS ({len(students)} total)")
    print("=" * 50)
    print(f"{'Name':<20} {'Average':<10} {'Grade':<5}")
    print("-" * 40)

    for name, grades in students.items():
        average = sum(grades.values()) / len(grades)

        if average >= 90:
            letter_grade = "A"
        elif average >= 80:
            letter_grade = "B"
        elif average >= 70:
            letter_grade = "C"
        elif average >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"

        print(f"{name:<20} {average:<10.1f} {letter_grade:<5}")

def calculate_statistics(students):
    """Calculate class statistics"""
    if not students:
        print("❌ No students in database!")
        return

    print("\n📈 CLASS STATISTICS")
    print("=" * 25)

    all_averages = []
    subject_totals = {}

    for name, grades in students.items():
        average = sum(grades.values()) / len(grades)
        all_averages.append(average)

        for subject, grade in grades.items():
            if subject not in subject_totals:
                subject_totals[subject] = []
            subject_totals[subject].append(grade)

    # Overall statistics
    class_average = sum(all_averages) / len(all_averages)
    highest_average = max(all_averages)
    lowest_average = min(all_averages)

    print(f"Class average: {class_average:.1f}")
    print(f"Highest average: {highest_average:.1f}")
    print(f"Lowest average: {lowest_average:.1f}")

    # Subject statistics
    print("\nSubject Averages:")
    print("-" * 20)
    for subject, grades in subject_totals.items():
        subject_avg = sum(grades) / len(grades)
        print(f"{subject:10}: {subject_avg:.1f}")

# Uncomment to run:
# student_grade_manager()
```

---

## Exercise 4: Text Processing Application

### TODO 4.1: Text Analyzer

```python
def text_analyzer():
    """Interactive text analysis tool"""

    print("📝 TEXT ANALYZER")
    print("=" * 20)

    # Get text input
    print("Enter your text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("❌ No text entered!")
        return

    text = " ".join(lines)

    # Perform analysis
    analyze_text(text)

def analyze_text(text):
    """Perform comprehensive text analysis"""

    print("\n📊 ANALYSIS RESULTS")
    print("=" * 30)

    # Basic statistics
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    paragraph_count = text.count('\n\n') + 1

    print(f"Characters (with spaces): {char_count}")
    print(f"Characters (no spaces): {char_count_no_spaces}")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Paragraphs: {paragraph_count}")

    # Reading statistics
    if word_count > 0:
        avg_word_length = char_count_no_spaces / word_count
        reading_time = word_count / 200  # Assume 200 words per minute

        print(f"Average word length: {avg_word_length:.1f} characters")
        print(f"Estimated reading time: {reading_time:.1f} minutes")

    # Character frequency analysis
    print("\n🔤 CHARACTER FREQUENCY")
    print("-" * 25)

    char_freq = {}
    for char in text.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1

    # Show top 5 most frequent characters
    if char_freq:
        sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
        print("Top 5 most frequent letters:")
        for i, (char, count) in enumerate(sorted_chars[:5], 1):
            percentage = (count / sum(char_freq.values())) * 100
            print(f"{i}. '{char}': {count} times ({percentage:.1f}%)")

    # Word frequency analysis
    print("\n📝 WORD FREQUENCY")
    print("-" * 20)

    # Clean and split words
    import string
    clean_text = text.lower()
    for punct in string.punctuation:
        clean_text = clean_text.replace(punct, "")

    words = clean_text.split()
    word_freq = {}

    for word in words:
        if len(word) > 2:  # Only count words longer than 2 characters
            word_freq[word] = word_freq.get(word, 0) + 1

    if word_freq:
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        print("Top 5 most frequent words:")
        for i, (word, count) in enumerate(sorted_words[:5], 1):
            print(f"{i}. '{word}': {count} times")

    # Text complexity analysis
    print("\n📈 COMPLEXITY ANALYSIS")
    print("-" * 25)

    if sentence_count > 0 and word_count > 0:
        avg_words_per_sentence = word_count / sentence_count
        print(f"Average words per sentence: {avg_words_per_sentence:.1f}")

        if avg_words_per_sentence < 15:
            complexity = "Simple"
        elif avg_words_per_sentence < 25:
            complexity = "Moderate"
        else:
            complexity = "Complex"

        print(f"Text complexity: {complexity}")

# Uncomment to run:
# text_analyzer()
```

---

## Exercise 5: Comprehensive Quiz System

### TODO 5.1: Python Basics Quiz

```python
def python_quiz():
    """Interactive Python basics quiz"""

    questions = [
        {
            "question": "What is the result of 5 + 3 * 2?",
            "options": ["A) 16", "B) 11", "C) 10", "D) 13"],
            "answer": "B",
            "explanation": "Due to operator precedence, multiplication happens first: 5 + (3 * 2) = 5 + 6 = 11"
        },
        {
            "question": "Which method removes whitespace from both ends of a string?",
            "options": ["A) remove()", "B) strip()", "C) clean()", "D) trim()"],
            "answer": "B",
            "explanation": "The strip() method removes whitespace from both ends of a string"
        },
        {
            "question": "What does the expression 'bool(0)' return?",
            "options": ["A) True", "B) False", "C) 0", "D) Error"],
            "answer": "B",
            "explanation": "In Python, 0 is falsy, so bool(0) returns False"
        },
        {
            "question": "What is the result of 10 // 3?",
            "options": ["A) 3.33", "B) 3", "C) 4", "D) 1"],
            "answer": "B",
            "explanation": "The // operator performs floor division, so 10 // 3 = 3"
        },
        {
            "question": "Which operator is used for exponentiation in Python?",
            "options": ["A) ^", "B) **", "C) exp()", "D) pow"],
            "answer": "B",
            "explanation": "Python uses ** for exponentiation, e.g., 2 ** 3 = 8"
        }
    ]

    print("🧠 PYTHON BASICS QUIZ")
    print("=" * 25)
    print("Test your knowledge of Week 1 concepts!")
    print("Type A, B, C, or D for each question.\n")

    score = 0
    total_questions = len(questions)

    for i, q in enumerate(questions, 1):
        print(f"Question {i}/{total_questions}:")
        print(f"{q['question']}\n")

        for option in q['options']:
            print(option)

        while True:
            answer = input("\nYour answer: ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("❌ Please enter A, B, C, or D")

        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is {q['answer']}")

        print(f"Explanation: {q['explanation']}\n")
        print("-" * 50)

    # Final results
    percentage = (score / total_questions) * 100

    print(f"\n🎯 QUIZ RESULTS")
    print("=" * 20)
    print(f"Score: {score}/{total_questions} ({percentage:.1f}%)")

    if percentage >= 90:
        grade = "Excellent! 🏆"
    elif percentage >= 80:
        grade = "Very Good! 🥇"
    elif percentage >= 70:
        grade = "Good! 🥈"
    elif percentage >= 60:
        grade = "Fair 🥉"
    else:
        grade = "Needs Improvement 📚"

    print(f"Grade: {grade}")

    # Recommendations
    if percentage < 80:
        print("\n📝 Recommendations:")
        print("- Review the theory materials in 01_Theory/")
        print("- Practice more exercises")
        print("- Try the calculator project")

# Uncomment to run:
# python_quiz()
```

---

## 🎯 Checklist hoàn thành

- [ ] Exercise 1: Interactive Data Collector
- [ ] Exercise 2: Interactive Calculator Suite
- [ ] Exercise 3: Data Processing System
- [ ] Exercise 4: Text Processing Application
- [ ] Exercise 5: Comprehensive Quiz System

## 📚 Tài liệu tham khảo

- Tất cả tài liệu trong `01_Theory/`
- `03_Projects/calculator_project.py` - Tham khảo project structure

## 💡 Integration Tips

- Luôn validate user input
- Provide clear error messages
- Use try-except for error handling
- Format output professionally
- Give users multiple chances to enter correct data
- Include help text và instructions

## 🏆 Final Challenge

Combine tất cả exercises thành một mega-program có:

- Main menu để chọn chức năng
- Data persistence (save/load user data)
- Advanced features như user accounts
- Comprehensive help system

## 🎊 Congratulations!

Nếu bạn hoàn thành tất cả exercises này, bạn đã thành thạo Python basics và sẵn sàng cho Week 2!
