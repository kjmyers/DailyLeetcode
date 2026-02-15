class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        m = len(a)-1
        n = len(b)-1

        ret = ""
        carry = 0

        while m >= 0 or n >= 0:

            if m >= 0:
                aNum = int(a[m])
            else:
                aNum = 0
            
            if n >= 0:
                bNum = int(b[n])
            else:
                bNum = 0

            cur = aNum + bNum + carry
            if cur > 1:
                carry = 1
                cur = cur - 2
            else:
                carry = 0
            
            ret = str(cur) + ret

            m -= 1
            n -= 1
        
        if carry:
            ret = "1" + ret
        
        return ret

        
