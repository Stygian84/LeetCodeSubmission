class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc=None
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]<0:
                if inc==True:
                    return False
                inc=False
            if nums[i+1]-nums[i]>0:
                if inc==False:
                    return False
                inc=True
        return True
        