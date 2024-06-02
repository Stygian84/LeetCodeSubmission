class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for item in s:
            if item=="*" and stack:
                stack.pop()
                continue
            stack.append(item)
        return "".join(stack)
        