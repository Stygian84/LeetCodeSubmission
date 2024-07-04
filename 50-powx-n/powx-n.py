class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==0:
            return 1.0
        if x==0.0 or x==1.0:
            return x

        if n<0:
            x=1/x
            n*=-1

        result = 1
        base = x

        while n > 0:
            if n % 2 == 1:   
                result *= base
            base *= base      
            n //= 2

        return result
