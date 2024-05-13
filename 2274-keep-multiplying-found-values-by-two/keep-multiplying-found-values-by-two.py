class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            if nums.count(original)==0:
                break
            original*=2
        return original
        