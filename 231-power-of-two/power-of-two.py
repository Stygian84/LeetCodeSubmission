class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        
        while n!=1 and n>=2:
            n/=2
        if n==1 or n==2:
            return True
        return False
        