class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result=0
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            else:
                count=0
            if count>0:
                result+=count
        return result