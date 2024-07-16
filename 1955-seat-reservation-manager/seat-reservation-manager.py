class SeatManager:

    def __init__(self, n: int):
        self.ls = []
        [heapq.heappush(self.ls, item) for item in range(1,n+1)]

    def reserve(self) -> int:
        return heapq.heappop(self.ls)

    def unreserve(self, seatNumber: int) -> None:
        return heapq.heappush(self.ls,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)