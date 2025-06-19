#!/usr/bin/env python3
"""
Project 3: NDVI Land Use Change Analysis for Vietnam
Week 4: Pandas Data Analysis

Author: [Your Name]
Date: [Current Date]
Description: Comprehensive analysis of vegetation changes and land use patterns using NDVI
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class NDVILandUseAnalyzer:
    """
    Comprehensive NDVI and land use change analyzer for Vietnam
    Handles satellite data processing and environmental monitoring
    """
    
    def __init__(self, data_path=None):
        """Initialize the NDVI analyzer"""
        self.data_path = data_path
        self.ndvi_data = None
        self.climate_data = None
        self.change_events = {}
        self.trends = {}
        self.indicators = {}
        self.alerts = []
        
        print("NDVI Land Use Analyzer initialized")
        print("Ready to analyze Vietnam vegetation changes (2015-2023)")
    
    def generate_sample_data(self):
        """
        Generate realistic NDVI and land use data for demonstration
        In real implementation, this would load from satellite imagery
        """
        print("Generating sample NDVI and land use data...")
        
        # Create monthly date range (2015-2023)
        dates = pd.date_range('2015-01-01', '2023-12-31', freq='MS')
        
        # Vietnam provinces
        provinces = [
            'An Giang', 'Bà Rịa-Vũng Tàu', 'Bắc Giang', 'Bắc Kạn', 'Bạc Liêu',
            'Bắc Ninh', 'Bến Tre', 'Bình Định', 'Bình Dương', 'Bình Phước',
            'Cà Mau', 'Cao Bằng', 'Đắk Lắk', 'Đắk Nông', 'Điện Biên',
            'Đồng Nai', 'Đồng Tháp', 'Gia Lai', 'Hà Giang', 'Hà Nam',
            'Hà Tĩnh', 'Hải Dương', 'Hậu Giang', 'Hòa Bình', 'Hưng Yên',
            'Khánh Hòa', 'Kiên Giang', 'Kon Tum', 'Lai Châu', 'Lâm Đồng'
        ]
        
        # Land cover types với typical NDVI ranges
        land_covers = {
            'Forest': {'base_ndvi': 0.8, 'variation': 0.1},
            'Cropland': {'base_ndvi': 0.6, 'variation': 0.2},
            'Grassland': {'base_ndvi': 0.5, 'variation': 0.15},
            'Urban': {'base_ndvi': 0.2, 'variation': 0.05},
            'Water': {'base_ndvi': -0.1, 'variation': 0.1}
        }
        
        protected_status = ['Protected', 'Non-protected']
        
        data = []
        np.random.seed(42)  # For reproducible results
        
        pixel_id = 1
        for province in provinces[:10]:  # Use first 10 provinces for demo
            for land_cover, props in land_covers.items():
                for status in protected_status:
                    for date in dates:
                        # Simulate seasonal NDVI patterns
                        seasonal_factor = 0.1 * np.sin(2 * np.pi * date.month / 12)
                        
                        # Long-term trend (slight decline for non-protected forest)
                        years_since_2015 = (date.year - 2015)
                        if land_cover == 'Forest' and status == 'Non-protected':
                            trend_factor = -0.005 * years_since_2015  # Deforestation
                        elif land_cover == 'Urban':
                            trend_factor = 0.002 * years_since_2015   # Slight greening
                        else:
                            trend_factor = 0
                        
                        # Base NDVI với variations
                        base_ndvi = props['base_ndvi']
                        variation = props['variation']
                        
                        # Climate impact (drought simulation in 2016, 2020)
                        climate_impact = 0
                        if date.year in [2016, 2020] and land_cover in ['Forest', 'Cropland']:
                            climate_impact = -0.1
                        
                        # Final NDVI calculation
                        ndvi = base_ndvi + seasonal_factor + trend_factor + climate_impact + \
                               np.random.normal(0, variation * 0.3)
                        ndvi = np.clip(ndvi, -1, 1)  # NDVI bounds
                        
                        # Simulate some missing data (clouds, etc.)
                        quality_flag = 'Good'
                        if np.random.random() < 0.15:  # 15% poor quality
                            quality_flag = np.random.choice(['Cloud', 'Shadow', 'Haze'])
                            if np.random.random() < 0.3:  # 30% of poor quality are NaN
                                ndvi = np.nan
                        
                        data.append({
                            'date': date,
                            'pixel_id': pixel_id,
                            'province': province,
                            'land_cover': land_cover,
                            'protected_status': status,
                            'ndvi': round(ndvi, 3) if not pd.isna(ndvi) else np.nan,
                            'latitude': 10.5 + np.random.uniform(-3, 6),
                            'longitude': 106.0 + np.random.uniform(-2, 4),
                            'elevation': np.random.uniform(0, 1500),
                            'slope': np.random.uniform(0, 30),
                            'quality_flag': quality_flag,
                            'area_km2': np.random.uniform(0.25, 1.0)  # Pixel area
                        })
                        
                        pixel_id += 1
        
        self.ndvi_data = pd.DataFrame(data)
        print(f"Generated {len(self.ndvi_data)} NDVI observations")
        print(f"Provinces: {self.ndvi_data['province'].nunique()}")
        print(f"Land covers: {self.ndvi_data['land_cover'].unique()}")
        print(f"Date range: {self.ndvi_data['date'].min()} to {self.ndvi_data['date'].max()}")
        
        return self.ndvi_data
    
    def load_and_clean_data(self):
        """Load and clean NDVI satellite data"""
        print("\n=== DATA LOADING AND CLEANING ===")
        
        # Generate sample data (in real project, load from satellite files)
        if self.ndvi_data is None:
            self.generate_sample_data()
        
        df = self.ndvi_data.copy()
        
        print(f"Raw data shape: {df.shape}")
        print(f"Missing NDVI values: {df['ndvi'].isnull().sum()} ({df['ndvi'].isnull().sum()/len(df)*100:.1f}%)")
        print(f"Quality flags distribution:")
        print(df['quality_flag'].value_counts())
        
        # Filter out poor quality data
        good_quality_mask = df['quality_flag'] == 'Good'
        df_clean = df[good_quality_mask].copy()
        
        # Interpolate missing NDVI values by land cover and location
        for land_cover in df_clean['land_cover'].unique():
            for province in df_clean['province'].unique():
                mask = (df_clean['land_cover'] == land_cover) & (df_clean['province'] == province)
                if mask.sum() > 0:
                    # Time-based interpolation
                    subset = df_clean[mask].sort_values('date')
                    df_clean.loc[mask, 'ndvi'] = subset['ndvi'].interpolate(method='time')
        
        # Add derived columns
        df_clean['year'] = df_clean['date'].dt.year
        df_clean['month'] = df_clean['date'].dt.month
        df_clean['season'] = df_clean['month'].map({
            12: 'Dry', 1: 'Dry', 2: 'Dry',
            3: 'Transition', 4: 'Transition', 5: 'Wet',
            6: 'Wet', 7: 'Wet', 8: 'Wet',
            9: 'Wet', 10: 'Transition', 11: 'Dry'
        })
        
        # Calculate vegetation health indicators
        df_clean['ndvi_anomaly'] = df_clean.groupby(['land_cover', 'province'])['ndvi'].transform(
            lambda x: (x - x.mean()) / x.std()
        )
        
        self.ndvi_data = df_clean
        print(f"\nCleaned data shape: {self.ndvi_data.shape}")
        print("Data cleaning completed!")
        
        return self.ndvi_data
    
    def classify_land_cover(self):
        """Enhanced land cover classification and health assessment"""
        print("\n=== LAND COVER CLASSIFICATION ===")
        
        if self.ndvi_data is None:
            self.load_and_clean_data()
        
        df = self.ndvi_data
        
        # Calculate land cover statistics
        land_cover_stats = df.groupby(['province', 'land_cover', 'protected_status']).agg({
            'ndvi': ['mean', 'std', 'min', 'max', 'count'],
            'area_km2': 'sum'
        }).round(3)
        
        print("Land Cover Statistics by Province:")
        print(land_cover_stats.head(10))
        
        # Vegetation health classification
        def classify_vegetation_health(ndvi, land_cover):
            if land_cover == 'Water':
                return 'N/A'
            elif land_cover == 'Urban':
                if ndvi > 0.3: return 'Green Urban'
                elif ndvi > 0.1: return 'Moderate Urban'
                else: return 'Dense Urban'
            elif land_cover in ['Forest', 'Grassland']:
                if ndvi > 0.7: return 'Healthy'
                elif ndvi > 0.5: return 'Moderate'
                elif ndvi > 0.3: return 'Stressed'
                else: return 'Degraded'
            elif land_cover == 'Cropland':
                if ndvi > 0.6: return 'Good Crop'
                elif ndvi > 0.4: return 'Moderate Crop'
                elif ndvi > 0.2: return 'Poor Crop'
                else: return 'Bare/Failed'
            else:
                return 'Unknown'
        
        df['vegetation_health'] = df.apply(
            lambda row: classify_vegetation_health(row['ndvi'], row['land_cover']), axis=1
        )
        
        # Health distribution
        health_dist = df.groupby(['land_cover', 'vegetation_health']).size().unstack(fill_value=0)
        print(f"\nVegetation Health Distribution:")
        print(health_dist)
        
        self.ndvi_data = df
        return land_cover_stats
    
    def detect_changes(self):
        """Detect significant land cover and vegetation changes"""
        print("\n=== CHANGE DETECTION ANALYSIS ===")
        
        if self.ndvi_data is None:
            self.load_and_clean_data()
        
        df = self.ndvi_data
        
        # Annual NDVI trends by land cover and protection status
        annual_ndvi = df.groupby(['year', 'land_cover', 'protected_status', 'province'])['ndvi'].mean().reset_index()
        
        change_results = {}
        
        # Detect significant trends for each group
        for land_cover in df['land_cover'].unique():
            for status in df['protected_status'].unique():
                for province in df['province'].unique():
                    subset = annual_ndvi[
                        (annual_ndvi['land_cover'] == land_cover) &
                        (annual_ndvi['protected_status'] == status) &
                        (annual_ndvi['province'] == province)
                    ]
                    
                    if len(subset) >= 5:  # Need at least 5 years for trend analysis
                        # Linear regression for trend
                        slope, intercept, r_value, p_value, std_err = stats.linregress(subset['year'], subset['ndvi'])
                        
                        # Significant change threshold
                        is_significant = p_value < 0.05 and abs(slope) > 0.005  # 0.005 NDVI/year
                        
                        if is_significant:
                            change_type = 'Improvement' if slope > 0 else 'Degradation'
                            total_change = slope * (subset['year'].max() - subset['year'].min())
                            
                            key = f"{province}_{land_cover}_{status}"
                            change_results[key] = {
                                'province': province,
                                'land_cover': land_cover,
                                'protected_status': status,
                                'trend_slope': slope,
                                'total_change': total_change,
                                'r_squared': r_value**2,
                                'p_value': p_value,
                                'change_type': change_type,
                                'significance': 'High' if p_value < 0.01 else 'Moderate'
                            }
        
        # Convert to DataFrame for analysis
        changes_df = pd.DataFrame(change_results).T
        
        if not changes_df.empty:
            print("Significant Vegetation Changes Detected:")
            print("-" * 60)
            
            # Top degradation cases
            degradation = changes_df[changes_df['change_type'] == 'Degradation'].sort_values('trend_slope')
            print("Top 5 Degradation Cases:")
            for idx, row in degradation.head().iterrows():
                print(f"  {row['province']} - {row['land_cover']} ({row['protected_status']})")
                print(f"    NDVI change: {row['total_change']:.3f} ({row['trend_slope']:.4f}/year)")
                print(f"    Significance: {row['significance']} (p={row['p_value']:.3f})")
            
            # Top improvement cases
            improvement = changes_df[changes_df['change_type'] == 'Improvement'].sort_values('trend_slope', ascending=False)
            print(f"\nTop 5 Improvement Cases:")
            for idx, row in improvement.head().iterrows():
                print(f"  {row['province']} - {row['land_cover']} ({row['protected_status']})")
                print(f"    NDVI change: {row['total_change']:.3f} ({row['trend_slope']:.4f}/year)")
                print(f"    Significance: {row['significance']} (p={row['p_value']:.3f})")
            
            # Protection effectiveness
            protected_changes = changes_df[changes_df['protected_status'] == 'Protected']['trend_slope'].mean()
            non_protected_changes = changes_df[changes_df['protected_status'] == 'Non-protected']['trend_slope'].mean()
            
            print(f"\nProtection Effectiveness:")
            print(f"  Protected areas average trend: {protected_changes:.4f} NDVI/year")
            print(f"  Non-protected areas average trend: {non_protected_changes:.4f} NDVI/year")
            print(f"  Protection benefit: {protected_changes - non_protected_changes:.4f} NDVI/year")
        
        self.change_events = change_results
        return changes_df
    
    def calculate_indicators(self):
        """Calculate environmental health and sustainability indicators"""
        print("\n=== ENVIRONMENTAL INDICATORS ===")
        
        if self.ndvi_data is None:
            self.load_and_clean_data()
        
        df = self.ndvi_data
        
        # 1. Vegetation Condition Index (VCI)
        def calculate_vci(group):
            ndvi_min = group['ndvi'].min()
            ndvi_max = group['ndvi'].max()
            ndvi_current = group['ndvi']
            if ndvi_max > ndvi_min:
                return ((ndvi_current - ndvi_min) / (ndvi_max - ndvi_min)) * 100
            else:
                return 50  # Default moderate condition
        
        df['vci'] = df.groupby(['province', 'land_cover'])['ndvi'].transform(calculate_vci)
        
        # 2. Forest Health Index
        forest_data = df[df['land_cover'] == 'Forest']
        if not forest_data.empty:
            forest_health = forest_data.groupby(['province', 'protected_status']).agg({
                'ndvi': 'mean',
                'vci': 'mean',
                'area_km2': 'sum'
            }).reset_index()
            
            # Composite forest health score (0-100)
            forest_health['forest_health_score'] = (
                forest_health['ndvi'] * 50 + forest_health['vci'] * 0.5
            ).clip(0, 100)
            
            print("Forest Health by Province and Protection Status:")
            print(forest_health.round(1))
        
        # 3. Land Use Diversity Index (Shannon-like index)
        def calculate_diversity_index(group):
            proportions = group['area_km2'] / group['area_km2'].sum()
            proportions = proportions[proportions > 0]  # Remove zeros
            if len(proportions) > 1:
                return -np.sum(proportions * np.log(proportions))
            else:
                return 0
        
        land_diversity = df.groupby('province').apply(
            lambda x: x.groupby('land_cover')['area_km2'].sum().pipe(
                lambda y: calculate_diversity_index(pd.DataFrame({'area_km2': y}))
            )
        ).reset_index()
        land_diversity.columns = ['province', 'land_diversity_index']
        
        print(f"\nLand Use Diversity Index by Province:")
        print(land_diversity.round(3))
        
        # 4. Deforestation Risk Score
        if not forest_data.empty:
            risk_factors = forest_data.groupby('province').agg({
                'ndvi': ['mean', 'std'],
                'ndvi_anomaly': lambda x: (x < -1).sum() / len(x),  # Severe stress events
                'protected_status': lambda x: (x == 'Non-protected').sum() / len(x)  # Unprotected ratio
            }).round(3)
            
            risk_factors.columns = ['avg_ndvi', 'ndvi_variability', 'stress_event_ratio', 'unprotected_ratio']
            
            # Composite risk score (higher = more risk)
            risk_factors['deforestation_risk'] = (
                (1 - risk_factors['avg_ndvi']) * 25 +  # Lower NDVI = higher risk
                risk_factors['ndvi_variability'] * 25 +  # Higher variability = higher risk
                risk_factors['stress_event_ratio'] * 25 +  # More stress events = higher risk
                risk_factors['unprotected_ratio'] * 25  # Less protection = higher risk
            ).clip(0, 100)
            
            print(f"\nDeforestation Risk Assessment:")
            print(risk_factors[['avg_ndvi', 'deforestation_risk']].sort_values('deforestation_risk', ascending=False))
        
        self.indicators = {
            'forest_health': forest_health if not forest_data.empty else None,
            'land_diversity': land_diversity,
            'deforestation_risk': risk_factors if not forest_data.empty else None
        }
        
        return self.indicators
    
    def generate_alerts(self):
        """Generate environmental monitoring alerts"""
        print("\n=== ALERT GENERATION ===")
        
        if self.ndvi_data is None:
            self.load_and_clean_data()
        
        df = self.ndvi_data
        alerts = []
        
        # Recent data (last 2 years)
        recent_data = df[df['year'] >= 2022]
        
        # Alert 1: Severe NDVI drops
        severe_drops = recent_data[
            (recent_data['ndvi_anomaly'] < -2) &  # 2 standard deviations below normal
            (recent_data['land_cover'].isin(['Forest', 'Cropland']))
        ]
        
        for _, row in severe_drops.iterrows():
            alerts.append({
                'type': 'Severe NDVI Drop',
                'priority': 'HIGH',
                'location': f"{row['province']} ({row['latitude']:.3f}, {row['longitude']:.3f})",
                'land_cover': row['land_cover'],
                'current_ndvi': row['ndvi'],
                'anomaly_score': row['ndvi_anomaly'],
                'date': row['date'],
                'area_affected': row['area_km2'],
                'description': f"NDVI dropped to {row['ndvi']:.3f} ({row['ndvi_anomaly']:.1f}σ below normal)"
            })
        
        # Alert 2: Unprotected forest stress
        forest_stress = recent_data[
            (recent_data['land_cover'] == 'Forest') &
            (recent_data['protected_status'] == 'Non-protected') &
            (recent_data['ndvi'] < 0.6)  # Below healthy forest threshold
        ]
        
        if not forest_stress.empty:
            stress_summary = forest_stress.groupby('province').agg({
                'area_km2': 'sum',
                'ndvi': 'mean'
            }).reset_index()
            
            for _, row in stress_summary.iterrows():
                if row['area_km2'] > 5:  # Significant area affected
                    alerts.append({
                        'type': 'Unprotected Forest Stress',
                        'priority': 'MEDIUM',
                        'location': row['province'],
                        'land_cover': 'Forest',
                        'current_ndvi': row['ndvi'],
                        'area_affected': row['area_km2'],
                        'description': f"{row['area_km2']:.1f} km² of unprotected forest showing stress"
                    })
        
        # Alert 3: Urban expansion into natural areas
        # (This would require temporal comparison - simplified here)
        urban_expansion = recent_data[
            (recent_data['land_cover'] == 'Urban') &
            (recent_data['ndvi'] < 0.15)  # Very low vegetation in urban areas
        ]
        
        if not urban_expansion.empty:
            expansion_by_province = urban_expansion.groupby('province')['area_km2'].sum()
            for province, area in expansion_by_province.items():
                if area > 10:  # Significant urban area
                    alerts.append({
                        'type': 'Dense Urban Development',
                        'priority': 'LOW',
                        'location': province,
                        'land_cover': 'Urban',
                        'area_affected': area,
                        'description': f"{area:.1f} km² of dense urban development detected"
                    })
        
        # Sort alerts by priority and area affected
        priority_order = {'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}
        alerts_df = pd.DataFrame(alerts)
        
        if not alerts_df.empty:
            alerts_df['priority_score'] = alerts_df['priority'].map(priority_order)
            alerts_df = alerts_df.sort_values(['priority_score', 'area_affected'], ascending=[False, False])
            
            print(f"Generated {len(alerts_df)} environmental alerts:")
            print("-" * 60)
            
            for idx, alert in alerts_df.head(10).iterrows():  # Show top 10 alerts
                print(f"[{alert['priority']}] {alert['type']}")
                print(f"  Location: {alert['location']}")
                print(f"  Description: {alert['description']}")
                if 'area_affected' in alert and pd.notna(alert['area_affected']):
                    print(f"  Area affected: {alert['area_affected']:.1f} km²")
                print()
        
        self.alerts = alerts
        return alerts_df if not alerts_df.empty else pd.DataFrame()
    
    def generate_report(self):
        """Generate comprehensive environmental monitoring report"""
        print("\n=== ENVIRONMENTAL MONITORING REPORT ===")
        
        # Ensure all analyses are completed
        if self.ndvi_data is None:
            self.load_and_clean_data()
        if not self.change_events:
            self.detect_changes()
        if not self.indicators:
            self.calculate_indicators()
        if not self.alerts:
            self.generate_alerts()
        
        df = self.ndvi_data
        
        # Summary statistics
        total_area = df['area_km2'].sum()
        forest_area = df[df['land_cover'] == 'Forest']['area_km2'].sum()
        protected_forest = df[
            (df['land_cover'] == 'Forest') & (df['protected_status'] == 'Protected')
        ]['area_km2'].sum()
        
        avg_forest_ndvi = df[df['land_cover'] == 'Forest']['ndvi'].mean()
        
        # Recent trends
        recent_changes = len([k for k, v in self.change_events.items() 
                            if v['change_type'] == 'Degradation'])
        
        num_alerts = len(self.alerts)
        
        # Generate report
        report = f"""
VIETNAM ENVIRONMENTAL MONITORING REPORT
======================================
Analysis Period: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

EXECUTIVE SUMMARY
-----------------
• Total monitored area: {total_area:.0f} km²
• Forest coverage: {forest_area:.0f} km² ({forest_area/total_area*100:.1f}% of monitored area)
• Protected forest: {protected_forest:.0f} km² ({protected_forest/forest_area*100:.1f}% of forest)
• Average forest NDVI: {avg_forest_ndvi:.3f}

CHANGE DETECTION RESULTS
------------------------
• Significant degradation cases detected: {recent_changes}
• Current active alerts: {num_alerts}
• Protection effectiveness: {'Confirmed' if protected_forest > 0 else 'Under Review'}

VEGETATION HEALTH STATUS
-----------------------"""
        
        if self.indicators and 'forest_health' is not None:
            forest_health = self.indicators['forest_health']
            if forest_health is not None:
                avg_protected_health = forest_health[
                    forest_health['protected_status'] == 'Protected'
                ]['forest_health_score'].mean()
                avg_unprotected_health = forest_health[
                    forest_health['protected_status'] == 'Non-protected'
                ]['forest_health_score'].mean()
                
                report += f"""
• Protected forest health: {avg_protected_health:.1f}/100
• Non-protected forest health: {avg_unprotected_health:.1f}/100
• Health difference: {avg_protected_health - avg_unprotected_health:.1f} points"""
        
        report += f"""

LAND USE DIVERSITY
------------------"""
        if self.indicators and 'land_diversity' is not None:
            land_diversity = self.indicators['land_diversity']
            avg_diversity = land_diversity['land_diversity_index'].mean()
            report += f"""
• Average land use diversity index: {avg_diversity:.2f}
• Most diverse province: {land_diversity.loc[land_diversity['land_diversity_index'].idxmax(), 'province']}
• Least diverse province: {land_diversity.loc[land_diversity['land_diversity_index'].idxmin(), 'province']}"""
        
        if self.alerts:
            high_priority_alerts = len([a for a in self.alerts if a['priority'] == 'HIGH'])
            report += f"""

PRIORITY ACTIONS REQUIRED
------------------------
• High priority alerts: {high_priority_alerts}
• Recommended immediate actions:
  - Deploy field verification teams to high-priority locations
  - Coordinate with local forest protection agencies
  - Enhance monitoring in identified risk areas
  - Update conservation strategies based on findings"""
        
        report += f"""

METHODOLOGY
-----------
• Data source: Simulated NDVI satellite observations
• Temporal resolution: Monthly (2015-2023)
• Spatial coverage: 10 Vietnamese provinces
• Quality control: Cloud masking and temporal interpolation
• Change detection: Linear trend analysis with statistical significance testing
• Health indicators: Vegetation Condition Index and composite scoring

LIMITATIONS
-----------
• This is a demonstration with simulated data
• Real implementation requires actual satellite imagery
• Ground truth validation recommended for operational use
• Temporal gaps may affect trend accuracy

Report generated by NDVI Land Use Analyzer v1.0
Contact: Environmental Monitoring Team
"""
        
        print(report)
        return report
    
    def save_results(self, output_dir="ndvi_analysis_results"):
        """Save all analysis results to files"""
        import os
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save processed NDVI data
        if self.ndvi_data is not None:
            self.ndvi_data.to_csv(f"{output_dir}/ndvi_processed_data.csv", index=False)
            print(f"NDVI data saved to {output_dir}/ndvi_processed_data.csv")
        
        # Save change detection results
        if self.change_events:
            changes_df = pd.DataFrame(self.change_events).T
            changes_df.to_csv(f"{output_dir}/vegetation_changes.csv")
            print(f"Change detection results saved to {output_dir}/vegetation_changes.csv")
        
        # Save indicators
        if self.indicators:
            for name, data in self.indicators.items():
                if data is not None:
                    if isinstance(data, pd.DataFrame):
                        data.to_csv(f"{output_dir}/{name}_indicators.csv", index=False)
                        print(f"{name} indicators saved to {output_dir}/{name}_indicators.csv")
        
        # Save alerts
        if self.alerts:
            alerts_df = pd.DataFrame(self.alerts)
            alerts_df.to_csv(f"{output_dir}/environmental_alerts.csv", index=False)
            print(f"Environmental alerts saved to {output_dir}/environmental_alerts.csv")


def main():
    """Main function to run complete NDVI land use analysis"""
    print("="*70)
    print("VIETNAM NDVI LAND USE CHANGE ANALYSIS PROJECT")
    print("Week 4: Pandas Data Analysis")
    print("="*70)
    
    # Initialize analyzer
    analyzer = NDVILandUseAnalyzer()
    
    # Run complete analysis pipeline
    try:
        # Step 1: Data processing
        analyzer.load_and_clean_data()
        
        # Step 2: Land cover classification
        analyzer.classify_land_cover()
        
        # Step 3: Change detection
        analyzer.detect_changes()
        
        # Step 4: Environmental indicators
        analyzer.calculate_indicators()
        
        # Step 5: Alert generation
        analyzer.generate_alerts()
        
        # Step 6: Generate comprehensive report
        analyzer.generate_report()
        
        # Step 7: Save all results
        analyzer.save_results()
        
        print("\n" + "="*70)
        print("ANALYSIS COMPLETED SUCCESSFULLY!")
        print("Check the 'ndvi_analysis_results' folder for all output files.")
        print("="*70)
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise

if __name__ == "__main__":
    main()
