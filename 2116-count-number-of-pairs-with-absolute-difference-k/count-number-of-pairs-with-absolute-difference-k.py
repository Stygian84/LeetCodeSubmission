class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        for idx in range(len(nums)):
            for next in nums[idx+1:]:
                if abs(next-nums[idx])==k:
                    count+=1

        return count