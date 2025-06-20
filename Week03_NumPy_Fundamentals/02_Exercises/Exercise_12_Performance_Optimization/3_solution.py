import numpy as np
import time

def main():
    """NumPy Performance Optimization Techniques"""
    print("=== PERFORMANCE OPTIMIZATION ===")
    print()
    
    # Test data size
    size = 1000000
    
    print("🚀 VECTORIZATION BENCHMARKS:")
    print(f"Testing with array size: {size:,}")
    print()
    
    # Create test data
    np.random.seed(42)
    arr1 = np.random.rand(size)
    arr2 = np.random.rand(size)
    
    # Method 1: Pure Python loop (slow)
    start_time = time.time()
    result_loop = []
    for i in range(len(arr1)):
        result_loop.append(arr1[i] * arr2[i] + np.sin(arr1[i]))
    loop_time = time.time() - start_time
    
    # Method 2: NumPy vectorized (fast)
    start_time = time.time()
    result_vectorized = arr1 * arr2 + np.sin(arr1)
    vectorized_time = time.time() - start_time
    
    speedup = loop_time / vectorized_time
    
    print(f"Pure Python loop: {loop_time:.3f} seconds")
    print(f"NumPy vectorized: {vectorized_time:.3f} seconds")
    print(f"Speedup: {speedup:.1f}x faster")
    print()
    
    # Memory optimization example
    print("💾 MEMORY OPTIMIZATION:")
    
    # Inefficient: Multiple temporary arrays
    start_time = time.time()
    x = np.random.rand(size)
    temp1 = x ** 2
    temp2 = np.sin(temp1)
    temp3 = temp2 + 1
    result_inefficient = np.sqrt(temp3)
    inefficient_time = time.time() - start_time
    
    # Efficient: In-place operations
    start_time = time.time()
    x = np.random.rand(size)
    x **= 2
    x = np.sin(x)
    x += 1
    np.sqrt(x, out=x)
    efficient_time = time.time() - start_time
    
    print(f"Inefficient approach: {inefficient_time:.3f} seconds")
    print(f"Efficient approach: {efficient_time:.3f} seconds")
    print(f"Speed improvement: {inefficient_time/efficient_time:.1f}x faster")
    print()
    
    # Advanced vectorization examples
    print("⚡ ADVANCED VECTORIZATION:")
    
    # Example: Distance matrix calculation
    points = np.random.rand(1000, 2)
    
    # Slow way: nested loops
    start_time = time.time()
    n = len(points)
    distances_loop = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distances_loop[i, j] = np.sqrt(np.sum((points[i] - points[j])**2))
    loop_time = time.time() - start_time
    
    # Fast way: broadcasting
    start_time = time.time()
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distances_fast = np.sqrt(np.sum(diff**2, axis=2))
    broadcast_time = time.time() - start_time
    
    print(f"Nested loops: {loop_time:.3f} seconds")
    print(f"Broadcasting: {broadcast_time:.3f} seconds")
    print(f"Speedup: {loop_time/broadcast_time:.1f}x faster")
    print()
    
    # Memory usage tips
    print("🧠 MEMORY USAGE TIPS:")
    
    # Use appropriate dtypes
    large_array = np.random.randint(0, 100, size, dtype=np.int64)
    optimized_array = np.random.randint(0, 100, size, dtype=np.int8)
    
    memory_saved = (large_array.nbytes - optimized_array.nbytes) / large_array.nbytes * 100
    
    print(f"int64 array: {large_array.nbytes / 1024**2:.1f} MB")
    print(f"int8 array: {optimized_array.nbytes / 1024**2:.1f} MB")
    print(f"Memory saved: {memory_saved:.1f}%")
    print()
    
    # Best practices summary
    print("📋 PERFORMANCE BEST PRACTICES:")
    print("✅ Use vectorized operations instead of loops")
    print("✅ Minimize temporary array creation")
    print("✅ Use appropriate data types")
    print("✅ Leverage broadcasting for multi-dimensional operations")
    print("✅ Use in-place operations when possible")
    print("✅ Profile your code to identify bottlenecks")
    print()
    
    print("🎯 OPTIMIZATION SUCCESS!")
    print(f"Total speedup demonstrated: {speedup:.0f}x - {loop_time/broadcast_time:.0f}x faster!")

if __name__ == "__main__":
    main()
