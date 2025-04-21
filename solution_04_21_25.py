class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        maxV = 0
        minV = 0

        for d in differences:
            prefix += d
            maxV = max(maxV, prefix)
            minV = min(minV, prefix)
        
        ret = (upper - lower) - (maxV - minV) + 1 

        return ret if ret > 0 else 0
