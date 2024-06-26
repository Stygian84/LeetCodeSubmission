class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows={}
        columns={}

        if not matrix:
            return
        
        m,n=len(matrix),len(matrix[0])
        i,j=0,0

        while i<m and j<n:
            if matrix[i][j] == 0:
                rows[i]=0
                columns[j]=0
            if j<n-1:
                j+=1
            else:
                i+=1
                j=0
        
        i,j=0,0
        while i<m and j<n:
            if i in rows:
                matrix[i][j]=0
            if j in columns:
                matrix[i][j]=0
            if j<n-1:
                j+=1
            else:
                i+=1
                j=0
        
        