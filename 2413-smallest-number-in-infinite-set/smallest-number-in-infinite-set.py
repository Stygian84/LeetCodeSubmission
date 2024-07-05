class SmallestInfiniteSet:

    def __init__(self):
        self.heap=[ i for i in range(1,1001)]
        self.s=set(self.heap)

    def popSmallest(self) -> int:
        value = heapq.heappop(self.heap)
        self.s.remove(value)
        return value

    def addBack(self, num: int) -> None:
        if num not in self.s:
            self.s.add(num)
            heapq.heappush(self.heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)