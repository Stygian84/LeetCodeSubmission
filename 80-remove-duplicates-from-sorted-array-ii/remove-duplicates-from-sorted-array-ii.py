class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        for item in nums:
            if (index==0 or index==1 or nums[index-2]!=item):
                nums[index]=item
                index+=1
        return index
        