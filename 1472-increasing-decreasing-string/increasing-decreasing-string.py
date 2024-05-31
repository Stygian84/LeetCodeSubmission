class Solution:
    def sortString(self, s: str) -> str:
        dc={}
        for item in s:
            dc[item]=dc.get(item,0)+1
        letter=[]
        for key in dc.keys():
            letter.append(key)
        letter.sort()

        res=""
        while any(value > 0 for value in dc.values()):
            for item in letter:
                if dc.get(item,0)>0:
                    res+=item
                    dc[item]-=1

            for item in letter[::-1]:
                if dc.get(item,0)>0:
                    res+=item
                    dc[item]-=1
            
        return res
        