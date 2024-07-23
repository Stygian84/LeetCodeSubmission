class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dc={}
        for item in nums:
            key=nums.count(item)
            dc[key]=dc.get(key,[])+[item]
        res=[]
        for i in range(len(nums)+1):
            try:
                ls=sorted(dc[i],reverse=True)
                res.extend(ls)
            except:
                pass
        return res