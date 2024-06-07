class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        n=len(prices)
        current = [0]*n
        profit=[0]*n
        cd=[0]*n
        current[0]=-prices[0]
        
        for i in range(1,n):
            current[i]=max(current[i-1],cd[i-1]-prices[i])
            profit[i]=current[i-1]+prices[i]
            cd[i]=max(profit[i-1],cd[i-1])
            #print(current,profit,cd)
        return max(profit[-1], cd[-1])
        