class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        subarrays=[]
        result=0
        for idx in range(len(nums)):
            for i in range(idx+1,len(nums)+1):
                subarrays.append(nums[idx:i])
        for item in subarrays:
            result+=len(set(item))**2
        return result