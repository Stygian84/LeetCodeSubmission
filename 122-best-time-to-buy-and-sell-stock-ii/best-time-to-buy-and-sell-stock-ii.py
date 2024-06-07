class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices[:]=prices[::-1]
        profit=0
        total_profit=0
        current_price=-1
        prev_max_profit=0

        for i in range(len(prices)):
            if prices[i]>current_price:
                current_price=prices[i]
            else:
                profit=current_price-prices[i]
                if prev_max_profit==0:
                    prev_max_profit=profit
                if profit>prev_max_profit:
                    continue
                else:
                    total_profit+=profit
                    prev_max_profit=0
                    current_price=prices[i]

        return total_profit