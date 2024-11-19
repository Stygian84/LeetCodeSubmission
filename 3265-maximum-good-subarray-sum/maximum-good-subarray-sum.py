class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        # store index 
        # if diff can be found in hash, calc sum usign prefix sum
        def calcSum(diff):
            nonlocal prefix_sum
            if diff in index_dict:
                index = index_dict[diff]
                if index==i:
                    return -math.inf
                
                if index==0:
                    total = prefix_sum[i]
                elif i == 0:
                    total = prefix_sum[index]
                else:
                    if i>index:
                        total = prefix_sum[i]-prefix_sum[index-1]
                    else:
                        total = prefix_sum[index]-prefix_sum[i-1]
                return total
            return -math.inf


        n = len(nums)
        prefix_sum = [0]*(n)
        index_dict = {}

        for i in range(n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        res = -math.inf
        for i in range(n):
            diff = nums[i]-k
            diff2 = nums[i]+k


            total = max(calcSum(diff),calcSum(diff2))
            
            res = max(res,total)

            if nums[i] not in index_dict:
                index_dict[nums[i]] = i
            else:
                #check which sum is greater
                if i<n-1:
                    sum1 = prefix_sum[i+1] - prefix_sum[index_dict[nums[i]]]
                    sum2 = prefix_sum[i+1] - prefix_sum[i] 
                    if sum2>sum1:
                        index_dict[nums[i]] = i

        if res == -math.inf:
            res = 0
        return res