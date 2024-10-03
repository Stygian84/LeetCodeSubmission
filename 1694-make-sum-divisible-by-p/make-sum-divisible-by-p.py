class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total = sum(nums)
        if total%p==0:
            return 0
        target = total%p
        prefix_sum = 0
        res = math.inf
        index = {0:-1}

        for i in range(len(nums)):
            prefix_sum+=nums[i]
            needed = (prefix_sum-target)%p

            if needed in index:
                res = min(res,i-index[needed])
            
            index[prefix_sum%p]=i
        
        if res == math.inf or res==len(nums):
            return -1
        return res
        '''total = sum(nums)
        if total%p==0:
            return 0

        n = len(nums)
        prefix_sum = [0]*n
        res = math.inf

        for i in range(n):
            prefix_sum[i] = prefix_sum[i-1]+nums[i]
            if (total-nums[i])%p==0:
                return 1

        for start in range(n):
            for end in range(start+1,n):
                
                removed = prefix_sum[end]-prefix_sum[start]
                #print(start,end,removed,total-removed)
                if end-start<res and (total-removed)%p==0:
                    res = end-start

        if res==math.inf:
            res=-1
        return res
        '''