class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
        res = []

        n = len(nums)
        for i in range(n):
            print(i+nums[i])
            target = i+nums[i]
            res.append(nums[(target%n)])
        return res