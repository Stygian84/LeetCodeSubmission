class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        for idx in range(len(nums)-2):
            value=nums[idx]+diff
            if value in nums:
                second_value=value+diff
                if second_value in nums:
                    count+=1
        return count