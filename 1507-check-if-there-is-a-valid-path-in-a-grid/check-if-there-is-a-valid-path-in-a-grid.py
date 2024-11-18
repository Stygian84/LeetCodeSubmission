class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        #row , col
        left,right,upper,lower = (0,-1),(0,1),(-1,0),(1,0)
        directions = [[left,right],
                        [upper,lower],
                        [left,lower],
                        [right,lower],
                        [left,upper],
                        [right,upper]]
        
        n,m = len(grid),len(grid[0])
        res = False
        
        seen = set()

        def dfs(row,col):
            nonlocal res,seen    
            seen.add((row,col))
            if row == n-1 and col == m-1:
                res = True
                return
            if res:
                return
            # check if current row,col value in grid[row][col] can connect to next grid[nx][ny] 
            current = grid[row][col]-1

            for direction in directions[current]:
                dx,dy = direction
                nx,ny = row+dx, col+dy
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in seen and (dx*(-1),dy*(-1)) in directions[grid[nx][ny]-1]:
                    dfs(nx,ny)
        
        dfs(0,0)

        return res