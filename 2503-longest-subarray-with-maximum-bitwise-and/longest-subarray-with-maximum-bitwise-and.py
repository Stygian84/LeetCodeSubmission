class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maximum = max(nums)
        if freq[maximum]==1:
            return 1
        
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