class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def countPrimes(n):
            if n<2:
                return 0
            dp = [True] * (n+1)
            dp[0]=False
            dp[1]=False

            for i in range(2,int(n**0.5)+1):
                if dp[i]:
                    for j in range(i*i, n+1, i):
                        dp[j] = False
            
            return dp.count(True)
        
        count = countPrimes(n)
        return (math.factorial(count)*math.factorial(n-count)) % (10**9+7)