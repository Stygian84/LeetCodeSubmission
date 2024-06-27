class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res=nums[0]
        sorted_num=sorted(nums[1:])

        return res+sorted_num[0]+sorted_num[1]