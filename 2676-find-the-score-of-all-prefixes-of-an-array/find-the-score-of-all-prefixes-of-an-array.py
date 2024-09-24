class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n

        max_num = 0
        for i in range(len(nums)):
            if nums[i]>max_num:
                max_num=nums[i]
            res[i] = res[i-1] + max_num + nums[i]
        
        return res