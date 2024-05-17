class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        curr_num=nums[0]
        count=1
        for item in nums[1:]:
            if item == curr_num:
                count+=1
            else:
                curr_num=item
                count=1
            if count>2:
                return False
        return True