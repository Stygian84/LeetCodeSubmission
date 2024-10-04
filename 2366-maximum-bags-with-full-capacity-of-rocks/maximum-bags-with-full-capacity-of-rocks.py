class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ls = []
        for c,r in zip(capacity,rocks):
            ls.append(c-r)
        
        ls.sort()
        
        res = 0
        for diff in ls:
            if diff>0:
                additionalRocks-=diff
            if additionalRocks<0:
                break
            res+=1
        return res
