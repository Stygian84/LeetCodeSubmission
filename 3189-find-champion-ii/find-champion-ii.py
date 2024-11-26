class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for u,v in edges:
            graph[v].append(u)

        res = []
        for i in range(n):
            if i not in graph:
                res.append(i)
        if len(res)==1:
            return res[0]
        return -1
        
