class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ls=s.split("0")
        res=[]
        for item in ls:
            if item:
                res.append(item)
        return len(res)==1