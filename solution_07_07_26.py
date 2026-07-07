class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        curMult = 1
        dig = 0
        total = 0

        while n > 0:
            cur = n % 10
            n = n // 10
            if cur != 0:
                total += cur
                dig += cur * curMult
                curMult *= 10
        
        return dig * total
