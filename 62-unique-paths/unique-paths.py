class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #mxn
        temp_ls=[0]*m
        dp=[]
        for _ in range(n):
            dp.append(temp_ls)
        dp[0][0]=0

        for i in range(n):
            dp[i][0]=1
        for i in range(m):
            dp[0][i]=1

            
        for x in range(1,n):
            for y in range(1,m):
                dp[x][y]=dp[x][y-1]+dp[x-1][y]

        return dp[n-1][m-1]

    
