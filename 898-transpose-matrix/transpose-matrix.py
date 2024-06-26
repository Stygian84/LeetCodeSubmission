class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])

        res=[[0 for _ in range(n)] for _ in range(m)] 
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i]=matrix[i][j]
        
        return res