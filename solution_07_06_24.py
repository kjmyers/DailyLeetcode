class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        cur = time + 1
        rev = False
        while cur > n:
            cur -= (n-1)
            rev = not rev
        if rev:
            return n - cur + 1
        else:
            return cur
