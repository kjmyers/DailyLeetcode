class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        l = 0
        r = len(piles) - 1
        c = r - 1
        ret = 0

        while l < c:
            ret += piles[c]
            r = c - 1
            c = r - 1
            l += 1

        return ret
