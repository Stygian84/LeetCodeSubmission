class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_count=0
        neg_count=0
        for item in nums:
            if item >0:
                pos_count+=1
            elif item<0:
                neg_count+=1
        return max(pos_count,neg_count)
        