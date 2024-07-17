class UndergroundSystem:

    def __init__(self):
        self.dc = {}  # {id: (start_station, start_time)}
        self.avg = {}  # {(start_station, end_station): (total_time, count)}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dc[id]=(stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        a=self.dc[id][0]
        b=stationName
        c=t
        d=self.dc[id][1]

        #self.dc[id]=[a+b,c-d]
        
        #add to self.avg
        if (a,b) in self.avg:
            prev_total = self.avg[(a,b)][0]
            prev_count = self.avg[(a,b)][1]

            self.avg[(a,b)] = [prev_total + (c-d), prev_count+1] 
        else:
            self.avg[(a,b)] = [c-d,1]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[(startStation,endStation)][0] / self.avg[(startStation,endStation)][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)