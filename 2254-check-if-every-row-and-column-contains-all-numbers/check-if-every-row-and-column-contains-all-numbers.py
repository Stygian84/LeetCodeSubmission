class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def checkRow(ls):
            return len(set(ls))==len(ls)
        for item in matrix:
            result=checkRow(item)
            if result==False:
                return False
        n=len(matrix)
        columns=[]
        for _ in range(n):
            columns.append([0] * n)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                columns[j][i]=matrix[i][j]
        
        for item in columns:
            result=checkRow(item)
            if result==False:
                return False
        return True