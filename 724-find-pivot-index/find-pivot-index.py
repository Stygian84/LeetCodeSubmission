class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        right_sum=sum(nums)
        if len(nums)==1:
            return 0
        res=-1
        for i in range(len(nums)):
            right_sum-=nums[i]
            if left_sum==right_sum:
                res=i
                break
            left_sum+=nums[i]
        return res