class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        n=len(s)
        dp=[0]*n

        for i in range(n):
            if s[i]=="(":
                stack.append(i)
            if s[i]==")" and stack:
                dp[stack.pop()]=1
                dp[i]=1
        print(dp)
        temp_length=0
        max_length=0
        for item in dp:
            if item==1:
                temp_length+=1
            else:
                max_length=max(temp_length,max_length)
                temp_length=0
        max_length=max(temp_length,max_length)

        return max_length