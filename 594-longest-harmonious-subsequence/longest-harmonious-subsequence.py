class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq={}
        for item in nums:
            freq[item]=freq.get(item,0)+1
        
        max_count=0
        for key,values in freq.items():
            try:
                count=freq[key]+freq[key-1]
                if count>max_count:max_count=count
            except:
                pass
            try:
                count=freq[key]+freq[key+1]
                if count>max_count:max_count=count
            except:
                pass
        return max_count
