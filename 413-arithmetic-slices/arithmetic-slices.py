class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        total_slices = 0
        current_slices = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current_slices += 1
                total_slices += current_slices
            else:
                current_slices = 0

        return total_slices