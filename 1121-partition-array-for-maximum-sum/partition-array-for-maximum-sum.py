class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*n
        for i in range(n):
            max_value=arr[i]
            for j in range(1,k+1):
                if i-j+1>=0:
                    max_value=max(arr[i-j+1],max_value) 
                    dp[i] = max(dp[i], (dp[i - j] if i - j >= 0 else 0) + max_value * j)
    

        print(dp)
        return dp[-1]
