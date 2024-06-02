class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        '''while True:
            stack=[]
            for item in s:
                stack.append(item)
                if len(stack)>=k and stack[-k:]==[item]*k:
                    stack=stack[:-k]
                    continue
            new_s = "".join(stack)
            if new_s == s:
                break
            s = new_s 
        return "".join(stack)'''

        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1] = (char, stack[-1][1] + 1)
            else:
                stack.append((char, 1))
            
            if stack[-1][1] == k:
                stack.pop()
        
        return ''.join(char * count for char, count in stack)
        