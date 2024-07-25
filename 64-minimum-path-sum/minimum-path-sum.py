class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp = [[0 for _ in range(m)]  for _ in range(n)]
        dp[0][0]=grid[0][0]

        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    continue
                value = grid[i][j]
                if i==0:
                    dp[i][j] = dp[i][j-1] + value
                elif j==0:
                    dp[i][j] = dp[i-1][j] + value
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + value
        
        #print(dp)
        return dp[-1][-1]