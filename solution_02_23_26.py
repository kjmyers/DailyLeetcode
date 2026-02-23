class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        codes = set()
        n = len(s)
        for i in range(n - k+1):
            codes.add(s[i:i+k])
        if len(codes) == 2**k:
            return True
        else:
            return False
