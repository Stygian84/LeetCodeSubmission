class Solution:
    def smallestNumber(self, n: int) -> int:
        
        res = 0
        i = 0
        while res<n:
            res += 2**i
            i += 1
        return res