class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        dc = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in dc:
                res.append(dc[diff])
                res.append(i)
                return res
            dc[nums[i]]=i
        
        return res