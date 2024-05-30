class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        init=1
        diff=0
        for item in nums:
            init+=item
            if init<1:
                diff+=(1-init)
                init=1
        return 1+diff
        