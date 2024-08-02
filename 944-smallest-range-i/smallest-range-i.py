class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        a,b=nums[0],nums[-1]
        if a+k>=b-k:
            return 0
        return (b-k)-(a+k)