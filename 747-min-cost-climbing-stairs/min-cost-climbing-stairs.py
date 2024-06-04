class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=0
        for i in range(2,n+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[n]
        '''cost.reverse()
        total=0
        idx=0
        while idx<len(cost)-2:
            print(idx)
            try:
                temp=cost[idx+1]
            except:
                break
            if cost[idx]>cost[idx+1]:
                total+=cost[idx+1]

            else:
                total+=cost[idx]
            try:
                if cost[idx+1]>cost[idx+2]:
                    idx+=2
                else:
                    idx+=1
            except:
                idx+=1
        return total'''