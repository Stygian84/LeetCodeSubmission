class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        dc={}
        min_value=math.inf
        min_value2=math.inf
        for item in ops:
            min_value=min(item[0],min_value)
            min_value2=min(item[1],min_value2)

        if min_value==math.inf or min_value2==math.inf:
            return m*n
        return min_value*min_value2