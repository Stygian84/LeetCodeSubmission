class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dc={}
        for item in nums:
            dc[item]=dc.get(item,0)+1
        for key,values in dc.items():
            if values==1:
                return key
