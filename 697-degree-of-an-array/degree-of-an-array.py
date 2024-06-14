class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        dc={}
        max_freq=-1
        max_key=[]
        for item in nums:
            dc[item]=dc.get(item,0)+1
            if dc[item]>max_freq:
                max_freq=dc[item]
                max_key=[item]
            if dc[item]==max_freq and item not in max_key:
                max_key.append(item)
        if max_freq==1:
            return 1

        start_dc={}
        end_dc={}
        for i in range(len(nums)):
            if nums[i] in max_key:
                
                if start_dc.get(nums[i],-1)==-1:
                    start_dc[nums[i]]=i
                else:
                    end_dc[nums[i]]=i
                    
        min_length=math.inf
        for key in start_dc.keys():
            min_length=min(min_length,end_dc[key]-start_dc[key]+1)

        return min_length