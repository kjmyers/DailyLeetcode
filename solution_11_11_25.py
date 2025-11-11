class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for s in strs:
            zc = s.count("0")
            oc = len(s) - zc
            for i in range(m, zc-1,-1):
                for j in range(n, oc-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zc][j-oc] + 1)
        
        return dp[m][n]
