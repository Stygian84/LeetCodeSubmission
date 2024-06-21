class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dc=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dc[i+j]+=[(j,mat[i][j])]
                
        
        res=[]
        odd=True
        for key,value in dc.items():
            ls=value
            if odd:
                ls.sort()
            else:
                ls.sort(reverse=True)
            for item in ls:
                res.append(item[-1])
            odd = not odd
            
        return res