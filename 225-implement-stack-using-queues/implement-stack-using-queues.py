class MyStack:

    def __init__(self):
        self.ls=[]
        

    def push(self, x: int) -> None:
        self.ls=[x]+self.ls
        

    def pop(self) -> int:
        return self.ls.pop(0)
        

    def top(self) -> int:
        return self.ls[0]
        

    def empty(self) -> bool:
        if self.ls==[]:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()