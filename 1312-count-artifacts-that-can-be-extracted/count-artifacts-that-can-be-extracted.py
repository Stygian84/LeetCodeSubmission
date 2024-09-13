class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
        count = 0
        matrix = [ [0]*n for _ in range(n)]

        #mark dig spots
        for x,y in dig:
            matrix[x][y]=1


        for r1,c1,r2,c2 in artifacts:
            
            flag = True
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    if matrix[i][j]!=1:
                        flag=False
                        break
            if flag:
                count+=1
        
        return count