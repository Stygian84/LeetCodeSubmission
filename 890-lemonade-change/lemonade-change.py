class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for money in bills:
            if money == 5:
                change[5]+=1

            elif money == 10:
                if change[5]>0:
                    change[5]-=1
                    change[10]+=1
                else:
                    return False

            else:
                #return 15
                if change[10]>=1 and change[5]>=1:
                    change[10]-=1
                    change[5]-=1

                elif change[5]>=3:
                    change[5]-=3

                else:
                    return False

        return True

        '''dc={}
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
        return True'''
        