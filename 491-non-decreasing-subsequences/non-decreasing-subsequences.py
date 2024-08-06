class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        n = len(nums)

        def backtrack(start,path):
            nonlocal res
            if len(path)>=2:
                x=tuple(path)
                if x not in seen:
                    seen.add(x)
                    res.append(path[:])
            
            for i in range(start,n):
                if path and nums[i]<path[-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return res