class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # {id: (start_station, start_time)}
        self.avg_times = {}  # {(start_station, end_station): (total_time, count)}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins[id]
        journey_time = t - start_time
        route = (start_station, stationName)

        if route in self.avg_times:
            total_time, count = self.avg_times[route]
            self.avg_times[route] = (total_time + journey_time, count + 1)
        else:
            self.avg_times[route] = (journey_time, 1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        total_time, count = self.avg_times[route]
        return total_time / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)