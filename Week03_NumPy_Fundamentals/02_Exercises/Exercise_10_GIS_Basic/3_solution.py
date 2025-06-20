import numpy as np

def main():
    """GIS Basic Operations - Solution"""
    print("=== GIS BASIC OPERATIONS ===")
    print()
    
    # Sample coordinates (latitude, longitude) for major Vietnamese cities
    hanoi_coords = np.array([21.0285, 105.8542])
    hcm_coords = np.array([10.8231, 106.6297])
    danang_coords = np.array([16.0471, 108.2068])
    
    # Create coordinate array for batch operations
    cities = np.array([hanoi_coords, hcm_coords, danang_coords])
    city_names = ['Hanoi', 'Ho Chi Minh', 'Da Nang']
    
    # 📍 COORDINATES
    print("📍 COORDINATES:")
    for i, name in enumerate(city_names):
        print(f"{name}: {cities[i]}")
    print()
    
    # 📏 DISTANCE CALCULATIONS
    print("📏 DISTANCE CALCULATIONS:")
    
    # Euclidean Distance
    print("Euclidean Distance:")
    euclidean_distances = calculate_euclidean_distances(cities, city_names)
    print()
    
    # Haversine Distance (Great Circle)
    print("Haversine Distance (Great Circle):")
    haversine_distances = calculate_haversine_distances(cities, city_names)
    print()
    
    # 📦 BOUNDING BOX FILTERING
    print("📦 BOUNDING BOX FILTERING:")
    # Vietnam bounding box
    bbox = {'lat_min': 10, 'lat_max': 22, 'lon_min': 105, 'lon_max': 109}
    filter_by_bounding_box(cities, city_names, bbox)
    print()
    
    # 🎯 NEAREST NEIGHBOR
    print("🎯 NEAREST NEIGHBOR:")
    target_point = np.array([18.5, 107.0])  # Point somewhere in central Vietnam
    nearest_neighbor_search(cities, city_names, target_point)
    print()
    
    # 📐 POLYGON OPERATIONS
    print("📐 POLYGON OPERATIONS:")
    polygon_operations(cities)

def calculate_euclidean_distances(cities, city_names):
    """Calculate Euclidean distances between cities"""
    n_cities = len(cities)
    for i in range(n_cities):
        for j in range(i + 1, n_cities):
            # Euclidean distance in degrees
            diff = cities[i] - cities[j]
            distance = np.sqrt(np.sum(diff**2))
            print(f"  {city_names[i]} ↔ {city_names[j]}: {distance:.2f} degrees")

def calculate_haversine_distances(cities, city_names):
    """Calculate Haversine distances between cities"""
    def haversine(lat1, lon1, lat2, lon2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))
        
        # Radius of earth in kilometers
        r = 6371
        return c * r
    
    n_cities = len(cities)
    for i in range(n_cities):
        for j in range(i + 1, n_cities):
            lat1, lon1 = cities[i]
            lat2, lon2 = cities[j]
            distance = haversine(lat1, lon1, lat2, lon2)
            print(f"  {city_names[i]} ↔ {city_names[j]}: {distance:.1f} km")

def filter_by_bounding_box(cities, city_names, bbox):
    """Filter cities within bounding box"""
    print(f"Bounding box: [{bbox['lat_min']}°N-{bbox['lat_max']}°N, {bbox['lon_min']}°E-{bbox['lon_max']}°E]")
    
    # Boolean indexing for filtering
    lat_mask = (cities[:, 0] >= bbox['lat_min']) & (cities[:, 0] <= bbox['lat_max'])
    lon_mask = (cities[:, 1] >= bbox['lon_min']) & (cities[:, 1] <= bbox['lon_max'])
    within_bounds = lat_mask & lon_mask
    
    print(f"Cities within bounds: {np.sum(within_bounds)}/{len(cities)}")
    
    for i, (name, in_bounds) in enumerate(zip(city_names, within_bounds)):
        status = "✅" if in_bounds else "❌"
        print(f"- {name}: {status}")

def nearest_neighbor_search(cities, city_names, target_point):
    """Find nearest city to target point"""
    print(f"Target point: {target_point}")
    
    # Calculate distances to target point
    distances = np.sqrt(np.sum((cities - target_point)**2, axis=1))
    
    # Find nearest neighbor
    nearest_idx = np.argmin(distances)
    nearest_city = city_names[nearest_idx]
    nearest_distance = distances[nearest_idx]
    
    print(f"Nearest city: {nearest_city} (distance: {nearest_distance:.2f} degrees)")

def polygon_operations(cities):
    """Calculate polygon area and centroid"""
    # Using shoelace formula for triangle area
    lat = cities[:, 0]
    lon = cities[:, 1]
    
    # Shoelace formula for polygon area
    n = len(cities)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += lat[i] * lon[j]
        area -= lat[j] * lon[i]
    area = abs(area) / 2.0
    
    # Calculate centroid
    centroid_lat = np.mean(lat)
    centroid_lon = np.mean(lon)
    
    print(f"Triangle area (Hanoi-HCM-DaNang): {area:.2f} square degrees")
    print(f"Centroid: [{centroid_lat:.2f}°N, {centroid_lon:.2f}°E]")

if __name__ == "__main__":
    main()
