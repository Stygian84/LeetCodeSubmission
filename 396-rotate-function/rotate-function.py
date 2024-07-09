class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        current_f = sum(i * num for i, num in enumerate(nums))
        
        max_f = current_f
        
        for k in range(1, n):
            current_f = current_f + total_sum - n * nums[-k]
            if current_f >max_f:
                max_f = current_f
        return max_f
        