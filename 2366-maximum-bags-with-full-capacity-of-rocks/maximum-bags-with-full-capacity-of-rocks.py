class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ls = []
        for c,r in zip(capacity,rocks):
            ls.append((c,r))
        
        ls.sort(key = lambda x:x[0]-x[1])
        
        res = 0
        for c,r in ls:
            diff = c-r
            if diff>0:
                additionalRocks-=diff
            if additionalRocks<0:
                break
            res+=1
        return res
