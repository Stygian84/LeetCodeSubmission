class Solution:
    def halveArray(self, nums: List[int]) -> int:
        init_total=sum(nums)
        
        count=0
        total=init_total

        max_heap=[]
        for num in nums:
            heapq.heappush(max_heap,-num)

        while total>init_total/2:
            count+=1

            largest = -heapq.heappop(max_heap)
            largest/=2
            total-=largest
            heapq.heappush(max_heap,-largest)

        return count