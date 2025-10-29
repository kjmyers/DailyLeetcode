class Solution:
    def smallestNumber(self, n: int) -> int:
        bl = len(str(bin(n))) - 3
        ret = 1
        for _ in range(bl):
            ret = (ret << 1) + 1
        return ret
