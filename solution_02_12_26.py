class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        ret = 0
        for l in range(n):
            d = defaultdict(int)
            for r in range(l, n):
                d[s[r]] += 1
                if len(set(d.values())) == 1:
                    ret = max(ret, r-l+1)
        
        return ret
