class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set=set(nums)
        count=len(nums_set)
        for item in nums_set:
            if item==0:
                count-=1
        return count
        