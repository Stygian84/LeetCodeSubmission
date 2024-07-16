class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)
        min_heap = []
        
        for j in range(1, n):
            heapq.heappush(min_heap, (arr[0] / arr[j], 0, j))
        for _ in range(k):
            frac, i, j = heapq.heappop(min_heap)
            if i + 1 < j:
                heapq.heappush(min_heap, (arr[i+1] / arr[j], i+1, j))
        
        return [arr[i], arr[j]]
        '''dc={}
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
        
        return dc[value]'''