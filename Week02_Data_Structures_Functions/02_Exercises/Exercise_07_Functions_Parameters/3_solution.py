#!/usr/bin/env python3
"""
Week 2 - Exercise 7: Functions with Parameters
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 7: Functions with Parameters ===\n")

# Function to calculate average
def calculate_average(scores):
    return sum(scores) / len(scores)

# Function to find grade with default scale
def find_grade(score, scale="standard"):
    if scale == "standard":
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    elif scale == "strict":
        if score >= 95:
            return "A"
        elif score >= 85:
            return "B"
        elif score >= 75:
            return "C"
        elif score >= 65:
            return "D"
        else:
            return "F"

# Function to analyze scores with default student name
def analyze_scores(scores, student_name="Student"):
    avg = calculate_average(scores)
    grade = find_grade(avg)
    highest = max(scores)
    lowest = min(scores)
    score_range = highest - lowest
    
    print(f"Student: {student_name}")
    print(f"Scores: {scores}")
    print(f"Average: {avg:.1f}")
    print(f"Grade: {grade}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Range: {score_range} points")

# Test with sample data
test_scores = [85, 92, 78, 96, 88]

print("=== Score Analysis System ===\n")
print(f"Test scores: {test_scores}")
print()

# Test individual functions
average = calculate_average(test_scores)
print(f"Average score: {average:.1f}")
print(f"Grade (standard scale): {find_grade(average)}")
print(f"Grade (strict scale): {find_grade(average, 'strict')}")
print()

# Test detailed analysis
print("Detailed Analysis for John:")
analyze_scores(test_scores, "John")
print()

print("Anonymous Analysis:")
analyze_scores(test_scores)
