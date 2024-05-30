class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dc={}
        res=[]
        for item in nums:
            dc[item]=dc.get(item,0)+1
        limit=len(nums)//3
        for key,values in dc.items():
            if values>limit:
                res.append(key)
        return res