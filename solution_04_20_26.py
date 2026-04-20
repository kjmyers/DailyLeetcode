class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ret = 0
        for i in range(n):
            if colors[i] != colors[0]:
                ret = max(ret, i)
            if colors[i] != colors[n-1]:
                ret = max(ret, n-1 - i)
        
        return ret
