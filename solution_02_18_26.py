class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        cur = n & 1
        n = n >> 1
        while n:
            if not ((1&n) ^ cur):
                return False
            cur = n & 1
            n = n >> 1
        return True
