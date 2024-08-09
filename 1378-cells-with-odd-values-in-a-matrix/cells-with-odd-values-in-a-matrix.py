class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        

        matrix = [[0]*n for _ in range(m)]
        
        count = 0

        for r,c in indices:

            for i in range(m):    
                for j in range(n):
                    if i==r:
                        matrix[i][j]+=1
                    if j==c:
                        matrix[i][j]+=1
                        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]%2==1:
                    count+=1

        return count
                