class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for item in nums:
            dict1[item]=dict1.get(item,0)+1
        for key,values in dict1.items():
            if values>=len(nums)/2:
                return key
        