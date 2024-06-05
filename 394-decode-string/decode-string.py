class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for item in s:
            stack.append(item)
            if item=="]":
                stack.pop()
                temp=""
                
                while stack[-1]!="[":
                    temp+=stack.pop()[::-1]
                stack.pop()

                temp=temp[::-1]
                increment=""
                while stack and stack[-1].isdigit():
                    increment+=stack.pop()
                    
                increment=int(increment[::-1])
                stack.append(temp*increment)
        print(stack)
        return "".join(stack)



        