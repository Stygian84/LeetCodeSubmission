class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        start_idx=0
        end_idx=0

        lowest_num=nums[0]
        highest_num=nums[-1]
        for i in range(len(nums)):
            if nums[i]!=lowest_num:
                break
            start_idx+=1
        for i in range(1,len(nums)):
            if nums[-i]!=highest_num:
                break
            end_idx-=1
        return len(nums[start_idx:end_idx])
        