class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        
        nums.sort()        
        n = len(nums)
        
        start = 0
        end = 0
        count = 0
        
        while end < n:
            if nums[end] > nums[start]:
                count += 1
                start += 1
            end += 1
        
        return count