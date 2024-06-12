class Solution:
    def calculate(self, s: str) -> int:
        
        def operate(a,b,operator):
            if operator=="-":
                return a-b
            elif operator=="+":
                return a+b
            elif operator=="*":
                return a*b
            else:
                return a//b
        
        ls=[]
        for item in s:
            if item.isdigit():
                if len(ls)>=1 and str(ls[-1]).isdigit():
                    ls[-1]=ls[-1]*10+int(item)
                    continue
                ls.append(int(item))
            elif item != " ":
                ls.append(item)

        if len(ls)==1:
            return ls[0]
        print(ls)
        stack=deque([])
        skip=0

        # do * and / first
        for i in range(len(ls)):
            if skip>0:
                skip-=1
                continue
            if str(ls[i]).isdigit():
                stack.append(ls[i])
            elif ls[i]=="*" or ls[i]=="/":
                a=stack.pop()
                b=ls[i+1]
                res=operate(a,b,ls[i])
                stack.append(res)
                skip=1
            else:
                stack.append(ls[i])
        
        print(stack)
        # do + and -
        while len(stack)>1:
            a=stack.popleft()
            operator=stack.popleft()
            b=stack.popleft()
            stack.appendleft(operate(a,b,operator))
        return stack.pop()