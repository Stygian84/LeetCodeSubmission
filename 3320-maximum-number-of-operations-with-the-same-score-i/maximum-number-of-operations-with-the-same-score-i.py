class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        result=0
        total=nums[0]+nums[1]
        while len(nums)>=2 and nums[0]+nums[1]==total :
            nums=nums[2:]
            result+=1
        return result

        