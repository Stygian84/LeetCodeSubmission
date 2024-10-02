class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        initial = bottom

        res = 0
        for s in special:
            res = max(res,s-initial)
            initial=s+1
        res = max(res,top-initial+1)
        return res