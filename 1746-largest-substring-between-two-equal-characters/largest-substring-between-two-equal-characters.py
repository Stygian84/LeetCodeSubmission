class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dc={}
        for idx in range(len(s)):
            dc[s[idx]]=dc.get(s[idx],[])+[idx]
        result=-1
        for key,values in dc.items():
            if len(values)>=2:
                diff=max(values)-min(values)-1
                if diff>result:
                    result=diff
        return result