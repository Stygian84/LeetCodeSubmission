class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_value=min(nums)
        count=0
        while min_value<k:
            nums.remove(min_value)
            min_value=min(nums)
            count+=1
        return count
        