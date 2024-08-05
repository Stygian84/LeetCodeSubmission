class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)


        def backtrack(total,path,i):
            if total == target:
                res.append(path[:])
                return
            
            for j in range(i,n):
                c = candidates[j]
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + c <= target:
                    path.append(c)
                    backtrack( total + c, path, j+1)
                    path.pop()
                else:
                    break

        print(candidates)
        backtrack(0,[],0)
        return res