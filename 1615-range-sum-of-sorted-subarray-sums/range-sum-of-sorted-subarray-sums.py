class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        total = []
        for i in range(n):
            total.append(nums[i])
            for j in range(i+1,n):
                total.append(sum(nums[i:j+1]))
        
        total.sort()
        res = sum(total[left-1:right])
        return res % (10**9+7) 