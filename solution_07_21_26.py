class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zeros = []
        n = len(s)
        i = 0
        curZeros = 0
        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1
            if s[start] == "0":
                zeros.append(i-start)
        
        m = len(zeros)
        ones = s.count("1")
        if m < 2:
            return ones
        
        best = 0
        for i in range(m-1):
            best = max(best, zeros[i] + zeros[i+1])
        return ones + best
