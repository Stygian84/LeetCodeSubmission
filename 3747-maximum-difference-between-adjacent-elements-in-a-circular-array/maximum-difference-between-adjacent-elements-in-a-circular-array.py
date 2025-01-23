class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0
        for i in range(n):
            res = max(abs(nums[i]-nums[i-1]),res)
        
        return res