class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        def diagonal(a,b):
            return a*a+b*b
        
        res = 0
        maximumDiagonal = -1
        for a,b in dimensions:
            d = diagonal(a,b)
            if d > maximumDiagonal:
                maximumDiagonal = d
                res = a*b
            elif d == maximumDiagonal:
                res = max(a*b,res)
        
        return res