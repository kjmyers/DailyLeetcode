class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ""
        for i in range(1,n+1):
            s += "{0:b}".format(int(i))
        return int(s,2) % (pow(10,9) + 7)
