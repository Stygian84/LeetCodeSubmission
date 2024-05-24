class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        '''
        nums.sort()
        while len(nums)>0:
            print(nums)
            max_value=nums[-1]
            if max_value*-1==nums[0]:
                return max_value
            while len(nums)>0 and max_value*-1>nums[0]:
                nums.pop(0)
            if len(nums)>0:
                if max_value*-1==nums[0]:
                    return max_value
                nums.pop(-1)
        return -1
        '''
        dc={}
        for item in nums:
            dc[item]=-item
        max_value=-1
        for value in dc.values():
            if value in dc:
                if value>max_value:
                    max_value=value
        return max_value