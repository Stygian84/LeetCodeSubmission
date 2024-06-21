class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        cols=[]
        
        for i in range(len(matrix[0])):
            col=[]
            for j in range(len(matrix)):
                col.append(matrix[j][i])
            cols.append(col)
        
        max_cols={}
        min_rows={}
        for i in range(len(cols)):
            max_cols[i]=max(cols[i])
        for j in range(len(matrix)):
            min_rows[j]=min(matrix[j])

        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==max_cols[j] and matrix[i][j]==min_rows[i]:
                    res.append(matrix[i][j])
        return res