class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        prefix_sum = [0]*n

        for i in range(n):
            prefix_sum[i] = prefix_sum[i-1]+nums[i]


        for i in range(n):
            if i-nums[i]>0:
                total += prefix_sum[i]-prefix_sum[i-nums[i]-1]
            else:
                total += prefix_sum[i]
                
        return total