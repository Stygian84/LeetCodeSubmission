class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total=nums[0]
        for idx in range(len(nums)-1):
            if nums[idx+1]-nums[idx]==1:
                total+=nums[idx+1]
            else:
                break
        while total in nums:
            total+=1
        return total

        