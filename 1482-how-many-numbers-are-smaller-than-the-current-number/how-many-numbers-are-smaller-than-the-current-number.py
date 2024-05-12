class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        for idx in range(len(nums)):
            count=0
            for item in nums:
                if nums[idx]>item:
                    count+=1
            result.append(count)
        return result
        