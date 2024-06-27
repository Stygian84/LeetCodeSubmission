class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        total=sum(nums)
        current_sum=0
        n=len(nums)

        res=[]
        for i in range(n-1,-1,-1):
            current_sum+=nums[i]
            total-=nums[i]
            res.append(nums[i])
            if current_sum>total:
                return res

        return res