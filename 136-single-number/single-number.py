class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for item in nums:
            res^=item
        return res
