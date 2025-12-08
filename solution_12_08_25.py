class Solution:
    def countTriples(self, n: int) -> int:
        ret = 0
        for a in range(1, n):
            for b in range(1, n):
                s = sqrt(a*a + b*b)
                if floor(s) == s and s <= n:
                    ret += 1
        
        return ret
