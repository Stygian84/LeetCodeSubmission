class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        n=len(cuts)
        dp = [ [0]*n for _ in range(n)]
        print(dp)
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (cuts[j] - cuts[i]))
        
        return dp[0][n - 1]