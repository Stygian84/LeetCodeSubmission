class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set=set(dictionary)
        dp=[math.inf]*(len(s)+1)
        dp[0]=0

        for i in range(1,len(s)+1):
            for j in range(i):
                substring=s[j:i]
                if substring in dict_set:
                    dp[i]=min(dp[i],dp[j])
                else:
                    dp[i]=min(dp[i],dp[j]+(i-j))
        return dp[-1]