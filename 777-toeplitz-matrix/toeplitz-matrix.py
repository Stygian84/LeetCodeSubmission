class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dc={}
        

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                idx=i-j
                if idx not in dc:
                    dc[idx]=matrix[i][j]
                else:
                    if matrix[i][j] != dc[idx]:
                        return False
        return True