class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return abs(nums[-1]-nums[0])
        nums.sort()
        
        left=0
        right=0
        
        n=len(nums)
        mid=n//2

        mid_left = nums[mid]
        mid_right = nums[mid+1]

        for item in nums:
            left += abs(mid_left - item)
            right += abs(mid_right - item)

        return min(left,right)