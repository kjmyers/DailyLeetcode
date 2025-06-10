class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        a1 = 0
        a2 = float('inf')
        for v in c.values():
            if v % 2 == 1:
                a1 = max(a1, v)
            else:
                a2 = min(a2, v)

        return a1 - a2
