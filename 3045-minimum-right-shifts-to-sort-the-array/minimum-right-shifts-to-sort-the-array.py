class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        res=0
        
        sorted_nums=sorted(nums)
        if sorted_nums==nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                continue
            else:
                res=i+1
                break
        ls=nums[res:]+nums[:res]
        if sorted_nums!=ls:
            return -1
        return len(nums)-(res)