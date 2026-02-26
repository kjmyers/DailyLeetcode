class Solution:
    def numSteps(self, s: str) -> int:
        
        ret = 0
        carry = 0
        for n in s[:0:-1]:
            if (n == '0' and carry == 0) or (n == '1' and carry == 1):
                ret += 1
            else:# (n == '1' and carry == 0) or (n == '0' and carry == 1):
                ret += 2
                carry = 1
        if carry:
            ret += 1
        return ret
