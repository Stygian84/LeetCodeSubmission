class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
    
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                max_stones = 0
                for x in range(1, min(2 * m, n - i) + 1):
                    if i + x < n:
                        max_stones = max(max_stones, suffix_sum[i] - dp[i + x][max(m, x)])
                    else:
                        max_stones = max(max_stones, suffix_sum[i])
                dp[i][m] = max_stones
        
        return dp[0][1]