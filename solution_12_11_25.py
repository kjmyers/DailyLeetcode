class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xvals = {}
        yvals = {}

        for x, y in buildings:
            if y not in xvals:
                xvals[y] = [-math.inf,math.inf]
            if x not in yvals:
                yvals[x] = [-math.inf,math.inf]
            
            yvals[x][0] = max(yvals[x][0], y)
            yvals[x][1] = min(yvals[x][1], y)

            xvals[y][0] = max(xvals[y][0], x)
            xvals[y][1] = min(xvals[y][1], x)
            
        ret = 0
        for x, y in buildings:
            if xvals[y][1] < x < xvals[y][0] and yvals[x][1] < y < yvals[x][0]:
                ret += 1
        return ret
