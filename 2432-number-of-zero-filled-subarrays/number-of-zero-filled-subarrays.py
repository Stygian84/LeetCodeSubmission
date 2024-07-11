class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        result = 0
        max_zeros = 0
        
        for num in nums:
            if num == 0:
                max_zeros += 1
                result += max_zeros
            else:
                max_zeros = 0
        
        return result