class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n=len(position)
        def isFeasible(dist):
            count=1
            last_pos=position[0]
            for i in range(1,n):
                if position[i]-last_pos>=dist:
                    count+=1
                    last_pos=position[i]
                    if count==m:
                        return True
            return False
        
        l=1
        r=position[-1]-position[0]
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if isFeasible(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res
