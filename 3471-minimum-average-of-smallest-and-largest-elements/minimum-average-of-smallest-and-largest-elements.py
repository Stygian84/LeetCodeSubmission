class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        min_value=math.inf

        l,r=0,len(nums)-1
        
        while l<r:
            
            value=(nums[l]+nums[r])/2
            if value<min_value:
                min_value=value
            l+=1
            r-=1
        
        return min_value