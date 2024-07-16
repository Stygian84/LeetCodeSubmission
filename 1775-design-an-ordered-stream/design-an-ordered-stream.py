class OrderedStream:

    def __init__(self, n: int):
        self.ls=[[] for _ in range(n+1)]
        
        self.ptr = 1
        self.n=n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ls[idKey]=value
        if self.ls[self.ptr]==[]:
            return []
        else:
            res=[]
            for i in range(self.ptr,self.n+1):
                if self.ls[i]!=[]:
                    res.append(self.ls[i])
                else:
                    break
            self.ptr+=len(res)
            return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)