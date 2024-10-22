class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        res = -1

        for x in nums:
            for y in nums:
                if abs(x-y)<=min(x,y):
                    res = max(res,x^y)
        return res