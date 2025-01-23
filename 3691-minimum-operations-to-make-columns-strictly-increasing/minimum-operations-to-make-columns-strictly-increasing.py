class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        total = 0
        for j in range(m):
            for i in range(1,n):
                if grid[i][j]<=grid[i-1][j]:
                    diff = grid[i-1][j]+1-grid[i][j]
                    total += diff
                    grid[i][j] = grid[i-1][j]+1
        
        return total