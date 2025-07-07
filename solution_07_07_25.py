class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        maxDay = max(event[1] for event in events)
        events.sort()
        pq = []
        ret = 0
        j = 0
        for i in range(1, maxDay+1):
            while j < len(events) and events[j][0] <= i:
                heappush(pq, events[j][1])
                j += 1
            
            while pq and pq[0] < i:
                heappop(pq)
            if pq:
                heappop(pq)
                ret += 1
        
        return ret
