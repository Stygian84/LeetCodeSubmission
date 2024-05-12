class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1=0
        result=[]
        for item in nums:
            sum1+=item
            result.append(sum1)
        return result
        