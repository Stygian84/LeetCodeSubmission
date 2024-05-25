class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspace(s):
            stack=[]
            for item in s:
                if item =="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(item)
            return "".join(stack)
    
        return backspace(s)==backspace(t)