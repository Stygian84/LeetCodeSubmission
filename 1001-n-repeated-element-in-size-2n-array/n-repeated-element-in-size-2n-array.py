class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        middle=int(len(nums)/2)
        count_left=nums.count(nums[middle-1])
        count_right=nums.count(nums[middle])
        if count_left>count_right:
            return nums[middle-1]
        return nums[middle]
        