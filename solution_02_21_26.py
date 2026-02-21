class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def isPrime(num):
            if num == 1:
                return False
            k = 2
            while k**2 <= num:
                if num % k == 0:
                    return False
                k += 1
            return True
        
        ret = 0
        for curNum in range(left, right+1):
            bits = curNum.bit_count()
            if isPrime(bits):
                ret += 1
        
        return ret
