class Solution:
    def checkDivisibility(self, n: int) -> bool:
        prod = 1
        summ = 0
        num = n
        while num:
            cur = num % 10
            summ += cur
            prod *= cur
            num //= 10
        total = summ + prod
        if n % total == 0:
            return True
        return False
