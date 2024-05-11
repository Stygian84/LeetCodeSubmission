class MinStack:

    def __init__(self):
        self.ls=[]
        

    def push(self, val: int) -> None:
        self.ls.append(val)
        

    def pop(self) -> None:
        self.ls.pop(-1)
        

    def top(self) -> int:
        return self.ls[-1]
        

    def getMin(self) -> int:
        return min(self.ls)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()