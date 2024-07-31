class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        n,m=len(grid),len(grid[0])
        res = 0
        def backtrack(x,y,path,visited,total):
            nonlocal res
            visited.add((x,y))
            res=max(res,total)

            for dx,dy in direction:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited and grid[nx][ny]!=0:
                    path.append((nx,ny))
                    visited.add((nx,ny))
                    backtrack(nx,ny,path,visited,total+grid[nx][ny])
                    visited.remove((nx,ny))
                    path.pop()
            return




        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    visited=set()
                    backtrack(i,j,[],visited,grid[i][j])
        return res


        