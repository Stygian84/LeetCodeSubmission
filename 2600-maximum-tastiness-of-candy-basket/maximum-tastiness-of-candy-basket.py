class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def isPossible(x):
            count=1
            last_picked = price[0]
            for i in range(1,len(price)):
                if price[i]-last_picked>=x:
                    count+=1
                    last_picked=price[i]
                if count>=k:
                    return True
            return False

        l=0
        r=price[-1]-price[0]
        while l<r:
            mid = (l+r+1)//2
            if isPossible(mid):
                l=mid
            else:
                r=mid-1
        return l