class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0

        pos=0
        ls=[0]*n
        for item in nums:
            if item!=0:
                ls[pos]=item
                pos+=1
        return ls       