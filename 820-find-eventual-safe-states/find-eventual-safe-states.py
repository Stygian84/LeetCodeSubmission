class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)

        state = [0]*n
        # 0 = not processed
        # 1 = in progress
        # 2 = safe
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1

            for neighbour in graph[node]:
                if state[neighbour]==1 or not dfs(neighbour):
                    return False
            state[node] = 2
            return True
        
        res = []

        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
        
        '''n = len(graph)

        seen = set()
        res = set()
        
        queue = deque([])
        for i in range(n):
            queue.append(i)
            if not graph[i]:
                res.add(i)


        while queue:
            current = queue.popleft()
            
            if set(graph[current]).issubset(res):
                res.add(current)

            for neighbours in graph[current]:
                if neighbours not in seen:
                    queue.append(neighbours)
                    seen.add(neighbours)
        print(seen)
        
        return list(res)'''