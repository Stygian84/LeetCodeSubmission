class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        left = 0
        right = sum(nums)

        total = 0
        for i in range(len(nums)-1):
            left += nums[i]
            right -= nums[i]
            if (right-left)%2==0:
                total+=1

        return total