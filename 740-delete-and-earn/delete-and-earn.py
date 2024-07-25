class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        freq = Counter(nums)
        n = len(freq)
        if n==1:
            return sum(nums)
        
        new_num=[nums[0]]
        for item in nums:
            if item!=new_num[-1]:
                new_num.append(item)

        dp=[0]*(n)
        dp[0]=freq[new_num[0]]*new_num[0]

        for i in range(1,len(new_num)):
            if new_num[i]-new_num[i-1]==1:
                dp[i]=max(dp[i-2]+freq[new_num[i]]*new_num[i],dp[i-1])
            else:
                dp[i]=dp[i-1]+freq[new_num[i]]*new_num[i]
        return dp[n-1]
