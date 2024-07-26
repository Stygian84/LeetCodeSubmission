class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        count=0
        def dfs(x,y):
            nonlocal count
            if (x,y) in visited:
                return
            visited.add((x,y))

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                    dfs(nx,ny)
                else:
                    count+=1


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dfs(i,j)
                    return count
        return count