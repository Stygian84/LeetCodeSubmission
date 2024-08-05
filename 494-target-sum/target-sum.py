class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0
        dp = defaultdict(int)
        dp[0] = 1  
        for num in nums:
            next_dp = defaultdict(int)
            for curr_sum in dp:
                next_dp[curr_sum + num] += dp[curr_sum]
                next_dp[curr_sum - num] += dp[curr_sum]
            dp = next_dp
        
        return dp[target]
        ''' res = 0
        n = len(nums)

        def backtrack(total,start,path):
            nonlocal res
            if len(path)==n:
                if total==target:
                    res+=1
                return
            
            item = nums[start]
            path.append(item)
            backtrack(total+item,start+1,path)
            path.pop()

            path.append(-item)
            backtrack(total-item,start+1,path)
            path.pop()
        

        backtrack(0,0,[])
        return res'''