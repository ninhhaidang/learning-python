# Giới Thiệu Python

## Python là gì?

Python là một ngôn ngữ lập trình bậc cao, được phát triển bởi Guido van Rossum và ra mắt lần đầu vào năm 1991. Python nổi tiếng với cú pháp đơn giản, dễ đọc và dễ học.

## Tại sao chọn Python cho Data Science và Viễn Thám?

### 1. **Cú pháp đơn giản**

```python
# Python
print("Hello, World!")

# So sánh với Java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### 2. **Thư viện phong phú**

- **NumPy**: Tính toán khoa học
- **Pandas**: Xử lý dữ liệu
- **Matplotlib/Seaborn**: Visualization
- **Scikit-learn**: Machine Learning
- **GDAL/Rasterio**: Viễn thám
- **GeoPandas**: Dữ liệu không gian

### 3. **Cộng đồng lớn**

- Tài liệu phong phú
- Stack Overflow support
- GitHub repositories
- Khóa học online

### 4. **Ứng dụng rộng rãi**

- Web Development (Django, Flask)
- Data Science & AI
- Automation & Scripting
- Scientific Computing
- Remote Sensing & GIS

## Lịch Sử và Phiên Bản

### Timeline quan trọng:

- **1991**: Python 0.9.0 - Phiên bản đầu tiên
- **2000**: Python 2.0 - Garbage collection, Unicode
- **2008**: Python 3.0 - Breaking changes, không tương thích ngược
- **2020**: Python 2.7 end of life
- **Hiện tại**: Python 3.8+ được khuyến nghị

### Python 2 vs Python 3:

```python
# Python 2
print "Hello World"
print 3/2  # Output: 1

# Python 3
print("Hello World")
print(3/2)  # Output: 1.5
```

## Triết Lý Python - The Zen of Python

```python
import this
```

Những nguyên tắc quan trọng:

- **Beautiful is better than ugly**
- **Explicit is better than implicit**
- **Simple is better than complex**
- **Readability counts**
- **There should be one obvious way to do it**

## Ứng Dụng Trong Viễn Thám

### 1. **Xử lý ảnh vệ tinh**

```python
import rasterio
import numpy as np

# Đọc ảnh vệ tinh
with rasterio.open('satellite_image.tif') as src:
    image = src.read()

# Tính chỉ số thực vật NDVI
red = image[0]
nir = image[1]
ndvi = (nir - red) / (nir + red)
```

### 2. **Phân tích dữ liệu khí tượng**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
weather_data = pd.read_csv('weather_station.csv')

# Vẽ biểu đồ nhiệt độ theo thời gian
plt.plot(weather_data['date'], weather_data['temperature'])
plt.title('Temperature Over Time')
plt.show()
```

### 3. **Machine Learning cho phân loại đất**

```python
from sklearn.ensemble import RandomForestClassifier

# Huấn luyện mô hình phân loại
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Dự đoán loại đất
predictions = rf.predict(X_test)
```

## Tài Nguyên Học Tập

### Documentation chính thức:

- https://docs.python.org/3/
- https://docs.python.org/3/tutorial/

### Sách hay:

- "Automate the Boring Stuff with Python"
- "Python Crash Course"
- "Learning Python" by Mark Lutz

### Online Platforms:

- Codecademy Python Course
- Python.org Beginner's Guide
- Real Python tutorials

## Bài Tập Thực Hành

1. Cài đặt Python và IDE
2. Chạy chương trình "Hello, World!" đầu tiên
3. Tìm hiểu về Python Interactive Shell
4. Khám phá Python documentation

## Câu Hỏi Ôn Tập

1. Python được phát triển bởi ai và khi nào?
2. Sự khác biệt chính giữa Python 2 và Python 3 là gì?
3. Tại sao Python phù hợp cho Data Science?
4. Kể tên 5 thư viện Python quan trọng cho viễn thám.
5. "The Zen of Python" là gì và tại sao nó quan trọng?
