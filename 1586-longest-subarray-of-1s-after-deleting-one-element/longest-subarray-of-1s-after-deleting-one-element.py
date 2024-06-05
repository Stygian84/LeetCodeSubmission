from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_count=0
        current= deque([])
        zeroes=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeroes+=1
                if zeroes==2:
                    while zeroes==2:
                        if (current.popleft()==0):
                            zeroes-=1
            current.append(nums[i])
            max_count=max(len(current)-1,max_count)
        return max_count