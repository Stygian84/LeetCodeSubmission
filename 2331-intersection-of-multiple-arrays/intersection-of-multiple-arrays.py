class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res=None
        if len(nums)==1:
            ls=nums[0]
            ls.sort()
            return ls
        for i in range(len(nums)-1):
            if res:
                res=set.intersection(res,set(nums[i+1]))
            else:
                res=set.intersection(set(nums[i]),set(nums[i+1]))
        ls=list(res)
        ls.sort()
        return ls
                