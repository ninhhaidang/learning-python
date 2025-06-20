#!/usr/bin/env python3
"""
Week 2 - Exercise 3: Basic Tuples
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 3: Basic Tuples ===\n")

# Create coordinate tuples for cities
hanoi_coords = (21.0285, 105.8542)
hcm_coords = (10.8231, 106.6297)
danang_coords = (16.0544, 108.2022)

# Print coordinates with nice formatting
print("City Coordinates:")
print(f"Hanoi: Latitude {hanoi_coords[0]}, Longitude {hanoi_coords[1]}")
print(f"Ho Chi Minh: Latitude {hcm_coords[0]}, Longitude {hcm_coords[1]}")
print(f"Da Nang: Latitude {danang_coords[0]}, Longitude {danang_coords[1]}")
print()

# Demonstrate tuple unpacking
lat, lon = hanoi_coords
print("Tuple unpacking example:")
print(f"Hanoi latitude: {lat}")
print(f"Hanoi longitude: {lon}")
print()

# Calculate Manhattan distances between cities
def manhattan_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return abs(lat1 - lat2) + abs(lon1 - lon2)

print("Distance calculations (Manhattan distance):")
print(f"Hanoi to Ho Chi Minh: {manhattan_distance(hanoi_coords, hcm_coords):.2f}")
print(f"Hanoi to Da Nang: {manhattan_distance(hanoi_coords, danang_coords):.2f}")
print(f"Ho Chi Minh to Da Nang: {manhattan_distance(hcm_coords, danang_coords):.2f}")
