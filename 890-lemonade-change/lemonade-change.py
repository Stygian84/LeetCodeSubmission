class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dc={}
        for item in bills:
            if item ==5:
                dc[item]=dc.get(item,0)+1
                continue
            if item ==10:
                if dc.get(5,0)==0:
                    return False
                else:
                    dc[5]-=1
                    dc[item]=dc.get(item,0)+1
                    continue
            else:
                if dc.get(10,0)>=1:
                    if dc.get(5,0)>=1:
                        dc[10]-=1
                        dc[5]-=1
                        dc[item]=dc.get(item,0)+1
                        continue
                    else:
                        return False
                if dc.get(5,0)>=3:
                    dc[5]-=3
                    dc[item]=dc.get(item,0)+1
                    continue
                else:
                    return False
        return True
        