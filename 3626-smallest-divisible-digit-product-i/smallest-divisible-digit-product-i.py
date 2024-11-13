class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def checkProduct(num:int):
            res = 1
            for digit in str(num):
                res*=int(digit)
            return res

        for i in range(n,n+11,1):
            x = checkProduct(i)
            if x%t == 0 :
                return i