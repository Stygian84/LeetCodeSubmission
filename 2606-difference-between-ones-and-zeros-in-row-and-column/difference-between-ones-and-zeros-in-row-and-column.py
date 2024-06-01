class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = {}
        zerosRow = {}
        onesCol = {}
        zerosCol = {}
        
        n = len(grid)     # number of rows
        m = len(grid[0])  # number of columns
        
        for row_idx in range(n):
            zerosRow[row_idx] = grid[row_idx].count(0)
            onesRow[row_idx] = grid[row_idx].count(1)
        
        for col_idx in range(m):
            cols = []
            for row_idx in range(n):
                cols.append(grid[row_idx][col_idx])
            zerosCol[col_idx] = cols.count(0)
            onesCol[col_idx] = cols.count(1)
        
        diff = [[0] * m for _ in range(n)] 
        for i in range(m):
            for j in range(n):
                diff[j][i]=onesRow[j]+onesCol[i]-zerosRow[j]-zerosCol[i]

        print(zerosCol, onesCol, zerosRow, onesRow)
        return diff