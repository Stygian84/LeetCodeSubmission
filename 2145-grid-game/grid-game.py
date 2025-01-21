class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # find prefix sum top and prefix sum bottom
        # cut the middle until both max at top and max bottom is at its lowest

        n = 2
        m = len(grid[0])
        if m==1:
            return 0

        prefix_top = [0]*(m+1)
        prefix_bot = [0]*(m)

        for i in range(m-1,-1,-1):
            prefix_top[i] = prefix_top[i+1]+grid[0][i]
        
        for i in range(m):
            prefix_bot[i] = prefix_bot[i-1]+grid[1][i]
        
        prefix_top.pop()
        

        #minimise top right and bottom left and return the maximum
        res = [] #top,bottom
        for i in range(m):
            if i==0:
                res.append(prefix_top[i+1])
            elif i==m-1:
                res.append(prefix_bot[i-1])
            else:
                res.append(max(prefix_top[i+1], prefix_bot[i-1]))

        return min(res)

