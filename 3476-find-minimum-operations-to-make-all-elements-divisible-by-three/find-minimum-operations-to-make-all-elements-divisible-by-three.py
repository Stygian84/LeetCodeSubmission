class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0

        for num in nums:
            lower=num//3*3
            higher=(num//3+1)*3
            count+=min(num-lower,higher-num)
        
        return count