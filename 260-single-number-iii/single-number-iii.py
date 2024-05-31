class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dc={}
        for item in nums:
            dc[item]=dc.get(item,0)+1
        res=[]
        for key,values in dc.items():
            if values==1:
                res.append(key)
        return res