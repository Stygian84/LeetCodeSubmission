class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            elif char == '*':
                min_open -= 1
                max_open += 1
            
            if min_open < 0:
                min_open = 0
            
            if max_open < 0:
                return False
        
        return min_open == 0
    
        '''count=0
        stack=[]
        for item in s:
            if item=="(":
                stack.append(item)
            elif item==")":
                if len(stack)==0:
                    if count>0:
                        count-=1
                        continue
                elif stack and stack[-1]=="(" :
                    stack.pop()
            else:
                count+=1
        print(stack,count)
        if len(stack)==0 or len(stack)<=count:
            return True
        else:
            return False'''