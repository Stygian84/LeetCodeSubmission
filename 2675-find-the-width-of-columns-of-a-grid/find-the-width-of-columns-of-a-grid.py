class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res=[]

        for j in range(len(grid[0])):
            max_length=0
            for i in range(len(grid)):
                num=grid[i][j]
                length=len(str(num))
                if length>max_length:
                    max_length=length
            res.append(max_length)
        return res