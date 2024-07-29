class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dc = defaultdict(int)

        for u,v in edges:
            dc[v]+=1

        res = []
        seen = set()
        for u,v in edges:
            if dc[u]==0 and u not in seen:
                res.append(u)
                seen.add(u)
        return res

