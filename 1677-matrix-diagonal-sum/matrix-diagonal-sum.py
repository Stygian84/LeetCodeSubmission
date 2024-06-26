class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=0

        n=len(mat[0])
        for i in range(len(mat)):
            for j in range(n):
                if i==j or i+j==n-1:
                    total+=mat[i][j]
        return total
        '''result=0
        for outer in range(len(mat)):
            for inner in range(len(mat[outer])):
                if outer%2==0 and inner%2==0:
                    result+=mat[outer][inner]
                elif outer%2==1 and inner%2:
                    result+=mat[outer][inner]
        return result'''
        