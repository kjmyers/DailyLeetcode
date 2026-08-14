class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        n = len(s)
        l = 0
        ret = 1

        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 2:
                count[s[l]] -= 1
                l += 1
            ret = max(ret, r - l + 1 )

        return ret
