class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def possible(v, k):
            i = 0
            while i < len(nums) and k > 0:
                if nums[i] <= v:
                    k -= 1
                    i += 2
                else:
                    i += 1
            return k==0
        items = list(sorted(set(nums)))
        lo, hi = 0, len(items) - 1
        while lo < hi:
            m = (lo + hi) // 2
            if possible(items[m], k):
                hi = m
            else:
                lo = m + 1
        return items[lo]