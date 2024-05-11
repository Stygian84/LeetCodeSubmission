class RandomizedSet:

    def __init__(self):
        self.dict={}
        self.ls=[]

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val]=0
            self.ls.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            self.dict.pop(val)
            self.ls.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.ls)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()