class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums2=nums[:]

        count=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                count+=1
                nums[i-1]=nums[i]
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                count+=1
                nums[i-1]=nums[i]
                
        count2 = 0
        for i in range(len(nums2)-1,0,-1):
            if nums2[i-1]>nums2[i]:
                count2+=1
                nums2[i]=nums2[i-1]
        for i in range(len(nums2)-1,0,-1):
            if nums2[i-1]>nums2[i]:
                count2+=1
                nums2[i]=nums2[i-1]

        if min(count,count2)>1:
            return False
        return True