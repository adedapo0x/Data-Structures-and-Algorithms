class UndergroundSystem:
    """
    We use two dicts, one to store check in info, id is the key, the check in station and time are used as values in a tuple
    to check in, we simply update the check in dict
    to check out we take the time to check in, compute the time travelled and update it in our second dict
    to get average time is just computing average for the a particular start - stop station using the second dict

    TC: O(1)
    SC: O(P + R) where P is the number of passengers in our system at the same time, and R is the number of distinct routes, say a-b, b-a, a-c etc
    the checkInDict comes at a cost of O(P) while for checkIn-checkOut we have O(R)
    """

    def __init__(self):
        self.checkInDict = collections.defaultdict(tuple)
        self.checkIn_checkOut = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInDict[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInStation, checkInTime = self.checkInDict.pop(id) # we remove as we get the info, no need to still store in our system once they check out
        timeDiff = t - checkInTime
        travelDest = (checkInStation, stationName)

        if travelDest in self.checkIn_checkOut:
            totalTime, numOfTimes = self.checkIn_checkOut[travelDest]
            self.checkIn_checkOut[travelDest] = (totalTime + timeDiff, numOfTimes + 1)
        else:
            self.checkIn_checkOut[travelDest] = (timeDiff, 1)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, numOfTimes = self.checkIn_checkOut[(startStation, endStation)]
        return totalTime / numOfTimes
        


    '''
    Same idea generally as the solution above, only difference is in how we store in the second dict
    here we use a list to keep track of all the computed times, so when we want to get an average, we sum up the list and divide by the number 
    of entries.
    I think the above is slightly better since in worst case scenario everybody check in and check out at the same station, so we have to iterate over the entire list in
    our second dict to get the sum. Not much of a difference sha, still O(1)
    '''


    def __init__(self):
        self.checkInDict = collections.defaultdict(tuple)
        self.checkIn_checkOut = collections.defaultdict(list)


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInDict[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInStation, checkInTime = self.checkInDict.pop(id) 
        self.checkIn_checkOut[(checkInStation, stationName)].append(t - checkInTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.checkIn_checkOut[(startStation, endStation)] 
        return sum(times) / len(times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)