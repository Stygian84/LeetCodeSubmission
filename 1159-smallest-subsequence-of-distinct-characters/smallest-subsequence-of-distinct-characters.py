class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen=set()
        stack=[]
        dc={}
        for i in range(len(s)):
            dc[s[i]]=i
        
        for i, char in enumerate(s):
            if char not in seen:
                while stack and char<stack[-1] and dc[stack[-1]]>i:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)

        return "".join(stack)