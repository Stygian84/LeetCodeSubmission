class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return nums[0]

        l,r=0,n-1

        while l<=r:
            mid = l + (r - l) // 2
            
            if mid == 0 or mid == n - 1 or (nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        '''res=0
        for num in nums:
            res^=num
        
        return res'''