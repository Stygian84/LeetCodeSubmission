class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        store = {}
        for l,r in queries:
            
            current = 0
            if (l,r) in store:
                res.append(store[(l,r)])
                continue

            for i in range(l,r+1):
                current^=arr[i]
            
            store[(l,r)]=current
            res.append(current)
        
        return res