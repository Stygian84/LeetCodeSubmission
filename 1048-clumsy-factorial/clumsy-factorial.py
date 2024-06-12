class Solution:
    def clumsy(self, n: int) -> int:
        if n==1:
            return 1

        operation=["*","/","+","-"]
        stack=deque([])
        j=0

        for i in range(n,0,-1):
            stack.append(i)
            stack.append(operation[j])
            j+=1
            if j>=4:
                j=0
        stack.pop()

        def operate(a,b,operator):
            if operator=="*":
                return a*b
            elif operator=="/":
                return math.trunc(a/b)

        result=[]
        while len(stack)>1:
            a=stack.popleft()
            operator=stack.popleft()
            b=stack.popleft()
            if operator=="+":
                result.append(a+b)
                stack.appendleft(a+b)
            elif operator=="-":
                stack.appendleft(-b)
                if len(stack)==1:
                    result.append(stack.popleft())
            else:
                stack.appendleft(operate(a,b,operator))
                if len(stack)==1:
                    result.append(stack.popleft())

        return sum(result)