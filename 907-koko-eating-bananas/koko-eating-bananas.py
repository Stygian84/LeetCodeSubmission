class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        low=1
        high=max(piles)
        def canEat(piles,h,banana):
            count=0
            for item in piles:
                count+=item//banana
                if item%banana!=0:
                    count+=1
            return count<=h

        while low<high:
            mid=(low+high)//2
            if canEat(piles,h,mid):
                high=mid
            else:
                low=mid+1
        return low