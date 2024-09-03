class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        
        buy=[] #max heap
        sell=[] #min heap
        total = 0
        for price,amount,order in orders:
            if order==0:#buy
                if sell:
                    
                    while sell and sell[0][0]<=price:
                        sell_price,sell_amount = heapq.heappop(sell)
                        if amount<sell_amount:
                            heapq.heappush(sell,(sell_price,sell_amount-amount))
                            amount=0
                            break
                        elif amount>sell_amount:
                            amount-=sell_amount
                        else:
                            amount=0
                            break
                
                if amount>0:
                    heapq.heappush(buy,(-price,amount))

            else:#sell
                if buy:
                    
                    while buy and -buy[0][0]>=price:
                        buy_price,buy_amount = heapq.heappop(buy)

                        if amount<buy_amount:
                            heapq.heappush(buy,(buy_price,buy_amount-amount))
                            amount=0
                            break
                        elif amount>buy_amount:
                            amount-=buy_amount
                        else:
                            amount=0
                            break
                                
                if amount>0:
                    heapq.heappush(sell,(price,amount))


        curr = 0
        for a,b in buy:
            curr+=b
        for c,d in sell:
            curr+=d
        
        return curr % (10**9+7)