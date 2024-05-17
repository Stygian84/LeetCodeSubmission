class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for idx in range(len(grid[0])-1):
            if grid[0][idx]==grid[0][idx+1]:
                return False
        for idx in range(len(grid)-1):
            if grid[idx]!=grid[idx+1]:
                return False
        return True