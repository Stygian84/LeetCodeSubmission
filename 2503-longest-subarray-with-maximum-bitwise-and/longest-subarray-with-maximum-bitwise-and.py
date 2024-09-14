class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)
        
        res = 0
        current = 0

        for num in nums:
            if num==maximum:
                current+=1
                if current>res:
                    res = current
            else:
                current=0
        return res