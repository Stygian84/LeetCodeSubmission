class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        count = 0
        while n>=1:
            n//=5
            count+=n
        
        return count