class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dc={}
        for item in nums:
            dc[item]=dc.get(item,0)+1
        res=[]
        while any(values > 0 for values in dc.values() ):
            temp_ls=[]
            for key,values in dc.items():
                if values>0:
                    temp_ls.append(key)
                    dc[key]-=1
            res.append(temp_ls)
        return res