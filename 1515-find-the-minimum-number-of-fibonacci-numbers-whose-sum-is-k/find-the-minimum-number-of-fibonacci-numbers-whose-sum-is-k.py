class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]

        while fib[-1]<k:
            fib.append(fib[-1]+fib[-2])
        count=0

        while k>0:
            if fib[-1]<=k:
                k-=fib[-1]
                count+=1
            fib.pop()
            
        return count