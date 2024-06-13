class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dc={}
        arr.sort()
        #remove zeroes
        zeroes=arr.count(0)
        if zeroes%2==1:
            return False
        
        for item in arr:
            if item!=0:
                dc[item]=dc.get(item,0)+1

        for key in dc.keys():
            if key<0:    
                if dc[key]>0 and key/2 in dc:
                    dc[key/2]-=dc[key]
                    dc[key]=0
            else:
                if dc[key]>0 and key*2 in dc:
                    dc[key*2]-=dc[key]
                    dc[key]=0
                    
        if all(value==0 for value in dc.values()):
            return True
        return False   