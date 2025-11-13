class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        zc = 0
        ret = 0
        for i in range(n-2,-1,-1):
            if s[i] == "1":
                if s[i+1] == "0":
                    zc += 1
                ret += zc
        
        return ret
