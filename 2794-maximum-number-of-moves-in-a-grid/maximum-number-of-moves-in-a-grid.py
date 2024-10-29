class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0]*m for _ in range(n)]
        
        #start from behind
        directions = [(-1,1),(0,1),(1,1)]

        for y in range(m-2,-1,-1):
            for x in range(n): 
                
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy

                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]>grid[x][y]:
                        dp[x][y] = max(dp[x][y],dp[nx][ny]+1)
        
        return max(dp[i][0] for i in range(n))
                


        '''directions = [(-1,1),(0,1),(1,1)]
        n,m = len(grid),len(grid[0])
        res = 0


        def dfs(x,y,count):
            nonlocal res
            if count>res:
                res=count

            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]>grid[x][y]:
                    dfs(nx,ny,count+1) 

        for i in range(n):
            dfs(i,0,0)
        return res'''