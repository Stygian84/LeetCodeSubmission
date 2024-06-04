class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=-math.inf
        window_sum=sum(nums[:k])
        for left in range(len(nums)-k+1):
            max_sum=max(max_sum,window_sum)
            if left<len(nums)-k:
                window_sum+=(nums[left+k]-nums[left])
        return max_sum/k