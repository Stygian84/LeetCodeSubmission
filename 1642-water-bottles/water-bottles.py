class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total=numBottles
        current=numBottles
        empty=current
        while empty>=numExchange:
            current=(empty)//numExchange
            empty=current+empty%numExchange
            total+=current
        return total
        
            