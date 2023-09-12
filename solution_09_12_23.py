class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        ret = 0
        used = set()
        print(c)
        for f in c.values():
            while f > 0 and f in used:
                f -= 1
                ret += 1
            used.add(f)


        return ret
