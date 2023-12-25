class UndergroundSystem:

    def __init__(self):
        self.station_data = defaultdict(dict)  #[numbers checked out, avarage, ]
        self.user_data = defaultdict(list) #id: enter time

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user_data[id] = [stationName, t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        t_initial = self.user_data[id][1]
        s_initial = self.user_data[id][0]

        if s_initial in self.station_data[stationName]:
            avg, num = self.station_data[stationName][s_initial]
            avg = (avg*num + (t - t_initial))/(num+1)
            self.station_data[stationName][s_initial] = [avg, num+1]
        else:
            self.station_data[stationName][s_initial] = [t-t_initial, 1]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_data[endStation][startStation][0]
#operations after checkin checkins = id: [station, time]
#oprations after checkout  chkouts = station : [update avarage, n+1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)