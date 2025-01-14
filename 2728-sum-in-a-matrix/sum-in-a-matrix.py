class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        matrix = []

        for row in nums:
            matrix.append(sorted(row))
        
        total = 0
        for j in range(len(matrix[0])):
            maximum = -1
            for i in range(len(matrix)):
                maximum = max(maximum,matrix[i][j])
            total+=maximum
        
        return total