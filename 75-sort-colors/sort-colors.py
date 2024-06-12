class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dc={0:0,1:0,2:0}
        for item in nums:
            dc[item]+=1
        for i in range(len(nums)):
            if dc[0]>0:
                nums[i]=0
                dc[0]-=1
            elif dc[1]>0:
                nums[i]=1
                dc[1]-=1
            else:
                nums[i]=2
                dc[2]-=1
        