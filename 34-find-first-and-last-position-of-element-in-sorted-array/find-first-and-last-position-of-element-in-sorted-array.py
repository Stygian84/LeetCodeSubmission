class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        try:
            first_idx=nums.index(target)
            second_idx=len(nums)-1-nums[::-1].index(target)
            return [first_idx,second_idx]
        except:
            return [-1,-1]
        '''
        def first_search(ls, target):
            left = 0
            right = len(ls) - 1
            result=-1

            while left <= right:
                mid = (left+right) // 2
                if ls[mid] == target:
                    result=mid
                    right=mid-1
                elif ls[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        def second_search(ls, target):
            left = 0
            right = len(ls) - 1
            result=-1

            while left <= right:
                mid = (left+right) // 2
                if ls[mid] == target:
                    result=mid
                    left=mid+1
                elif ls[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        first_idx=first_search(nums,target)
        if first_idx==-1:
            return [-1,-1]
        else:
            second_idx=second_search(nums,target)
            return [first_idx,second_idx]