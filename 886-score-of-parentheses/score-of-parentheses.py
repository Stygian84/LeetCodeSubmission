class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=1
        for item in s:
            if item=="(":
                stack.append(item)
            else:
                if item==")":
                    if stack[-1]=="(": #if () convert to 1 push to stack
                        stack.pop()
                        stack.append(1)
                    elif stack[-1]!="(":
                        score=0
                        while stack[-1]!="(": #if (12), add all inside then times 2
                            score+=stack.pop()
                        if stack:
                            stack.pop() #remove ( from stack
                        stack.append(score*2)
                               
        
        return sum(stack)
            
