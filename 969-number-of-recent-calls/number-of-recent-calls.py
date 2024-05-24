class RecentCounter:

    def __init__(self):
        self.counter=[]

    def ping(self, t: int) -> int:
        self.counter.append(t)
        count=0
        for item in self.counter:
            if t-3000<=item<=t:
                count+=1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)