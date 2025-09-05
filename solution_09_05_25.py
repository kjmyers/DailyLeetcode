class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        numOps = 1
        while True:
            x = num1 - (num2 * numOps)
            if x < numOps:
                return -1
            if numOps >= x.bit_count():
                return numOps
            numOps += 1
