class UndergroundSystem:

    def __init__(self):
        self.dc = {}  # {id: (start_station, start_time)}
        self.avg = {}  # {(start_station, end_station): (total_time, count)}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dc[id]=(stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        a,d=self.dc[id]
        b=stationName
        c=t

        #self.dc[id]=[a+b,c-d]
        
        #add to self.avg
        if (a,b) in self.avg:
            prev_total,prev_count = self.avg[(a,b)]

            self.avg[(a,b)] = [prev_total + (c-d), prev_count+1] 
        else:
            self.avg[(a,b)] = [c-d,1]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        x,y=self.avg[(startStation,endStation)]
        return x/y
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)