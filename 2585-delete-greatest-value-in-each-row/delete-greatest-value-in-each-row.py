class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        count=0
        while len(grid[0])>0:
            ls=[]
            for item in grid:
                ls.append(max(item))
                item.remove(max(item))
            count+=max(ls)
        
        return count