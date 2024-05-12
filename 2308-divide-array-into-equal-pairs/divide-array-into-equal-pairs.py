class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dict1={}
        for item in nums:
            dict1[item]=dict1.get(item,0)+1
        for value in dict1.values():
            if value%2!=0:
                return False
        return True
        