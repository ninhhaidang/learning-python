import numpy as np

def main():
    """Xử lý ảnh grayscale cơ bản với NumPy"""
    print("=== XỬ LÝ ẢNH GRAYSCALE ===")
    print()
    
    # Tạo ảnh grayscale ngẫu nhiên
    np.random.seed(42)
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)
    
    print("Ảnh gốc (10x10):")
    print(image)
    print()
    
    # Áp dụng threshold để tạo ảnh binary
    threshold_image = np.where(image > 128, 255, 0)
    
    print("Ảnh sau threshold (binary):")
    print(threshold_image)
    print()
    
    # Tính histogram phân bố pixel
    hist_ranges = [(0, 64), (64, 128), (128, 192), (192, 256)]
    
    print("📊 HISTOGRAM PHÂN BỐ PIXEL:")
    for i, (low, high) in enumerate(hist_ranges):
        count = np.sum((image >= low) & (image < high))
        percentage = count / image.size * 100
        print(f"[{low}-{high-1}]: {count:4d} pixels ({percentage:.1f}%)")
    print()
    
    # Tìm vùng 3x3 sáng nhất
    max_avg = 0
    max_pos = (0, 0)
    min_avg = 255
    min_pos = (0, 0)
    
    for i in range(image.shape[0] - 2):
        for j in range(image.shape[1] - 2):
            region = image[i:i+3, j:j+3]
            avg = np.mean(region)
            
            if avg > max_avg:
                max_avg = avg
                max_pos = (i, j)
            
            if avg < min_avg:
                min_avg = avg
                min_pos = (i, j)
    
    print("🔍 PHÂN TÍCH VÙNG:")
    print(f"Vùng sáng nhất (3x3) tại vị trí {max_pos}: trung bình {max_avg:.1f}")
    print(f"Vùng tối nhất (3x3) tại vị trí {min_pos}: trung bình {min_avg:.1f}")
    print()
    
    # Biến đổi ảnh
    image_flip_h = np.flip(image, axis=1)  # Flip ngang
    image_flip_v = np.flip(image, axis=0)  # Flip dọc
    
    print("🔄 BIẾN ĐỔI ẢNH:")
    print("Ảnh flip ngang (horizontal flip):")
    print(image_flip_h)
    print()
    
    print("Ảnh flip dọc (vertical flip):")
    print(image_flip_v)
    print()
    
    # Thống kê bổ sung
    print("📊 THỐNG KÊ BỔ SUNG:")
    print(f"- Độ sáng trung bình: {np.mean(image):.1f}")
    print(f"- Pixel sáng nhất: {np.max(image)}")
    print(f"- Pixel tối nhất: {np.min(image)}")
    print(f"- Độ tương phản: {np.std(image):.1f}")

if __name__ == "__main__":
    main()
