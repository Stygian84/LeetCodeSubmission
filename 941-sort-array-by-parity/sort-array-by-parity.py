class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result=[]
        for item in nums:
            if item%2==0:
                result=[item]+result
            else:
                result+=[item]
        return result
        