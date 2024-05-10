class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            first_idx=nums.index(target)
            second_idx=len(nums)-1-nums[::-1].index(target)
            return [first_idx,second_idx]
        except:
            return [-1,-1]
        def binary_search(ls, target):
            left = 0
            right = len(ls) - 1

            while left <= right:
                mid = (left+right) // 2
                if ls[mid] == target:
                    return mid
                elif ls[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return 'not found'
        first_idx=binary_search(nums,target)
        if first_idx=='not found':
            return [-1,-1]
        else:
            second_idx=len(nums)-binary_search(nums[::-1],target)
            return [first_idx,second_idx]