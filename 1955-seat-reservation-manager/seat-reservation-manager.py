class SeatManager:

    def __init__(self, n: int):
        self.ls = []
        self.pointer = 1

    def reserve(self) -> int:
        if len(self.ls)>0:
            res=self.ls[0]
            heapq.heappop(self.ls)
        else:
            res=self.pointer
            self.pointer+=1
        return res

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.ls,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)