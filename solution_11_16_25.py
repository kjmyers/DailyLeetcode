class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        l = 0
        ret = 0
        while l < n:
            if s[l] == "1":
                r = l
                while r < n and s[r] == "1":
                    r += 1
                totalOnes = r - l
                ret += (totalOnes * (totalOnes + 1))//2
                l = r
            else:
                l += 1
        
        return ret % (10**9 + 7)
