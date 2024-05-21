class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum=sum(nums)
        dig_sum=0
        for item in nums:
            for digit in str(item):
                dig_sum+=int(digit)
        return abs(ele_sum-dig_sum)
        