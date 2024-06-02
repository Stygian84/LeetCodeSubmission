class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        while True:
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
        return "".join(stack)
        