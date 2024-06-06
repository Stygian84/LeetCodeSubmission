class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize==1:
            return True
        hand.sort()
        dc={}
        for item in hand:
            dc[item]=dc.get(item,0)+1
        
        for key,values in dc.items():
            if values>0:
                for i in range(groupSize):
                    try:
                        dc[key+i]-=values
                        if dc[key+i]<0:
                            return False
                    except:
                        return False
        
        if (all(value==0 for value in dc.values())):
            return True
        return False