class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result=0
        for item in nums:
            if len(str(item))%2==0:
                result+=1
        return result
        