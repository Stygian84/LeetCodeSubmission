class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return sqrt(point[0]**2 + point[1]**2)
        
        max_heap = []
        
        for point in points:
            dist = distance(point)
            
            heapq.heappush(max_heap, (-dist, point))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        closest_points = [point for _, point in max_heap]
        
        return closest_points