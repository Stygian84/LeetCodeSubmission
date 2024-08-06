class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)

        def backtrack(start,path):
            nonlocal res
            if len(path)>=2:
                if path[:] not in res:
                    res.append(path[:])
            
            for i in range(start,n):
                if path and nums[i]<path[-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return res