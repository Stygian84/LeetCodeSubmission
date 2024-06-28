class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        road_count = [0]*n
        for a,b in roads:
            road_count[a]+=1
            road_count[b]+=1
        
        sorted_cities = sorted(range(n), key=lambda x: road_count[x], reverse=True)
        
        city_values = [0] * n
        value = n
        for city in sorted_cities:
            city_values[city] = value
            value -= 1
        
        total_importance = 0
        for a, b in roads:
            total_importance += city_values[a] + city_values[b]
        
        return total_importance
        