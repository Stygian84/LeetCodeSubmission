class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1

        max_area=0
        while left<=right:
            distance=right-left
            area=min(height[left],height[right])*distance
            max_area=max(area,max_area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area