#!/usr/bin/env python3
"""
Week 2 - Exercise 8: Basic If-Else
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 8: Basic If-Else ===\n")

# Test values
temperature = 28  # Celsius
uv_index = 7

print("=== Weather Analysis System ===\n")
print(f"Temperature: {temperature}°C")
print(f"UV Index: {uv_index}")
print()

# Classify temperature
print("Temperature Analysis:")
if temperature < 15:
    temp_category = "Cold"
elif temperature <= 24:
    temp_category = "Cool"
elif temperature <= 30:
    temp_category = "Warm"
else:
    temp_category = "Hot"

print(f"{temperature}°C is classified as: {temp_category}")
print()

# Classify UV index
print("UV Analysis:")
if uv_index <= 2:
    uv_category = "Low"
elif uv_index <= 5:
    uv_category = "Moderate"
elif uv_index <= 7:
    uv_category = "High"
else:
    uv_category = "Very High"

print(f"UV Index {uv_index} is classified as: {uv_category}")
print()

# Activity recommendations
print("Activity Recommendations:")
if temp_category == "Cold":
    print("- Temperature is cold: Indoor activities recommended")
elif temp_category == "Cool":
    print("- Temperature is cool: Perfect for outdoor activities")
elif temp_category == "Warm":
    print("- Temperature is warm: Great for outdoor activities")
else:
    print("- Temperature is hot: Limit outdoor activities, stay hydrated")

if uv_category == "Low":
    print("- UV is low: No special sun protection needed")
elif uv_category == "Moderate":
    print("- UV is moderate: Light sun protection recommended")
elif uv_category == "High":
    print("- UV is high: Use sunscreen and hat")
else:
    print("- UV is very high: Strong sun protection required")

# Overall recommendation
if temperature >= 20 and temperature <= 30 and uv_index <= 5:
    print("- Overall recommendation: Perfect weather for outdoor activities!")
elif temperature >= 15 and uv_index <= 7:
    print("- Overall recommendation: Good for outdoor activities with sun protection")
else:
    print("- Overall recommendation: Consider indoor activities or take extra precautions")

print()

# Test edge cases
print("Testing edge cases:")
test_temps = [-5, 15, 30, 35]
for temp in test_temps:
    if temp < 15:
        category = "Cold"
    elif temp <= 24:
        category = "Cool"
    elif temp <= 30:
        category = "Warm"
    else:
        category = "Hot"
    print(f"Temperature {temp}°C: {category}")

print()
test_uvs = [0, 3, 8]
for uv in test_uvs:
    if uv <= 2:
        category = "Low"
    elif uv <= 5:
        category = "Moderate"
    elif uv <= 7:
        category = "High"
    else:
        category = "Very High"
    print(f"UV Index {uv}: {category}")
