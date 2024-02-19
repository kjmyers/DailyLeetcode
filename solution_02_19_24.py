class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        bn = str(bin(n))[2:]
        c = 0
        for d in bn:
            if d == '1':
                c += 1
            if c > 1:
                return False

        return True
