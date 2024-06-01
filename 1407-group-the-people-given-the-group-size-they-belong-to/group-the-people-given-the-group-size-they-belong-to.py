class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dc={}
        for idx in range(len(groupSizes)):
            dc[groupSizes[idx]] = dc.get(groupSizes[idx], []) + [idx]
        res=[]
        for key,values in dc.items():
            for i in range(0,len(values),key):
                res.append(values[i:i+key])
        return res
                   