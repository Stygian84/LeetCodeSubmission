class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        start, end = None, None
        empty = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] != -1:
                    empty += 1

        def dfs(x, y, count):
            if (x, y) == end:
                return count == empty
            
            temp, grid[x][y] = grid[x][y], -1
            paths = 0
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != -1:
                    paths += dfs(nx, ny, count + 1)
            
            grid[x][y] = temp
            return paths

        return dfs(start[0], start[1], 1)
    