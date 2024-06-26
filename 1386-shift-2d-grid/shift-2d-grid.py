class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        
        nums = [item for row in grid for item in row]
        
        if k > len(nums):
            k=k% len(nums)
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]

        rows=len(grid)
        cols=len(grid[0])
        res = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(nums[i * cols + j])
            res.append(row)
        
        return res