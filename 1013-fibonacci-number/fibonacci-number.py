class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n<=2:
            return 1
        sum1=1
        sum2=1
        result=0
        for i in range(2,n):
            result=sum1+sum2
            sum1=sum2
            sum2=result
        return result
        