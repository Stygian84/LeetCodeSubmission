class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(k):
            count=0
            for item in quantities:
                count+=math.ceil(item/k)
            return count<=n
        low=0
        high=max(quantities)
        while low<high:
            mid=(low+high)//2
            if mid!=0 and canDistribute(mid):
                high=mid
            else:
                low=mid+1
        return low
        
        