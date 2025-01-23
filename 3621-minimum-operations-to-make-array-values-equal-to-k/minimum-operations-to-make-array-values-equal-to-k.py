class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        if min(nums)<k:
            return -1

        unique = set(nums)

        if k in unique:
            return len(unique)-1
        return len(unique)