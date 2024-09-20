class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        dp = [True] * (n+1)
        dp[0]=False
        dp[1]=False

        for i in range(2,int(n**0.5)+1):
            if dp[i]:
                for j in range(i*i,n+1,i):
                    dp[j]=False
        
        return dp[:-1].count(True)