class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dc={}
        counter=0
        for item in arr:
            dc[item]=dc.get(item,0)+1
        for key,values in dc.items():
            if values==1:
                counter+=1
                if counter==k:
                    return key
        return ""
        '''
        counter=0
        for item in arr:
            if arr.count(item) ==1:
                counter+=1
                if counter==k:
                    return item
        return ""
        '''