class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''dc={}
        for item in nums:
            dc[item]=dc.get(item,0)+1
            
        for i in range(1,len(nums)+2):
            if dc.get(i,0)==0:
                return i
        '''
        n=len(nums)
        for i in range(n):
            while nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1