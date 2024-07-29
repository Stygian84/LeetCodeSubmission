class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        res = []
        def dfs(node,path):
            path.append(node)
            if node == n-1:
                res.append(path[:])
                return
            else:
                for neighbour in graph[node]:
                    dfs(neighbour,path)
                    path.pop()


        dfs(0,[])
        return res