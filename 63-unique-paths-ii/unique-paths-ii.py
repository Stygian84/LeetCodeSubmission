class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        grid=[ [0]*n for _ in range(m)]
            
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        grid[0][0]=1

        for i in range(1,n):
            if obstacleGrid[0][i]==0 :
                grid[0][i]=grid[0][i-1]
        for i in range(1,m):
            if obstacleGrid[i][0]==0 :
                grid[i][0]=grid[i-1][0]
                
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    grid[i][j]=0
                else:
                    grid[i][j]=grid[i][j-1]+grid[i-1][j]
        return grid[m-1][n-1]