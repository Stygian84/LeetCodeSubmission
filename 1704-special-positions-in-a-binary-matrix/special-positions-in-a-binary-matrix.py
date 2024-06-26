class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res=0
        dc={}
        rows=defaultdict(int)
        cols=defaultdict(int)



        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    rows[i]+=1
                    cols[j]+=1
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and rows[i]==1 and cols[j]==1:
                    res+=1
        return res