class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #TODO
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m) for _ in range(n)]
        res = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==1:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    res += dp[i][j]
        return res
