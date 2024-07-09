class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dc={}
        for item in arr:
            dc[item]=dc.get(item,0)+1
        
        sorted_dict = dict(sorted(dc.items(), key=lambda item: item[1]))

        n=len(sorted_dict)
        count=0
        for values in sorted_dict.values():
            if values<=k:
                k-=values
                count+=1
            else:
                return n-count
        return n-count