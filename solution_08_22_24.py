class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)
        ret = []
        for c in range(2,len(a)):
            if a[c] == '1':
                ret.append('0')
            else:
                ret.append('1')

        return int(''.join(ret),2)
