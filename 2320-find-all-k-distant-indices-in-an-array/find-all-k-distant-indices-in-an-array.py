class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []

        idx_key = []
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                idx_key.append(i)

        for i in range(n):
            for idx in idx_key:
                if abs(i-idx)<=k:
                    res.append(i)
                    break
        
        return res