# Project 2: Satellite Image Processing - Starter Code

"""
Satellite Image Processing System
Week 3 - NumPy Fundamentals Project

Hướng dẫn:
1. Đọc kỹ yêu cầu trong Project2_Satellite_Processing.md
2. Hoàn thiện các hàm TODO trong file này
3. Test từng module với dữ liệu nhỏ trước
4. Chạy main() để xem kết quả pipeline hoàn chỉnh

Structure:
- SatelliteImageGenerator: Tạo ảnh vệ tinh synthetic
- ImagePreprocessor: Tiền xử lý ảnh
- SpectralAnalyzer: Phân tích phổ và phân loại
- ChangeDetector: Phát hiện thay đổi
"""

import numpy as np
import json
from datetime import datetime

class SatelliteImageGenerator:
    """Generate synthetic satellite imagery"""
    
    def __init__(self, height=100, width=100, num_bands=4):
        self.height = height
        self.width = width
        self.num_bands = num_bands
        self.band_names = ['Blue', 'Green', 'Red', 'NIR']
        
        # Spectral signatures for different land cover types
        self.signatures = {
            'Water': [45, 40, 25, 15],
            'Vegetation': [30, 50, 40, 120],
            'Urban': [80, 85, 90, 95],
            'Bare_Soil': [70, 80, 100, 85],
            'Clouds': [200, 210, 220, 230]
        }
        
    def create_temporal_scenes(self):
        """Create 2022 and 2024 satellite scenes"""
        # TODO: Create two scenes with temporal changes
        
        # Generate base scene for 2022
        scene_2022 = self._generate_base_scene()
        
        # Generate 2024 scene with changes
        scene_2024 = self._apply_temporal_changes(scene_2022)
        
        # Save metadata
        self._save_metadata()
        
        return scene_2022, scene_2024
    
    def _generate_base_scene(self):
        """Generate the base 2022 satellite scene"""
        # TODO: Implement realistic land cover pattern generation
        # Create a scene with spatial patterns for different land covers
        
        scene = np.zeros((self.height, self.width, self.num_bands), dtype=np.uint8)
        
        # Simple implementation - replace with more sophisticated patterns
        # Water bodies (top-left region)
        scene[0:30, 0:40] = self.signatures['Water']
        
        # Vegetation (center-right)
        scene[20:80, 40:90] = self.signatures['Vegetation']
        
        # Urban areas (bottom-left)
        scene[60:100, 0:50] = self.signatures['Urban']
        
        # Bare soil (remaining areas)
        mask = np.all(scene == 0, axis=2)
        scene[mask] = self.signatures['Bare_Soil']
        
        # Add noise for realism
        noise = np.random.normal(0, 10, scene.shape).astype(np.int16)
        scene = np.clip(scene.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        
        return scene
    
    def _apply_temporal_changes(self, base_scene):
        """Apply temporal changes to create 2024 scene"""
        # TODO: Implement realistic temporal changes
        # - Urban expansion
        # - Deforestation
        # - Water level changes
        
        scene_2024 = base_scene.copy()
        
        # Example: Urban expansion (convert some vegetation to urban)
        # TODO: Implement more sophisticated change patterns
        
        # Convert some vegetation pixels to urban (simulate urban growth)
        vegetation_mask = self._get_land_cover_mask(base_scene, 'Vegetation')
        
        # Select random vegetation pixels for urban conversion
        veg_indices = np.where(vegetation_mask)
        if len(veg_indices[0]) > 0:
            # Convert 10% of vegetation to urban
            num_changes = len(veg_indices[0]) // 10
            change_indices = np.random.choice(len(veg_indices[0]), num_changes, replace=False)
            
            for idx in change_indices:
                row, col = veg_indices[0][idx], veg_indices[1][idx]
                scene_2024[row, col] = self.signatures['Urban']
        
        return scene_2024
    
    def _get_land_cover_mask(self, scene, land_cover_type):
        """Get boolean mask for specific land cover type"""
        # TODO: Implement spectral-based classification
        signature = np.array(self.signatures[land_cover_type])
        
        # Simple implementation: check similarity to signature
        # In practice, would use more sophisticated classification
        distances = np.linalg.norm(scene - signature, axis=2)
        threshold = 30  # Adjust based on noise level
        
        return distances < threshold
    
    def _save_metadata(self):
        """Save scene metadata"""
        metadata = {
            'scene_size': [self.height, self.width],
            'num_bands': self.num_bands,
            'band_names': self.band_names,
            'data_type': 'uint8',
            'spatial_resolution': 10,  # meters
            'coordinate_system': 'UTM_48N',
            'generation_date': datetime.now().isoformat(),
            'spectral_signatures': self.signatures
        }
        
        # TODO: Save to data/metadata.json
        print("Metadata saved (TODO: implement file saving)")


class ImagePreprocessor:
    """Preprocess satellite imagery"""
    
    def __init__(self):
        # Radiometric correction parameters
        self.gain = [0.01, 0.01, 0.01, 0.01]  # Convert DN to reflectance
        self.offset = [0.0, 0.0, 0.0, 0.0]
        
    def process_image(self, scene):
        """Apply preprocessing pipeline"""
        # TODO: Implement full preprocessing pipeline
        
        # 1. Radiometric correction
        processed = self._radiometric_correction(scene)
        
        # 2. Atmospheric correction (simplified)
        processed = self._atmospheric_correction(processed)
        
        # 3. Quality assessment
        quality_mask = self._quality_assessment(processed)
        
        return processed, quality_mask
    
    def _radiometric_correction(self, scene):
        """Convert DN values to reflectance"""
        # TODO: Implement proper radiometric correction
        # reflectance = (DN × gain) + offset
        
        # Convert to float for calculations
        scene_float = scene.astype(np.float32)
        
        # Apply gain and offset
        for band in range(scene.shape[2]):
            scene_float[:, :, band] = (scene_float[:, :, band] * self.gain[band]) + self.offset[band]
        
        # Scale to 0-1 range for reflectance
        reflectance = scene_float / 255.0
        
        return np.clip(reflectance, 0, 1)
    
    def _atmospheric_correction(self, reflectance):
        """Simple atmospheric correction"""
        # TODO: Implement atmospheric correction
        # This is simplified - real atmospheric correction is complex
        
        # Simple haze removal (subtract minimum value per band)
        corrected = reflectance.copy()
        
        for band in range(reflectance.shape[2]):
            min_val = np.percentile(reflectance[:, :, band], 1)  # Dark object subtraction
            corrected[:, :, band] = reflectance[:, :, band] - min_val
            
        return np.clip(corrected, 0, 1)
    
    def _quality_assessment(self, reflectance):
        """Assess image quality and create masks"""
        # TODO: Implement quality assessment
        # - Cloud detection
        # - Saturation detection
        # - Data completeness check
        
        quality_mask = np.ones((reflectance.shape[0], reflectance.shape[1]), dtype=bool)
        
        # Simple cloud detection (high reflectance in all bands)
        cloud_threshold = 0.8
        potential_clouds = np.all(reflectance > cloud_threshold, axis=2)
        quality_mask[potential_clouds] = False
        
        return quality_mask


class SpectralAnalyzer:
    """Analyze spectral characteristics and classify images"""
    
    def __init__(self):
        self.indices = {}
        
    def classify_image(self, scene_data):
        """Classify image into land cover types"""
        scene, quality_mask = scene_data
        
        # TODO: Implement comprehensive classification
        
        # 1. Calculate spectral indices
        indices = self._calculate_indices(scene)
        
        # 2. Perform classification
        classification = self._threshold_classification(scene, indices)
        
        # 3. Apply quality mask
        classification[~quality_mask] = 0  # No data
        
        return classification
    
    def _calculate_indices(self, scene):
        """Calculate vegetation and water indices"""
        # TODO: Implement spectral index calculations
        
        # Extract bands (assuming Blue, Green, Red, NIR order)
        blue = scene[:, :, 0]
        green = scene[:, :, 1]
        red = scene[:, :, 2]
        nir = scene[:, :, 3]
        
        indices = {}
        
        # NDVI: (NIR - Red) / (NIR + Red)
        indices['NDVI'] = (nir - red) / (nir + red + 1e-8)
        
        # NDWI: (Green - NIR) / (Green + NIR)
        indices['NDWI'] = (green - nir) / (green + nir + 1e-8)
        
        # SAVI: ((NIR - Red) / (NIR + Red + L)) * (1 + L)
        L = 0.5
        indices['SAVI'] = ((nir - red) / (nir + red + L)) * (1 + L)
        
        self.indices = indices
        return indices
    
    def _threshold_classification(self, scene, indices):
        """Classify using threshold-based rules"""
        # TODO: Implement classification rules
        
        classification = np.zeros((scene.shape[0], scene.shape[1]), dtype=np.uint8)
        
        # Classification scheme:
        # 0: No Data, 1: Water, 2: Vegetation, 3: Urban, 4: Bare Soil, 5: Clouds
        
        # Water: high NDWI, low NIR
        water_mask = (indices['NDWI'] > 0.3) & (scene[:, :, 3] < 0.2)
        classification[water_mask] = 1
        
        # Vegetation: high NDVI
        veg_mask = (indices['NDVI'] > 0.4) & (~water_mask)
        classification[veg_mask] = 2
        
        # Urban: moderate values in all bands
        urban_mask = ((scene[:, :, 0] > 0.2) & (scene[:, :, 1] > 0.2) & 
                     (scene[:, :, 2] > 0.2) & (indices['NDVI'] < 0.2) & (~water_mask))
        classification[urban_mask] = 3
        
        # Bare soil: remaining pixels
        remaining_mask = classification == 0
        classification[remaining_mask] = 4
        
        return classification


class ChangeDetector:
    """Detect changes between temporal images"""
    
    def __init__(self):
        self.change_types = {
            0: 'No Change',
            1: 'Water Loss',
            2: 'Water Gain', 
            3: 'Vegetation Loss',
            4: 'Vegetation Gain',
            5: 'Urban Expansion',
            6: 'Other Change'
        }
        
    def detect_changes(self, scene_2022_data, scene_2024_data):
        """Detect changes between two time periods"""
        # TODO: Implement change detection algorithms
        
        scene_2022, mask_2022 = scene_2022_data
        scene_2024, mask_2024 = scene_2024_data
        
        # 1. Image differencing
        diff_map = self._image_differencing(scene_2022, scene_2024)
        
        # 2. Index-based change detection
        index_changes = self._index_based_changes(scene_2022, scene_2024)
        
        # 3. Classification-based changes
        # This would use classifications from SpectralAnalyzer
        
        return diff_map, index_changes
    
    def _image_differencing(self, scene1, scene2):
        """Simple image differencing"""
        # TODO: Implement change detection through differencing
        
        # Calculate difference in each band
        diff = scene2 - scene1
        
        # Calculate magnitude of change
        change_magnitude = np.linalg.norm(diff, axis=2)
        
        # Threshold for significant change
        change_threshold = 0.1
        change_mask = change_magnitude > change_threshold
        
        return change_mask.astype(np.uint8)
    
    def _index_based_changes(self, scene1, scene2):
        """Detect changes using spectral indices"""
        # TODO: Implement index-based change detection
        
        # Calculate NDVI for both scenes
        analyzer = SpectralAnalyzer()
        indices_2022 = analyzer._calculate_indices(scene1)
        indices_2024 = analyzer._calculate_indices(scene2)
        
        # NDVI change
        ndvi_change = indices_2024['NDVI'] - indices_2022['NDVI']
        
        # Classify changes
        change_map = np.zeros_like(ndvi_change, dtype=np.uint8)
        
        # Vegetation loss (NDVI decrease > 0.2)
        veg_loss = ndvi_change < -0.2
        change_map[veg_loss] = 3
        
        # Vegetation gain (NDVI increase > 0.2)
        veg_gain = ndvi_change > 0.2
        change_map[veg_gain] = 4
        
        return change_map
    
    def generate_change_report(self, class_2022, class_2024, change_map):
        """Generate comprehensive change analysis report"""
        # TODO: Implement report generation
        
        print("\\n" + "="*50)
        print("CHANGE DETECTION REPORT")
        print("="*50)
        
        # Calculate area statistics
        # TODO: Implement detailed statistics
        
        print("Change analysis complete!")
        print("TODO: Generate detailed statistics and save to file")


def main():
    """Main processing pipeline"""
    print("=" * 60)
    print("SATELLITE IMAGE PROCESSING SYSTEM")
    print("=" * 60)
    
    # 1. Generate synthetic satellite data
    print("\\n1. Generating synthetic satellite imagery...")
    generator = SatelliteImageGenerator()
    scene_2022, scene_2024 = generator.create_temporal_scenes()
    print(f"Generated scenes shape: {scene_2022.shape}")
    
    # 2. Preprocess images
    print("\\n2. Preprocessing images...")
    preprocessor = ImagePreprocessor()
    scene_2022_processed = preprocessor.process_image(scene_2022)
    scene_2024_processed = preprocessor.process_image(scene_2024)
    print("Preprocessing complete.")
    
    # 3. Spectral analysis and classification
    print("\\n3. Performing spectral analysis...")
    analyzer = SpectralAnalyzer()
    classification_2022 = analyzer.classify_image(scene_2022_processed)
    classification_2024 = analyzer.classify_image(scene_2024_processed)
    print("Classification complete.")
    
    # 4. Change detection
    print("\\n4. Detecting changes...")
    change_detector = ChangeDetector()
    change_results = change_detector.detect_changes(
        scene_2022_processed, scene_2024_processed
    )
    print("Change detection complete.")
    
    # 5. Generate reports
    print("\\n5. Generating change report...")
    change_detector.generate_change_report(
        classification_2022, classification_2024, change_results[0]
    )
    
    print("\\n" + "=" * 60)
    print("PROCESSING COMPLETE!")
    print("=" * 60)
    print("Results saved to outputs/ folder (TODO: implement file saving)")


if __name__ == "__main__":
    main()
