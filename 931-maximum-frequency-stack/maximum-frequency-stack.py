class FreqStack:

    def __init__(self):
        self.dc={}
        self.freq_stack={}
        self.max_freq=0
        

    def push(self, val: int) -> None:
        freq=self.dc.get(val,0)+1
        self.dc[val]=freq
        self.max_freq=max(self.max_freq,freq)

        if freq not in self.freq_stack:
            self.freq_stack[freq]=[]
        self.freq_stack[freq].append(val)
        

    def pop(self) -> int:
        val=self.freq_stack[self.max_freq].pop()
        
        self.dc[val] -=1
        
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()