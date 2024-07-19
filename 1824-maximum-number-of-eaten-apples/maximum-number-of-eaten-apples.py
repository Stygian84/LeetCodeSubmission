class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        i = 0
        min_heap = []
        count = 0
        
        while i < len(apples) or min_heap:
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(min_heap, (i + days[i], apples[i]))
            
            while min_heap and min_heap[0][0] <= i:
                heapq.heappop(min_heap)
            
            if min_heap:
                expiration, apple_count = heapq.heappop(min_heap)
                if apple_count > 1:
                    heapq.heappush(min_heap, (expiration, apple_count - 1))
                count += 1
            
            i += 1
        
        return count
            