class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dc={}
        for i in range(len(nums)):
            for item in nums[i+1:]+nums[:i]:
                if item>nums[i]:
                    dc[i]=item
                    break
        result=[]
        for i in range(len(nums)):
            result.append(dc.get(i,-1))
        return result