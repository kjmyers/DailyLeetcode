class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        l = 0
        ones = 0
        n = len(s)
        ret = s
        for r in range(n):
            if s[r] == "1":
                ones += 1
            while ones > k or s[l] == "0":
                if s[l] == "1":
                    ones -= 1
                l += 1
            if ones == k:
                t = s[l : r + 1]
                if len(t) < len(ret) or len(t) == len(ret) and t < ret:
                    ret = t
        return ret
