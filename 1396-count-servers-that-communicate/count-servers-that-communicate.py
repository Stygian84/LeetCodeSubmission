class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        
        rows = defaultdict(int)
        columns = defaultdict(int)
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    rows[i]+=1
                    columns[j]+=1
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (rows[i]>1 or columns[j]>1):
                    count+=1
        return count


        '''directions = [(0,1),(1,0),(0,-1),(-1,0)]
        n,m = len(grid),len(grid[0])
        seen = set()
        def dfs(x,y):
            seen.add((x,y))
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1 and (nx,ny) not in seen:
                    dfs(nx,ny)

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    dfs(i,j)

        return len(seen)'''