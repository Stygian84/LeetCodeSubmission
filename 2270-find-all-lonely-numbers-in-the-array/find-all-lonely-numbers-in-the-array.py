class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dc={}
        for item in nums:
            dc[item]=dc.get(item,0)+1
        res=[]
        for key,value in dc.items():
            if value==1:
                if dc.get(key-1,0)==0 and dc.get(key+1,0)==0:
                    res.append(key)
        return res