class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def getProd(num):
            mult = 1
            while num:
                cur = num % 10
                mult *= cur
                num = num // 10
            return mult
        for i in range(n,n+10):
            if getProd(i) % t == 0:
                return i
