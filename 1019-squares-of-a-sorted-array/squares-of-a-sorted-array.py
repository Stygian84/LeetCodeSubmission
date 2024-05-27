class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for item in nums:
            res.append(item**2)
        res.sort()
        return res
        