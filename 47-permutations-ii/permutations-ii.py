class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        n = len(nums)
        seen = set()
        def backtrack(start,path):
            if len(path)==n:
                res.add(tuple(path[:]))
                return
            
            for i in range(n):
                if i not in seen:
                    seen.add(i)
                    path.append(nums[i])
                    backtrack(i,path)
                    path.pop()
                    seen.remove(i)

        for i in range(n):
            backtrack(i,[])

        result = []
        for item in res:
            result.append(list(item))
        return result



