import numpy as np
import time

def main():
    """Broadcasting và Vectorization với NumPy"""
    print("=== BROADCASTING & VECTORIZATION ===")
    print()
    
    # Tạo data với shape khác nhau
    np.random.seed(42)
    matrix_2d = np.random.randint(1, 10, (4, 5))
    vector_1d = np.random.randint(1, 5, 5)
    scalar = 2
    
    print("Original 2D Matrix (4x5):")
    print(matrix_2d)
    print()
    print("1D Vector (5,):")
    print(vector_1d)
    print()
    print("Scalar:", scalar)
    print()
    
    # Broadcasting operations
    print("🔢 BROADCASTING OPERATIONS:")
    print()
    
    # Matrix + Vector broadcasting
    result_add = matrix_2d + vector_1d
    print("1. Matrix + Vector (4x5 + 5):")
    print(result_add)
    print()
    
    # Matrix * Scalar broadcasting
    result_mult = matrix_2d * scalar
    print("2. Matrix * Scalar (4x5 * scalar):")
    print(result_mult)
    print()
    
    # Normalization using broadcasting
    print("📊 NORMALIZATION (Z-score):")
    matrix_mean = np.mean(matrix_2d)
    matrix_std = np.std(matrix_2d)
    normalized = (matrix_2d - matrix_mean) / matrix_std
    
    print(f"Original mean: {matrix_mean:.1f}, std: {matrix_std:.1f}")
    print("Normalized matrix:")
    print(np.round(normalized, 2))
    print()
    
    # Distance matrix calculation
    print("🎯 DISTANCE MATRIX:")
    points = np.random.rand(3, 2) * 10
    print(f"Points shape: {points.shape}")
    
    # Broadcasting để tính distance matrix
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distances = np.sqrt(np.sum(diff**2, axis=2))
    
    print("Distance matrix (3x3):")
    print(np.round(distances, 2))
    print()
    
    # Performance comparison
    print("⚡ PERFORMANCE COMPARISON:")
    
    # Method 1: Loop (slow)
    start_time = time.time()
    result_loop = np.zeros((1000, 1000))
    for i in range(1000):
        for j in range(1000):
            result_loop[i, j] = i + j
    loop_time = time.time() - start_time
    
    # Method 2: Broadcasting (fast)
    start_time = time.time()
    i_array = np.arange(1000)[:, np.newaxis]
    j_array = np.arange(1000)[np.newaxis, :]
    result_vectorized = i_array + j_array
    vectorized_time = time.time() - start_time
    
    speedup = loop_time / vectorized_time
    
    print(f"Loop method: {loop_time:.4f} seconds")
    print(f"Vectorized method: {vectorized_time:.4f} seconds")
    print(f"Speedup: {speedup:.1f}x faster")
    print()
    
    # Demonstrate broadcasting rules
    print("📐 BROADCASTING RULES DEMO:")
    a = np.ones((3, 4))
    b = np.ones((4,))
    c = np.ones((3, 1))
    
    print(f"Array a shape: {a.shape}")
    print(f"Array b shape: {b.shape}")
    print(f"Array c shape: {c.shape}")
    print(f"a + b result shape: {(a + b).shape}")
    print(f"a + c result shape: {(a + c).shape}")

if __name__ == "__main__":
    main()
