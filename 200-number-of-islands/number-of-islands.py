class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs_grid(grid, x, y,visited):
            if (x, y) in visited:
                return
            visited.add((x, y))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                    dfs_grid(grid, nx, ny, visited)
            return 

        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1") and ((i, j) not in visited):
                    dfs_grid(grid, i, j, visited)
                    count += 1
        return count