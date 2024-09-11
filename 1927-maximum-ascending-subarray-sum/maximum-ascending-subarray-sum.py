class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res = 0
        total = 0
        for i in range(len(nums)-1):
            total+=nums[i]
            if nums[i+1]<=nums[i]:
                res = max(res,total)
                total = 0
        if nums[-1]>nums[-2]:
            total+=nums[-1]
            res = max(res,total)
        return res