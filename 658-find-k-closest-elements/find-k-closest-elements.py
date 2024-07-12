class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        l,r=0,n-1
        
        start=-1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid+1
            else:
                r = mid
        while l!=0 and abs(arr[l-1]-x)<=abs(arr[l]-x):
            l-=1
        start = l

        l,r=start-1,start+1

        res=deque([arr[start]])
        k-=1
        while k>0:
            if l >= 0 and r < n:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.appendleft(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.appendleft(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1
            
            k-=1
        return res
                