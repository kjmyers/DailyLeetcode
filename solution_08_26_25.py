class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ret = 0
        diagsq = 0
        for l, w in dimensions:
            if (l*l + w*w) > diagsq:
                diagsq = l*l + w*w
                ret = l*w
            if (l*l + w*w) == diagsq:
                ret = max(ret, l*w)
        
        return ret
