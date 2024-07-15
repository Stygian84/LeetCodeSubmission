class Solution:
    def halveArray(self, nums: List[int]) -> int:
        init_total=sum(nums)
        target = init_total/2

        max_heap=[-num for num in nums]
        heapq.heapify(max_heap)

        total=init_total
        count=0

        while total>target:
            count+=1

            largest = -heapq.heappop(max_heap)
            largest/=2
            total-=largest
            heapq.heappush(max_heap,-largest)

        return count