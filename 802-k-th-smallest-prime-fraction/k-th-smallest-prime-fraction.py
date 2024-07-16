class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        dc={}
        n=len(arr)
        ls=[]
        for i in range(n-1):
            for j in range(i+1,n):
                fraction=arr[i]/arr[j]
                dc[fraction]=[arr[i],arr[j]]
                heapq.heappush(ls,fraction)
        
        value=None
        for i in range(k):
            value=heapq.heappop(ls)
        
        return dc[value]