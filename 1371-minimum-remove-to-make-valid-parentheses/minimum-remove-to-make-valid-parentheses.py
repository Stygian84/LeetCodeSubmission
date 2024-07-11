class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op=0
        cl=0

        res=[]
        for item in s:
            if item == "(":
                op+=1
            elif item == ")":
                op-=1
                if op<0:
                    op=0
                    continue
            res.append(item)

        result=""
        op=0
        for i in range(len(res)-1,-1,-1):
            item = res[i]
            if item == ")":
                op+=1
            elif item == "(":
                op-=1
                if op<0:
                    op=0
                    continue
            result+=item
        
    
        return result[::-1]