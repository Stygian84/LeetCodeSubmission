class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result=[]
        dc={}
        for i in range(len(s)):
            if s[i]==c:
                dc[i]=0
        for idx in range(len(s)):
            min_value=math.inf
            for key in dc.keys():
                value=abs(idx-key)
                if value<min_value:
                    min_value=value
            result.append(min_value)
        return result