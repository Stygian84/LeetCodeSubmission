class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        i=0
        while k>0 and i<len(nums): 
            if nums[i]<0:
                nums[i]*=-1
                i+=1
                k-=1
            else:
                break
        if k>0 and k%2==1:
            nums.sort()
            nums[0]*=-1
            
        return sum(nums)