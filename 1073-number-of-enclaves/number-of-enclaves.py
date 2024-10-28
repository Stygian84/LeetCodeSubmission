class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        n,m = len(grid),len(grid[0])


        def dfs(x,y):
            grid[x][y]=2
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                    dfs(nx,ny)
                    grid[nx][ny]=2
        
        for i in range(n):
            if i==0 or i==n-1:
                for j in range(m):
                    if grid[i][j]==1:
                        dfs(i,j)
            else:
                if grid[i][0]==1:
                    dfs(i,0)
                if grid[i][m-1]==1:
                    dfs(i,m-1)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    count+=1
        return count