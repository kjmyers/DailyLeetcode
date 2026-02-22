class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        ret = 0
        for i in range(32):
            if (n >> i) & 1 == 1:
                if last is not -1:
                    ret = max(ret, i-last)
                last = i
        
        return ret
