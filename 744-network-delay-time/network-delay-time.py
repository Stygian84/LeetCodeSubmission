class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        min_heap = [(0,k)]
        delay = {i: math.inf for i in range(1,n+1)}
        delay[k]=0

        while min_heap:
            time,node = heapq.heappop(min_heap)

            if time>delay[node]:
                continue
            
            for neighbour,duration in graph[node]:
                new_time = time+duration
                if new_time<delay[neighbour]:
                    delay[neighbour]=new_time
                    heapq.heappush(min_heap,(new_time,neighbour))
        
        if math.inf in delay.values():
            return -1
        return max(delay.values())