class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sqrt_sum_squares(point):
            return sqrt(point[0]**2 + point[1]**2)

        sorted_points = sorted(points, key=sqrt_sum_squares)
        
        return sorted_points[:k]