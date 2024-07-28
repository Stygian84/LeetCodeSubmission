class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        distances = dict()
        secondDistances = dict()
        pq = []
        heapq.heappush(pq, (0, 1))

        while len(pq) > 0:
            currTime, node = heapq.heappop(pq)
            if node in secondDistances:
                continue
            if node in distances:
                if currTime == distances[node]:
                    continue
                secondDistances[node] = currTime
            else:
                distances[node] = currTime
            if (currTime % (2 * change)) >= change:
                currTime += (change - currTime % change)
            for neighbor in graph[node]:
                heapq.heappush(pq, (currTime + time, neighbor))

        return secondDistances[n]