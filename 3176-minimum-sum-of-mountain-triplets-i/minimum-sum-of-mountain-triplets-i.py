class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res=math.inf
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]<nums[j] and nums[k]<nums[j]:
                        res=min(res,nums[i]+nums[j]+nums[k])
        if res==math.inf:
            return -1
        return res