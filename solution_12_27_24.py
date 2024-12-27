class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        maxL = [0] * n

        maxL[0] = values[0]
        ret = 0

        for i in range(1, n):
            curR = values[i] - i
            ret = max(ret, maxL[i-1] + curR)
            curL = values[i] + i
            maxL[i] = max(maxL[i-1], curL)
        
        return ret
