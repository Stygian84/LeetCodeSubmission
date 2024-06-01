class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        res=set()
        while len(nums)>0:
            min=nums.pop(0)
            max=nums.pop(-1)
            avg=(min+max)/2
            res.add(avg)
        return len(res)
