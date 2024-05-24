class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        count=0
        for item in s:
            if item=="(" and count>0:
                stack.append(item)
            elif item==")" and count>1:
                stack.append(item)
            if item=="(":
                count+=1
            else:
                count-=1
        return "".join(stack)