class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        #-1 not marked(unguarded), 0 walls, 1 guarded, 2 guard
        matrix = [[-1]*n for _ in range(m)]
        #print(matrix)

        for r,c in walls:
            matrix[r][c]=0
        for r,c in guards:
            matrix[r][c]=2
        
        for r,c in guards:
            #up
            x,y = r-1,c
            while x>=0 and matrix[x][y]!=0 and matrix[x][y]!=2:
                matrix[x][y]=1
                x-=1
            
            #down
            x,y = r+1,c
            while x<m and matrix[x][y]!=0 and matrix[x][y]!=2:
                matrix[x][y]=1
                x+=1

            #right
            x,y = r,c+1
            while y<n and matrix[x][y]!=0 and matrix[x][y]!=2:
                matrix[x][y]=1
                y+=1
            
            #left
            x,y = r,c-1
            while y>=0 and matrix[x][y]!=0 and matrix[x][y]!=2:
                matrix[x][y]=1
                y-=1


        count=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==-1:
                    count+=1
        return count