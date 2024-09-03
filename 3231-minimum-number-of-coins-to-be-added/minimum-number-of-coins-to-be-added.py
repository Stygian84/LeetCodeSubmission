class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        
        coins.sort()
        fill=1
        count=0
        i=0

        while fill<=target:
            if i<len(coins):
                if coins[i]<=fill:
                    fill+=coins[i]
                    i+=1
                else:
                    fill+=fill
                    count+=1
            else:
                fill+=fill
                count+=1
        
        return count
