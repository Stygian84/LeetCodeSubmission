class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        # idx = color
        dc = {}
        # color = idx
        dc2 = defaultdict(list)
        res = []
        for f,c in queries:
            if f in dc:
                dc2[dc[f]].remove(f)
                if len(dc2[dc[f]])==0:
                    del dc2[dc[f]]
            
            dc[f]=c
            dc2[c].append(f)
        
            res.append(len(dc2))

        return res