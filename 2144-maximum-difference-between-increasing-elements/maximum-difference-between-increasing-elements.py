class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        max_diff = -1
        minimum = math.inf

        for i in range(len(nums)):
            if nums[i]<minimum:
                minimum = nums[i]
            elif nums[i]>minimum:
                max_diff = max(max_diff,nums[i]-minimum)
        
        return max_diff