class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res=[]

        dc={}
        for a,b,c in zip(indices,sources,targets):
            if a in dc:
                #check which one is valid
                source1=dc[a][0]
                n=len(source1)
                if s[a:a+n]!=source1:
                    dc[a]=[b,c]
            
            else:
                dc[a]=[b,c]
        print(dc)
        skip=0
        for i in range(len(s)):
            
            if skip>0:
                skip-=1
                continue

            if i in dc:
                n=len(dc[i][0])
                
                if s[i:i+n]==dc[i][0]:
                    res.append(dc[i][1])
                    skip=n-1
                else:
                    res.append(s[i])
            else:
                res.append(s[i])
        
        return "".join(res)