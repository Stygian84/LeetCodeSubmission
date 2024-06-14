class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dc={}
        for item in dominoes:
            ls=sorted(item)
            ls=tuple(ls)
            dc[ls]=dc.get(ls,0)+1
        def calc(x):
            return x*(x-1)/2
        total=0
        for value in dc.values():
            total+=calc(value)
        return int(total)