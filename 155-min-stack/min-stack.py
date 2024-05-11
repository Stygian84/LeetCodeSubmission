class MinStack:

    def __init__(self):
        self.ls=[]
        self.min_hist=[]
        

    def push(self, val: int) -> None:
        self.ls.append(val)
        if self.min_hist==[]:
            self.min_hist.append(val)
        elif val<=self.min_hist[-1]:
            self.min_hist.append(val)
        

    def pop(self) -> None:
        if self.ls[-1]==self.min_hist[-1]:
            self.min_hist.pop(-1)
        self.ls.pop(-1)
        

    def top(self) -> int:
        return self.ls[-1]
        

    def getMin(self) -> int:
        return self.min_hist[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()