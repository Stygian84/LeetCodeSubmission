class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = 0
        empty = 0
        
        while True:
            total+=numBottles
            empty+=numBottles
            numBottles = 0

            if empty-numExchange<0:
                break

            while empty-numExchange>=0:
                numBottles+=1
                empty-=numExchange
                numExchange+=1

            #print(numBottles,empty,numExchange,total)
        return total