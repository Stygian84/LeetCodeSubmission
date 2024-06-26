class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        dc=defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dc[i-j].append(grid[i][j])

        res=[row[:] for row in grid]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                arr=dc[i-j]
                idx = i
                if i-j>0:
                    idx-=(i-j)
                left = len(set(arr[:idx]))
                right = len(set(arr[idx+1:]))
                
                res[i][j]=abs(left-right)


        return res