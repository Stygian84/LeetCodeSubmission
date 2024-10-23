class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        coins = 0

        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        def dfs(l,r):
            if l+1==r:
                return 0
            if dp[l][r]>0:
                return dp[l][r]

            for i in range(l+1,r):
                gain = nums[l]*nums[i]*nums[r]
                dp[l][r] = max(dp[l][r], dfs(l,i) + gain + dfs(i,r))

            return dp[l][r]

        return dfs(0,n-1) 


        ''' def dfs(arr,total):
            nonlocal coins
            if len(arr)<=2:
                coins = max(coins,total)
                return
            
            for i in range(1,len(arr)-1):
                
                new_arr = arr[:i]+arr[i+1:] 
                new_total = total + arr[i-1]*arr[i]*arr[i+1]
                
                dfs(new_arr,new_total)

        dfs(nums,0)
        return coins'''