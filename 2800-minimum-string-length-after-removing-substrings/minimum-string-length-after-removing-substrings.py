class Solution:
    def minLength(self, s: str) -> int:
        while ("AB" in s) or( "CD" in s):
            stack=[]
            for item in s:
                if stack:
                    if item=="B" and stack[-1]=="A":
                        stack.pop()
                    elif item=="D" and stack[-1]=="C":
                        stack.pop()
                    else:
                        stack.append(item)
                else:
                    stack.append(item)
            s="".join(stack)
        print(s)
        return len(s)
        