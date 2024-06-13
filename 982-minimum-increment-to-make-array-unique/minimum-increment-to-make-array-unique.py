class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        count=0
        for idx in range(1,len(nums)):
            if nums[idx]>nums[idx-1]:
                continue
            else:
                original=nums[idx]
                nums[idx]=nums[idx-1]+1
                count+=(nums[idx]-original)
        return count        
        