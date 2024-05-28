class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n<1:
            return False
        while n>4:
            n/=4
            print(n)
        if n==1 or n==4:
            return True
        return False

        