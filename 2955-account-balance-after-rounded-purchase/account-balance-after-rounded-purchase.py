class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        min_ten=math.inf
        result=0
        for i in range(0,110,10):
            difference=abs(purchaseAmount-i)
            if difference<=min_ten:
                min_ten=difference
                result=i
        return 100-result
        