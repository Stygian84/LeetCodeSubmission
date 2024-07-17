class Bitset:

    def __init__(self, size: int):
        self.bit = [0]*size
        self.one_count = 0
        self.n = size
        self.isFlip = False

    def fix(self, idx: int) -> None:
        if self.isFlip:
            if self.bit[idx]==1:
                self.one_count +=1
                self.bit[idx]=0
        else:
            
            if self.bit[idx]==0:
                self.one_count +=1
                self.bit[idx]=1

    def unfix(self, idx: int) -> None:
        if self.isFlip:
            if self.bit[idx]==0:
                self.one_count -=1
                self.bit[idx]=1
        else:
            
            if self.bit[idx]==1:
                self.one_count -=1
                self.bit[idx]=0

    def flip(self) -> None:
        self.isFlip = not self.isFlip
        self.one_count = self.n - self.one_count

    def all(self) -> bool:
        return self.one_count == self.n

    def one(self) -> bool:
        return self.one_count > 0

    def count(self) -> int:
        return self.one_count

    def toString(self) -> str:
        if self.isFlip:
            res = [str(1 - item) for item in self.bit]
        else:
            res = [str(item) for item in self.bit]
        return ''.join(res)



# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()