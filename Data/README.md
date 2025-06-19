# Data Directory

## 📁 Cấu Trúc Dữ Liệu

### Sample_Datasets/

Chứa các bộ dữ liệu mẫu cho thực hành:

- `titanic.csv` - Classic dataset cho classification
- `boston_housing.csv` - Housing prices cho regression
- `iris.csv` - Flower classification dataset
- `sales_data.csv` - Business sales data
- `weather_station.csv` - Meteorological data
- `stock_prices.csv` - Financial time series

### Satellite_Images/

Dữ liệu ảnh vệ tinh:

- `landsat_sample.tif` - Landsat 8 sample image
- `sentinel2_sample.tif` - Sentinel-2 sample image
- `modis_ndvi.tif` - MODIS NDVI time series
- `dem_sample.tif` - Digital elevation model

### Weather_Data/

Dữ liệu khí tượng:

- `temperature_timeseries.csv` - Long-term temperature data
- `precipitation_data.csv` - Rainfall measurements
- `climate_stations.csv` - Weather station locations
- `extreme_events.csv` - Extreme weather events

### GIS_Data/

Dữ liệu không gian vector:

- `vietnam_provinces.shp` - Vietnam administrative boundaries
- `roads_network.shp` - Road network data
- `land_use.shp` - Land use classifications
- `water_bodies.shp` - Rivers and lakes

## 🔗 Data Sources

### Public Datasets:

- **Kaggle**: https://www.kaggle.com/datasets
- **UCI ML Repository**: https://archive.ics.uci.edu/ml/
- **NASA Earthdata**: https://earthdata.nasa.gov/
- **USGS Earth Explorer**: https://earthexplorer.usgs.gov/
- **Copernicus Open Access Hub**: https://scihub.copernicus.eu/

### Vietnam-specific Data:

- **General Statistics Office**: https://www.gso.gov.vn/
- **Vietnam National University**: Data portal
- **MONRE**: Ministry of Natural Resources and Environment

## 📋 Data Usage Guidelines

1. **Educational Purpose Only**: All datasets are for learning
2. **Attribution**: Credit original data sources
3. **Privacy**: No personal/sensitive information
4. **Size Limits**: Keep files under 100MB for GitHub
5. **Format Standards**: Prefer CSV, GeoTIFF, Shapefile formats

## 🛠️ Data Preparation Tools

```python
# Example data loading
import pandas as pd
import geopandas as gpd
import rasterio

# Load tabular data
df = pd.read_csv('Data/Sample_Datasets/sales_data.csv')

# Load spatial vector data
gdf = gpd.read_file('Data/GIS_Data/vietnam_provinces.shp')

# Load raster data
with rasterio.open('Data/Satellite_Images/landsat_sample.tif') as src:
    image = src.read()
```
