class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        print(events)

        total = 0
        n= len(events)
        i = 0
        day = 1
        min_heap = []

        while i<n or min_heap:

            while i<n and events[i][0]==day:
                heapq.heappush(min_heap,events[i][1])
                i+=1
            
            while min_heap and min_heap[0]<day:
                heapq.heappop(min_heap)
            
            if min_heap:
                total+=1
                heapq.heappop(min_heap)
            day+=1
        
        return total