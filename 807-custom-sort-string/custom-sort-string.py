class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dc={}
        for item in s:
            dc[item]=dc.get(item,0)+1
        s=""
        for item in order:
            s+=item*dc.get(item,0)
            dc[item]=0
        for key,values in dc.items():
            if values>0:
                s+=key*values
                dc[key]=0
        return s