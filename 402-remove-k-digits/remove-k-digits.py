class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        count=0
        for i in range(len(num)):
            
            while stack and count<k and stack[-1]>num[i]:
                stack.pop()
                count += 1
            stack.append(num[i])
        while count<k:
            stack.pop()
            count+=1
        res="".join(stack).lstrip("0") 
        if res=="":
            return "0"
        else:
            return res