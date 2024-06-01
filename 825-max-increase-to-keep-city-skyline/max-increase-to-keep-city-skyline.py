class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total=0
        max_col_dc={}
        for i in range(len(grid)):
            cols=[]
            for j in range(len(grid[i])):
                cols.append(grid[j][i])
            max_col=max(cols)
            max_col_dc[i]=max_col

        for i in range(len(grid)):
            max_row=max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j]<min(max_row,max_col_dc[j]):
                    total+=min(max_row,max_col_dc[j])-grid[i][j]
        return total