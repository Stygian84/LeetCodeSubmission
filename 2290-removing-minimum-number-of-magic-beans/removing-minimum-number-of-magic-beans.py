class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        beans.sort()
        n= len(beans)
        total = sum(beans)
        res = math.inf
        
        for i in range(n):
            removal = total - beans[i] * (n - i)
            res = min(res,removal)
        
        return res