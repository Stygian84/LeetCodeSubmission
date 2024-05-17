class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result=1
        inc=None
        count=1
        for idx in range(len(nums)-1):
            if nums[idx]>nums[idx+1] and not inc:
                inc=True
                count=1
            elif nums[idx]<nums[idx+1] and inc:
                inc=False
                count=1
            elif nums[idx]==nums[idx+1]:  
                inc=False
                count=1
                continue
            count+=1
            if count>result:
                result=count
        return result