class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        row = defaultdict(int)
        column = defaultdict(int)

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i]+=1
                    column[j]+=1
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (row[i]>1 or column[j]>1):
                    count+=1
        return count