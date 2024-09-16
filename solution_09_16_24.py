class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []

        for t in timePoints:
            time.append( (int(t[:2]),int(t[3:])))
        
        time.sort()

        minTime = float('inf')
        n = len(time)
        for i in range(1,n):
            minTime = min(minTime, ((time[i][0] - time[i-1][0]) * 60) + (time[i][1] - time[i-1][1]) )
        minTime = min(minTime, (((time[0][0]+24) - time[n-1][0] - 1) * 60) + ((time[0][1]+60) - time[n-1][1]) )



        return minTime
