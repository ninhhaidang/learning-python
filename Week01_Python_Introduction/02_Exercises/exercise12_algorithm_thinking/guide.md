# Hướng dẫn Exercise 12: Algorithm Thinking

## Tổng quan

Bài tập này phát triển tư duy thuật toán thông qua việc implement các algorithms cơ bản. Bạn sẽ học cách phân tích complexity, optimize performance và visualize algorithm behavior.

## Chuẩn bị

Đảm bảo bạn đã nắm vững:

- Loops (for, while) và nested loops
- List manipulation và list comprehension
- String operations
- Mathematical operations
- Functions và recursion concepts
- Basic understanding của time complexity

## Chi tiết từng Algorithm Module

### Algorithm 1: Sorting và Searching

**Bubble Sort Implementation:**

Bubble sort là algorithm đơn giản nhất để hiểu cách sorting hoạt động.

```python
def bubble_sort(arr):
    n = len(arr)
    steps = []

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # Save step for visualization
        steps.append(arr.copy())

    return arr, steps

# Usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_arr, sort_steps = bubble_sort(numbers.copy())
```

**Linear Search Implementation:**

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Performance comparison
import time

start_time = time.time()
result = linear_search(numbers, 22)
our_time = time.time() - start_time

start_time = time.time()
builtin_result = numbers.index(22)
builtin_time = time.time() - start_time
```

**Kiến thức quan trọng:**

- Nested loops cho bubble sort
- Time complexity: O(n²) vs O(n)
- List copying để preserve original data
- Performance measurement với `time` module

### Algorithm 2: Pattern Generation

**Triangle Number Pattern:**

```python
def triangle_pattern(rows):
    for i in range(1, rows + 1):
        # Print spaces for centering
        spaces = " " * (rows - i)
        # Print numbers
        numbers = " ".join([str(i)] * i)
        print(spaces + numbers)

# Diamond pattern
def diamond_pattern(n):
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
```

**Fibonacci Sequence:**

```python
def fibonacci_sequence(n):
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

# Recursive version (less efficient)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```

**Prime Number Generation:**

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Sieve of Eratosthenes (more efficient)
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [i for i in range(2, limit + 1) if is_prime[i]]
```

**Kiến thức quan trọng:**

- String formatting và alignment
- Mathematical sequence patterns
- Optimization techniques (sieve vs trial division)
- Space vs time complexity trade-offs

### Algorithm 3: String Algorithms

**Palindrome Check:**

```python
def is_palindrome(s):
    # Method 1: Simple reverse
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

# Method 2: Two pointers
def is_palindrome_two_pointers(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

**Word Frequency Counter:**

```python
def word_frequency(text):
    # Clean and split text
    words = text.lower().replace(",", "").replace(".", "").split()

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Using collections.Counter (more pythonic)
from collections import Counter

def word_frequency_counter(text):
    words = text.lower().replace(",", "").replace(".", "").split()
    return dict(Counter(words))
```

**Remove Duplicates Preserving Order:**

```python
def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Using dict (Python 3.7+ maintains insertion order)
def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))
```

**Kiến thức quan trọng:**

- String slicing và reverse `[::-1]`
- Dictionary methods: `get()`, `Counter`
- Set operations cho deduplication
- Two-pointer technique

### Algorithm 4: Mathematical Algorithms

**Greatest Common Divisor (GCD):**

```python
def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

# Recursive version
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd_euclidean(a, b)
```

**Pascal's Triangle:**

```python
def pascal_triangle(rows):
    triangle = []

    for i in range(rows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        row_str = " ".join(map(str, row))
        padding = (max_width - len(row_str)) // 2
        print(" " * padding + row_str)
```

**Prime Check Optimization:**

```python
def is_prime_optimized(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors only
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True
```

**Kiến thức quan trọng:**

- Euclidean algorithm cho GCD
- Combinatorics và mathematical sequences
- Optimization: checking only odd numbers
- Memory management với large computations

### Algorithm 5: Problem Optimization

**Coin Change Problem:**

```python
def make_change(amount, coins=[25, 10, 5, 1]):
    """
    Greedy algorithm for making change
    Works for standard coin systems
    """
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result

def make_change_optimal(amount, coins):
    """
    Dynamic programming approach
    Finds minimum number of coins
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

**Simple Knapsack Problem:**

```python
def knapsack_01(weights, values, capacity):
    """
    0/1 Knapsack using dynamic programming
    """
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

**Grid Path Finding:**

```python
def shortest_path_grid(grid):
    """
    Find shortest path in grid using dynamic programming
    """
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    # Fill first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill first column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill rest of the grid
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[rows-1][cols-1]
```

**Kiến thức quan trọng:**

- Greedy vs Dynamic Programming approaches
- 2D array manipulation
- Optimization problems thinking
- Time/space complexity analysis

## Algorithm Analysis và Optimization

### Time Complexity Analysis

```python
import time
import random

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

# Compare different approaches
def compare_sorting():
    data = [random.randint(1, 1000) for _ in range(1000)]

    # Bubble sort
    bubble_result, bubble_time = measure_time(bubble_sort, data.copy())

    # Built-in sort
    builtin_result, builtin_time = measure_time(sorted, data.copy())

    print(f"Bubble sort: {bubble_time:.4f}s")
    print(f"Built-in sort: {builtin_time:.4f}s")
    print(f"Speedup: {bubble_time/builtin_time:.1f}x")
```

### Memory Usage Optimization

```python
def fibonacci_memory_efficient(n):
    """
    Calculate fibonacci without storing all values
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def generator_fibonacci():
    """
    Generator for infinite fibonacci sequence
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

## Debugging và Testing Strategies

### Unit Testing cho Algorithms

```python
def test_algorithms():
    # Test sorting
    test_data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data, _ = bubble_sort(test_data.copy())
    assert sorted_data == sorted(test_data), "Bubble sort failed"

    # Test search
    assert linear_search([1, 2, 3, 4, 5], 3) == 2, "Linear search failed"
    assert linear_search([1, 2, 3, 4, 5], 6) == -1, "Linear search failed"

    # Test palindrome
    assert is_palindrome("racecar") == True, "Palindrome check failed"
    assert is_palindrome("hello") == False, "Palindrome check failed"

    # Test GCD
    assert gcd_euclidean(48, 18) == 6, "GCD calculation failed"

    print("All tests passed!")

if __name__ == "__main__":
    test_algorithms()
```

### Algorithm Visualization

```python
def visualize_bubble_sort(arr):
    n = len(arr)
    print(f"Original: {arr}")

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped:
            print(f"Step {i + 1}: {arr}")
        else:
            break

    return arr
```

## Tips để Master Algorithm Thinking

### 1. Problem Analysis Framework

```python
def solve_problem_framework(problem):
    """
    1. Understand the problem
    2. Identify input/output
    3. Think of edge cases
    4. Choose appropriate data structures
    5. Design algorithm
    6. Implement
    7. Test and optimize
    """
    pass
```

### 2. Common Algorithm Patterns

- **Divide and Conquer:** Break problem into smaller subproblems
- **Dynamic Programming:** Store results to avoid recomputation
- **Greedy:** Make locally optimal choices
- **Backtracking:** Try all possibilities systematically
- **Two Pointers:** Efficient array/string processing

### 3. Performance Optimization

```python
# Use appropriate data structures
# List vs Set for membership testing
def find_common_slow(list1, list2):
    return [x for x in list1 if x in list2]  # O(n*m)

def find_common_fast(list1, list2):
    set2 = set(list2)
    return [x for x in list1 if x in set2]  # O(n+m)
```

## Common Pitfalls và Solutions

### 1. Off-by-one Errors

```python
# Wrong
for i in range(len(arr) - 1):  # Missing last element

# Right
for i in range(len(arr)):
```

### 2. Infinite Loops

```python
# Wrong
while True:
    # Missing break condition

# Right
while condition:
    # Update condition variables
    pass
```

### 3. Memory Issues

```python
# Inefficient for large data
def inefficient_fibonacci(n):
    if n <= 1:
        return n
    return inefficient_fibonacci(n-1) + inefficient_fibonacci(n-2)

# Better with memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

## Mở rộng và Next Steps

### Advanced Algorithms để học tiếp:

1. **Graph Algorithms:** BFS, DFS, Dijkstra
2. **Advanced Sorting:** Merge Sort, Quick Sort, Heap Sort
3. **String Algorithms:** KMP, Boyer-Moore
4. **Tree Algorithms:** Binary Search Trees, AVL Trees
5. **Advanced DP:** Longest Common Subsequence, Edit Distance

### Practice Resources:

- LeetCode Easy problems
- HackerRank algorithm challenges
- Project Euler mathematical problems
- Implement data structures from scratch

Hãy thực hành implement từng algorithm một cách cẩn thận, analyze complexity và optimize performance!
