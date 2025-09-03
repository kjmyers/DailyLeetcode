class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        points.sort(key=lambda x: (x[0], -x[1]))

        for i in range(n):
            pointA = points[i]
            xMin = pointA[0] - 1
            xMax = float('inf')
            yMin = -float('inf')
            yMax = pointA[1] + 1
            
            for j in range(i+1, n):
                pointB = points[j]
                if (pointB[0] > xMin
                    and pointB[0] < xMax
                    and pointB[1] > yMin
                    and pointB[1] < yMax):
                    
                    ans += 1
                    xMin = pointB[0]
                    yMin = pointB[1]
        return ans
