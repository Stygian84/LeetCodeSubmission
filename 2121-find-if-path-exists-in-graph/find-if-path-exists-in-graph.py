class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        res = False
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node,seen):
            #seen.add(node)
            nonlocal res
            seen.add(node)
            if node == destination:
                res = True
                return
            if res:
                return

            for dest in graph[node]:
                if dest not in seen:
                    dfs(dest,seen)

            return 
        
        seen = set()
        seen.add(source)
        dfs(source,seen)
        return res

        
        
        
        '''visited=set()

        def dfs(x,y,visited):
            if (x,y) in visited:
                return
            visited.add((x,y))
            for a,b in edges:
                dfs(a,b,visited)
        
        for a,b in edges:
            dfs(a,b,visited)
        return (source,destination) in visited'''