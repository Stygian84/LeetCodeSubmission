class MedianFinder:

    def __init__(self):
        self.low = []  
        self.high = [] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        
        if self.low and self.high and (-self.low[0] > self.high[0]):
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        
        if len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()