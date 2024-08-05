class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        def backtrack(total,path,seen):
            if len(path)>k:
                return
            if total == n and len(path)==k:
                res.append(path[:])
                return
            
            for i in range(1,10):
                if i not in seen and total+i <= n and len(path)<k:
                    seen.add(i)
                    path.append(i)
                    backtrack(total+i,path,seen)
                    path.pop()
                    seen.remove(i)
                else:
                    break
        backtrack(0,[],set())
        return res