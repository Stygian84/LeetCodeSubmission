class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum(nums)
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))

        seen = set()

        res = []
        for a,b in queries:
            if total>0:
                if a not in seen:
                    total-=nums[a]
                    seen.add(a)
                
                for _ in range(b):
                    if heap:
                        value,idx = heapq.heappop(heap)
                        while heap and idx in seen:
                            value,idx = heapq.heappop(heap)
                        if not heap and idx in seen:
                            total=0
                            break
                        seen.add(idx)
                        total-=value
                    else:
                        total = 0
                        break

            else:
                total=0        

            res.append(total)
    
        return  res