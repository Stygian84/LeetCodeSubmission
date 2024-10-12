class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        #think of each interval is assigned to n rooms
        #if all rooms are full, create 1 more room , count+1
        intervals.sort()#sort based on start
        
        heap = []
        for start,end in intervals:
            if heap and heap[0]<start:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
        return len(heap)