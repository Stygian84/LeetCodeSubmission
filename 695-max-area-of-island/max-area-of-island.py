class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        max_area=0
        area=0
        def dfs(x,y):
            nonlocal area
            if (x,y) in visited:
                return
            visited.add((x,y))
            area+=1

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                    dfs(nx,ny)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    dfs(i,j)
                    max_area=max(area,max_area)
                    area=0
        return max_area