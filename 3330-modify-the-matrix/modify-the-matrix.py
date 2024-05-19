class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ls=[]
        for i in range(len(matrix[0])):
            temp_ls=[0]*len(matrix)
            ls.append(temp_ls)
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                ls[i][j]=matrix[j][i]
        dc={}
        for idx in range(len(ls)):
            dc[idx]=max(ls[idx])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==-1:
                    matrix[i][j]=dc[j]

        return matrix