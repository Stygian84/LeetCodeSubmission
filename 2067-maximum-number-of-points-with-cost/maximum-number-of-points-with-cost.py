class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        
        dp = points[0]
        
        for r in range(1, n):
            left_to_right = [0] * m
            right_to_left = [0] * m
            
            left_to_right[0] = dp[0]
            for c in range(1, m):
                left_to_right[c] = max(left_to_right[c-1] - 1, dp[c])
            
            right_to_left[-1] = dp[-1]
            for c in range(m-2, -1, -1):
                right_to_left[c] = max(right_to_left[c+1] - 1, dp[c])
            
            for c in range(m):
                dp[c] = points[r][c] + max(left_to_right[c], right_to_left[c])
    
        return max(dp)
