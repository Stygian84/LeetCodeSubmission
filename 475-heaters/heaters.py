class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        n = len(houses)
        m = len(heaters)
        
        max_radius = 0
        i = 0  
        j = 0  
        
        while i < n:
            while j < m - 1 and abs(heaters[j + 1] - houses[i]) <= abs(heaters[j] - houses[i]):
                j += 1
            
            max_radius = max(max_radius, abs(heaters[j] - houses[i]))
            i += 1
        
        return max_radius

