class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        length=len(nums)
        if length<=1:
            return False
        if nums[-1]==nums[-2]==length-1 and len(nums)-1==len(set(nums)):
            return True
        return False