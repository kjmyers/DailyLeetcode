class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.times = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers.keys():
            self.customers[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customers.keys():
            print(self.customers[id])
            self.times[(self.customers[id][0], stationName)].append(t - self.customers[id][1])
            del self.customers[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.times[(startStation,endStation)])/len(self.times[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
