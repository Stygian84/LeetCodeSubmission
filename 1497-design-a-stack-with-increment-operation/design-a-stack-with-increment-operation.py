class CustomStack:

    def __init__(self, maxSize: int):
        self.ls = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.ls)<self.maxSize:
            self.ls.append(x)
        

    def pop(self) -> int:
        if self.ls:
            return self.ls.pop()
        return -1
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.ls))):
            self.ls[i]+=val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)