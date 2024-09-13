class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        area_row = 0
        area_col = 0
        top = n*n

        for i in range(n):
            row = grid[i]
            area_row += max(row)
            col = []
            for j in range(n):
                col.append(grid[j][i])
                if grid[i][j]==0:
                    top-=1
            area_col += max(col)
        
        return area_row+area_col+top