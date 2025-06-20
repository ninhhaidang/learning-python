# Exercise 12: Algorithm Thinking

## Mô tả bài tập

Phát triển tư duy thuật toán thông qua các bài toán logic, pattern recognition và optimization cơ bản.

## Yêu cầu

Thực hiện các nhiệm vụ sau trong file `practice.py`:

### Algorithm 1: Sorting và Searching

1. Tạo list số ngẫu nhiên
2. Implement bubble sort (sắp xếp nổi bọt)
3. Implement linear search (tìm kiếm tuyến tính)
4. So sánh performance với built-in functions
5. Visualize sorting process

### Algorithm 2: Pattern Generation

6. Tạo pattern tam giác số
7. Tạo pattern kim cương
8. Tạo Fibonacci sequence
9. Tạo pattern spiral numbers
10. Generate Prime numbers

### Algorithm 3: String Algorithms

11. Kiểm tra palindrome
12. Find longest word in sentence
13. Count word frequency
14. Remove duplicates preserving order
15. Implement simple encryption/decryption

### Algorithm 4: Mathematical Algorithms

16. Tính greatest common divisor (GCD)
17. Tính least common multiple (LCM)
18. Check if number is prime
19. Generate Pascal's triangle
20. Calculate compound interest

### Algorithm 5: Problem Optimization

21. Find optimal change making (coins)
22. Pack items in knapsack (simplified)
23. Find shortest path in grid
24. Optimize resource allocation
25. Minimize cost calculation

## Đầu ra mong đợi

```
=== SORTING & SEARCHING ===
Original: [64, 34, 25, 12, 22, 11, 90]
Bubble Sort Steps:
  Step 1: [34, 25, 12, 22, 11, 64, 90]
  Step 2: [25, 12, 22, 11, 34, 64, 90]
  ...
Final: [11, 12, 22, 25, 34, 64, 90]

Linear Search for 22: Found at index 2
Built-in search: 0.001ms vs Our search: 0.005ms

=== PATTERN GENERATION ===
Triangle Pattern:
    1
   2 2
  3 3 3
 4 4 4 4

Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

=== STRING ALGORITHMS ===
"racecar" is palindrome: True
"hello world" longest word: "hello" (5 chars)
Word frequency: {'hello': 2, 'world': 1, 'python': 3}

=== MATHEMATICAL ALGORITHMS ===
GCD(48, 18) = 6
LCM(48, 18) = 144
Is 17 prime? True

Pascal's Triangle:
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

=== OPTIMIZATION ===
Change for 67 cents:
  Quarters: 2 (50¢)
  Dimes: 1 (10¢)
  Nickels: 1 (5¢)
  Pennies: 2 (2¢)
Total coins: 6

Knapsack (capacity=10):
  Item: Book (value=5, weight=3)
  Item: Phone (value=8, weight=4)
  Total value: 13, Total weight: 7
```

## Kiến thức cần nắm

- Algorithm design principles
- Time complexity basics
- Space complexity awareness
- Iterative vs recursive thinking
- Pattern recognition
- Mathematical reasoning
- Optimization strategies
- Performance measurement

## Mức độ khó: ⭐⭐⭐⭐⭐
