class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        total_product = reduce(mul, nums, 1)
        if total_product==0:
            return 0
        if total_product>0:
            return 1
        else:
            return -1
        