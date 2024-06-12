class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        if nums[l]==target:
            return True
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            if nums[l] == nums[mid]:
                l += 1
                continue
            if nums[mid]>=nums[l]: #left to mid increasin
                if nums[l]<=target<nums[mid]:
                    r=mid-1 #must be in the first half
                else:
                    l=mid+1 
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1 
                else:
                    r=mid-1 
        return False
        