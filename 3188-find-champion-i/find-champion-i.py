class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for idx in range(len(grid)):
            if grid[idx].count(0)==1:
                return idx
        