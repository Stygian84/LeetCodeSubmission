class MedianFinder:

    def __init__(self):
        self.ls=[]
        self.i=0
        self.count=0

    def addNum(self, num: int) -> None:
        bisect.insort(self.ls, num)
        
        self.count+=1
        if self.count==2:
            self.count=0
            self.i+=1

    def findMedian(self) -> float:
        if self.count==0:
            return (self.ls[self.i]+self.ls[self.i-1])/2
        return self.ls[self.i]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()