class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dc={}
        for item in nums:
            dc[item]=dc.get(item,0)+1
        sorted_dc=dict(sorted(dc.items(), key=lambda item: item[1],reverse=True))
        
        res=[]
        count=0
        for key in sorted_dc.keys():
            if count==k:
                break
            res.append(key)
            count+=1
        return res