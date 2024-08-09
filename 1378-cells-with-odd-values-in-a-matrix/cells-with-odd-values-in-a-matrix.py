class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        

        matrix = [[0]*n for _ in range(m)]
        
        x = len(indices)
        last = False
        count = 0

        for idx in range(x):
            r,c = indices[idx]
            if idx == x-1:
                last = True

            for i in range(m):    
                for j in range(n):
                    if i==r:
                        matrix[i][j]+=1
                    if j==c:
                        matrix[i][j]+=1
                    if last:
                        if matrix[i][j]%2==1:
                            count+=1

        return count
                