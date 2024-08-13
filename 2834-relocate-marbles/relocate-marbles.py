class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        
        dc = Counter(nums)
        
        i = 0
        n = len(moveFrom)
        while i < n:
            if moveTo[i]!=moveFrom[i]:
                dc[moveTo[i]]=1
                dc[moveFrom[i]]=0
            i+=1

        res = []
        for k,v in dc.items():
            if v>0:
                res.append(k)
        
        res.sort()
        return res
        

