class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res=0
        if left:
            res=max(left)
        if right:
            res=max(res,n-min(right))
        return res
        