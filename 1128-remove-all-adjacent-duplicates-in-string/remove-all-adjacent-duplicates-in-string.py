class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for item in s:
            if stack and item in stack[-1]:
                stack.pop()
            else:
                stack.append(item)
        return "".join(stack)