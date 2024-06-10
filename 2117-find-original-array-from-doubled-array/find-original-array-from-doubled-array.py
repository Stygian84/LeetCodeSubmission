class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2==1:
            return []
        res=[]
        dc1={}
        changed.sort()
        for item in changed:
            dc1[item]=dc1.get(item,0)+1
        
        for item in changed:
            if dc1.get(item,0)==0:
                continue
            if dc1.get(item*2,0)==0:
                continue
            dc1[item]-=1
            dc1[item*2]-=1
            if dc1[item]<0:
                return []
            res.append(item)
        print(res)
        return res if len(res) * 2 == len(changed) else []