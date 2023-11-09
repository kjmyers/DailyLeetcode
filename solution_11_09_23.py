class Solution:
    def countHomogenous(self, s: str) -> int:
        ret = 1
        curLen = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                curLen += 1
                ret += curLen
            else:
                curLen = 1
                ret += 1
        
        return ret % (10**9 + 7)
