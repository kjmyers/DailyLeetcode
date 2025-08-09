class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cur = 1
        power = 0
        while cur <= n:
            if n == cur:
                return True
            cur *= 2
        return False
