class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(grid, i, j, n):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 0:
                return
                
            grid[i][j] = 1
            
            dfs(grid, i + 1, j, n)
            dfs(grid, i - 1, j, n)
            dfs(grid, i, j + 1, n)
            dfs(grid, i, j - 1, n)


        n = len(grid)
        expanded_grid = [[0] * (3 * n) for _ in range(3 * n)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded_grid[3 * i][3 * j + 2] = 1
                    expanded_grid[3 * i + 1][3 * j + 1] = 1
                    expanded_grid[3 * i + 2][3 * j] = 1
                elif grid[i][j] == '\\':
                    expanded_grid[3 * i][3 * j] = 1
                    expanded_grid[3 * i + 1][3 * j + 1] = 1
                    expanded_grid[3 * i + 2][3 * j + 2] = 1


        regions = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if expanded_grid[i][j] == 0:
                    dfs(expanded_grid, i, j, 3 * n)
                    regions += 1
                    
        return regions