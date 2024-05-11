class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dc={}
        for i in nums:
            if i in dc:
                return True
            else:
                dc[i]=0
        return False