class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        while len(nums)>k:
            nums.remove(min(nums))
        return nums