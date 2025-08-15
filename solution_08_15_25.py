class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        ones = n.bit_count()
        zeros = n.bit_length() - ones

        if ones == 1 and zeros % 2 == 0:
            return True
        else:
            return False
