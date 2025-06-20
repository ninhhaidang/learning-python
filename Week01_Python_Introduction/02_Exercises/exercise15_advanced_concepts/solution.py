#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 15: Advanced Concepts Preview - Solution
Giới thiệu và thực hành với các khái niệm Python nâng cao
"""

import math
import json
from datetime import datetime

def main():
    """Hàm chính giới thiệu các khái niệm Python nâng cao"""
    print("🚀 EXERCISE 15: ADVANCED CONCEPTS PREVIEW")
    print("=" * 50)
    
    # Preview 1: Functions và Modules
    functions_and_modules()
    
    # Preview 2: Lists và Loops
    lists_and_loops()
    
    # Preview 3: Dictionaries và Data Structures
    dictionaries_and_data_structures()
    
    # Preview 4: File Operations
    file_operations()
    
    # Preview 5: Object-Oriented Preview
    object_oriented_preview()
    
    # Preview 6: Advanced Features
    advanced_features()

def functions_and_modules():
    """Preview 1: Functions và Modules"""
    print("\n=== FUNCTIONS & MODULES ===")
    
    # 1. Định nghĩa function đơn giản
    def greet():
        return "Hello from function!"
    
    # 2. Function với parameters và return value
    def calculate_area(length, width):
        """Tính diện tích hình chữ nhật"""
        return length * width
    
    # 3. Function với default parameters
    def introduce(name, age=25, city="Ha Noi"):
        return f"My name is {name}, I'm {age} years old, from {city}"
    
    # Test functions
    print(greet())
    area = calculate_area(5, 3)
    print(f"Calling calculate_area(5, 3):")
    print(f"Area of rectangle: {area}")
    
    # 4. Import và sử dụng modules
    print("\nUsing math module:")
    print(f"√16 = {math.sqrt(16)}")
    print(f"π = {math.pi}")
    
    # 5. Simulate custom module
    print("\nCustom module imported successfully!")
    
    # Default parameters demo
    print(f"\n{introduce('Alice')}")
    print(f"{introduce('Bob', 30, 'Ho Chi Minh')}")

def lists_and_loops():
    """Preview 2: Lists và Loops"""
    print("\n=== LISTS & LOOPS ===")
    
    # 1. Create và manipulate lists
    numbers = [1, 2, 3, 4, 5]
    print(f"Original list: {numbers}")
    
    # 2. Sử dụng for loops với lists
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    print(f"Squared list: {squared}")
    
    # 3. List comprehensions cơ bản (preview)
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")
    
    # 4. Nested lists và 2D arrays
    print("\n2D Matrix:")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    for row in matrix:
        print(row)
    
    # 5. Enumerate preview
    print("\nEnumerate example:")
    fruits = ["apple", "banana", "orange"]
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    
    # Zip preview
    print("\nZip example:")
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")

def dictionaries_and_data_structures():
    """Preview 3: Dictionaries và Data Structures"""
    print("\n=== DICTIONARIES ===")
    
    # 1. Create complex dictionaries
    student = {
        "name": "Alice",
        "age": 20,
        "grades": [85, 92, 78],
        "info": {
            "major": "CS",
            "year": 2
        }
    }
    
    print("Student data:")
    print(json.dumps(student, indent=2))
    
    # 2. Working với nested dictionaries
    print(f"\nStudent name: {student['name']}")
    print(f"Major: {student['info']['major']}")
    print(f"Average grade: {sum(student['grades']) / len(student['grades']):.1f}")
    
    # 3. Multiple students (list of dictionaries)
    students = [
        {"name": "Alice", "grades": [85, 92, 78]},
        {"name": "Bob", "grades": [88, 85, 92]},
        {"name": "Charlie", "grades": [90, 87, 95]}
    ]
    
    # 4. Dictionary comprehensions preview
    grade_averages = {}
    for student in students:
        name = student["name"]
        avg = sum(student["grades"]) / len(student["grades"])
        grade_averages[name] = round(avg, 1)
    
    print(f"\nGrade averages: {grade_averages}")
    
    # 5. JSON-like data manipulation
    course_data = {
        "course": "Python Programming",
        "students": len(students),
        "instructor": "Dr. Smith",
        "duration": "12 weeks"
    }
    
    print(f"\nCourse info: {course_data['course']}")
    print(f"Total students: {course_data['students']}")

def file_operations():
    """Preview 4: File Operations"""
    print("\n=== FILE OPERATIONS ===")
    
    # Simulate file reading (since we can't actually create files in this context)
    print("Reading data.txt:")
    simulated_file_content = [
        "Python is awesome",
        "Learning is fun",
        "Keep coding!"
    ]
    
    for i, line in enumerate(simulated_file_content, 1):
        print(f"Line {i}: {line}")
    
    # CSV processing simulation
    print("\nCSV Processing:")
    csv_data = [
        ["Name", "Age", "Score"],
        ["Alice", "20", "85"],
        ["Bob", "22", "92"],
        ["Charlie", "19", "78"]
    ]
    
    # Print as table
    for row in csv_data:
        print(f"{row[0]:<8} {row[1]:<3} {row[2]}")
    
    # File writing simulation
    print("\n✓ File operations completed successfully")
    print("(In real scenario, files would be created/read from disk)")

def object_oriented_preview():
    """Preview 5: Object-Oriented Preview"""
    print("\n=== OBJECT-ORIENTED PREVIEW ===")
    
    # 1. Simple class definition
    class Car:
        # 2. Class attributes
        wheels = 4
        
        def __init__(self, make, model, year):
            # 3. Instance attributes
            self.make = make
            self.model = model
            self.year = year
            self.is_running = False
        
        # 4. Methods
        def start_engine(self):
            self.is_running = True
            return "Starting engine..."
        
        def stop_engine(self):
            self.is_running = False
            return "Engine stopped."
        
        def get_info(self):
            return f"{self.make} {self.model} ({self.year})"
    
    # 5. Object creation và usage
    print("Creating a Car object:")
    my_car = Car("Toyota", "Camry", 2020)
    print(f"Car: {my_car.get_info()}")
    print(my_car.start_engine())
    print(f"Car is now {'running' if my_car.is_running else 'stopped'}!")
    
    # 6. Inheritance preview
    class ElectricCar(Car):
        def __init__(self, make, model, year, battery_capacity):
            super().__init__(make, model, year)
            self.battery_capacity = battery_capacity
            self.charge_level = 50
        
        def charge(self, amount):
            self.charge_level = min(100, self.charge_level + amount)
            return f"Charging: {self.charge_level - amount}% → {self.charge_level}%"
    
    print("\nInheritance example:")
    tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
    print(f"Electric car {tesla.charge(30)}")

def advanced_features():
    """Preview 6: Advanced Features"""
    print("\n=== ADVANCED FEATURES ===")
    
    # 1. Lambda functions
    square = lambda x: x ** 2
    print(f"Lambda function: square(5) = {square(5)}")
    
    # 2. Map function
    numbers = [1, 2, 3, 4, 5]
    squared_map = list(map(lambda x: x ** 2, numbers))
    print(f"Map result: {squared_map}")
    
    # 3. Filter function
    all_numbers = list(range(1, 11))
    even_filtered = list(filter(lambda x: x % 2 == 0, all_numbers))
    print(f"Filter result: {even_filtered}")
    
    # 4. Simple decorator preview
    def timer_decorator(func):
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Function '{func.__name__}' took {end - start:.3f} seconds")
            return result
        return wrapper
    
    @timer_decorator
    def greet(name):
        return f"Hello, {name}!"
    
    print("\nSimple decorator applied:")
    message = greet("Alice")
    
    # 5. Generator preview
    def fibonacci_generator(n):
        a, b = 0, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1
    
    print("\nGenerator example:")
    fib_sequence = list(fibonacci_generator(8))
    print(f"Fibonacci: {', '.join(map(str, fib_sequence))}")
    
    # 6. Context manager preview
    class SimpleContextManager:
        def __enter__(self):
            print("Opening resource...")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Closing resource...")
    
    print("\nContext manager:")
    with SimpleContextManager():
        print("Using resource...")
    print("File opened and closed automatically ✓")

# Preview of advanced concepts coming in next weeks
def preview_next_weeks():
    """Giới thiệu nội dung các tuần tiếp theo"""
    roadmap = {
        "Week 02": "Control Flow (if/else, loops)",
        "Week 03": "Functions và Modules",
        "Week 04": "Data Structures",
        "Week 05": "File Handling",
        "Week 06": "Object-Oriented Programming",
        "Week 07": "Error Handling",
        "Week 08": "Libraries và Packages",
        "Week 09": "Web Scraping",
        "Week 10": "Data Analysis",
        "Week 11": "Machine Learning Basics",
        "Week 12": "Final Project"
    }
    
    print("\n📚 ROADMAP - TUẦN TIẾP THEO")
    print("=" * 40)
    for week, topic in roadmap.items():
        print(f"{week}: {topic}")

if __name__ == "__main__":
    main()
    preview_next_weeks()
    print("\n🎯 CHÚC MỪNG!")
    print("Bạn đã hoàn thành Week 01 - Python Introduction!")
    print("Sẵn sàng cho hành trình học Python nâng cao! 🚀")
