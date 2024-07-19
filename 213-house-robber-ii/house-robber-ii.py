class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        
        def robbing(nums):
            dp=[0]*n

            dp[0]=nums[0]
            dp[1]=max(dp[0],nums[1])

            for i in range(2,n):
                if i==n-1:
                    dp[i]=dp[i-1]
                else:
                    dp[i]=max(dp[i-2]+nums[i],dp[i-1])

            return dp[n-1]
        return max(robbing(nums),robbing(nums[::-1]))