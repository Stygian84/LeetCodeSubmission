class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        idx_one = -1
        idx_n = -1

        for i in range(n):
            if nums[i]==1:
                idx_one=i
            elif nums[i]==n:
                idx_n=i
            if idx_one!=-1 and idx_n!=-1:
                break
        
        if idx_one<idx_n:
            return idx_one+ (n-idx_n-1)
        
        return idx_one+ (n-idx_n-1)-1