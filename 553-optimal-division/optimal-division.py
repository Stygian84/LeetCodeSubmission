class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        
        n = len(nums)
        if n == 1:
            return str(nums[0])
        
        for i in range(n):
            nums[i] = str(nums[i])
        
        if n == 2:
            return "/".join(nums)
        
        nums[1] = "("+nums[1]
        
        return "/".join(nums)+")"