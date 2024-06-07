class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices)==0:
            return 0
        total_profit = 0

        current_price=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<current_price:
                current_price=prices[i]
            elif prices[i]>current_price and prices[i]-current_price>fee:
                total_profit+=prices[i]-current_price-fee
                current_price=prices[i]-fee
        return total_profit