class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left=len(grid[0])
        right=-len(grid[0])
        top=len(grid)
        bot=-len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    if i<top: top=i
                    if i>bot: bot=i
                    if j>right: right=j
                    if j<left: left=j

        width = right-left+1
        height = bot-top+1

        return width*height
