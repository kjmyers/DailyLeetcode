class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = list(set([x[0] for x in points]))
        ret = 0
        l.sort()
        for i in range(1,len(l)):
            ret = max(ret, l[i] - l[i-1])

        return ret
