class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)
        
        res = 0
        before = None
        for i in range(len(nums)):
            if nums[i]==maximum:
                if before==None:
                    before=i
                else:
                    res = max(res,i-before)
            else:
                before = None
        return res+1