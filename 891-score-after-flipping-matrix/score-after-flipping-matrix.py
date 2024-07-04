class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n=len(grid) #3
        m=len(grid[0]) #4
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1-row[i]
        
        res = []
        column = []
        for i in range(m):
            column = []
            zero_count = 0

            for j in range(n):
                column.append(grid[j][i])
                if grid[j][i]==0:
                    zero_count += 1
                    
            if zero_count > n-zero_count: #flip
                for k in range(len(column)):
                    column[k]=1-column[k]

            res.append(column)

        total = 0
        for i in range(m):
            total += sum(res[i]) * 2**(m-i-1)

        
        
        return total
