class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2:
            cur = ""
            for i in range(len(s)-1):
                cur += str((int(s[i]) + int(s[i+1])) % 10)
            s = cur
        
        return s[0] == s[1]
