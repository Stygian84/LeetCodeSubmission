class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
    
        max_global=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            if dp[i]>max_global:
                max_global=dp[i]
        return max_global