class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.ls=[]
        self.k=k
        for item in nums:
            heapq.heappush(self.ls,item)
            if len(self.ls) > self.k:
                heapq.heappop(self.ls)

    def add(self, val: int) -> int:
        heapq.heappush(self.ls,val)
        if len(self.ls) > self.k:
            heapq.heappop(self.ls)
        return self.ls[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)