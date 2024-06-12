class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for item in s:
            if item ==")":
                temp_str=""
                while stack and stack[-1]!="(":
                    temp_str+=stack.pop()[::-1]
                stack.pop() #remove (
                stack.append(temp_str)
            else:
                stack.append(item)
        return "".join(stack)