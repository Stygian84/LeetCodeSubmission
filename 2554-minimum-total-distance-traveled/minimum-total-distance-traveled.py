class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        #TODO
        # factory = [pos,limit]
        # fix all robot by moving them to nearest factory
        # find min distance
        factory.sort()
        robot.sort()
        
        n = len(robot)
        m = len(factory)
        
        dp = [[math.inf]*(m+1) for _ in range(n+1)]
        
        for j in range(m+1):
            dp[0][j] = 0
            
        for j in range(1,m+1):
            for i in range(1,n+1):
                dp[i][j] = dp[i][j-1]
                dist = 0
                for k in range(1, min(factory[j - 1][1], i) + 1):
                    dist += abs(robot[i-k] - factory[j-1][0])
                    
                    dp[i][j] = min(dp[i][j],dp[i-k][j-1]+dist)
                    
        return dp[n][m]
        