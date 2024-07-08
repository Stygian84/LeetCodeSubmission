class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(amount):
            total=0
            count=1
            for item in weights:
                total+=item
                if item>amount:
                    return False
                if total>amount:
                    count+=1
                    total=item
                    if count>days:
                        return False
            return True

        l=1
        r=sum(weights)
        if days==1:
            return r
        res=-1
        while l<=r:
            mid = (l+r)//2
            if isPossible(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
