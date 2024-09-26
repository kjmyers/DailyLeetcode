class MyCalendar:

    def __init__(self):
        self.times = []
        

    def book(self, start: int, end: int) -> bool:
        i = bisect_right(self.times,(start,end))
        if ((i > 0 and self.times[i-1][1] > start) or
        (i < len(self.times) and self.times[i][0] < end)):
            return False
        self.times.append((start,end))
        self.times.sort()
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
