class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        res = 0
        for a in range(1, n + 1):
            if a > 999:
                res += 1
        return res
