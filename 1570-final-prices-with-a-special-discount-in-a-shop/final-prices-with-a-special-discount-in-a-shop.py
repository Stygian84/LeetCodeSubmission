class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result=[-1]*len(prices)
        for idx in range(len(prices)):
            for i in range(idx+1,len(prices)):
                if prices[i]<=prices[idx]:
                    result[idx]=prices[idx]-prices[i]
                    break
            if result[idx]==-1:
                result[idx]=prices[idx]
        return result
        