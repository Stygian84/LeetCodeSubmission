class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        n = len(nums)
        m = len(nums[0])
        total = 0
        
        for i in range(n):
            row = nums[i]
            row.sort()

        for i in range(m):
            maximum = 0
            for j in range(n):
                number = nums[j][i]
                if number>maximum:
                    maximum=number

            total+=maximum
        
        return total