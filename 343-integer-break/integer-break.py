class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        else:
            return 3 ** (n // 3) * 2
        
        '''dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        
        return dp[n]'''
    '''
    2 1 1x1
    3 2 2x1
    4 4 2x2
    5 6 3x2
    6 9 3x3
    7 12 3x2x2
    8 18 3x3x2
    9 27 3x3x3
    10 36 4x3x3
    11 54 4x4x3
    12 81 3x3x3x3
    13 108 4x3x3x3
    14 162 2x3x3x3x3x3
    '''