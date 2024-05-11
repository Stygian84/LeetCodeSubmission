class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum1=0
        for i in range(1,n):
            sum1+=i
            if n-sum1<=i:
                return i
        return 1

        