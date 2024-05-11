class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums=set(nums)
        first_max=max(set_nums)
        set_nums.remove(first_max)
        if len(set_nums)==0:
            return first_max
        set_nums.remove(max(set_nums))
        if len(set_nums)==0:
            return first_max
        else:
            return max(set_nums)
            
        