#!/usr/bin/env python3
"""
Week 2 - Exercise 9: Basic For Loops
Solution File

Student Name: Solution
Date: Week 2
"""

print("=== Week 2 - Exercise 9: Basic For Loops ===\n")

# Product data
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
prices = [15000000, 250000, 800000, 5000000, 1200000]

print("=== Store Sales Analysis ===\n")

# Print product list with enumerate
print("Product List:")
for i, (product, price) in enumerate(zip(products, prices), 1):
    print(f"{i}. {product}: {price:,} VND")
print()

# Calculate statistics
total_products = len(products)
total_revenue = sum(prices)
average_price = total_revenue / total_products

print("Sales Statistics:")
print(f"Total Products: {total_products}")
print(f"Total Revenue: {total_revenue:,} VND")
print(f"Average Price: {average_price:,.0f} VND")
print()

# Find most expensive and cheapest
max_price = max(prices)
min_price = min(prices)
max_index = prices.index(max_price)
min_index = prices.index(min_price)

print(f"Most Expensive: {products[max_index]} ({max_price:,} VND)")
print(f"Cheapest: {products[min_index]} ({min_price:,} VND)")
print()

# Count products over 1 million
expensive_products = []
for product, price in zip(products, prices):
    if price > 1000000:
        expensive_products.append((product, price))

print(f"Products over 1 million VND: {len(expensive_products)}")
for product, price in expensive_products:
    print(f"- {product}: {price:,} VND")
print()

# Price categories
categories = {
    "Under 500K": 0,
    "500K - 1M": 0, 
    "1M - 5M": 0,
    "Over 5M": 0
}

for price in prices:
    if price < 500000:
        categories["Under 500K"] += 1
    elif price < 1000000:
        categories["500K - 1M"] += 1
    elif price < 5000000:
        categories["1M - 5M"] += 1
    else:
        categories["Over 5M"] += 1

print("Price Categories:")
for category, count in categories.items():
    print(f"{category}: {count} products")
