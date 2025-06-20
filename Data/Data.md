# 📊 Dữ Liệu Thực Hành

## 🗂️ Tổng quan Dataset

Thư mục này chứa các dataset được sử dụng trong khóa học, được tổ chức theo từng tuần và loại dữ liệu.

## 📁 Cấu trúc thư mục Data

```
Data/
├── sample_data/           # Dữ liệu mẫu nhỏ cho thực hành
├── csv_files/            # File CSV cho pandas practice
├── geospatial/           # Dữ liệu không gian
│   ├── vector/           # Shapefile, GeoJSON
│   └── raster/           # GeoTIFF, satellite images
├── satellite/            # Dữ liệu vệ tinh
│   ├── landsat/          # Landsat imagery
│   ├── sentinel/         # Sentinel imagery
│   └── modis/            # MODIS data
└── machine_learning/     # Dataset cho ML projects
```

## 🛰️ Dữ liệu Viễn thám

### Landsat Data

- **Nguồn**: USGS Earth Explorer
- **Phân giải**: 30m (multispectral), 15m (panchromatic)
- **Ứng dụng**: Phân tích thảm thực vật, giám sát đô thị, tính toán chỉ số

### Sentinel-2 Data

- **Nguồn**: ESA Copernicus Hub
- **Phân giải**: 10m, 20m, 60m
- **Ứng dụng**: Nông nghiệp, rừng, thay đổi sử dụng đất

### MODIS Data

- **Nguồn**: NASA Earth Data
- **Phân giải**: 250m-1km
- **Ứng dụng**: Giám sát khí hậu, cháy rừng, nhiệt độ bề mặt

## 🗺️ Dữ liệu Vector

### Administrative Boundaries

- **Định dạng**: Shapefile, GeoJSON
- **Nội dung**: Ranh giới hành chính Việt Nam
- **Nguồn**: OpenStreetMap, GADM

### Road Networks

- **Định dạng**: Shapefile
- **Nội dung**: Mạng lưới đường giao thông
- **Ứng dụng**: Network analysis, accessibility

### Points of Interest (POI)

- **Định dạng**: CSV với coordinates
- **Nội dung**: Trường học, bệnh viện, điểm du lịch
- **Ứng dụng**: Spatial analysis, clustering

## 📈 Dataset Machine Learning

### Land Cover Classification

- **Features**: Spectral bands, indices (NDVI, NDWI)
- **Target**: Land cover classes
- **Size**: 10,000+ samples

### Urban Growth Prediction

- **Features**: Population, infrastructure, economic indicators
- **Target**: Urban expansion areas
- **Time series**: 2000-2020

### Crop Yield Estimation

- **Features**: Weather data, soil properties, satellite indices
- **Target**: Crop yield (tons/hectare)
- **Coverage**: Mekong Delta region

## 🔧 Download Scripts

### Script tự động download

```python
# download_data.py - Script để tải về tất cả dataset cần thiết
# Sẽ được tạo trong Week09 khi học về web scraping
```

## 📋 Checklist Download

- [ ] Sample CSV files (Week 5-6)
- [ ] Vector data (Week 11)
- [ ] Raster data (Week 10)
- [ ] Satellite imagery (Week 12)
- [ ] ML datasets (Week 12)

## 📝 Metadata

Mỗi dataset đều có file metadata.txt hoặc README.md riêng mô tả:

- Nguồn dữ liệu
- Ngày thu thập
- Hệ tọa độ
- Cách sử dụng
- Giấy phép (license)

## ⚠️ Lưu ý quan trọng

1. **Dung lượng**: Tổng dung lượng ~2GB
2. **License**: Kiểm tra license trước khi sử dụng
3. **Cập nhật**: Dataset được cập nhật theo nhu cầu khóa học
4. **Backup**: Nên backup dữ liệu ra nơi khác

## 🌐 Nguồn dữ liệu miễn phí

- [USGS Earth Explorer](https://earthexplorer.usgs.gov/)
- [ESA Copernicus Hub](https://scihub.copernicus.eu/)
- [NASA Earth Data](https://earthdata.nasa.gov/)
- [OpenStreetMap](https://www.openstreetmap.org/)
- [GADM](https://gadm.org/) - Administrative boundaries
