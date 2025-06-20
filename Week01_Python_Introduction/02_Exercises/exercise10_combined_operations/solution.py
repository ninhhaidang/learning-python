"""
Exercise 10: Combined Operations - Complete Solution

This file demonstrates integration of all Week 1 Python concepts:
- Variables and data types
- Operators and expressions  
- Input/output operations
- String formatting
- Type conversions
- Boolean logic

The program creates a multi-function application with menu system.
"""

import math

def display_menu():
    """Display the main menu options"""
    print("=== Python Fundamentals Integration ===")
    print()
    print("Choose a program to run:")
    print("1. Personal Information Manager")
    print("2. Budget Calculator")
    print("3. Grade Analyzer")
    print("4. Geometry Calculator")
    print("5. Unit Converter")
    print("6. Exit")
    print()

def personal_info_manager():
    """Task 1: Personal Information Manager"""
    print("=== PERSONAL INFORMATION MANAGER ===")
    print()
    
    # Collect personal data
    name = input("Enter your full name: ").strip()
    age = int(input("Enter your age: "))
    height_cm = float(input("Enter your height in cm: "))
    weight_kg = float(input("Enter your weight in kg: "))
    birth_year = int(input("Enter your birth year: "))
    
    # Calculate derived information
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    age_in_days = age * 365
    current_year = 2024  # Assumed current year
    
    # Determine BMI category
    if bmi < 18.5:
        bmi_status = "Underweight"
    elif bmi < 25:
        bmi_status = "Normal"
    elif bmi < 30:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obese"
    
    # Display formatted profile
    print()
    print("┌─────────────────────────────────────┐")
    print("│         PERSONAL PROFILE            │")
    print("├─────────────────────────────────────┤")
    print(f"│ Name: {name:<29} │")
    print(f"│ Age: {age} years ({age_in_days:,} days){'':>11} │")
    print(f"│ Height: {height_cm} cm ({height_m:.2f} m){'':>11} │")
    print(f"│ Weight: {weight_kg} kg{'':>20} │")
    print(f"│ BMI: {bmi:.1f} ({bmi_status}){'':>16} │")
    print(f"│ Birth Year: {birth_year}{'':>21} │")
    print("└─────────────────────────────────────┘")

def budget_calculator():
    """Task 2: Budget Calculator"""
    print("=== BUDGET CALCULATOR ===")
    print()
    
    # Get income
    income = float(input("Enter your monthly income: $"))
    
    # Get expenses
    print("Enter your expenses:")
    rent = float(input("  Rent: $"))
    food = float(input("  Food: $"))
    transportation = float(input("  Transportation: $"))
    entertainment = float(input("  Entertainment: $"))
    other = float(input("  Other: $"))
    
    # Calculate totals
    total_expenses = rent + food + transportation + entertainment + other
    remaining = income - total_expenses
    savings_rate = (remaining / income) * 100 if income > 0 else 0
    
    # Determine budget status
    if savings_rate >= 20:
        status = "✅ Excellent Budget"
    elif savings_rate >= 10:
        status = "✅ Good Budget"
    elif savings_rate >= 0:
        status = "⚠️ Tight Budget"
    else:
        status = "❌ Over Budget"
    
    # Display results
    print()
    print("┌─────────────────────────────┐")
    print("│       BUDGET SUMMARY        │")
    print("├─────────────────────────────┤")
    print(f"│ Monthly Income: ${income:,.2f}{'':>7} │")
    print(f"│ Total Expenses: ${total_expenses:,.2f}{'':>7} │")
    print(f"│ Remaining: ${remaining:,.2f}{'':>12} │")
    print(f"│ Savings Rate: {savings_rate:.1f}%{'':>10} │")
    print(f"│ Status: {status:<15} │")
    print("└─────────────────────────────┘")

def grade_analyzer():
    """Task 3: Grade Analyzer"""
    print("=== GRADE ANALYZER ===")
    print()
    
    # Get number of subjects
    num_subjects = int(input("How many subjects? "))
    
    subjects = []
    scores = []
    
    # Collect scores for each subject
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        score = float(input(f"Enter score for {subject}: "))
        subjects.append(subject)
        scores.append(score)
    
    # Calculate statistics
    total_score = sum(scores)
    average = total_score / num_subjects
    highest = max(scores)
    lowest = min(scores)
    
    # Determine letter grade
    if average >= 90:
        letter_grade = "A"
        gpa_point = 4.0
    elif average >= 80:
        letter_grade = "B"
        gpa_point = 3.0
    elif average >= 70:
        letter_grade = "C"
        gpa_point = 2.0
    elif average >= 60:
        letter_grade = "D"
        gpa_point = 1.0
    else:
        letter_grade = "F"
        gpa_point = 0.0
    
    # Determine pass/fail
    pass_status = "PASS" if average >= 60 else "FAIL"
    
    # Display results
    print()
    print("┌─────────────────────────────────┐")
    print("│         GRADE REPORT            │")
    print("├─────────────────────────────────┤")
    
    for i, (subject, score) in enumerate(zip(subjects, scores)):
        print(f"│ {subject}: {score}{'':>20} │")
    
    print("├─────────────────────────────────┤")
    print(f"│ Average: {average:.1f}{'':>20} │")
    print(f"│ Letter Grade: {letter_grade}{'':>17} │")
    print(f"│ GPA Point: {gpa_point}{'':>18} │")
    print(f"│ Status: {pass_status}{'':>21} │")
    print(f"│ Highest: {highest}{'':>20} │")
    print(f"│ Lowest: {lowest}{'':>21} │")
    print("└─────────────────────────────────┘")

def geometry_calculator():
    """Task 4: Geometry Calculator"""
    print("=== GEOMETRY CALCULATOR ===")
    print()
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Cylinder")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        # Rectangle
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        perimeter = 2 * (length + width)
        
        print(f"\nRectangle Results:")
        print(f"Area: {area:.2f} square units")
        print(f"Perimeter: {perimeter:.2f} units")
        
    elif choice == "2":
        # Circle
        radius = float(input("Enter radius: "))
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        
        print(f"\nCircle Results:")
        print(f"Area: {area:.2f} square units")
        print(f"Circumference: {circumference:.2f} units")
        
    elif choice == "3":
        # Triangle
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        side1 = float(input("Enter side 1: "))
        side2 = float(input("Enter side 2: "))
        side3 = float(input("Enter side 3: "))
        
        area = 0.5 * base * height
        perimeter = side1 + side2 + side3
        
        print(f"\nTriangle Results:")
        print(f"Area: {area:.2f} square units")
        print(f"Perimeter: {perimeter:.2f} units")
        
    elif choice == "4":
        # Cylinder
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        
        base_area = math.pi * radius ** 2
        volume = base_area * height
        surface_area = 2 * base_area + 2 * math.pi * radius * height
        
        print(f"\nCylinder Results:")
        print(f"Volume: {volume:.2f} cubic units")
        print(f"Surface Area: {surface_area:.2f} square units")
    else:
        print("Invalid choice!")

def unit_converter():
    """Task 5: Unit Converter"""
    print("=== UNIT CONVERTER ===")
    print()
    print("Choose conversion type:")
    print("1. Temperature (Celsius ↔ Fahrenheit)")
    print("2. Length (Meters ↔ Feet)")
    print("3. Weight (Kg ↔ Pounds)")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        # Temperature conversion
        temp_choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").upper()
        
        if temp_choice == "C":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.1f}°F")
        elif temp_choice == "F":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.1f}°C")
        else:
            print("Invalid choice!")
            
    elif choice == "2":
        # Length conversion
        length_choice = input("Convert (M)eters to Feet or (F)eet to Meters? ").upper()
        
        if length_choice == "M":
            meters = float(input("Enter length in meters: "))
            feet = meters * 3.28084
            print(f"{meters} m = {feet:.2f} ft")
        elif length_choice == "F":
            feet = float(input("Enter length in feet: "))
            meters = feet / 3.28084
            print(f"{feet} ft = {meters:.2f} m")
        else:
            print("Invalid choice!")
            
    elif choice == "3":
        # Weight conversion
        weight_choice = input("Convert (K)g to Pounds or (P)ounds to Kg? ").upper()
        
        if weight_choice == "K":
            kg = float(input("Enter weight in kg: "))
            pounds = kg * 2.20462
            print(f"{kg} kg = {pounds:.2f} lbs")
        elif weight_choice == "P":
            pounds = float(input("Enter weight in pounds: "))
            kg = pounds / 2.20462
            print(f"{pounds} lbs = {kg:.2f} kg")
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")

def main():
    """Main program with menu system"""
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                personal_info_manager()
            elif choice == "2":
                budget_calculator()
            elif choice == "3":
                grade_analyzer()
            elif choice == "4":
                geometry_calculator()
            elif choice == "5":
                unit_converter()
            elif choice == "6":
                print("Thank you for using Python Fundamentals Integration!")
                break
            else:
                print("Invalid choice! Please enter 1-6.")
            
            # Ask if user wants to continue
            print()
            continue_choice = input("Continue? (y/n): ").lower()
            if continue_choice != 'y':
                print("Thank you for using Python Fundamentals Integration!")
                break
                
        except ValueError:
            print("Invalid input! Please enter numeric values where required.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        print("\n" + "="*50 + "\n")

# Run the main program
if __name__ == "__main__":
    main()
