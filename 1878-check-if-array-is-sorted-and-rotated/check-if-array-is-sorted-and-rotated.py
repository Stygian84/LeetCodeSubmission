class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(set(nums))==len(nums):

            min_idx=nums.index(min(nums))

            result=nums[min_idx:]+nums[:min_idx]
            print(result)
            nums.sort()
            print(nums,"b")
            return result==nums
        else:
            copy=sorted(nums)            
            for i in range(len(nums)):
                result=nums[i:]+nums[:i]
                print(result,"a")
                if result==copy:
                    return True
            return False
        