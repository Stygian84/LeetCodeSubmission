class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0,0]]*(n+1) # store (no of zero, no of one)



        for i in range(n):
            a,b = dp[i]
            if s[i]=="0":
                dp[i+1] = [a+1,b]
            else:
                dp[i+1] = [a,b+1]
        
        min_flips = float('inf')

    
        for i in range(n+1):
            flips = dp[i][1] + (dp[-1][0] - dp[i][0])
            min_flips = min(min_flips, flips)
        return min_flips
        '''n=len(s)
        
        flag = False
        zero = 0
        one = 0
        after_zero = 0
        for i in range(n):
            if s[i]=="0":
                zero+=1
                if flag:
                    after_zero+=1
            else:
                one+=1
                flag=True
        
        after_one = 0
        s=s[::-1]
        flag=False
        for i in range(n):
            if s[i]=="0":
                flag=True
            else:
                if flag:
                    after_one+=1
        return min(zero,one,after_zero,after_one)'''
