class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res=[]
        d=len(s)
        i=0
        for item in s:
            if item=="I":
                res.append(i)
                i+=1
            else:
                res.append(d)
                d-=1
        res.append(d)
        return res        