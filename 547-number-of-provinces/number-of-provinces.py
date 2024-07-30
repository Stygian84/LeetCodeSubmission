class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        total = 0

        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    graph[i].append(j)



        visited = set()
        count = 0

        def dfs(start,visited):
            stack = [start]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        
        for node in graph:
            if node not in visited:
                visited.add(node)
                dfs(node,visited)
                count+=1
        return count