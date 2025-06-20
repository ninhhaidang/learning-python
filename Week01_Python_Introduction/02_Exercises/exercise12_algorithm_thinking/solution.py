"""
Exercise 12: Algorithm Thinking - Complete Solution

This file demonstrates algorithmic thinking through various classic algorithms
and problem-solving approaches using only Week 1 Python concepts.

Key concepts demonstrated:
- Algorithm design and implementation
- Pattern recognition and generation
- Searching and sorting algorithms
- Mathematical algorithms
- Basic optimization techniques
"""

import random
import time

def algorithm1_sorting_searching():
    """Algorithm 1: Sorting và Searching"""
    print("=== SORTING & SEARCHING ===")
    
    # Tạo list số ngẫu nhiên
    original_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {original_list}")
    
    # Implement bubble sort
    def bubble_sort(arr):
        n = len(arr)
        arr_copy = arr.copy()
        steps = []
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
            steps.append(arr_copy.copy())
        
        return arr_copy, steps
    
    sorted_list, steps = bubble_sort(original_list)
    
    print("Bubble Sort Steps:")
    for i, step in enumerate(steps[:3], 1):  # Hiển thị 3 bước đầu
        print(f"  Step {i}: {step}")
    if len(steps) > 3:
        print("  ...")
    print(f"Final: {sorted_list}")
    
    # Implement linear search
    def linear_search(arr, target):
        for i, value in enumerate(arr):
            if value == target:
                return i
        return -1
    
    target = 22
    index = linear_search(sorted_list, target)
    if index != -1:
        print(f"\nLinear Search for {target}: Found at index {index}")
    else:
        print(f"\nLinear Search for {target}: Not found")
    
    # So sánh performance
    large_list = list(range(1000))
    random.shuffle(large_list)
    
    start_time = time.time()
    result1 = 500 in large_list  # Built-in
    builtin_time = (time.time() - start_time) * 1000
    
    start_time = time.time()
    result2 = linear_search(large_list, 500)  # Our implementation
    our_time = (time.time() - start_time) * 1000
    
    print(f"Built-in search: {builtin_time:.3f}ms vs Our search: {our_time:.3f}ms")

def algorithm2_pattern_generation():
    """Algorithm 2: Pattern Generation"""
    print("\n=== PATTERN GENERATION ===")
    
    # Triangle Pattern
    def triangle_pattern(n):
        print("Triangle Pattern:")
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            numbers = " ".join([str(i)] * i)
            print(spaces + numbers)
    
    triangle_pattern(4)
    
    # Diamond Pattern
    def diamond_pattern(n):
        print("\nDiamond Pattern:")
        # Upper half
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            stars = "* " * i
            print(spaces + stars)
        # Lower half
        for i in range(n - 1, 0, -1):
            spaces = " " * (n - i)
            stars = "* " * i
            print(spaces + stars)
    
    diamond_pattern(3)
    
    # Fibonacci sequence
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    fib_sequence = fibonacci(10)
    print(f"\nFibonacci: {', '.join(map(str, fib_sequence))}")
    
    # Generate Prime numbers
    def generate_primes(limit):
        primes = []
        for num in range(2, limit + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes
    
    primes = generate_primes(30)
    print(f"\nPrime numbers: {', '.join(map(str, primes))}")

def algorithm3_string_algorithms():
    """Algorithm 3: String Algorithms"""
    print("\n=== STRING ALGORITHMS ===")
    
    # Kiểm tra palindrome
    def is_palindrome(s):
        s = s.lower().replace(" ", "")
        return s == s[::-1]
    
    test_word = "racecar"
    print(f'"{test_word}" is palindrome: {is_palindrome(test_word)}')
    
    # Find longest word
    def find_longest_word(sentence):
        words = sentence.split()
        longest = ""
        for word in words:
            # Remove punctuation
            clean_word = ''.join(c for c in word if c.isalpha())
            if len(clean_word) > len(longest):
                longest = clean_word
        return longest
    
    sentence = "hello world python"
    longest = find_longest_word(sentence)
    print(f'"{sentence}" longest word: "{longest}" ({len(longest)} chars)')
    
    # Count word frequency
    def count_word_frequency(text):
        words = text.lower().split()
        frequency = {}
        for word in words:
            clean_word = ''.join(c for c in word if c.isalpha())
            if clean_word:
                frequency[clean_word] = frequency.get(clean_word, 0) + 1
        return frequency
    
    text = "hello world hello python world hello python python"
    freq = count_word_frequency(text)
    print(f"Word frequency: {freq}")
    
    # Remove duplicates preserving order
    def remove_duplicates(lst):
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    original = [1, 2, 3, 2, 4, 3, 5, 1]
    unique = remove_duplicates(original)
    print(f"Remove duplicates: {original} → {unique}")
    
    # Simple encryption/decryption (Caesar cipher)
    def caesar_cipher(text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        return result
    
    original_text = "Hello World"
    encrypted = caesar_cipher(original_text, 3)
    decrypted = caesar_cipher(encrypted, -3)
    print(f"Encryption: '{original_text}' → '{encrypted}' → '{decrypted}'")

def algorithm4_mathematical_algorithms():
    """Algorithm 4: Mathematical Algorithms"""
    print("\n=== MATHEMATICAL ALGORITHMS ===")
    
    # Greatest Common Divisor (GCD)
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # Least Common Multiple (LCM)
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    
    num1, num2 = 48, 18
    print(f"GCD({num1}, {num2}) = {gcd(num1, num2)}")
    print(f"LCM({num1}, {num2}) = {lcm(num1, num2)}")
    
    # Check if number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    test_num = 17
    print(f"Is {test_num} prime? {is_prime(test_num)}")
    
    # Pascal's Triangle
    def pascals_triangle(n):
        triangle = []
        for i in range(n):
            row = [1]
            if triangle:
                for j in range(len(triangle[-1]) - 1):
                    row.append(triangle[-1][j] + triangle[-1][j + 1])
                row.append(1)
            triangle.append(row)
        return triangle
    
    triangle = pascals_triangle(5)
    print("\nPascal's Triangle:")
    for i, row in enumerate(triangle):
        spaces = " " * (len(triangle) - i - 1)
        row_str = " ".join(map(str, row))
        print(spaces + row_str)
    
    # Compound Interest
    def compound_interest(principal, rate, time, compound_frequency=1):
        amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
        return amount
    
    principal = 1000
    rate = 0.05  # 5%
    time = 3  # years
    final_amount = compound_interest(principal, rate, time)
    print(f"\nCompound Interest: ${principal} at {rate*100}% for {time} years = ${final_amount:.2f}")

def algorithm5_optimization():
    """Algorithm 5: Problem Optimization"""
    print("\n=== OPTIMIZATION ===")
    
    # Optimal change making
    def make_change(amount):
        coins = [25, 10, 5, 1]  # quarters, dimes, nickels, pennies
        coin_names = ["Quarters", "Dimes", "Nickels", "Pennies"]
        result = {}
        
        for i, coin in enumerate(coins):
            count = amount // coin
            if count > 0:
                result[coin_names[i]] = count
                amount -= count * coin
        
        return result
    
    amount = 67
    change = make_change(amount)
    print(f"Change for {amount} cents:")
    total_coins = 0
    for coin_name, count in change.items():
        coin_value = {"Quarters": 25, "Dimes": 10, "Nickels": 5, "Pennies": 1}[coin_name]
        print(f"  {coin_name}: {count} ({count * coin_value}¢)")
        total_coins += count
    print(f"Total coins: {total_coins}")
    
    # Simple Knapsack Problem
    def simple_knapsack(items, capacity):
        # items: list of (name, value, weight)
        # Simple greedy approach: sort by value/weight ratio
        ratios = []
        for name, value, weight in items:
            if weight > 0:
                ratios.append((value / weight, name, value, weight))
        
        ratios.sort(reverse=True)
        
        selected = []
        total_value = 0
        total_weight = 0
        
        for ratio, name, value, weight in ratios:
            if total_weight + weight <= capacity:
                selected.append((name, value, weight))
                total_value += value
                total_weight += weight
        
        return selected, total_value, total_weight
    
    items = [
        ("Book", 5, 3),
        ("Phone", 8, 4),
        ("Laptop", 15, 8),
        ("Tablet", 12, 5)
    ]
    capacity = 10
    
    selected, total_value, total_weight = simple_knapsack(items, capacity)
    print(f"\nKnapsack (capacity={capacity}):")
    for name, value, weight in selected:
        print(f"  Item: {name} (value={value}, weight={weight})")
    print(f"Total value: {total_value}, Total weight: {total_weight}")
    
    # Find shortest path in grid (simplified)
    def shortest_path_steps(start, end):
        x1, y1 = start
        x2, y2 = end
        return abs(x2 - x1) + abs(y2 - y1)  # Manhattan distance
    
    start = (0, 0)
    end = (3, 4)
    steps = shortest_path_steps(start, end)
    print(f"\nShortest path from {start} to {end}: {steps} steps")

def main_menu():
    """Menu chính cho tất cả algorithms"""
    while True:
        print("\n" + "="*50)
        print("=== ALGORITHM THINKING CHALLENGES ===")
        print("1. Sorting & Searching")
        print("2. Pattern Generation")
        print("3. String Algorithms")
        print("4. Mathematical Algorithms")
        print("5. Optimization Problems")
        print("6. Run All Algorithms")
        print("7. Exit")
        
        choice = input("\nChọn algorithm (1-7): ")
        
        if choice == "1":
            algorithm1_sorting_searching()
        elif choice == "2":
            algorithm2_pattern_generation()
        elif choice == "3":
            algorithm3_string_algorithms()
        elif choice == "4":
            algorithm4_mathematical_algorithms()
        elif choice == "5":
            algorithm5_optimization()
        elif choice == "6":
            algorithm1_sorting_searching()
            algorithm2_pattern_generation()
            algorithm3_string_algorithms()
            algorithm4_mathematical_algorithms()
            algorithm5_optimization()
        elif choice == "7":
            print("Cảm ơn bạn đã tham gia Algorithm Thinking!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để tiếp tục...")

# Chạy chương trình chính
if __name__ == "__main__":
    main_menu()
