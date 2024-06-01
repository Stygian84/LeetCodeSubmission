class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicate = -1
        missing = -1
        
        if nums[0] != 1:
            missing = 1
            
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                duplicate = nums[idx]
            elif nums[idx] != nums[idx - 1] + 1:
                missing = nums[idx - 1] + 1
        
        if missing == -1 and nums[-1] != len(nums):
            missing = len(nums)
        
        return [duplicate, missing]
