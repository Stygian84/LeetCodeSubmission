class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        seen = set(nums)
        checked = set()

        res = -1
        for i in range(len(nums)):
            current = nums[i]
            if current in checked:
                continue
            checked.add(current)
            length = 1
            while current*current in seen:
                checked.add(current*current)
                current = current*current
                length+=1
                
            if length!=1:
                res = max(res,length)
        return res
            