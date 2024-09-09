class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        
        def isGood(a,b,c,m):
            return ((a**b%10)**c)%m == target
        
        res = []

        n = len(variables)

        for i in range(n):
            a,b,c,m = variables[i]
            if isGood(a,b,c,m):
                res.append(i)
        
        return res
