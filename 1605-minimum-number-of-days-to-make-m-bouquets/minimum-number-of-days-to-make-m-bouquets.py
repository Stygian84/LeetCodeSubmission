class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        n=len(bloomDay)
        if m*k>n:
            return -1
        
        def isFeasible(day):
            count=0
            i=0
            total=0
            while i<n:
                if bloomDay[i]<=day:
                    i+=1
                    count+=1
                    if count>=k:
                        total+=1
                        count=0
                        if total==m:
                            return True
                        continue
                else:
                    i+=1
                    count=0
            return False
        low=1
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            if isFeasible(mid):
                high=mid-1
            else:
                low=mid+1
        return low