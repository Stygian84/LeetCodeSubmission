class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def isInCircle(center,radius,point):
            h,k = center
            x,y = point
            distance = math.sqrt((x-h)**2+(y-k)**2)
            return distance <= radius

        n = len(bombs)

        graph = defaultdict(list)

        for i in range(n):
            h,k,r = bombs[i]

            for j in range(n):
                x,y,_ = bombs[j]
                if i!=j:
                    if isInCircle((h,k),r,(x,y)):
                        graph[i].append(j)
        print(graph)
        def bfs(start):
            queue = deque([start])
            visited = set()
            visited.add(start)
            count = 0
            while queue:
                node = queue.popleft()
                count += 1
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return count

        res = 1
        nodes = list(graph.keys())
        for node in nodes:
            res = max(res,bfs(node))
        return res
