class Solution:
    def numTilings(self, n: int) -> int:
        dp=[-1]*(n+1)
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5
        if n==4:
            return 11
        dp[0]=1
        dp[1]=2
        dp[2]=5
        dp[3]=11
        for i in range(4,n+1):
            dp[i]=dp[i-1]-dp[i-2]+dp[i-2]+dp[i-3]+dp[i-1]
        return dp[n-1]%(10**9+7)
        