class Router(object):

    def __init__(self, memoryLimit):
        self.mpp = {} # to track duplicates
        self.queue = deque() # to store packets in FIFO order
        self.timestamps = {} # for timestamps tracking
        self.removed = {}
        self.limit = memoryLimit # maxSize allowed

    def addPacket(self, source, destination, timestamp):
        packet = (source, destination, timestamp)
        # checking for duplicate
        if packet in self.mpp:
            return False
        if len(self.queue) == self.limit: # remove the first element if queue is full
            self.forwardPacket()
        self.queue.append(packet)
        self.mpp[packet] = 1
        if destination not in self.timestamps:
            self.timestamps[destination] = []
        self.timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self):
        if not self.queue:
            return []
        res = self.queue.popleft()
        del self.mpp[res]
        temp = res[1]
        self.removed[temp] = self.removed.get(temp, 0) + 1
        return list(res)

    def getCount(self, destination, startTime, endTime):
        if destination not in self.timestamps:
            return 0
        p = self.timestamps[destination]
        temp = self.removed.get(destination, 0)
        right = bisect.bisect_left(p, startTime, temp)
        left = bisect.bisect_right(p, endTime, temp)
        return left - right


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
