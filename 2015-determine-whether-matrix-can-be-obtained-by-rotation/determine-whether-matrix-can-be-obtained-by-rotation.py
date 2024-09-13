class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(matrix):
            n = len(matrix)
            res = [ [0]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    res[i][j] = matrix[j][n-i-1]
            return res

        for _ in range(4):
            mat = rotate(mat)
            if mat==target:
                return True
        return False
            