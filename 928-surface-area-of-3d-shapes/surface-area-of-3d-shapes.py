class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        total=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    total+=2
                        
                    for dx,dy in direction:
                        ni, nj = i + dx, j + dy

                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                            neighbor_height = grid[ni][nj]
                        else:
                            neighbor_height = 0

                        total += max(grid[i][j] - neighbor_height, 0)

        return total