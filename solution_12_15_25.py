class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 1
        l = 0
        r = 1
        ret = 0
        while l < n:
            while r < n and prices[r] == prices[r-1] - 1:
                r += 1
            # Should have string of descent, add to result
            descentLen = r - l
            ret += (descentLen*(descentLen+1)) //2
            l = r
            r = l+1
        return ret
