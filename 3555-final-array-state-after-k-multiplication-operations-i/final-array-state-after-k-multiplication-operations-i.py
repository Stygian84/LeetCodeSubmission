class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        
        for _ in range(k):
            x,i = heapq.heappop(heap)    
            x*=multiplier
            heapq.heappush(heap,(x,i))
        
        res = [0]*len(nums)

        for x,i in heap:
            res[i]=x
        return res
        