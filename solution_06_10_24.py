class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sheights = sorted(heights)
        ret = 0
        for i in range(len(heights)):
            if heights[i] != sheights[i]:
                ret += 1
        return ret
