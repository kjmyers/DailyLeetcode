class Solution:
    def minInsertions(self, s: str) -> int:

        self.memo = {}
        l = len(s)

        def lcs(s1, s2, m, n):
            if m == 0 or n == 0:
                return 0
            if (m,n) in self.memo:
                return self.memo[(m,n)]
            
            if s1[m-1] == s2[n-1]:
                self.memo[(m,n)] = 1 + lcs(s1,s2, m-1, n-1)
                return self.memo[(m,n)]
            
            self.memo[(m,n)] = max(lcs(s1, s2, m-1, n), lcs(s1, s2, m, n-1))
            return self.memo[(m,n)]
        return l - lcs(s, s[::-1], l, l)
