class Solution:
    def triangleType(self, nums: List[int]) -> str:
        count=0
        nums.sort()
        if nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[0]+nums[2]>nums[1]:
            pass
        else:
            return "none"
        if nums[0]==nums[1]:
            count+=1
        if nums[1]==nums[2]:
            count+=1
        if nums[0]==nums[2]:
            count+=1
        if count==3:
            return "equilateral"
        elif count==2 or count==1:
            return "isosceles"
        else:
            return "scalene"