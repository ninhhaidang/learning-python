#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 14: Creative Applications - Solution
Ứng dụng kiến thức Python vào các dự án sáng tạo và thực tế
"""

import random
import string
from datetime import datetime, timedelta

def main():
    """Hàm chính chạy tất cả các project sáng tạo"""
    print("🎨 EXERCISE 14: CREATIVE APPLICATIONS")
    print("=" * 50)
    
    # Project 1: ASCII Art Generator
    ascii_art_generator()
    
    # Project 2: Password Generator & Manager
    password_generator_manager()
    
    # Project 3: Personal Finance Tracker
    finance_tracker()
    
    # Project 4: Text-based Adventure Game
    adventure_game()
    
    # Project 5: Data Visualization (ASCII)
    ascii_data_visualization()
    
    # Project 6: Mini Applications
    mini_applications()

def ascii_art_generator():
    """Project 1: ASCII Art Generator"""
    print("\n=== ASCII ART GENERATOR ===")
    
    # 1. Banner text generator
    text = "PYTHON"
    print(f'Input: "{text}"')
    print()
    
    # ASCII font for PYTHON
    ascii_font = {
        'P': ["██████ ", "██   ██", "██████ ", "██     ", "██     "],
        'Y': ["██    ██", " ██  ██ ", "  ████  ", "   ██   ", "   ██   "],
        'T': ["████████", "   ██   ", "   ██   ", "   ██   ", "   ██   "],
        'H': ["██   ██", "██   ██", "███████", "██   ██", "██   ██"],
        'O': [" ██████ ", "██    ██", "██    ██", "██    ██", " ██████ "],
        'N': ["███   ██", "████  ██", "██ ██ ██", "██  ████", "██   ███"]
    }
    
    # Print banner
    for i in range(5):
        line = ""
        for char in text:
            if char in ascii_font:
                line += ascii_font[char][i] + " "
        print(line)
    
    print()
    
    # 2. Triangle pattern
    print("Triangle Pattern:")
    height = 5
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)
    
    print()
    
    # 3. Square pattern
    print("Square Pattern:")
    size = 5
    for i in range(size):
        if i == 0 or i == size - 1:
            print("* " * size)
        else:
            print("* " + "  " * (size - 2) + "*")
    
    print()
    
    # 4. Circle pattern (simplified)
    print("Circle Pattern:")
    radius = 3
    for i in range(2 * radius + 1):
        for j in range(2 * radius + 1):
            distance = ((i - radius) ** 2 + (j - radius) ** 2) ** 0.5
            if abs(distance - radius) < 0.7:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def password_generator_manager():
    """Project 2: Password Generator & Manager"""
    print("\n=== PASSWORD GENERATOR ===")
    
    # 1. Generate secure password
    def generate_password(length=12, use_upper=True, use_lower=True, 
                         use_numbers=True, use_special=True):
        chars = ""
        if use_lower:
            chars += string.ascii_lowercase
        if use_upper:
            chars += string.ascii_uppercase
        if use_numbers:
            chars += string.digits
        if use_special:
            chars += "!@#$%^&*"
        
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
    
    # 2. Check password strength
    def check_password_strength(password):
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 25
            feedback.append("Length: ✓ (12+ chars)")
        else:
            feedback.append(f"Length: ✗ ({len(password)} chars, need 12+)")
        
        # Character type checks
        if any(c.isupper() for c in password):
            score += 20
            feedback.append("Uppercase: ✓")
        else:
            feedback.append("Uppercase: ✗")
        
        if any(c.islower() for c in password):
            score += 20
            feedback.append("Lowercase: ✓")
        else:
            feedback.append("Lowercase: ✗")
        
        if any(c.isdigit() for c in password):
            score += 15
            feedback.append("Numbers: ✓")
        else:
            feedback.append("Numbers: ✗")
        
        if any(c in "!@#$%^&*" for c in password):
            score += 20
            feedback.append("Special chars: ✓")
        else:
            feedback.append("Special chars: ✗")
        
        return score, feedback
    
    # Generate and test password
    password = generate_password()
    score, feedback = check_password_strength(password)
    
    print(f"Generated Password: {password}")
    
    if score >= 90:
        strength = "Excellent"
    elif score >= 70:
        strength = "Good"
    elif score >= 50:
        strength = "Fair"
    else:
        strength = "Weak"
    
    print(f"Strength Score: {score}/100 ({strength})")
    for item in feedback:
        print(f"- {item}")

def finance_tracker():
    """Project 3: Personal Finance Tracker"""
    print("\n=== FINANCE TRACKER ===")
    
    # Sample data
    current_date = datetime.now()
    month_name = current_date.strftime("%B %Y")
    
    income = 5000
    expenses = {
        "Food": 800,
        "Rent": 1500,
        "Transport": 300,
        "Other": 600
    }
    
    total_expenses = sum(expenses.values())
    net_savings = income - total_expenses
    savings_goal = 2000
    goal_percentage = (net_savings / savings_goal) * 100
    
    print(f"📊 MONTHLY REPORT - {month_name}")
    print(f"Income: ${income:,}")
    print(f"Expenses: ${total_expenses:,}")
    
    for category, amount in expenses.items():
        percentage = (amount / total_expenses) * 100
        print(f"  - {category}: ${amount} ({percentage:.0f}%)")
    
    print(f"Net Savings: ${net_savings:,}")
    print(f"Goal: ${savings_goal:,} ({goal_percentage:.0f}% achieved)")
    
    # Simple expense visualization
    print("\nExpense Breakdown:")
    max_width = 30
    for category, amount in expenses.items():
        bar_length = int((amount / max(expenses.values())) * max_width)
        bar = "█" * bar_length + "░" * (max_width - bar_length)
        print(f"{category:10} {bar} ${amount}")

def adventure_game():
    """Project 4: Text-based Adventure Game"""
    print("\n=== ADVENTURE GAME ===")
    print("🏰 WELCOME TO DUNGEON QUEST!")
    print("You are in a dark castle...")
    
    # Game state
    player = {
        "location": "entrance",
        "inventory": ["sword", "shield", "potion"],
        "hp": 100
    }
    
    dragon = {
        "hp": 100,
        "awake": False
    }
    
    locations = {
        "entrance": {
            "description": "You stand at the castle entrance. Dark corridors lead north and east.",
            "exits": {"north": "throne_room", "east": "armory"}
        },
        "throne_room": {
            "description": "A grand throne room. A dragon sleeps here.",
            "exits": {"south": "entrance"}
        },
        "armory": {
            "description": "An old armory with rusty weapons.",
            "exits": {"west": "entrance"}
        }
    }
    
    def show_status():
        current_location = locations[player["location"]]
        print(f"\n{current_location['description']}")
        if player["location"] == "throne_room" and not dragon["awake"]:
            print("A dragon sleeps here.")
        elif player["location"] == "throne_room" and dragon["awake"]:
            print(f"An angry dragon faces you! Dragon HP: {dragon['hp']}/100")
    
    def process_command(command):
        if command.startswith("go "):
            direction = command.split()[1]
            current_location = locations[player["location"]]
            if direction in current_location["exits"]:
                player["location"] = current_location["exits"][direction]
                show_status()
            else:
                print("You can't go that way.")
        
        elif command == "inventory":
            print("Items:", ", ".join(player["inventory"]))
        
        elif command.startswith("use "):
            item = command.split()[1]
            if item in player["inventory"]:
                if item == "sword" and player["location"] == "throne_room":
                    if not dragon["awake"]:
                        print("You attack the dragon! It wakes up!")
                        dragon["awake"] = True
                        dragon["hp"] -= 20
                    else:
                        print("You strike the dragon!")
                        dragon["hp"] -= 20
                    print(f"Dragon HP: {dragon['hp']}/100")
                    if dragon["hp"] <= 0:
                        print("🎉 You defeated the dragon! You win!")
                        return False
                else:
                    print(f"You use the {item}.")
            else:
                print("You don't have that item.")
        
        elif command == "quit":
            return False
        else:
            print("Commands: go <direction>, inventory, use <item>, quit")
        
        return True
    
    # Simple demo
    show_status()
    commands = ["go north", "inventory", "use sword"]
    
    for cmd in commands:
        print(f"> {cmd}")
        if not process_command(cmd):
            break

def ascii_data_visualization():
    """Project 5: Data Visualization (ASCII)"""
    print("\n=== DATA VISUALIZATION ===")
    
    # Bar chart
    print("Sales Data Q4 2024:")
    sales_data = {"Oct": 200, "Nov": 260, "Dec": 320}
    max_value = max(sales_data.values())
    
    for month, value in sales_data.items():
        bar_length = int((value / max_value) * 30)
        bar = "█" * bar_length
        print(f"{month} {bar} {value}")
    
    print()
    
    # Pie chart simulation
    print("Pie Chart - Market Share:")
    market_data = {"Product A": 60, "Product B": 30, "Product C": 10}
    
    for product, percentage in market_data.items():
        filled = int(percentage / 5)  # Each symbol represents 5%
        empty = 20 - filled
        chart = "█" * filled + "░" * empty
        print(f"{product} {chart} {percentage}%")
    
    print()
    
    # Line graph (simplified)
    print("Temperature Trend (7 days):")
    temps = [18, 22, 25, 23, 20, 19, 21]
    max_temp = max(temps)
    min_temp = min(temps)
    
    for i, temp in enumerate(temps):
        height = int(((temp - min_temp) / (max_temp - min_temp)) * 10)
        spaces = " " * height
        print(f"Day {i+1}: {spaces}* ({temp}°C)")

def mini_applications():
    """Project 6: Mini Applications"""
    print("\n=== MINI APPLICATIONS ===")
    
    # Unit converter
    print("🌡️  UNIT CONVERTER")
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"{celsius}°C = {fahrenheit}°F = {kelvin}K")
    print()
    
    # Simple calendar
    print("📅 CALENDAR GENERATOR")
    print("    December 2024")
    print("Mo Tu We Th Fr Sa Su")
    
    # Simple December 2024 calendar
    days = [
        "                   1",
        " 2  3  4  5  6  7  8",
        " 9 10 11 12 13 14 15",
        "16 17 18 19 20 21 22",
        "23 24 25 26 27 28 29",
        "30 31"
    ]
    
    for day_row in days:
        print(day_row)
    
    print()
    
    # File organizer simulator
    print("📁 FILE ORGANIZER")
    files = [
        "photo1.jpg", "photo2.png", "document.pdf", "report.docx",
        "video.mp4", "music.mp3", "presentation.pptx", "data.csv",
        "image3.gif", "archive.zip", "notes.txt", "budget.xlsx"
    ]
    
    categories = {
        "Images": [".jpg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx", ".pptx"],
        "Media": [".mp4", ".mp3"],
        "Archives": [".zip"]
    }
    
    organized = {cat: [] for cat in categories}
    organized["Other"] = []
    
    for file in files:
        categorized = False
        for category, extensions in categories.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                organized[category].append(file)
                categorized = True
                break
        if not categorized:
            organized["Other"].append(file)
    
    print(f"Processed {len(files)} files:")
    for category, file_list in organized.items():
        if file_list:
            print(f"- {category}: {len(file_list)} files → /{category}/")

if __name__ == "__main__":
    main()
    print("\n🎉 Hoàn thành tất cả Creative Applications!")
    print("Bạn đã thực hành thành công các dự án sáng tạo với Python!")
