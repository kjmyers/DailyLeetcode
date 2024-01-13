class Solution:
    def minSteps(self, s: str, t: str) -> int:

        diff = Counter(s) - Counter(t)

        return sum(diff.values())
