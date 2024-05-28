class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n<3:
            return False
        while n!=1 and n>=3:
            n/=3
        if n==1 or n==3:
            return True
        return False