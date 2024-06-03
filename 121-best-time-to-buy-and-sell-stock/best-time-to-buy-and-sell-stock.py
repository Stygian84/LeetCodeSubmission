class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_value=math.inf
        for idx in range(len(prices)):
            value= prices[idx]
            if value<=min_value:
                min_value=value
                continue
            profit=max(value-min_value,profit)
        return profit
        '''
        profit=0
        for idx in range(len(prices)):
            value = prices[idx]
            if idx!=len(prices)-1:
                next=max( prices[idx+1:])
                if (value<next) and ((next-value)>profit):
                    profit=next-value
            
        return profit'''