class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for i in range(n):
            total += sum(nums[max(0,i-nums[i]):i+1])
        
        return total