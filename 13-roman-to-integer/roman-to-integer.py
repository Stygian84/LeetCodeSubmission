class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        value=0
        for idx in range(len(s)):
            if  idx<len(s)-1 and(dict1[s[idx+1]]>dict1[s[idx]]) :
                value-=dict1[s[idx]]
            else:
                value+=dict1[s[idx]]   
        return value