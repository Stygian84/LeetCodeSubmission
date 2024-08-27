class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
        def minFlip(line):
            n = len(line)
            flips = 0
            for i in range(n//2):
                if line[i] != line[n-i-1]:
                    flips+=1
            return flips
        
        totalRow = 0 
        for row in grid:
            totalRow+=minFlip(row)
        
        total=0
        m = len(grid)
        n = len(grid[0])
        for j in range(n):
            col = [grid[i][j] for i in range(m)]
            total+=minFlip(col)
        return min(total,totalRow)
    
        '''n = len(grid)
        m = len(grid[0])

        count = 0

        for i in range(n//2):
            for j in range(m//2):
                top_left = grid[i][j]
                top_right = grid[i][m - j - 1]
                bottom_left = grid[n - i - 1][j]
                bottom_right = grid[n - i - 1][m - j - 1]

                vals = [top_left, top_right, bottom_left, bottom_right]
                max_freq = max(vals.count(0), vals.count(1))
                
                count += 4 - max_freq
        
        return count'''