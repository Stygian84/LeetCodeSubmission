class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        count = 0
        while len(nums)>=2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x>=k:
                return count
            
            count+=1

            new = 2*x + y
            heapq.heappush(nums,new)
        
        return count