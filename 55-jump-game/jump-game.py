class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 1
        step = nums[0]
        n = len(nums)

        for i in range(1,n):
            step-=1
            if step<0:
                return False
            if nums[i]>step:
                step = nums[i]
            
            
        return True
