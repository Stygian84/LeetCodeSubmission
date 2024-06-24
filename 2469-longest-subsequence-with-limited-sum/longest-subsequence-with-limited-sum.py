class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum=[0]*len(nums)
        prefix_sum[0]=nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        
        res=[]
        for query in queries:
            idx=0
            for i in range(len(prefix_sum)):
                if prefix_sum[i]>query:
                    break
                idx+=1
            res.append(idx)
        return res