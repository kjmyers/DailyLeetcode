class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(t) - Counter(s)
        for key in c.keys():
            ret = key
        return ret
