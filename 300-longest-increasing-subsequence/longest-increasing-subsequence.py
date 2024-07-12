class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub = []
        for x in nums:
            pos = bisect_left(sub, x)
            if pos == len(sub):
                sub.append(x)
            else:
                sub[pos] = x
                
        return len(sub)