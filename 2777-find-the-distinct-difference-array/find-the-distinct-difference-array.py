class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]

        for i in range(len(nums)):
            prefix = len(set(nums[:i+1]))
            suffix = len(set(nums[i+1:]))
            res.append(prefix-suffix)
        
        return res