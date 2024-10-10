class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        ls = []
        for i in range(n):
            ls.append((nums[i],i))
        ls.sort()
        min_idx = n
        res = 0
        for num, idx in ls:
            res = max(res, idx-min_idx)
            min_idx = min(min_idx, idx)
        return res

        '''n=len(nums)
        res = 0
        for i in range(n):
            for j in range(n-1,i,-1):
                if j-i<res:
                    break
                if nums[i]<=nums[j]:
                    res = max(res,j-i)
                    break
        return res'''