class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]

        for item in s:
            if item.isdigit():
                stack.pop()
            else:
                stack.append(item)

        return "".join(stack)