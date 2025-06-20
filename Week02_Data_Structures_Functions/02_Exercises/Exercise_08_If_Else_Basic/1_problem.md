# Week 2 - Exercise 8: Basic If-Else

**Câu lệnh điều kiện If-Else cơ bản**

## 🎯 Mục tiêu

- Sử dụng if, elif, else statements
- Kết hợp điều kiện với logical operators
- Tạo hệ thống phân loại đơn giản
- Xử lý input validation

---

## 📋 Đề bài

Tạo hệ thống phân loại nhiệt độ và thời tiết:

### Yêu cầu:

1. **Phân loại nhiệt độ** (lạnh, mát, ấm, nóng)
2. **Đánh giá chỉ số UV** (thấp, trung bình, cao, rất cao)
3. **Khuyến nghị hoạt động** dựa trên nhiệt độ và UV
4. **Xử lý input** không hợp lệ

---

## 💻 Yêu cầu cụ thể

```python
# Test với các giá trị cụ thể
temperature = 28  # Celsius
uv_index = 7

# 1. Phân loại nhiệt độ
# < 15: Lạnh
# 15-24: Mát
# 25-30: Ấm
# > 30: Nóng

# 2. Đánh giá UV index
# 0-2: Thấp
# 3-5: Trung bình
# 6-7: Cao
# 8+: Rất cao

# 3. Khuyến nghị hoạt động
# Dựa trên cả nhiệt độ và UV
```

---

## 🎯 Expected Output

```
=== Weather Analysis System ===

Temperature: 28°C
UV Index: 7

Temperature Analysis:
28°C is classified as: Warm

UV Analysis:
UV Index 7 is classified as: High

Activity Recommendations:
- Temperature is warm: Great for outdoor activities
- UV is high: Use sunscreen and hat
- Overall recommendation: Good for outdoor activities with sun protection

Testing edge cases:
Temperature -5°C: Cold
Temperature 15°C: Cool
Temperature 30°C: Warm
Temperature 35°C: Hot

UV Index 0: Low
UV Index 3: Moderate
UV Index 8: Very High
```

---

## 💡 Hints

- Sử dụng `if temperature < 15:` cho điều kiện
- `elif` cho nhiều điều kiện
- `else` cho trường hợp còn lại
- Kết hợp điều kiện: `if temp > 25 and uv < 3:`
