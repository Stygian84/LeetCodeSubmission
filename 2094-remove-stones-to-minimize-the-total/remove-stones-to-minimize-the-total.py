class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-num for num in piles]
        heapq.heapify(max_heap)
        total=sum(piles)

        for _ in range(k):
            biggest = -heapq.heappop(max_heap)
            new_value = biggest-biggest//2
            total -= biggest-new_value
            heapq.heappush(max_heap,-new_value)
            
        return total
        
