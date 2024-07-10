class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        
        for i in range(n):
            if s[i] == 'R':
                nums[i] += d
            else:
                nums[i] -= d 
            
        nums.sort()
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        total = 0
        for i in range(1, n):
            total += nums[i] * i - prefix_sum[i - 1]

        return total%(10**9 + 7)