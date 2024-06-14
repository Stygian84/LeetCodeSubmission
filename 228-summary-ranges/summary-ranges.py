class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res=[]
        start=nums[0]
        for i in range(len(nums)):
            value=nums[i]
            if i!=len(nums)-1 and nums[i+1]-value==1:
                continue
            else:
                if start!=value:
                    res.append("{}->{}".format(start,value))
                else:
                    res.append("{}".format(value))
                if i!=len(nums)-1:
                    start=nums[i+1]
        return res
    