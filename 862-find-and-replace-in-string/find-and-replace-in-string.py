class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res=[]

        dc={}
        for a,b,c in zip(indices,sources,targets):
            n=len(b)
            if s[a:a+n]==b: #check if valid
                dc[a]=[b,c]
            
        skip=0
        for i in range(len(s)):
            
            if skip>0:
                skip-=1
                continue

            if i in dc:
                n=len(dc[i][0])
                res.append(dc[i][1])
                skip=n-1

            else:
                res.append(s[i])
        
        return "".join(res)