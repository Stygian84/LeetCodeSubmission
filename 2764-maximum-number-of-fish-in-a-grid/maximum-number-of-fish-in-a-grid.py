class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        n = len(grid)
        m = len(grid[0])
        res = 0

        def bfs(start):
            queue = deque([start])
            total = 0
            seen = set()
            seen.add(start)

            while queue:
                x,y = queue.popleft()
                total += grid[x][y]

                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m and (nx,ny) not in seen and grid[nx][ny]!=0:
                        queue.append((nx,ny))
                        seen.add((nx,ny))
            return total

        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    result = bfs((i,j))
                    if result>res:
                        res = result
        return res