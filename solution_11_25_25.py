class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remain = 0
        for l in range(1, k+1):
            remain = (remain*10 + 1) % k
            if remain == 0:
                return l
        return -1
