class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        # abcd abdc adbc dabc
        # if grid[i][i+1:]!=[0]*(n-1-i)
        for i in range(n):
            if grid[i][i+1:]!=[0]*(n-1-i): #invalid
                #find grid
                j = i
                while grid[j][i+1:]!=[0]*(n-i-1):
                    j+=1
                    if j>=n:
                        return -1
                for idx in range(j,i,-1):
                    grid[idx],grid[idx-1] = grid[idx-1],grid[idx]
                    count+=1
                    #print(count,grid,i)
        return count