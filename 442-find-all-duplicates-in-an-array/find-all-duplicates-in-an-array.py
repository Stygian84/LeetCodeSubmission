class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicates = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]
        
        return duplicates