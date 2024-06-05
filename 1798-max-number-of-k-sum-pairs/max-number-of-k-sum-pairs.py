class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        count=0
        while l<r:
            total=nums[l]+nums[r]
            if total==k:
                count+=1
                l+=1
                r-=1
            elif total>k:
                r-=1
            else:
                l+=1
        return count
        