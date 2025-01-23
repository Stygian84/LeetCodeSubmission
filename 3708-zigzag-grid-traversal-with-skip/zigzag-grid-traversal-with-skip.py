class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        #move to most right
        #drop to next row
        #move to most left


        res = []

        n = len(grid)
        m = len(grid[0])

        skip = False

        for i in range(n):   
            if i%2==0: #right
                for j in range(m):
                    if skip:
                        skip = False
                        continue
                    res.append(grid[i][j])
                    skip = True
            else:
                for j in range(m-1,-1,-1):
                    if skip:
                        skip = False
                        continue
                    res.append(grid[i][j])
                    skip = True
        return res