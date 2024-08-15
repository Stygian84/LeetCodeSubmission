class MyCalendar:

    def __init__(self):
        self.ls = []

    def book(self, start: int, end: int) -> bool:
        if not self.ls:
            self.ls.append((start,end))
            return True

        else:
            for a,b in self.ls:
                if start>=a and (start<b or end<b):
                    return False
                if start<=a and (end>a or end>b):
                    return False
            self.ls.append((start,end))
            self.ls.sort()
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)