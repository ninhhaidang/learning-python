# Project 2: Satellite Image Processing System 🛰️

## Mục tiêu Project

Xây dựng hệ thống xử lý ảnh vệ tinh đơn giản sử dụng NumPy, mô phỏng xử lý dữ liệu viễn thám cho phân tích land cover và change detection.

## Yêu cầu Kỹ thuật

### Phase 1: Image Data Generation (25 điểm)

**File: `image_generator.py`**

1. **Synthetic Satellite Scene Creation**

   - Tạo 2 scenes (2022 và 2024) với size 100×100 pixels
   - 4 spectral bands: Blue, Green, Red, NIR (Near-Infrared)
   - Digital Number values: 0-255 (8-bit)
   - Simulate realistic land cover patterns

2. **Land Cover Classes**

   - Water bodies (DN: 20-50 across bands)
   - Vegetation (high NIR, moderate Red, low Blue)
   - Urban areas (moderate values across all bands)
   - Bare soil (low NIR, moderate Red)
   - Clouds (high values across all bands)

3. **Temporal Changes**
   - Urban expansion (convert vegetation/bare soil to urban)
   - Deforestation (convert vegetation to bare soil)
   - Water level changes
   - New cloud patterns

### Phase 2: Image Preprocessing (25 điểm)

**File: `preprocessor.py`**

1. **Radiometric Corrections**

   - Convert DN to reflectance values (0-1 scale)
   - Apply gain and offset corrections
   - Atmospheric correction simulation

2. **Geometric Corrections**

   - Image registration (align 2022 and 2024 scenes)
   - Resampling and interpolation
   - Coordinate system simulation

3. **Quality Assessment**
   - Check for saturated pixels
   - Cloud detection and masking
   - Data completeness analysis

### Phase 3: Spectral Analysis (30 điểm)

**File: `spectral_analyzer.py`**

1. **Vegetation Indices Calculation**

   - NDVI: (NIR - Red) / (NIR + Red)
   - SAVI: ((NIR - Red) / (NIR + Red + L)) × (1 + L), where L=0.5
   - EVI: 2.5 × ((NIR - Red) / (NIR + 6×Red - 7.5×Blue + 1))

2. **Water Indices**

   - NDWI: (Green - NIR) / (Green + NIR)
   - MNDWI: (Green - SWIR) / (Green + SWIR) # simulate SWIR

3. **Land Cover Classification**
   - Threshold-based classification using indices
   - Multi-band classification
   - Accuracy assessment using confusion matrix

### Phase 4: Change Detection (20 điểm)

**File: `change_detector.py`**

1. **Image Differencing**

   - Pixel-wise subtraction between 2022 and 2024
   - Threshold-based change detection
   - Change magnitude calculation

2. **Index-based Change Detection**

   - NDVI change analysis
   - Vegetation gain/loss detection
   - Urban expansion mapping

3. **Change Statistics**
   - Area calculations for each change type
   - Change rate calculations
   - Hotspot detection

## Deliverables

### Required Files

```
Project2_Satellite_Processing/
├── src/
│   ├── image_generator.py     # Synthetic image creation
│   ├── preprocessor.py        # Image preprocessing
│   ├── spectral_analyzer.py   # Spectral indices & classification
│   ├── change_detector.py     # Change detection algorithms
│   └── main.py               # Main processing pipeline
├── data/
│   ├── scene_2022.npy        # 2022 satellite image (100×100×4)
│   ├── scene_2024.npy        # 2024 satellite image (100×100×4)
│   ├── metadata.json         # Image metadata and parameters
│   └── ground_truth.npy      # Reference classification (optional)
├── outputs/
│   ├── ndvi_2022.npy         # NDVI map 2022
│   ├── ndvi_2024.npy         # NDVI map 2024
│   ├── classification_2022.npy  # Land cover map 2022
│   ├── classification_2024.npy  # Land cover map 2024
│   ├── change_map.npy        # Change detection results
│   ├── statistics.csv        # Area statistics by class
│   └── change_report.txt     # Change analysis report
├── README.md                 # Project documentation
└── demo.py                   # Interactive demonstration
```

### Sample Code Structure

**main.py:**

```python
import numpy as np
from src.image_generator import SatelliteImageGenerator
from src.preprocessor import ImagePreprocessor
from src.spectral_analyzer import SpectralAnalyzer
from src.change_detector import ChangeDetector

def main():
    print("=== SATELLITE IMAGE PROCESSING SYSTEM ===")

    # 1. Generate synthetic satellite data
    generator = SatelliteImageGenerator()
    scene_2022, scene_2024 = generator.create_temporal_scenes()

    # 2. Preprocess images
    preprocessor = ImagePreprocessor()
    scene_2022_processed = preprocessor.process_image(scene_2022)
    scene_2024_processed = preprocessor.process_image(scene_2024)

    # 3. Spectral analysis
    analyzer = SpectralAnalyzer()
    classification_2022 = analyzer.classify_image(scene_2022_processed)
    classification_2024 = analyzer.classify_image(scene_2024_processed)

    # 4. Change detection
    change_detector = ChangeDetector()
    change_map = change_detector.detect_changes(
        scene_2022_processed, scene_2024_processed
    )

    # 5. Generate reports
    change_detector.generate_change_report(
        classification_2022, classification_2024, change_map
    )

    print("Processing complete! Check outputs/ folder for results.")

if __name__ == "__main__":
    main()
```

## Grading Rubric

### Technical Implementation (60%)

- **Image Generation (15%)**: Realistic synthetic data, proper array structures
- **Preprocessing (15%)**: Correct radiometric/geometric corrections
- **Spectral Analysis (20%)**: Accurate index calculations, classification
- **Change Detection (10%)**: Proper change algorithms implementation

### Functionality (25%)

- **Core Features (15%)**: All required functions working correctly
- **Advanced Features (10%)**: Creative extensions, optimization

### Code Quality (15%)

- **Documentation (8%)**: Clear README, well-commented code
- **Structure (7%)**: Modular design, proper error handling

## Technical Specifications

### Image Data Format

```python
# Satellite scene array structure
scene_shape = (100, 100, 4)  # Height × Width × Bands
band_names = ['Blue', 'Green', 'Red', 'NIR']
data_type = np.uint8  # 8-bit unsigned integer (0-255)

# Metadata structure
metadata = {
    'acquisition_date': '2022-03-15',
    'sensor': 'Simulated_MSI',
    'spatial_resolution': 10,  # meters
    'radiometric_resolution': 8,  # bits
    'bands': band_names,
    'coordinate_system': 'UTM_48N',
    'scene_center': [16.0471, 108.2068]  # Da Nang coordinates
}
```

### Land Cover Classes

```python
# Classification scheme
LAND_COVER_CLASSES = {
    0: 'No Data',
    1: 'Water',
    2: 'Vegetation',
    3: 'Urban',
    4: 'Bare Soil',
    5: 'Clouds'
}

# Typical spectral signatures (DN values)
SPECTRAL_SIGNATURES = {
    'Water': {'Blue': 45, 'Green': 40, 'Red': 25, 'NIR': 15},
    'Vegetation': {'Blue': 30, 'Green': 50, 'Red': 40, 'NIR': 120},
    'Urban': {'Blue': 80, 'Green': 85, 'Red': 90, 'NIR': 95},
    'Bare_Soil': {'Blue': 70, 'Green': 80, 'Red': 100, 'NIR': 85},
    'Clouds': {'Blue': 200, 'Green': 210, 'Red': 220, 'NIR': 230}
}
```

### Spectral Indices Formulas

```python
def calculate_ndvi(red, nir):
    """Normalized Difference Vegetation Index"""
    return (nir - red) / (nir + red + 1e-8)  # Add small value to avoid division by zero

def calculate_ndwi(green, nir):
    """Normalized Difference Water Index"""
    return (green - nir) / (green + nir + 1e-8)

def calculate_savi(red, nir, L=0.5):
    """Soil Adjusted Vegetation Index"""
    return ((nir - red) / (nir + red + L)) * (1 + L)
```

## Sample Output

```
=== SATELLITE IMAGE PROCESSING RESULTS ===
Study Area: 100km × 100km (10,000 pixels)
Time Period: 2022 → 2024 (2 years)

IMAGE STATISTICS:
2022 Scene:
- Water bodies: 1,847 pixels (18.5%)
- Vegetation: 4,521 pixels (45.2%)
- Urban areas: 2,156 pixels (21.6%)
- Bare soil: 1,476 pixels (14.8%)

2024 Scene:
- Water bodies: 1,823 pixels (18.2%)
- Vegetation: 4,234 pixels (42.3%)
- Urban areas: 2,543 pixels (25.4%)
- Bare soil: 1,400 pixels (14.0%)

CHANGE DETECTION RESULTS:
Urban Expansion:
- New urban areas: 387 pixels (3.9%)
- Vegetation converted to urban: 287 pixels
- Bare soil converted to urban: 100 pixels

Vegetation Changes:
- Net vegetation loss: 287 pixels (2.9%)
- Deforestation detected: 15 clusters
- Average deforestation patch size: 19.1 pixels

Water Body Changes:
- Water level decrease: 24 pixels (1.3%)
- New water bodies: 0 pixels
- Dried water areas: 24 pixels

SPECTRAL INDICES SUMMARY:
NDVI Statistics:
- 2022 mean NDVI: 0.34 (±0.28)
- 2024 mean NDVI: 0.31 (±0.27)
- NDVI change: -0.03 (indicating vegetation decline)

Processing Performance:
- Image generation: 0.15 seconds
- Preprocessing: 0.23 seconds
- Classification: 0.41 seconds
- Change detection: 0.18 seconds
- Total processing time: 0.97 seconds
```

## Resources

### Remote Sensing Background

- [Introduction to Remote Sensing](https://www.usgs.gov/landsat-missions/what-remote-sensing)
- [Spectral Indices Database](https://www.indexdatabase.de/)
- [Land Cover Classification](https://gisgeography.com/image-classification-techniques-remote-sensing/)

### NumPy for Image Processing

- [NumPy Array Manipulation](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)
- [Multi-dimensional Arrays](https://numpy.org/doc/stable/user/basics.indexing.html)
- [Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)

### Vietnam Land Cover

- [Vietnam Forest Cover](https://www.fao.org/forestry/country/57506/en/vnm/)
- [Mekong Delta Land Use](https://www.mdpi.com/2072-4292/10/9/1384)

## Support

- **Office Hours**: Tuesdays/Thursdays 2-4 PM
- **Satellite Data**: Sample datasets provided in course materials
- **Technical Help**: Forum available for NumPy-specific questions

**Happy coding! 🛰️📊**
