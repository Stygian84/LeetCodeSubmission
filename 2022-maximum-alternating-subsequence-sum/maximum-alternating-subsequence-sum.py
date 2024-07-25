class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        # check increasing -> decreasing -> increasing
        # at increasing find max, at decreasing find min
        # max and min are always at turning point
        total = 0

        increasing = True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if increasing: #if increasing, add maximum
                    total+=nums[i-1]
                    increasing = False
            else:
                if not increasing: #if decreasing, decrease minimum
                    total-=nums[i-1]
                    increasing = True
        
        if increasing: #add last element if end at increasing
            total+=nums[-1]

        return total