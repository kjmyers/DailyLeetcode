class Solution:
    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        else:
            return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
