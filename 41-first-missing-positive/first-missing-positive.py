class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dc={}
        for item in nums:
            dc[item]=dc.get(item,0)+1
            
        for i in range(1,len(nums)+2):
            if dc.get(i,0)==0:
                return i
