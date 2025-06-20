# Exercise 07: Inventory Management System

## 🎯 Mục tiêu

- Sử dụng NumPy sorting và searching functions
- Thực hành Boolean indexing cho inventory filtering
- Áp dụng aggregation functions cho báo cáo thống kê
- Xây dựng system quản lý kho hàng thông minh

## 📋 Đề bài: Quản lý Kho hàng Thông minh

Xây dựng hệ thống quản lý kho hàng cho cửa hàng với 50 sản phẩm.

### Yêu cầu:

1. **Tạo inventory database** với thông tin sản phẩm
2. **Sorting operations** theo giá, số lượng, tên
3. **Search functions** tìm sản phẩm theo criteria
4. **Low stock alert** các sản phẩm sắp hết
5. **Revenue analysis** tính toán doanh thu và lợi nhuận
6. **Reorder suggestions** đề xuất nhập hàng

### Input mẫu:

```python
import numpy as np
np.random.seed(42)
n_products = 50

# Tạo database sản phẩm
product_ids = np.arange(1001, 1001 + n_products)
quantities = np.random.randint(0, 100, n_products)
prices = np.random.uniform(10, 500, n_products)
costs = prices * np.random.uniform(0.5, 0.8, n_products)
```

### Expected Output:

```
=== INVENTORY MANAGEMENT SYSTEM ===

📦 INVENTORY OVERVIEW:
Total products: 50
Total stock units: 2,450
Total inventory value: $456,789.50
Average price per item: $186.50

🔍 SORTING & SEARCHING:

Top 5 Most Expensive Products:
ID: 1025 | Price: $487.90 | Stock: 45 | Value: $21,955.50
ID: 1012 | Price: $456.20 | Stock: 32 | Value: $14,598.40
ID: 1033 | Price: $445.80 | Stock: 67 | Value: $29,868.60
ID: 1008 | Price: $423.10 | Stock: 12 | Value: $5,077.20
ID: 1041 | Price: $398.50 | Stock: 78 | Value: $31,083.00

⚠️  LOW STOCK ALERT (< 10 units):
ID: 1015 | Stock: 3 | Price: $234.50 | Status: CRITICAL
ID: 1028 | Stock: 7 | Price: $156.80 | Status: LOW
ID: 1042 | Stock: 8 | Price: $298.70 | Status: LOW

📊 REVENUE ANALYSIS:
Products > $300: 15 items (30.0%)
High-value stock (>$10k): 12 items
Potential revenue: $912,345.70
Estimated profit margin: 35.2%

📋 REORDER SUGGESTIONS:
Priority 1: Product 1015 (Stock: 3, Weekly sales: 12)
Priority 2: Product 1028 (Stock: 7, Weekly sales: 8)
Priority 3: Product 1042 (Stock: 8, Weekly sales: 6)

Suggested reorder quantities:
ID 1015: Order 50 units (Cost: $11,725.00)
ID 1028: Order 30 units (Cost: $4,704.00)
ID 1042: Order 25 units (Cost: $7,467.50)
```

## 💡 Hướng dẫn

### Các hàm NumPy cần sử dụng:

- `np.argsort()` - sorting with indices
- `np.where()` - conditional selection
- `np.searchsorted()` - binary search
- `np.sum()`, `np.mean()` - aggregations
- Boolean indexing cho filtering

### Gợi ý thực hiện:

1. Tạo structured arrays hoặc multiple arrays cho database
2. Sử dụng `argsort()` để sort theo multiple criteria
3. Boolean indexing để tìm low stock items
4. Aggregation functions cho statistical analysis
5. Vectorized operations cho revenue calculations

## ✅ Tiêu chí đánh giá

- [ ] Tạo đúng inventory database với các fields cần thiết
- [ ] Sử dụng sorting functions hiệu quả
- [ ] Áp dụng Boolean indexing để filter data
- [ ] Tính toán thống kê chính xác (revenue, profit)
- [ ] Implement reorder suggestion logic
- [ ] Output format professional, dễ đọc
