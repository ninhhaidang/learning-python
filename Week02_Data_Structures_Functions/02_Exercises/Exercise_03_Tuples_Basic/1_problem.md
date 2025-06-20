# Week 2 - Exercise 3: Basic Tuples

**Tạo và sử dụng Tuples cơ bản**

## 🎯 Mục tiêu

- Hiểu sự khác biệt giữa tuple và list
- Tạo và truy cập tuples
- Sử dụng tuple unpacking
- Ứng dụng tuples cho tọa độ địa lý

---

## 📋 Đề bài

Quản lý tọa độ các thành phố Việt Nam:

### Yêu cầu:

1. **Tạo tuples** chứa tọa độ (latitude, longitude) của các thành phố
2. **Truy cập** từng thành phần của tuple
3. **Sử dụng tuple unpacking** để tách tọa độ
4. **Tính khoảng cách** đơn giản giữa 2 điểm

---

## 💻 Yêu cầu cụ thể

```python
# 1. Tạo tuples cho tọa độ các thành phố
hanoi_coords = (21.0285, 105.8542)
hcm_coords = (10.8231, 106.6297)
danang_coords = (16.0544, 108.2022)

# 2. In tọa độ với format đẹp
# 3. Sử dụng tuple unpacking
# 4. Tính khoảng cách Manhattan (|lat1-lat2| + |lon1-lon2|)
```

---

## 🎯 Expected Output

```
City Coordinates:
Hanoi: Latitude 21.0285, Longitude 105.8542
Ho Chi Minh: Latitude 10.8231, Longitude 106.6297
Da Nang: Latitude 16.0544, Longitude 108.2022

Tuple unpacking example:
Hanoi latitude: 21.0285
Hanoi longitude: 105.8542

Distance calculations (Manhattan distance):
Hanoi to Ho Chi Minh: 11.03
Hanoi to Da Nang: 7.19
Ho Chi Minh to Da Nang: 7.59
```

---

## 💡 Hints

- Tuple được tạo với `(item1, item2)`
- Tuple unpacking: `lat, lon = coordinates`
- Khoảng cách Manhattan: `abs(lat1-lat2) + abs(lon1-lon2)`
- Tuples là immutable (không thể thay đổi)
