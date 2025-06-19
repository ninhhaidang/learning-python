# Exercise 01: Pandas Series Fundamentals

## Mục tiêu

- Nắm vững cách tạo và thao tác với Pandas Series
- Hiểu về indexing, slicing và selection trong Series
- Thực hiện statistical operations và data cleaning
- Áp dụng Series trong phân tích dữ liệu thực tế

## Bài tập

### Bài 1: Phân tích dữ liệu nhiệt độ Việt Nam

Bạn là một nhà khí tượng học và cần phân tích dữ liệu nhiệt độ trung bình của các thành phố lớn ở Việt Nam trong tháng 3/2024.

**Dữ liệu nhiệt độ (°C):**

- Hà Nội: [22, 25, 28, 26, 24, 27, 29, 31, 28, 26, 23, 25, 27, 30, 32, 29, 27, 25, 26, 28, 30, 33, 31, 29, 27, 25, 26, 28, 30, 29, 27]
- TP.HCM: [28, 31, 33, 32, 30, 29, 31, 34, 35, 33, 31, 29, 30, 32, 34, 36, 33, 31, 30, 32, 34, 35, 37, 34, 32, 30, 31, 33, 35, 34, 32]
- Đà Nẵng: [24, 27, 29, 28, 26, 25, 28, 30, 32, 29, 27, 25, 26, 28, 30, 32, 29, 27, 26, 28, 30, 31, 33, 30, 28, 26, 27, 29, 31, 30, 28]

**Yêu cầu:**

1. Tạo 3 Series cho nhiệt độ của từng thành phố với index là ngày (1-31)
2. Tính nhiệt độ trung bình, cao nhất, thấp nhất của từng thành phố
3. Tìm ngày có nhiệt độ cao nhất và thấp nhất ở mỗi thành phố
4. Đếm số ngày có nhiệt độ > 30°C ở mỗi thành phố
5. Tạo Series chứa chênh lệch nhiệt độ giữa TP.HCM và Hà Nội
6. Tìm 5 ngày nóng nhất và 5 ngày lạnh nhất của cả tháng (tất cả thành phố)

**Output mẫu:**

```
=== PHÂN TÍCH NHIỆT ĐỘ VIỆT NAM - THÁNG 3/2024 ===

HÀ NỘI:
- Nhiệt độ trung bình: 27.0°C
- Nhiệt độ cao nhất: 33°C (ngày 22)
- Nhiệt độ thấp nhất: 22°C (ngày 1)
- Số ngày > 30°C: 8 ngày

TP.HCM:
- Nhiệt độ trung bình: 32.3°C
- Nhiệt độ cao nhất: 37°C (ngày 23)
- Nhiệt độ thấp nhất: 28°C (ngày 1)
- Số ngày > 30°C: 25 ngày

ĐÀ NẴNG:
- Nhiệt độ trung bình: 28.4°C
- Nhiệt độ cao nhất: 33°C (ngày 23)
- Nhiệt độ thấp nhất: 24°C (ngày 1)
- Số ngày > 30°C: 10 ngày

CHÊNH LỆCH TP.HCM - HÀ NỘI:
- Chênh lệch trung bình: 5.3°C
- Chênh lệch lớn nhất: 8°C (ngày 16)
- Chênh lệch nhỏ nhất: 3°C (ngày 11)
```

### Bài 2: Phân tích điểm thi đại học

Bạn là giáo viên phụ trách khối 12 và cần phân tích kết quả thi thử đại học môn Toán của lớp.

**Dữ liệu điểm số (thang 10):**
[8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 9.3, 8.1, 6.9, 8.7, 7.8, 9.0, 8.2, 7.1, 8.6, 9.2, 7.6, 8.4, 7.9, 8.8, 6.7, 9.4, 8.0, 7.3, 8.3, 7.7, 9.1, 8.5, 7.4, 8.9]

**Yêu cầu:**

1. Tạo Series với index là mã học sinh (HS001, HS002, ...)
2. Tính điểm trung bình, trung vị, độ lệch chuẩn
3. Phân loại học sinh theo thang điểm:
   - Xuất sắc: ≥ 9.0
   - Giỏi: 8.0 - 8.9
   - Khá: 7.0 - 7.9
   - Trung bình: 6.0 - 6.9
   - Yếu: < 6.0
4. Tìm top 5 và bottom 5 học sinh
5. Tính phần trăm học sinh đạt từ Khá trở lên
6. Chuẩn hóa điểm (Z-score) và tìm học sinh có điểm chuẩn hóa cao nhất/thấp nhất

### Bài 3: Phân tích giá cổ phiếu VN-Index

Bạn là một analyst và cần phân tích dữ liệu giá đóng cửa của VN-Index trong 20 phiên gần nhất.

**Dữ liệu giá đóng cửa (điểm):**
[1245.67, 1252.34, 1248.91, 1255.78, 1262.45, 1258.12, 1263.89, 1271.56, 1268.23, 1274.90, 1281.67, 1277.34, 1283.01, 1289.78, 1285.45, 1291.12, 1297.89, 1293.56, 1299.23, 1305.90]

**Yêu cầu:**

1. Tạo Series với index là datetime (20 ngày gần nhất)
2. Tính % thay đổi hàng ngày
3. Tính volatility (độ biến động) = std của % thay đổi
4. Tìm phiên tăng/giảm mạnh nhất
5. Tính moving average 5 ngày và 10 ngày
6. Đếm số phiên tăng và số phiên giảm
7. Tìm streak tăng/giảm liên tiếp dài nhất

**Output mẫu:**

```
=== PHÂN TÍCH VN-INDEX - 20 PHIÊN GẦN NHẤT ===

Giá đóng cửa:
- Cao nhất: 1,305.90 (2024-03-20)
- Thấp nhất: 1,245.67 (2024-03-01)
- Tăng trưởng tổng: +4.84%

Biến động hàng ngày:
- Thay đổi trung bình: +0.24%
- Volatility: 0.67%
- Tăng mạnh nhất: +1.23% (2024-03-08)
- Giảm mạnh nhất: -0.89% (2024-03-03)

Xu hướng:
- Số phiên tăng: 13
- Số phiên giảm: 6
- Streak tăng dài nhất: 4 phiên
- MA5 cuối: 1,295.54
- MA10 cuối: 1,281.23
```

## Hướng dẫn giải

### Tips chung:

1. **Tạo Series:** Sử dụng `pd.Series(data, index=index_list, name='series_name')`
2. **Statistical functions:** `.mean()`, `.median()`, `.std()`, `.min()`, `.max()`, `.count()`
3. **Indexing:** `.loc[]` cho label-based, `.iloc[]` cho position-based
4. **Boolean indexing:** `series[series > threshold]`
5. **Sorting:** `.sort_values()`, `.sort_index()`
6. **String operations:** `.apply(lambda x: ...)` cho custom functions

### Bài 1 - Nhiệt độ:

- Dùng `pd.date_range()` cho datetime index
- `.idxmax()` và `.idxmin()` để tìm ngày có giá trị cao/thấp nhất
- Boolean indexing để đếm ngày > 30°C
- `.diff()` để tính chênh lệch

### Bài 2 - Điểm thi:

- `.apply()` với function phân loại điểm
- `.value_counts()` để đếm từng loại
- `(series - series.mean()) / series.std()` cho Z-score
- `.nlargest()` và `.nsmallest()` cho top/bottom

### Bài 3 - Cổ phiếu:

- `.pct_change()` cho % thay đổi
- `.rolling(window).mean()` cho moving average
- `.cumsum()` cho cumulative calculations
- Custom function để tìm streak

## Tiêu chí đánh giá

- [ ] **Code chạy đúng (40%)**: Tất cả yêu cầu được implement và chạy không lỗi
- [ ] **Kết quả chính xác (30%)**: Output match với expected results
- [ ] **Code quality (20%)**: Clean code, proper variable naming, comments
- [ ] **Pandas best practices (10%)**: Sử dụng đúng methods, efficient operations

## Bonus Points

- Tạo visualization đơn giản với matplotlib
- Handle edge cases (missing data, invalid values)
- Add statistical insights và business interpretation
- Optimize performance cho large datasets
- [ ] [TODO: Tiêu chí 2]
