class TimeMap:

    def __init__(self):
        self.dc=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.dc[key], [timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dc:
            ls=self.dc[key]
            l=0
            r=len(ls)-1
            closest = ""
            while l<=r:
                mid=(l+r)//2
                if ls[mid][0]==timestamp:
                    return ls[mid][1]
                elif ls[mid][0]>timestamp:
                    r=mid-1
                else:
                    closest=ls[mid][1]  
                    l=mid+1
            return closest

        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)