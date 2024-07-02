class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()

        res=math.inf
        for i in range(len(nums)-1):
            res=min(nums[i+1]-nums[i],res)
        
        return res