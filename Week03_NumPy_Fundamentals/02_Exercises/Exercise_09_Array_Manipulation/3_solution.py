import numpy as np

def main():
    """Advanced Array Manipulation - Solution"""
    print("=== ADVANCED ARRAY MANIPULATION ===")
    print()
    
    # Set random seed for reproducible results
    np.random.seed(42)
    
    # Create test arrays
    arr_1d = np.arange(12)
    arr_2d = np.random.randint(1, 10, (3, 4))
    arr_3d = np.random.randint(1, 5, (2, 3, 4))
    
    # 📊 RESHAPING OPERATIONS
    print("📊 RESHAPING OPERATIONS:")
    print(f"Original 1D {arr_1d.shape}: {arr_1d}")
    
    # Reshape to different dimensions
    reshaped_3x4 = arr_1d.reshape(3, 4)
    print("Reshaped to (3,4):")
    print(reshaped_3x4)
    print()
    
    reshaped_2x6 = arr_1d.reshape(2, 6)
    print("Reshaped to (2,6):")
    print(reshaped_2x6)
    print()
    
    # 🔗 STACKING OPERATIONS
    print("🔗 STACKING OPERATIONS:")
    array_a = arr_2d.copy()
    array_b = np.random.randint(1, 10, (3, 4))
    
    print(f"Array A (3x4): {array_a.tolist()}")
    print(f"Array B (3x4): {array_b.tolist()}")
    print()
    
    # Vertical stacking (vstack)
    v_stacked = np.vstack([array_a, array_b])
    print("Vertical stack (6x4):")
    print(v_stacked)
    print()
    
    # Horizontal stacking (hstack)
    h_stacked = np.hstack([array_a, array_b])
    print("Horizontal stack (3x8):")
    print(h_stacked)
    print()
    
    # 🎯 FANCY INDEXING
    print("🎯 FANCY INDEXING:")
    flat_array = arr_2d.flatten()
    print(f"Original array: {flat_array}")
    
    # Index-based selection
    indices = [0, 2, 5, 8]
    fancy_indexed = flat_array[indices]
    print(f"Indices {indices}: {fancy_indexed}")
    
    # Boolean indexing
    boolean_mask = flat_array > 6
    boolean_indexed = flat_array[boolean_mask]
    print(f"Boolean mask (>6): {boolean_indexed}")
    print()
    
    # 📐 ADVANCED SLICING
    print("📐 ADVANCED SLICING:")
    print(f"3D Array shape: {arr_3d.shape}")
    
    # Extract middle rows from all matrices
    middle_rows = arr_3d[:, 1, :]
    print("Slice [:, 1, :]: Extract middle rows from all matrices")
    print(f"Result shape: {middle_rows.shape}")
    print(middle_rows)
    print()
    
    # First matrix, all rows, every 2nd column
    first_matrix_cols = arr_3d[0, :, ::2]
    print("Slice [0, :, ::2]: First matrix, all rows, every 2nd column")
    print(f"Result shape: {first_matrix_cols.shape}")
    print(first_matrix_cols)
    print()
    
    # 🔄 ARRAY CONCATENATION
    print("🔄 ARRAY CONCATENATION:")
    
    # Concatenate along axis 0 (vertical)
    concat_axis0 = np.concatenate([array_a, array_b], axis=0)
    print(f"Concatenate along axis 0: Shape {concat_axis0.shape}")
    
    # Concatenate along axis 1 (horizontal)
    concat_axis1 = np.concatenate([array_a, array_b], axis=1)
    print(f"Concatenate along axis 1: Shape {concat_axis1.shape}")
    print()
    
    # 💡 PERFORMANCE TIPS
    print("💡 PERFORMANCE TIPS:")
    print("- Use views instead of copies when possible")
    print("- Leverage broadcasting for efficient operations")
    print("- Choose appropriate axis for operations")
    print()
    
    # Demonstrate view vs copy
    print("📈 VIEW vs COPY DEMONSTRATION:")
    original = np.arange(6).reshape(2, 3)
    view_array = original[:, 1:]  # This creates a view
    copy_array = original[:, 1:].copy()  # This creates a copy
    
    print(f"Original: \n{original}")
    print(f"View shares memory: {np.shares_memory(original, view_array)}")
    print(f"Copy shares memory: {np.shares_memory(original, copy_array)}")
    
    # Modify view affects original
    view_array[0, 0] = 999
    print(f"After modifying view:\n{original}")

if __name__ == "__main__":
    main()
