class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)//2):
            result+=int(str(nums[i])+str(nums[-(i+1)]))
        if len(nums)%2==1:
            result+=int(nums[len(nums)//2])
        return result
        