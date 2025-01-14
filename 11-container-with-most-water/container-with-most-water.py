class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        res = 0
        while l<=r:
            dist = r-l
            if height[l]<height[r]:
                res = max(res, dist*height[l])
                l+=1
            else:
                res = max(res, dist*height[r])
                r-=1
        
        return res
            
