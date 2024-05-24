class RecentCounter:

    def __init__(self):
        self.counter=[]
        self.length=0

    def ping(self, t: int) -> int:
        self.counter.append(t)
        count=0
        self.length+=1
        for item in self.counter[::-1]:
            if item<t-3000:
                break
            else:
                count+=1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)